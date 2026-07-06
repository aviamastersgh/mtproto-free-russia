#!/usr/bin/env python3
import re, sys, random, socket, urllib.request, urllib.parse
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed

TIMEOUT = 8
MAX_WORKERS = 30
MAX_CONFIGS = 500

SOURCES = [
    "https://raw.githubusercontent.com/SoliSpirit/mtproto/master/all_proxies.txt",
]

# MTProto-ссылки встречаются в двух видах:
#   tg://proxy?server=HOST&port=PORT&secret=SECRET
#   https://t.me/proxy?server=HOST&port=PORT&secret=SECRET
LINK_RE = re.compile(
    r'(?:tg://proxy|https?://t\.me/proxy)\?[^\s"\'<>]+',
    re.IGNORECASE
)


def fetch_url(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read()
        return raw.decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"  [SKIP] {url[:70]}... → {e}", file=sys.stderr)
        return ""


def extract_configs(text):
    return [m.group(0) for m in LINK_RE.finditer(text)]


def parse_host_port_secret(link):
    try:
        q = urllib.parse.urlparse(link).query
        params = urllib.parse.parse_qs(q)
        host = params.get("server", [None])[0]
        port = int(params.get("port", [None])[0])
        secret = params.get("secret", [None])[0]
        return host, port, secret
    except Exception:
        return None, None, None


def check_config(link):
    host, port, secret = parse_host_port_secret(link)
    if not host or not port or not secret:
        return False
    try:
        # Базовая проверка: TCP-коннект до сервера.
        # Полноценный MTProto-handshake можно добавить позже (обмен obfuscated
        # hello-пакетом с использованием secret), пока ограничиваемся TCP —
        # так же, как было в оригинальном fetch_vpn.py для VLESS/VMess/SS.
        with socket.create_connection((host, port), timeout=TIMEOUT):
            return True
    except Exception:
        return False


def normalize_link(link):
    """Приводим все ссылки к формату tg://proxy?... для единообразия."""
    host, port, secret = parse_host_port_secret(link)
    if not host or not port or not secret:
        return None
    return f"tg://proxy?server={host}&port={port}&secret={secret}"


def update_readme(all_count, ver_count, ts):
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            readme = f.read()

        ts_badge = ts.replace("-", "_").replace(" ", "_").replace(":", "%3A")

        stats_block = (
            f'<!-- STATS_START -->\n'
            f'<a href="https://raw.githubusercontent.com/aviamastersgh/mtproto-free-russia/main/all_proxies.txt">'
            f'<img src="https://img.shields.io/badge/Все_прокси-{all_count}-4C8BF5?style=for-the-badge&logo=server&logoColor=white" alt="All proxies"/></a>\n'
            f'<a href="https://raw.githubusercontent.com/aviamastersgh/mtproto-free-russia/main/verified_proxies.txt">'
            f'<img src="https://img.shields.io/badge/Проверенные-{ver_count}-2ea44f?style=for-the-badge&logo=checkmarx&logoColor=white" alt="Verified proxies"/></a>\n'
            f'<img src="https://img.shields.io/badge/Обновлено-{ts_badge}-f97316?style=for-the-badge&logo=clockify&logoColor=white" alt="Updated"/>\n'
            f'<!-- STATS_END -->'
        )

        readme = re.sub(
            r'<!-- STATS_START -->.*?<!-- STATS_END -->',
            stats_block,
            readme,
            flags=re.DOTALL
        )

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(readme)
        print("[UPDATE] README.md обновлён")
    except FileNotFoundError:
        print("[SKIP] README.md не найден")


def main():
    print("=" * 60)
    print(f"MTProto Fetcher: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 60)

    if not SOURCES:
        print("[WARN] Список SOURCES пуст — добавьте источники в скрипт.")

    all_configs, seen = [], set()
    for url in SOURCES:
        print(f"[FETCH] {url[:70]}...")
        text = fetch_url(url)
        found = extract_configs(text)
        new = 0
        for c in found:
            norm = normalize_link(c)
            if norm and norm not in seen:
                seen.add(norm)
                all_configs.append(norm)
                new += 1
        print(f"  → найдено {len(found)}, новых {new}")

    print(f"\nВсего уникальных: {len(all_configs)}")
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    header_all = (
        f"# Free MTProto Proxies | NosokVPNBot\n"
        f"# Обновлено: {ts}\n# Всего: {len(all_configs)}\n"
        f"# Telegram: https://t.me/NosokVPNBot?start=partner_8655864538\n#\n"
    )
    with open("all_proxies.txt", "w", encoding="utf-8") as f:
        f.write(header_all + "\n".join(all_configs) + "\n")
    print(f"[SAVE] all_proxies.txt — {len(all_configs)}")

    print(f"\n[CHECK] TCP-проверка ({MAX_WORKERS} потоков)...")
    sample = all_configs[:]
    random.shuffle(sample)
    verified, checked = [], 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(check_config, c): c for c in sample}
        for future in as_completed(futures):
            checked += 1
            try:
                ok = future.result()
            except Exception:
                ok = False
            if ok:
                verified.append(futures[future])
                if len(verified) >= MAX_CONFIGS:
                    for f in futures:
                        f.cancel()
                    break
            if checked % 50 == 0:
                print(f"  проверено {checked}/{len(sample)}, рабочих: {len(verified)}")

    print(f"\nРабочих: {len(verified)} из {checked}")
    header_ver = (
        f"# Verified MTProto Proxies | NosokVPNBot\n"
        f"# Обновлено: {ts}\n# Проверенных: {len(verified)}\n"
        f"# Telegram: https://t.me/NosokVPNBot?start=partner_8655864538\n#\n"
    )
    with open("verified_proxies.txt", "w", encoding="utf-8") as f:
        f.write(header_ver + "\n".join(verified) + "\n")
    print(f"[SAVE] verified_proxies.txt — {len(verified)}")

    update_readme(len(all_configs), len(verified), ts)
    print("\n✅ Готово!")


if __name__ == "__main__":
    main()
