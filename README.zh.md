<div align="center">

# 🔓 免费 MTProto 俄罗斯代理

**MTProto 代理**

*免费的 Telegram MTProto 代理 · 绕过俄罗斯联邦通信监管局（РКН）封锁 · 支持 Telegram 官方客户端*

</div>

---

## 📑 目录

- [关于项目](#-关于项目)
- [两个文件的区别](#-两个文件的区别)
- [快速连接](#-快速连接)
- [如何在 Telegram 中添加代理——分步说明](#-如何在-telegram-中添加代理分步说明)
- [支持的客户端](#-支持的客户端)
- [稳定 VPN——个人密钥](#-稳定-vpn个人密钥)
- [什么是 MTProto](#-什么是-mtproto)
- [常见问题](#-常见问题)
- [镜像站点（GitHub 被封锁时使用）](#-镜像站点github-被封锁时使用)
- [免责声明](#️-免责声明)

---

## 💙 支持本项目

**本项目仅靠热情和捐赠维持运作。服务器测试、检测耗费的时间、镜像维护、加快更新——这一切都需要金钱和精力。**

如果今天代理帮到了你，非常欢迎你的支持 ❤️

最方便的捐赠方式：
- USDT (TRC-20) → `TLkat7EH1LZ6aZB3nQ3yScJD1a9CSkYV1d`
- Solana (SOL) → `H8dJ9wJmCzYqBjvPW5fXkA8dTFngmpvLfNvQcn2mJGdS`
- Bitcoin → `bc1q376tjzk663f3kkrkvtgnqy2p9xat5klk5dytag`

> 即使许多人只捐一点点，累积起来也能保证稳定更新和新增镜像。谢谢！🙏

也别忘了点个 ⭐ Star，并分享给在俄罗斯需要免费访问 Telegram 的人。

---

## 📖 关于项目

本仓库是一个**公共免费 MTProto 代理聚合器**，用于在俄罗斯境内绕过 РКН（俄罗斯联邦通信监管局）的封锁，使用 Telegram 更加顺畅。

脚本每 **2 小时**自动执行以下操作：
- 📥 从公开来源收集代理
- 🔍 去除重复项
- ✅ 检测每台服务器的可用性
- 📤 发布两个包含最新结果的文件

无需注册，无需账号。复制代理链接——Telegram 会自动连接。

如果你需要稳定性而不想占用公共代理池的负载，请查看["稳定 VPN——个人密钥"](#-稳定-vpn个人密钥)部分。

---

## 📂 两个文件的区别？

### `all_proxies.txt` —— 所有找到的代理

包含从所有来源找到的**全部**代理（已去重）。其中部分可能暂时无法使用——服务器可能过载、下线或被封锁。

➡️ **适用场景：** 你有时间自己测试多台服务器，或者标准文件没有帮助。

```
https://raw.githubusercontent.com/aviamastersgh/mtproto-free-russia/main/all_proxies.txt
```

### `verified_proxies.txt` —— 仅可用代理 ✅（推荐）

从整个代理池中筛选出检测时**实际能建立连接**的服务器。

➡️ **适用场景：** 大多数情况下，这是最好的起点。

```
https://raw.githubusercontent.com/aviamastersgh/mtproto-free-russia/main/verified_proxies.txt
```

### 对比表

| 文件 | 数量 | 检测 | 适合谁 |
|------|-----|------|--------|
| `all_proxies.txt` | 最多 | ✅ | 想要更多选择，愿意自己测试 |
| `verified_proxies.txt` | 较少 | ✅ | **大多数用户** |

---

## ⚡ 快速连接

打开文件，复制形如 `https://t.me/proxy?server=...&port=...&secret=...` 的链接并跳转——Telegram 会自动提示连接。

**推荐（可用服务器）：**
```
https://raw.githubusercontent.com/aviamastersgh/mtproto-free-russia/main/verified_proxies.txt
```

**所有代理：**
```
https://raw.githubusercontent.com/aviamastersgh/mtproto-free-russia/main/all_proxies.txt
```

**如果 GitHub 被封锁** —— 使用 GitHack 镜像：
```
https://raw.githack.com/aviamastersgh/mtproto-free-russia/main/verified_proxies.txt
```

---

## 📱 如何在 Telegram 中添加代理——分步说明

### 方法 1 —— 通过直接链接（最简单）

1. 通过上方链接打开 `verified_proxies.txt` 文件
2. 复制任意一行——这是一个形如 `https://t.me/proxy?server=1.2.3.4&port=443&secret=ee...` 的现成链接
3. 将链接粘贴到浏览器地址栏，或在手机上打开
4. Telegram 会自动打开并显示 **"连接代理"** 窗口
5. 点击 **"连接"**

### 方法 2 —— 通过 Telegram 设置手动添加

1. 打开代理文件，找到包含 `server`、`port`、`secret` 参数的那一行
2. 在 Telegram 中：**设置 → 高级 → 连接类型 → 代理**
3. 点击 **"添加代理"** → **MTProto**
4. 手动填入：服务器、端口、密钥（从复制的那一行获取）
5. 保存并通过开关启用代理

### Android / iOS

操作方式与上文相同：**设置 → 数据和存储 → 代理设置**（或 **高级 → 代理**，视版本而定）→ **添加代理** → MTProto。

### 桌面端（Windows / macOS / Linux）

**设置 → 高级设置 → 连接设置 → 添加代理** → MTProto → 手动填入数据。

---

## 📱 支持的客户端

| 客户端 | 平台 | MTProto 支持 |
|--------|------|--------------|
| **Telegram（官方）** | Android / iOS / Windows / macOS / Linux | ✅ 原生支持 |
| **Telegram X** | Android | ✅ 原生支持 |
| **Telegram Web** | 浏览器 | ✅ 通过 `t.me/proxy` 链接 |

> MTProto 代理**仅**在 Telegram 内部生效——它不是覆盖整个设备流量的 VPN。若需要其他应用也能使用，请参见 [vpn-free-russia](https://github.com/aviamastersgh/vpn-free-russia)。

---

## 🔒 稳定 VPN——个人密钥

公共代理是免费的，但没有保障：服务器可能过载、变更，有时速度较慢。这对于公共来源聚合器来说是正常现象。

如果你需要专属服务器上的稳定连接（而不仅仅是 Telegram 代理，而是完整的 VPN）——可以通过 Telegram 机器人获取个人密钥：

<div align="center">

### 🤖 [@NosokVPNBot](https://t.me/NosokVPNBot?start=partner_8655864538)

*个人密钥 · 专属服务器 · 稳定连接*

</div>

---

## 🔒 什么是 MTProto

**MTProto Proxy** 是 Telegram 自主研发的协议，专为绕过封锁而设计。

| 特点 | 说明 |
|------|------|
| **速度** | 轻量级协议，延迟极低 |
| **伪装性** | 流量看起来像普通 TCP 流量，比传统 VPN 更难被 DPI 检测分析 |
| **作用范围** | 仅在 Telegram 内部生效（聊天、通话、频道）——不代理其他应用 |
| **简便性** | 一个链接即可连接，无需安装额外应用 |

---

## ❓ 常见问题

<details>
<summary><strong>添加了代理，但 Telegram 无法连接，怎么办？</strong></summary>

1. 确认使用的是 `verified_proxies.txt`，而不是 `all_proxies.txt`
2. 依次尝试文件中的几行不同代理——并非所有服务器负载都相同
3. 检查是否完整复制了该行，包括 `secret` 部分
4. 手动刷新文件——代理每 2 小时更新一次，旧的可能已失效

</details>

<details>
<summary><strong>为什么昨天代理还能用，今天就不行了？</strong></summary>

公共免费服务器没有稳定性保障。它们可能被 РКН 封锁、因用户过多而过载，或被所有者下线。

因此列表每 2 小时更新一次。如果当前服务器停止响应，请重新查看 `verified_proxies.txt`。

</details>

<details>
<summary><strong>使用公共 MTProto 代理安全吗？</strong></summary>

公共代理是由陌生运营者提供的免费服务器。MTProto 会对数据进行加密，但服务器所有者理论上仍可看到连接的元数据（例如你连接的是哪个 Telegram 服务器 IP）。

**建议：** 如需更高隐私性，请使用专属服务器上的个人密钥。

</details>

<details>
<summary><strong>MTProto 代理和 VPN 是一回事吗？</strong></summary>

不是。MTProto 代理**仅**代理 Telegram 的流量（聊天、通话、频道）。其他应用——浏览器、其他即时通讯软件——仍将不经过绕过封锁而正常（或无法）工作。若需要整个设备的完整 VPN，请使用 [vpn-free-russia](https://github.com/aviamastersgh/vpn-free-russia)。

</details>

<details>
<summary><strong>如果 GitHub 被封锁怎么办？</strong></summary>

使用镜像站点——即使 GitHub 被封锁也能正常访问：

| 镜像 | 使用方法 |
|------|----------|
| **GitHack**（推荐） | 将上方任意链接中的 `raw.githubusercontent.com` 替换为 `raw.githack.com` |
| **jsDelivr** | `https://cdn.jsdelivr.net/gh/aviamastersgh/mtproto-free-russia@main/verified_proxies.txt` |

</details>

---

## 🌍 镜像站点（GitHub 被封锁时使用）

| 镜像 | `verified_proxies.txt` | `all_proxies.txt` |
|------|------------------------|--------------------|
| **GitHack** | [链接](https://raw.githack.com/aviamastersgh/mtproto-free-russia/main/verified_proxies.txt) | [链接](https://raw.githack.com/aviamastersgh/mtproto-free-russia/main/all_proxies.txt) |
| **jsDelivr** | [链接](https://cdn.jsdelivr.net/gh/aviamastersgh/mtproto-free-russia@main/verified_proxies.txt) | [链接](https://cdn.jsdelivr.net/gh/aviamastersgh/mtproto-free-russia@main/all_proxies.txt) |

> **GitHack** —— 实时代理，始终为最新内容。**jsDelivr** —— CDN，可能会缓存长达 24 小时。

---

## ‼️ 免责声明

*作者并非上述所列 MTProto 代理的所有者、开发者或提供者。本仓库是一个独立的信息聚合器，汇总公开可用的数据。*

*本资料面向该信息合法的国家/地区的公民，包括用于研究和教育目的。*

*作者不鼓励也不提倡将代理用于违反法律的目的。使用责任由用户自行承担。*

*请仅将代理用于合法目的：保护个人数据、安全远程访问、网络隐私。*

*所有信息均按"原样"提供，不保证准确性和时效性。*
