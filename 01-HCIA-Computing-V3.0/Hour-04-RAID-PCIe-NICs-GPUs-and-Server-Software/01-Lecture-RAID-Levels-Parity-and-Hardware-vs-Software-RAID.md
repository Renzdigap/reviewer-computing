# 📖 RAID Levels, Parity, Hot Spare & Hardware vs. Software RAID

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 04 — RAID Arrays, PCIe Bus, NICs/iNICs, GPU/NPU, Power/Cooling & Server Software (Sprint 1 of 4)  
**Format:** Bite-Sized Lecture (8 mins) → Followed immediately by `02-Exercise-RAID-Capacity-Fault-Tolerance-and-Parity-Lab` (8 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.03, pp. 159–169

---

## 🎯 Learning Objectives
- Understand the 3 core RAID technologies (Data striping, Mirroring, Data parity) and calculate utilization and fault tolerance for RAID 0, 1, 1E, 5, 6, 10, 01, 50, and 60
- Explain Global vs. Dedicated Hot Spare and why RAID is NOT a substitute for data backup
- Contrast Software RAID (and its 6 unsupported features) with Built-in and External Hardware RAID

---

### 1. RAID Core Technologies & Standard/Nested Levels (pp. 159–163)
Proposed by **Prof. D.A. Patterson** at UC Berkeley in **1988**, **RAID (Redundant Array of Independent Disks)** combines multiple physical disks into logical disks/volumes (**LUNs**) using **Data striping**, **Mirroring**, and **Data parity** (XOR or Galois field P+Q).

| RAID Level | Min Disks | Drive Utilization (N disks, M spans) | Fault Tolerance & Key Mechanism (pp. 160–163) |
| :--- | :---: | :---: | :--- |
| **RAID 0** | ≥ 1 (or ≥ 2) | **100%** (N) | **0 failed disks**. Striping only; highest read/write speed, **low reliability** (graphics workstations). |
| **RAID 1** | ≥ 2 (2N) | **50%** (N/2) | **1 disk per mirror pair**. Mirroring only; high reliability & read speed, medium write speed. |
| **RAID 1E** | ≥ 3 | **50%** (N/2) | Each disk has two stripe groups where the next stripe group holds the **right-shifted misplaced mirror** of the previous stripe group. Tolerates **1 disk offline** (or **2 non-adjacent disks** if ≥ 4 disks, provided first and last disks do not fail together). |
| **RAID 5** | ≥ 3 | **$(N - 1)/N** | **1 failed disk**. Cyclically distributed XOR parity (P_0 = D_0 \oplus D_1$). Single disk failure causes performance degradation during rebuild. |
| **RAID 6** | ≥ 4 | **$(N - 2)/N** | **2 failed disks simultaneously**. Two independent distributed parity codes: **P** (P_0 = D_0 \oplus D_1) and **Q** (Q_0 = (D_0 \cdot K_0) \oplus (D_1 \cdot K_1)$ in Galois field). |
| **RAID 10 vs. 01** | ≥ 4 (even) | **50%** | **RAID 10** mirrors first (RAID 1) then stripes (RAID 0); tolerates 1 failed disk per RAID 1 span. **RAID 01** stripes first (RAID 0) then mirrors (RAID 1) — losing 1 disk loses an entire stripe and degrades the array into a non-redundant RAID 0! |
| **RAID 50** | ≥ 6 | **$(N - M)/N** | **RAID 5 first, then RAID 0** across M spans (≥ 2 spans × 3 disks = 6$ disks min). Tolerates 1 disk failure per RAID 5 span. |
| **RAID 60** | ≥ 8 (theory) | **$(N - 2M)/N** | **RAID 6 first, then RAID 0** across M spans (≥ 2 spans × 4 disks = 8$ disks min on p.161–162). Tolerates 2 disk failures per RAID 6 span. |

---

### 2. Hot Spare, Reconstruction & Why RAID != Backup (pp. 164–165)
- **Hot Spare**: Automatically replaces a faulty disk in a redundant RAID group and triggers **reconstruction**:
  - **Global Hot Spare**: Shared by **all** redundant RAID groups in the system.
  - **Dedicated Hot Spare**: Dedicated to **one specific** redundant RAID group.
- **RAID Cannot Replace Data Backup (p. 165)**: RAID only protects against physical disk failures; it **cannot** prevent data loss from **viruses, human error, accidental deletion, or OS/file system corruption**.

---

### 3. Software RAID vs. Hardware RAID (Built-in & External) (pp. 166–169)
- **Software RAID (p. 167)**: Executed by OS kernel disk code using host **CPU** (high CPU overhead for RAID 5 XOR). **Six functions NOT supported by Software RAID**:
  1. Hot swap of hard disks
  2. Hot spare of hard disks
  3. Remote array management
  4. Bootable arrays
  5. Array configuration on hard disks
  6. S.M.A.R.T. for disks
- **Built-in Hardware RAID**: Uses a PCIe RAID controller card (e.g., **Avago MegaRAID SAS 9440-8i** with Mini-SAS **SFF-8643** ports, heat sink, heartbeat LED, and chip overtemperature LED) with its own independent processor and cache memory; supports bootable arrays.
- **External Hardware RAID**: Independent external disk array subsystem connected via standard controller; supports dual controllers, hot swap, and ultra-large capacity.

---

## 🔑 Key Takeaways
- **Drive utilization formulas: RAID 0 = 100%, RAID 1 / 10 / 1E = 50%, RAID 5 = (N-1)/N, RAID 6 = (N-2)/N, RAID 50 = (N-M)/N, RAID 60 = (N-2M)/N.**
- **RAID 10 mirrors first (RAID 1) then stripes (RAID 0) and is more fault-tolerant than RAID 01 (which stripes first then mirrors).**
- **RAID 50 requires at least 6 disks (2 × 3-disk RAID 5 spans); theoretical RAID 60 requires at least 8 disks (2 × 4-disk RAID 6 spans).**
- **Software RAID consumes host CPU cycles and does NOT support hot swap, hot spare, remote array management, bootable arrays, or disk S.M.A.R.T.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: RAID CANNOT replace data backup because RAID cannot protect against viruses, accidental file deletion, or OS/filesystem corruption (p. 165)!

> [!WARNING]
> EXAM TRAP: In RAID 1E with >= 4 disks, two offline disks can be tolerated ONLY if they are NOT adjacent (and the first and last disks are not offline simultaneously).

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`02-Exercise-RAID-Capacity-Fault-Tolerance-and-Parity-Lab.html`](./02-Exercise-RAID-Capacity-Fault-Tolerance-and-Parity-Lab.html)** (or [`02-Exercise-RAID-Capacity-Fault-Tolerance-and-Parity-Lab.md`](./02-Exercise-RAID-Capacity-Fault-Tolerance-and-Parity-Lab.md)) to apply this concept in an interactive lab workbench!
