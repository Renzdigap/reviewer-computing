# 📖 Logical Volume Management (LVM) — PV, VG, LV Creation, Online Expansion & Reduction

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 06 — openEuler Disk Partitioning, LVM & Network Management (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `06-Exercise-LVM-PV-VG-LV-and-Resize-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.05, pp. 283–300

---

## 🎯 Learning Objectives
- Define the 5 core LVM components: Physical Volume (PV), Volume Group (VG), Physical Extent (PE — default 4 MB), Logical Extent (LE), and Logical Volume (LV)
- Create and inspect PVs, VGs, and LVs using `pvcreate`/`pvs`, `vgcreate`/`vgs`, and `lvcreate`/`lvs`
- Execute online LV capacity expansion (`lvextend` + `resize2fs`) and safe offline LV capacity reduction (`umount` -> `e2fsck -f` -> `resize2fs` -> `lvreduce` -> `mount`)

---

### 1. LVM Architecture & Core Components
**Logical Volume Management (LVM)** is a logical storage layer built **above physical disks/partitions and below file systems**, enabling dynamic capacity expansion/reduction, disk striping, mirroring, and snapshots.

| Component | Definition & Key Rules (Ch.05, pp. 284–285) |
| :--- | :--- |
| **PV (Physical Volume)** | Underlying physical drive (`/dev/sdd`) or partition (`/dev/sdb1`, partition ID changed from `83` to **`8e`** in `fdisk`). |
| **VG (Volume Group)** | Storage pool combining **one or more PVs** (`VG` shields underlying PV boundaries). |
| **PE (Physical Extent)** | **Smallest unit that can be addressed by LVM.** Default size is **4 MB**. **Once a VG's PE size is determined (`vgcreate -s`), it CANNOT be changed**, and all PVs in the same VG share the same PE size. |
| **LE (Logical Extent)** | **Minimum storage unit that can be allocated** in LVM. In the same VG, **LE size = PE size** (1:1 correspondence). |
| **LV (Logical Volume)** | Logical partition carved out of a VG, formatted with `mkfs` and mounted for end users. |

---

### 2. LVM Creation & Management Commands
1. **PV Commands:**
   * Create: **`pvcreate /dev/hda{6,7,8,9}`** (options: `-f` force, `-u` UUID, `-y` answer yes).
   * Inspect/Manage: **`pvs`** (concise overview), **`pvdisplay`** (detailed), **`pvscan`**, **`pvchange`**, **`pvresize`**, **`pvremove`**, **`pvmove`**, **`pvck`**.
2. **VG Commands:**
   * Create: **`vgcreate [-l max_LV] [-p max_PV] [-s PE_size] vg1000 /dev/sdb1 /dev/sdb2`**
   * Inspect/Manage: **`vgs`**, **`vgdisplay`**, **`vgscan`**, **`vgextend`** (add PVs to VG), **`vgreduce`** (remove PV from VG after moving data), **`vgremove`**, **`vgrename`**, **`vgchange`**, **`vgcfgbackup`**, **`vgcfgrestore`**, **`vgimport`**, **`vgexport`**.
3. **LV Commands:**
   * Create: **`lvcreate -L 200M [-n lvname] vg1000`** (`-L` specifies size in K/M/G/T; **`-l`** specifies number of **LEs**; **`-s`** creates a snapshot).
   * Inspect/Manage: **`lvs`**, **`lvdisplay [-m]`**, **`lvscan`**, **`lvextend [--resizefs]`**, **`lvreduce`**, **`lvresize`**, **`lvremove`**, **`lvrename`**, **`lvconvert`**.

---

### 3. Expanding vs. Reducing LV Capacity (High-Yield Exam Workflows!)
* **Expanding LV Capacity (Supports ONLINE expansion without unmounting! — Ch.05, p.298):**
  1. Run **`vgs`** to check if the VG has sufficient free space (if not, run `vgextend`).
  2. Expand the LV: **`lvextend -L +SIZE lv_device`** (or `lvresize -L +200M /dev/vg1000/lvol0`).
  3. Resize the `ext4` file system online: **`resize2fs device`** (or use `lvextend --resizefs` in newer versions).
* **Reducing LV Capacity (Risky — MUST unmount and shrink file system FIRST! — Ch.05, p.299):**
  1. Determine target size and verify enough space for existing data.
  2. Unmount the file system (**`umount`**) and run a forcible check (**`e2fsck -f device`**).
  3. **Shrink the file system first:** **`resize2fs device TARGET_SIZE`**.
  4. **Shrink the LV second:** **`lvreduce -L TARGET_SIZE lv_device`**.
  5. **Mount** the file system again (**`mount`**).

---

## 🔑 Key Takeaways
- **The default Physical Extent (PE) size in LVM is 4 MB; once set during vgcreate, a VG's PE size cannot be changed, and LE size equals PE size within the same VG.**
- **In lvcreate/lvresize, uppercase '-L' specifies capacity in bytes (K/M/G/T), whereas lowercase '-l' specifies the number of Logical Extents (LEs).**
- **LV expansion can be done ONLINE without unmounting (vgs -> lvextend -> resize2fs), whereas LV reduction MUST be done OFFLINE in strict order: umount -> e2fsck -f -> resize2fs -> lvreduce -> mount.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Never run 'lvreduce' BEFORE 'resize2fs'! When expanding, you expand the LV first (lvextend) and the file system second (resize2fs); when reducing, you MUST unmount, check (e2fsck -f), shrink the file system first (resize2fs), and shrink the LV second (lvreduce)!

> [!WARNING]
> EXAM TRAP: When using fdisk to create a partition for LVM, the default partition ID is 83 (Linux); change it to 8e (Linux LVM) before running pvcreate.

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-LVM-PV-VG-LV-and-Resize-Lab.html`](./06-Exercise-LVM-PV-VG-LV-and-Resize-Lab.html)** (or [`06-Exercise-LVM-PV-VG-LV-and-Resize-Lab.md`](./06-Exercise-LVM-PV-VG-LV-and-Resize-Lab.md)) to apply this concept in an interactive lab workbench!
