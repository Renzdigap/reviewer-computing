# 📖 Drive Interfaces (SATA/SAS/NVMe), Form Factors & IOPS Benchmarks

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 03 — Server Hardware Architecture: CPU, Memory, Mainboard & Storage Drives (Sprint 4 of 4)  
**Format:** Bite-Sized Lecture (8 mins) → Followed immediately by `08-Exercise-Drive-Interface-Rates-and-IOPS-Benchmark-Lab` (8 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.03, pp. 155–158

---

## 🎯 Learning Objectives
- Physically and logically distinguish SATA, SAS, and PCIe (NVMe) drive interfaces and their 1.0/2.0/3.0 transmission rates
- Explain NVMe advantages and 3.5-inch LFF vs. 2.5-inch SFF physical dimensions
- Compare 4 KB Random Write IOPS and 128 KB Sequential Read Bandwidth across all 6 drive types

---

### 1. Drive Interfaces: SATA vs. SAS vs. PCIe (NVMe) (pp. 155–156)
Mainstream server drives use **SATA**, **SAS**, and **PCIe (NVMe)** interfaces:
- **Physical Connector Distinction (p. 155)**:
  - **SATA interface**: Has a **physical gap (notch)** between the power and data pin segments.
  - **SAS interface**: **Does NOT have a gap** between the segments, and features a **secondary edge connector on the back** (enabling dual-port multipath access and higher rates). SAS backplanes are compatible with SATA drives, but SATA backplanes cannot accept SAS drives.
- **Transmission Rates by Protocol Version (p. 155)**:

| Interface Type | Version 1.0 | Version 2.0 | Version 3.0 |
| :--- | :---: | :---: | :---: |
| **SAS** | **3 Gbit/s** | **6 Gbit/s** | **12 Gbit/s** |
| **SATA** | **1.5 Gbit/s** | **3 Gbit/s** | **6 Gbit/s** (600 MB/s) |

- **NVMe (Non-Volatile Memory Express, pp. 156, 225)**:
  - A driver and protocol standard for high-performance **PCIe SSDs** that unifies PCIe SSD drivers from various vendors and integrates them into the OS. Its external physical interface is **PCIe**.
  - **Two Key Advantages**:
    1. **High performance**: Directly connects to CPUs through the **PCIe bus**, bypassing SAS/SATA controllers to deliver ultra-high IOPS, high bandwidth, and low latency.
    2. **Standardization**: Mature OS driver ecosystem.

---

### 2. Drive Physical Form Factors: LFF vs. SFF (p. 157)
Although SSDs have no spinning platters, they use the same form factors as HDDs:
- **3.5-inch HDD — LFF (Large Form Factor)**:
  - H × W = 147 mm × 101.85 mm, enterprise depth = 26.1 mm.
- **2.5-inch HDD — SFF (Small Form Factor)**:
  - H × W = 100.45 mm × 69.85 mm, enterprise depth = 15 mm.
- **2.5-inch SSD — SFF (Small Form Factor)**:
  - H × W = 100.45 mm × 69.85 mm, depth can be **7 mm, 9.5 mm, or 15 mm** (never exceeds 15 mm).

---

### 3. Key Performance Indicators (KPIs) & Benchmark Table (p. 158)
The 5 key drive performance indicators are: **Drive capacity (volume)**, **Rotational speed (HDDs only)**, **Average access time**, **Data transfer rate (bandwidth)**, and **IOPS (Input/Output Operations Per Second)**.

| Drive Type | IOPS (4 KB Random Write) | Bandwidth (128 KB Sequential Read) |
| :--- | :---: | :---: |
| **SATA HDD** | **330** | **200 MB/s** |
| **SAS 10K HDD** | **350** | **195 MB/s** |
| **SAS 15K HDD** | **450** | **290 MB/s** |
| **SATA SSD** | **30–60K** | **540 MB/s** |
| **SAS SSD** | **155K** | **1000 MB/s** |
| **NVMe SSD** | **300K** | **3500 MB/s** |

---

## 🔑 Key Takeaways
- **SATA 1.0/2.0/3.0 rates are 1.5 / 3 / 6 Gbit/s; SAS 1.0/2.0/3.0 rates are 3 / 6 / 12 Gbit/s.**
- **A SATA connector has a gap between pin sections; a SAS connector has no gap and includes a back-side connector.**
- **3.5-inch drives are LFF (147 mm × 101.85 mm × 26.1 mm); 2.5-inch drives are SFF (100.45 mm × 69.85 mm, depth <= 15 mm).**
- **NVMe SSD connects directly to the CPU via PCIe, delivering ~300K IOPS (4 KB random write) and ~3500 MB/s (128 KB sequential read).**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Do not confuse SAS 3.0 (12 Gbit/s) with SATA 3.0 (6 Gbit/s / 600 MB/s)!

> [!WARNING]
> EXAM TRAP: LFF stands for 3.5-inch drives, while SFF stands for 2.5-inch drives (and 2.5-inch SSD depth never exceeds 15 mm).

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`08-Exercise-Drive-Interface-Rates-and-IOPS-Benchmark-Lab.html`](./08-Exercise-Drive-Interface-Rates-and-IOPS-Benchmark-Lab.html)** (or [`08-Exercise-Drive-Interface-Rates-and-IOPS-Benchmark-Lab.md`](./08-Exercise-Drive-Interface-Rates-and-IOPS-Benchmark-Lab.md)) to apply this concept in an interactive lab workbench!
