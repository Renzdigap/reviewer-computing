# OS Compatibility & Installing openEuler 22.03 LTS on TaiShan 2280

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 07 — OS Compatibility, openEuler 22.03 LTS Installation, Drivers/Firmware & Service Deployment (Sprint 1 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `02-Exercise-Mounting-ISO-and-openEuler-Partitioning-Lab` (7 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.05, pp. 326–332, 346

---

## Learning Objectives
- Verify OS and hardware component compatibility using the Kunpeng Computing Compatibility Checker before OS installation
- Mount `openEuler-22.03-LTS-aarch64-dvd.iso` via the iBMC Remote Virtual Console and select the DVD-ROM drive boot option (Ch.05 Quiz Q1!)
- Trace the complete openEuler 22.03 LTS installation flow and custom storage partitioning (`/boot`, `/boot/efi`, `swap`, `/`)

---

### 1. Server OS & Component Compatibility Check (pp. 327–328)
- Before installing an OS on a server, you **must check both OS compatibility and component compatibility** of the server.
- **TaiShan 200 (model 2280) Supported OSs**: Supports **CentOS, Ubuntu, openEuler**, SUSE, Kylin, EulerOS, etc.
- **Official Tool**: Query the **Kunpeng Computing Compatibility Checker** (`https://info.support.huawei.com/computing/ftca/en/product/taishan-server`).

---

### 2. Mounting an ISO File & Boot Option Selection (p. 329 — Official Quiz Q1!)
To install **openEuler 22.03 LTS (`openEuler-22.03-LTS-aarch64-dvd.iso`)** via the iBMC WebUI:
1. Log in to the **Remote Virtual Console** through the iBMC WebUI.
2. On the virtual console menu bar, mount the image file **`openEuler-22.03-LTS-aarch64-dvd.iso`** to the virtual **DVD-ROM** and change the boot option to **`DVD-ROM drive`** (Official Ch.05 Quiz Q1 on p. 346!).
3. Restart the server and select **`Install openEuler 22.03-LTS`** in the GRUB installation menu.
4. Select the language for installation on the openEuler welcome page.

---

### 3. Complete openEuler 22.03 LTS Installation Workflow & Partitioning (pp. 330–332)
```
[OS language selection]
         |
         v
[Installation Summary Page]
  |-- 1. Software selection (e.g., Minimal Install / Server with GUI)
  |-- 2. Installation drive & Partition configuration (Automatic vs. Custom)
  |-- 3. Optional configurations:
  |       - Root password setting
  |       - User creation
  |       - Network configuration
  |       - Host name configuration
         |
         v
[OS installation] --> [Reboot and ISO file detachment]
```
- **Partition Configuration (pp. 331–332)**:
  - By default, partitions are configured **automatically**; select **`Custom`** under *Storage Configuration* for manual partitioning.
  - Standard UEFI AArch64 partitions on TaiShan 200:
    - **`/boot/efi`**: EFI System Partition (required for UEFI boot on Arm64)
    - **`/boot`**: Stores kernel and initramfs boot loader files
    - **`swap`**: Virtual memory swap partition
    - **`/`**: Root file system partition
  - Once installation completes, **detach the ISO file** from the virtual DVD-ROM and click **Reboot System**.

---

## Key Takeaways
- **Always check both OS compatibility and component compatibility using the Kunpeng Computing Compatibility Checker before installing an OS.**
- **To install openEuler using `openEuler-22.03-LTS-aarch64-dvd.iso` on the iBMC Remote Virtual Console, select the 'DVD-ROM drive' boot option (Ch.05 Quiz Q1).**
- **Partitions are configured automatically by default; choose 'Custom' under Storage Configuration to manually create `/boot/efi`, `/boot`, `swap`, and `/`, and detach the ISO before rebooting.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.05 Quiz Q1): 'To install the OS using the openEuler-22.03-LTS-aarch64-dvd.iso file, which of the following boot options needs to be used?' -> B. DVD-ROM drive (NOT Hard disk drive, Floppy drive, or PXE)!

> [!WARNING]
> EXAM TRAP: Remember to detach the virtual ISO file at the end of OS installation before rebooting, or the server may boot back into the installer if DVD-ROM is set as permanent first boot device.

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`02-Exercise-Mounting-ISO-and-openEuler-Partitioning-Lab.html`](./02-Exercise-Mounting-ISO-and-openEuler-Partitioning-Lab.html)** (or [`02-Exercise-Mounting-ISO-and-openEuler-Partitioning-Lab.md`](./02-Exercise-Mounting-ISO-and-openEuler-Partitioning-Lab.md)) to apply this concept in an interactive lab workbench!
