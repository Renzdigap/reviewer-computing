# 📖 TaiShan 200 (2280) Default Credentials & iBMC Initial Setup

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 06 — Computing Product Deployment: Equipment Room, iBMC, BIOS & RAID Configuration (Sprint 2 of 4)  
**Format:** Bite-Sized Lecture (8 mins) → Followed immediately by `04-Exercise-iBMC-Default-IP-Credentials-and-WebUI-Navigation-Lab` (8 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.05, pp. 296–308

---

## 🎯 Learning Objectives
- Memorize the exact default IP, subnet mask, and all 3 default user/password pairs of TaiShan 200 (model 2280)
- Know how to query the iBMC IP in BIOS and configure Network, Firmware, Local Users, NTP, VNC, and SNMP in iBMC WebUI
- Compare SNMPv1 (RFC 1157), SNMPv2 (RFC 1901), and SNMPv3 security recommendations

---

### 1. Default Values of TaiShan 200 (Model 2280) (p. 297 — Must Memorize!)
| Category | Item | Official Default Value (p. 297) | Remarks |
| :--- | :--- | :--- | :--- |
| **iBMC Management Network Port** | IP Address & Subnet Mask | IP: **`192.168.2.100`**<br>Subnet Mask: **`255.255.255.0`** | Can be queried/changed in BIOS (`Advanced > IPMI iBMC Configuration > iBMC Configuration`) or iBMC WebUI |
| **Default iBMC Login User** | User Name & Password | User: **`root`**<br>Password: **`Huawei12#$`** | Default underlying iBMC user |
| **iBMC WebUI or CLI Login** | User Name & Password | User: **`Administrator`**<br>Password: **`Admin@9000`** | Select Domain: **`Local iBMC`** when logging in to `https://192.168.2.100` |
| **iBMC U-Boot Data / BIOS** | Default Password | Password: **`Admin@9000`** | Used for U-Boot and BIOS Setup entry |

*(Note on Peripheral Ports, p. 298: The front and rear panels of TaiShan 2280 feature a **VGA port** for display output and **USB 3.0 ports**, but **lack PS/2 ports** for keyboard/mouse — connect a USB keyboard/mouse directly or use a USB-to-PS/2 adapter.)*

---

### 2. iBMC WebUI Initial Configuration Navigation Paths (pp. 300–308)
Connect a PC to the iBMC management port via crossover or twisted-pair cable, browse to `https://192.168.2.100`, enter `Administrator` / `Admin@9000`, and select **`Local iBMC`**:

| Task | Exact iBMC WebUI Menu Path (pp. 300–308) |
| :--- | :--- |
| **Change iBMC Management IP** | **`iBMC Settings > Network Settings`** (locate **Network Protocols** area \rightarrow Save) |
| **Check Version & Upgrade Firmware** | **`iBMC Settings > Firmware Upgrade`** (upload file, optionally select *Restart iBMC immediately after upgrade*) |
| **Change Initial Password** | **`User & Security > Local Users`** (click **Edit** next to the user) |
| **Configure Time Zone & NTP** | **`iBMC Settings > Time Zone & NTP`** (synchronizes host clocks with **UTC** within **1 ms on LAN** and **tens of ms on WAN**) |
| **Enable VNC** | **`Services > VNC`** (provides remote video display and keyboard/mouse control) |
| **Enable SNMP** | **`Services > SNMP`** |

---

### 3. SNMP Versions Supported by iBMC (p. 308)
- **SNMPv1**: First official SNMP version defined in **RFC 1157**; poses security risks (cleartext community strings).
- **SNMPv2**: Experimental protocol defined in **RFC 1901** adopting a community-based management architecture; poses security risks.
- **SNMPv3**: Third official SNMP version revising previous versions with **enhanced security (authentication + encryption)** and remote configuration. **For security purposes, always use SNMPv3!**

---

## 🔑 Key Takeaways
- **TaiShan 200 (2280) default iBMC IP is 192.168.2.100/24 (255.255.255.0); iBMC WebUI/CLI login is Administrator / Admin@9000 (Domain: Local iBMC); default iBMC user is root / Huawei12#$; U-Boot/BIOS password is Admin@9000.**
- **TaiShan 2280 has VGA and USB 3.0 ports on front/rear panels, but NO PS/2 ports.**
- **Query iBMC IP via BIOS at Advanced > IPMI iBMC Configuration > iBMC Configuration, or change it in iBMC WebUI at iBMC Settings > Network Settings > Network Protocols.**
- **SNMPv1 (RFC 1157) and SNMPv2 (RFC 1901) have security risks; SNMPv3 is recommended for security.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Distinguish the two default accounts on p. 297: iBMC WebUI/CLI uses `Administrator` / `Admin@9000`, while the default iBMC login user is `root` / `Huawei12#$`!

> [!WARNING]
> EXAM TRAP: Know the exact iBMC WebUI menu paths: Firmware Upgrade, Network Settings, and Time Zone & NTP are under `iBMC Settings`; Local Users is under `User & Security`; VNC and SNMP are under `Services`.

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`04-Exercise-iBMC-Default-IP-Credentials-and-WebUI-Navigation-Lab.html`](./04-Exercise-iBMC-Default-IP-Credentials-and-WebUI-Navigation-Lab.html)** (or [`04-Exercise-iBMC-Default-IP-Credentials-and-WebUI-Navigation-Lab.md`](./04-Exercise-iBMC-Default-IP-Credentials-and-WebUI-Navigation-Lab.md)) to apply this concept in an interactive lab workbench!
