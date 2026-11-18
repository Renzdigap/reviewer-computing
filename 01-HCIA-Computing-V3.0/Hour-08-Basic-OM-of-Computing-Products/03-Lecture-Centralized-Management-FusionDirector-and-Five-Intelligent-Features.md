# 📖 Centralized Management: FusionDirector & Five Intelligent Features

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 08 — Basic O&M of Computing Products: iBMA, iBMC, Smart Provisioning, FusionDirector, eSight, SmartKit & eService (Sprint 2 of 4)  
**Format:** Bite-Sized Lecture (8 mins) → Followed immediately by `04-Exercise-FusionDirector-Device-Adding-and-Intelligent-Features-Lab` (8 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.06, pp. 377–400

---

## 🎯 Learning Objectives
- Compare the 4 server adding modes in FusionDirector (Manual adding, Batch import, DHCP auto IP allocation, SSDP auto discovery) and log export limits (100 servers)
- Master the Five Intelligent Features of FusionDirector: Intelligent Deployment, Asset, Version, Fault, and Energy Efficiency Management
- Know exact FusionDirector rules and specifications (Server Profile edit/delete restrictions, 30 concurrent OS deployments, 2-hour timeout, Location vs. SN/MAC Auto Go-Online)

---

### 1. FusionDirector Basic Features: 4 Device Adding Modes & Log Collection (pp. 378–381)
**FusionDirector** is Huawei's centralized O&M platform for batch server management, communicating southbound with server **iBMCs** via **Redfish** and northbound with upper-layer OSS via **Web/Portal, Redfish, and SNMP**:
- **Four Server Adding Modes (p. 379)**:
  1. **Manual adding**: Fuzzy device adding when devices have **consecutive IP addresses** and the **same device accounts**.
  2. **Batch import**: Accurate device adding via template when devices already have **IP addresses and accounts** configured.
  3. **DHCP automatic IP address allocation**: Used when devices are in DHCP mode and **accounts, SNs, and MAC addresses** are known (*Restriction*: requires a **DHCP relay server** on the network).
  4. **SSDP automatic discovery**: Uses **IP-SN mapping mode** (known SNs/accounts) or **IP resource pool allocation mode** (allocates random IPs when device info is unknown). (*Restriction*: **FusionDirector and the devices MUST be on the same Layer 2 (L2) network**!).
- **One-Click Log Collection (p. 380)**: Exports logs of **a maximum of 100 servers at a time** in one-click mode.

---

### 2. FusionDirector's Five Intelligent Features (pp. 382–400)
1. **Intelligent Deployment Management (pp. 383–385)**:
   - **Server Profile (p. 383)**: Configures BIOS, RAID, BMC, NIC, and PCIe topology for a specific server model (Server + NIC + RAID card combination).
     - *Rules*: Profile **binding is separated from application** (must **bind** before **applying**). You can **delete** a profile **only when it is NOT bound to any server**; you can **modify** a profile **only when it is NOT applied to any server**; backup profiles **cannot** be imported to a different or reinstalled FusionDirector!
   - **OS Deployment (p. 384)**: Out-of-band deployment (no DHCP/TFTP/PXE required!), **requires servers with Smart Provisioning** and an **OS deployment license**, formats the system disk, has a **2-hour timeout**, and deploys **a maximum of 30 devices at the same time**.
   - **Automatic Go-Online Planning (p. 385)**:
     - *Location-based planning*: Uses **iRM** to obtain rack **U marks**.
     - *SN/MAC-based planning*: Uses **DHCP** (must be in the same DHCP broadcast domain as FusionDirector).
     - *Mutual Exclusion Rule*: Enabling **location planning automatically disables SN/MAC planning**, and vice versa!
2. **Intelligent Asset Management (pp. 386–389)**: Hardware automatically identifies and reports rack **U space** assets (**100% asset accuracy**, improves inbound counting efficiency by **>95%**, component-level CPU/memory/disk tracking, 1-year asset change history).
3. **Intelligent Version Management (pp. 390–394)**: Connects to **HOUP** (*Huawei Online Update Platform*) via out-of-band channels (consumes zero service bandwidth) for **OTA** baseline push, common/OTA/periodic update schedules, firmware/driver update, and software installation/update/rollback/uninstallation.
4. **Intelligent Fault Management (pp. 395–396)**: AI-based **Disk Fault Prediction** (risk charts) and **Memory Fault Prediction** (DIMM health & historical self-healing records).
5. **Intelligent Energy Efficiency Management (pp. 397–400)**: Solves data center pain points (rack space utilization only 40%–50%, rack power usage 50%, electricity ≥ 78% of op costs). Provides AI rack power prediction, **cabinet-level power capping**, PSU hibernation, and 4 optimization analyses: **Power distribution** (batch power capping), **Temperature risk** (power off overheated air-intake servers), **Load optimization** (batch operations on low-load servers), and **Space optimization**.

---

## 🔑 Key Takeaways
- **FusionDirector SSDP discovery requires FusionDirector and managed servers to be on the same L2 network; one-click log export supports up to 100 servers at a time.**
- **FusionDirector Five Intelligent Features: Intelligent Deployment, Intelligent Asset, Intelligent Version (HOUP/OTA), Intelligent Fault (Disk & Memory prediction), and Intelligent Energy Efficiency Management.**
- **Server Profile rules: Delete is allowed ONLY when not bound to any server; Modify is allowed ONLY when not applied to any server.**
- **FusionDirector OS deployment is out-of-band (requires Smart Provisioning + license, no PXE/DHCP/TFTP needed), has a 2-hour timeout, and deploys up to 30 devices concurrently.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Do not confuse the Server Profile edit vs. delete restrictions (p. 383/414): You can DELETE a profile only when it is NOT BOUND to any server; you can MODIFY a profile only when it is NOT APPLIED to any server!

> [!WARNING]
> EXAM TRAP: In FusionDirector Automatic Go-Online Planning (p. 385), Location planning (via iRM U-marks) and SN/MAC planning (via DHCP) are mutually exclusive — enabling one automatically disables the other!

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`04-Exercise-FusionDirector-Device-Adding-and-Intelligent-Features-Lab.html`](./04-Exercise-FusionDirector-Device-Adding-and-Intelligent-Features-Lab.html)** (or [`04-Exercise-FusionDirector-Device-Adding-and-Intelligent-Features-Lab.md`](./04-Exercise-FusionDirector-Device-Adding-and-Intelligent-Features-Lab.md)) to apply this concept in an interactive lab workbench!
