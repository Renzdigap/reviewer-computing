# Persistent Storage, File Systems & Disk Partitioning (`fdisk`, `parted`, MBR vs. GPT)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 06 — openEuler Disk Partitioning, LVM & Network Management (Sprint 1 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `02-Exercise-Fdisk-and-Parted-Partitioning-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.05, pp. 256–276

---

## Learning Objectives
- Identify the 3 persistent storage layers, openEuler's default file system (`ext4`), and commands to view file system/disk info (`lsblk -f`, `blkid`, `df -T`, `fdisk -l`, `df -h`)
- Decode Linux disk and partition device names (`/dev/xxyN`) across IDE (`hd`), SCSI/SATA/SAS/SSD (`sd`), and virtio (`vd`) drives
- Compare MBR vs. GPT partitioning limits and partition drives using `fdisk` and `parted`

---

### 1. Persistent Storage Layers, File Systems & Disk Inspection
* **3 Layers of Linux Persistent Storage:** (1) **File system** (organizes/manages file data), (2) **Disk partitions** (logical sections), (3) **Physical drives** (HDD, SSD, NVMe).
* **File Systems on openEuler:**
  * **Default file system on openEuler:** **`ext4`** (Ch.05, p.259).
  * Other supported file systems: **XFS** (high-performance journaling FS by Silicon Graphics, excels at large files), **VFAT** (DOS/Windows FAT16/FAT32), **NFS** (UNIX network file sharing), **ISO 9660** (optical discs/ISOs), **Btrfs**, etc.
  * **Check File System Type:** **`lsblk -f`**, **`blkid`**, or **`df -T`**.
  * **Check Disk & Mount Space:** **`fdisk -l`** (lists all mounted and unmounted disks/partitions) and **`df -h`** (checks mounted disk space and usage).
* **Disk Interfaces:** **IDE (PATA / parallel port)**, **SATA (serial port)**, **SCSI / SAS** (server-grade, hot-swappable, high stability), and **Fibre Channel (FC)**.

---

### 2. Device Naming (`/dev/xxyN`) & Partition Types
In `/dev/xxyN`:
* **`xx` (Device Type):** **`hd`** (IDE disk), **`sd`** (SCSI, SAS, SATA, and SSD disks), **`vd`** (virtio virtual disk), **`fd`** (floppy disk).
* **`y` (Device Letter):** `a` = 1st disk, `b` = 2nd disk (e.g., `/dev/hda` = 1st IDE disk, `/dev/sdb` = 2nd SCSI/SATA disk).
* **`N` (Partition Number):**
  * **`1 to 4`:** Reserved for **Primary partitions** or the **Extended partition** (at most **1 extended partition** per disk, which cannot be used directly until divided into logical partitions).
  * **`5 and above`:** **Logical partitions ALWAYS start from 5!** Example: **`/dev/sdb6` is the second logical partition on the second SCSI disk**!

---

### 3. MBR (`fdisk`) vs. GPT (`parted`)
| Feature | MBR (Master Boot Record — `fdisk`) | GPT (GUID Partition Table — `parted`) |
| :--- | :--- | :--- |
| **Firmware & Address Bits** | Legacy **BIOS**; **32-bit** sector values. | **UEFI** standard; **64-bit** LBA values. |
| **Max Disk/Partition Size** | **2 TB** maximum (`fdisk` does not support >2 TB). | **18 EB** maximum (supports >2 TB). |
| **Max Partitions** | **4 primary** (or 3 primary + 1 extended). Total usable: **SCSI max 15** (4 primary or 12 logical); **IDE max 63** (4 primary or 60 logical). | **128 partitions** per disk (no primary/extended/logical distinction). |
| **Interactive Commands** | `fdisk /dev/sdb`: **`n`** (new: `p` primary, `e` extended, `l` logical), **`d`** (delete), **`p`** (print table), **`l`** (list IDs: `82` swap, `83` Linux, **`8e` Linux LVM**), **`t`** (change ID), **`w`** (save & exit), **`q`** (quit without saving). | `parted /dev/sdb`: **`mklabel gpt`** (set GPT table), **`mkpart`** (create partition), **`print`**, **`resizepart`**, **`rm`**, **`quit`**. Non-interactive: `parted /dev/sdb mklabel gpt` -> `parted /dev/sdb mkpart primary 0 1000`. |

---

## Key Takeaways
- **The default file system on openEuler is ext4; check file system types using 'lsblk -f', 'blkid', or 'df -T'.**
- **In /dev/xxyN, partitions 1–4 are primary or extended partitions, and logical partitions ALWAYS start at 5 (so /dev/sdb6 is the 2nd logical partition on the 2nd SCSI disk).**
- **MBR (fdisk) is limited to 2 TB and 4 primary partitions (or 3 primary + 1 extended), whereas GPT (parted) supports up to 18 EB and 128 partitions.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Even if you create only 1 primary partition (/dev/sdb1) and 1 extended partition (/dev/sdb2), the very first logical partition inside that extended partition is ALWAYS numbered 5 (/dev/sdb5), and the second logical partition is /dev/sdb6!

> [!WARNING]
> EXAM TRAP: In fdisk, partition ID '83' is standard Linux, '82' is Linux swap, and '8e' is Linux LVM (must change 83 to 8e using 't' when preparing a partition for LVM).

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`02-Exercise-Fdisk-and-Parted-Partitioning-Lab.html`](./02-Exercise-Fdisk-and-Parted-Partitioning-Lab.html)** (or [`02-Exercise-Fdisk-and-Parted-Partitioning-Lab.md`](./02-Exercise-Fdisk-and-Parted-Partitioning-Lab.md)) to apply this concept in an interactive lab workbench!
