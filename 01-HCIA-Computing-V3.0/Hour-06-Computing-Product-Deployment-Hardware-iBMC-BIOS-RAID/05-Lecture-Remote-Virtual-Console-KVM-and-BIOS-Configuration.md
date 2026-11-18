# 📖 Remote Virtual Console (KVM) & BIOS/PXE Configuration

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 06 — Computing Product Deployment: Equipment Room, iBMC, BIOS & RAID Configuration (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `06-Exercise-BIOS-POST-Boot-Order-and-PXE-Configuration-Lab` (7 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.05, pp. 309–317

---

## 🎯 Learning Objectives
- Distinguish Private vs. Shared modes of Java and HTML5 Integrated Remote Consoles on iBMC
- Master BIOS entry keys (`Delete` or `F4`), the 7-step BIOS POST sequence, and saving changes (`F10`)
- Configure Boot Sequence (`Boot > Boot Type Order`), onboard NIC UEFI PXE (`Advanced > LOM Configuration > PXE Configuration`), and iBMC WebUI `System > BIOS Settings`

---

### 1. iBMC Remote Virtual Console (KVM): Private vs. Shared Modes (p. 310)
On the iBMC WebUI **Home** page, clicking **Virtual Console \rightarrow Start** offers four options across **Java** and **HTML5** Integrated Remote Consoles:
- **Java / HTML5 Integrated Remote Console (Private)**: Allows **only 1 local user or VNC user** to access and operate the server through iBMC at a time.
- **Java / HTML5 Integrated Remote Console (Shared)**: Allows **up to 2 local users or 5 VNC users** to simultaneously access and perform operations on the server through iBMC (each user can view operations performed by the others).

---

### 2. Entering the BIOS & The 7-Step POST Sequence (pp. 311–312)
- **Entering BIOS Setup (p. 311)**: Power on or reset the server from the Remote Virtual Console, press **`Delete` or `F4`** when the boot menu appears, and enter the BIOS password (default: **`Admin@9000`**).
- **Power-On Self-Test (POST) 7-Step Sequence (p. 312)**:
  1. **Initialization of the data bus and control bus** (enables inter-device data transmission)
  2. **CPU self-check** (checks model, frequency, functions, caches; sets CPU operating mode)
  3. **Memory self-check** (verifies presence, capacity, speed; configures operating mode and clock frequency)
  4. **Graphics card self-check** (checks model and video memory capacity; sets display mode)
  5. **Self-check of drives and other devices** (checks HDDs/SSDs, optical drive, USB peripherals)
  6. **Result presentation** (presents self-check result via **beep codes** or **on-screen messages**)
  7. **OS startup** (loads OS from bootable device and hands over control to the OS)

---

### 3. Key BIOS Configuration Tasks & iBMC BIOS Settings (pp. 313–317)
| BIOS Configuration Task | Exact Menu Path & Keybindings (pp. 313–317) |
| :--- | :--- |
| **Configure iBMC IP/User** | **`Advanced > IPMI iBMC Configuration > iBMC Configuration`** |
| **Set System Date & Time** | **`Main > System Date`** or **`Main > System Time`** |
| **Set Boot Sequence** | **`Boot > Boot Type Order`**: Use **`+` or `-`** keys to move a boot option up or down, then press **`F10`** (*Save configuration changes and exit?* \rightarrow **Yes**). |
| **Configure PXE for Onboard NIC** | **`Advanced > LOM Configuration > PXE Configuration`**: Select `PXE1 Configuration` \rightarrow **`Enable`**, set **PXE Boot Capability** to **`UEFI: IPv4`**, **`UEFI: IPv6`**, or **`UEFI: IPv4/IPv6`**, then press **`F10`** to save and restart. |
| **Set Preferred Boot Medium via iBMC WebUI** | **`System > BIOS Settings`**: Select the preferred boot medium to take effect **one time** or **permanently**. |

---

## 🔑 Key Takeaways
- **Remote Virtual Console (Private) allows 1 local or VNC user; (Shared) allows up to 2 local users or 5 VNC users simultaneously.**
- **Press Delete or F4 during boot to enter the TaiShan 200 BIOS; use + or - to adjust Boot Type Order; press F10 to save and exit.**
- **The 7-step BIOS POST order is: Data/control bus init -> CPU self-check -> Memory self-check -> Graphics card self-check -> Drives/peripherals self-check -> Result presentation (beep codes/messages) -> OS startup.**
- **Enable PXE for the onboard NIC at Advanced > LOM Configuration > PXE Configuration (supports UEFI: IPv4, UEFI: IPv6, or UEFI: IPv4/IPv6).**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: In Shared mode of the HTML5/Java Integrated Remote Console, the concurrency limit is up to 2 local users OR 5 VNC users (not 10 users)!

> [!WARNING]
> EXAM TRAP: To enter the BIOS on a TaiShan 200 (2280) server, press `Delete` or `F4` (and press `F10` to save and exit).

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-BIOS-POST-Boot-Order-and-PXE-Configuration-Lab.html`](./06-Exercise-BIOS-POST-Boot-Order-and-PXE-Configuration-Lab.html)** (or [`06-Exercise-BIOS-POST-Boot-Order-and-PXE-Configuration-Lab.md`](./06-Exercise-BIOS-POST-Boot-Order-and-PXE-Configuration-Lab.md)) to apply this concept in an interactive lab workbench!
