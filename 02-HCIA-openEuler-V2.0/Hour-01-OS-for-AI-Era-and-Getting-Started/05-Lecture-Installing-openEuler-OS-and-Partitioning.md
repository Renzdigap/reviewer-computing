# 📖 Installing openEuler OS, Hardware Architectures & Partition Planning

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 01 — OS for the AI Era & Getting Started with openEuler (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `06-Exercise-openEuler-Installation-and-Partition-Plan-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.02, pp. 38–45, 52

---

## 🎯 Learning Objectives
- Identify the 6 processor architectures and 4 application scenarios supported by openEuler
- Distinguish manual installation (USB, CD-ROM, Virtual CD-ROM/ISO) vs. batch automated installation using Kickstart
- Configure recommended boot/system partitions (/, /boot, /boot/efi, swap) and Software Selection profiles (Minimum, Server, Hypervisor)

---

### 1. Pre-Installation Planning: Architectures, Scenarios & Modes
Before installing openEuler, administrators must match the installation ISO package to both the target **chip architecture** and **application scenario** (packages across different architectures are incompatible):
* **6 Supported Processor Architectures:** **x86**, **Arm (AArch64)**, **SW64**, **RISC-V**, **LoongArch**, and **PowerPC**.
* **4 Application Scenarios:** **Server**, **Cloud Computing**, **Edge Computing**, and **Embedded Systems**.
* **Installation Modes:**
  * **Individual Setup:** USB drives, physical CD-ROMs, or virtual CD-ROM drives (mounting `.iso` image).
  * **Batch Installation:** Automated installation using the **Kickstart** tool, which supports:
    1. **Semi-automatic installation:** Specify the location of the kickstart file; Kickstart configures keyboard, language, and partitions automatically.
    2. **Full automation:** The entire OS installation is automated without manual intervention.

---

### 2. Boot Menu & Recommended System Partitions
When booting from the openEuler 24.03/20.03 LTS ISO:
* **Boot Menu Options:**
  * `Install openEuler 24.03 LTS`: Directly install the system.
  * `Test this media & install openEuler 24.03 LTS`: Check the software package integrity first, then install.
  * `Troubleshooting -->`: Rescue and diagnostic mode.
  * Keybindings: `▲`/`▼` to select, **`e`** to edit the selected boot item, or **`c`** for a command prompt.
* **Recommended Manual Partitions (`Installation Destination`):**
  In manual partitioning mode, you can configure **common (standard) partitions**, **logical volumes (LVM)**, or **thin-provisioning logical volumes**:

| Partition / Mount Point | Purpose & Sizing Guideline |
| :--- | :--- |
| **`/` (Root partition)** | **Everything in Linux starts from the root partition.** Stores core OS directories. |
| **`/boot`** | Stores kernel and boot loader files required for system booting. |
| **`/boot/efi`** | Boot device and application program started by the **Extensible Firmware Interface (EFI/UEFI)**. |
| **`swap`** | Virtual memory swap partition used to swap dirty data from RAM when memory is insufficient. **Sizing rule:** If physical memory is small, set `swap` to **twice (2×) the memory size**; if memory is large, reduce the swap ratio accordingly. |

---

### 3. Software Selection & Root/User Account Creation
* **3 Software Selection Base Environments (openEuler 24.03 LTS):**
  1. **Minimum installation:** Most software is not installed (default CLI); ideal for learning Linux architecture or minimal footprint servers.
  2. **Server:** Installs software packages tailored for enterprise server scenarios.
  3. **Hypervisor:** Installs virtualization host software packages.
* **Root Password & User Creation:**
  * `root` is the super administrator with the highest permissions.
  * **Official Ch.02 Quiz Q1 Note:** Page 45 states *"During openEuler installation, you need to set the password of the root user. You can create a common user as required."* However, **Official Ch.02 Quiz Q1 (p.52)** states: *"(True or false) You do not need to specify the password of the root user during the openEuler OS installation. However, you must specify the password of the root user when logging in to the OS after the installation."* -> **Official Answer Key: A (True)**. Remember this exact wording if it appears verbatim on the exam!

---

## 🔑 Key Takeaways
- **openEuler supports 6 processor architectures: x86, Arm, SW64, RISC-V, LoongArch, and PowerPC, across 4 scenarios: Server, Cloud, Edge, and Embedded.**
- **For batch automated installations, openEuler uses the Kickstart tool (semi-automatic or full automation).**
- **Recommended partitions are /, /boot, /boot/efi, and swap (set swap to 2x RAM when memory is small); software selection offers Minimum installation, Server, and Hypervisor.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Official Ch.02 Quiz Q1 Verbatim Key): In the official Ch.02 Quiz (p.52), the statement 'You do not need to specify the password of the root user during the openEuler OS installation. However, you must specify the password of the root user when logging in to the OS after the installation' is keyed as A (True). Memorize this exact official answer key!

> [!WARNING]
> EXAM TRAP: At the GRUB installation menu, pressing 'e' edits the selected boot item, while pressing 'c' opens a command prompt.

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-openEuler-Installation-and-Partition-Plan-Lab.html`](./06-Exercise-openEuler-Installation-and-Partition-Plan-Lab.html)** (or [`06-Exercise-openEuler-Installation-and-Partition-Plan-Lab.md`](./06-Exercise-openEuler-Installation-and-Partition-Plan-Lab.md)) to apply this concept in an interactive lab workbench!
