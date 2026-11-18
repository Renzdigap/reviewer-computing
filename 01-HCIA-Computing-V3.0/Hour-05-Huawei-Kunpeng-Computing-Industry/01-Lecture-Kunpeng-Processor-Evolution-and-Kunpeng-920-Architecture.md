# Kunpeng Processor Evolution & Kunpeng 920 Physical Architecture

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 05 — Huawei Kunpeng Processors, TaiShan Servers, openEuler/openGauss & HPC (Sprint 1 of 4)  
**Format:** Bite-Sized Lecture (8 mins) - Followed immediately by `02-Exercise-Kunpeng-920-Die-Cluster-Core-and-HCCS-Lab` (7 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.04, pp. 231–239, 279

---

## Learning Objectives
- Trace Huawei's chip evolution from 1991 ASIC to K3, Kunpeng 912 (Hi1612), Kunpeng 916, and Kunpeng 920
- Master the physical hierarchy of Kunpeng 920: SoC, Chip, Die (2 CPU dies + 1 I/O die via CoWoS), Cluster (8 per die), and Core (4 per cluster)
- Know all Kunpeng 920 performance metrics, HCCS bus (480 Gbit/s, up to 256 cores across 4 sockets), RAS-45, and DEMT

---

### 1. Evolution of Huawei Kunpeng Processors (pp. 231, 233, 236)
Huawei's Kunpeng open hardware platform spans **Processor \rightarrow Single Node ( Kunpeng Open Motherboard / Server) \rightarrow Cluster**, paired with **Kunpeng DevKit** and **Kunpeng BoostKit**:
- **Motherboard Highlights (p. 231)**: **25% higher motherboard performance** (56G SerDes), **15% lower failure rate** than industry average (signal bit error rate BER < 10^{-12}), and **15% higher energy efficiency ratio** via **Dynamic Energy Management Technology (DEMT)**.

| Year | Chip / Processor | Milestone Significance (pp. 233, 236) |
| :---: | :--- | :--- |
| **1991** | First ASIC chip | Huawei's first ASIC chip for transmission networks |
| **2005** | First Arm wireless chip | First Arm-based chip for wireless base stations |
| **2009** | **K3** | First Arm-based mobile smartphone CPU (predecessor of **Kirin**) |
| **2014** | **Kunpeng 912 (Hi1612)** | Huawei's **first Arm-based 64-bit (AArch64) processor** |
| **2016** | **Kunpeng 916** | **Industry's first Arm processor that supports multiple sockets** (data center predecessor) |
| **Jan 2019** | **Kunpeng 920** | **Industry's first 7 nm data center–level Arm processor** |

---

### 2. Kunpeng 920 Physical Hierarchy: SoC, Chip, Die, Cluster & Core (pp. 234–237)
- **Area Density Advantage (p. 235)**: The area of an Arm core is only **1/7** of that of an x86 core; for the same chip size, the number of Arm cores is **more than 4 times** that of x86 cores.
- **Five Physical Architecture Concepts (pp. 234, 237)**:
  1. **SoC (System on a Chip)**: Integrates the **CPU, southbridge, RoCE NIC, SAS/drive controller, and hardware encryption/compression acceleration engines** on a single chip (4 chips integrated into 1!).
  2. **Chip**: Encapsulated package using **Chip on Wafer on Substrate (CoWoS)** packaging technology.
  3. **Die**: Minimum physical silicon unit of a chip. **Kunpeng 920 encapsulates 3 dies**:
     - **2 Compute (CPU) dies**: Each CPU die contains up to **32 cores** (8 clusters × 4 cores) and **4 DDR4 memory controllers** (2 × 4 = 8 DDR4 channels total).
     - **1 I/O die**: Provides **PCIe 4.0/CCIX** interfaces, **100GE RoCE** Ethernet ports, SAS/SATA storage controllers, inter-chip cache coherence interface, and hardware acceleration engines.
  4. **Cluster**: Set of cores; **1 Cluster = 4 Cores**, and **1 CPU Die = 8 Clusters** (8 × 4 = 32 cores/die, 64 cores/processor).
  5. **Core**: Computing unit of the CPU.

---

### 3. HCCS Interconnect & Performance Gains (pp. 237–239 — Official Quiz Q1!)
- **HCCS (Huawei Cache Coherence System, p. 237)**: Provides cache-coherent memory access across kernels, devices, and clusters with up to **480 Gbit/s inter-chip bandwidth**, supporting **2-socket and 4-socket NUMA interconnection** with up to **256 physical cores** (4 × 64).
- **Performance Gains vs. Previous Generation (pp. 238–239)**:
  - **2.9x** single-processor integer computing performance (**3.9x** CPU core performance) and **4x** chip density.
  - **8-channel DDR4 controller**: Increases memory bandwidth by **60%**.
  - **PCIe 4.0 (compatible with PCIe 3.0/2.0/1.0) & CCIX**: Increases total I/O bandwidth by **66%**.
  - **100GE RoCE Ethernet**: Increases network bandwidth by **4x**.
  - **Reliability**: Supports **RAS-45** features.

---

## Key Takeaways
- **Kunpeng processor evolution: 2014 Kunpeng 912 (Hi1612, first 64-bit Arm) -> 2016 Kunpeng 916 (first multi-socket Arm) -> Jan 2019 Kunpeng 920 (first 7nm data center Arm).**
- **Kunpeng 920 encapsulates 3 dies via CoWoS: 2 CPU dies (each with 8 clusters × 4 cores = 32 cores and 4 DDR4 controllers) + 1 I/O die (PCIe 4.0, 100GE RoCE, SAS controller, KAE accelerators).**
- **Huawei Cache Coherence System (HCCS) delivers up to 480 Gbit/s inter-chip bandwidth, connecting up to 4 Kunpeng 920 sockets (256 physical cores).**
- **Kunpeng 920 (Ch.04 Quiz Q1): 7nm process, 8-channel DDR4 (+60% BW), PCIe 4.0 compatible with 3.0/2.0/1.0 (+66% I/O BW), 100GE RoCE (+4x network BW), and multiple built-in accelerators.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Kunpeng 920 has THREE dies in total: TWO CPU dies (32 cores + 4 DDR4 channels each) and ONE I/O die — NOT 4 dies or 1 monolithic die!

> [!WARNING]
> EXAM TRAP: Do not confuse Kunpeng 912/Hi1612 (2014, first 64-bit Arm) with Kunpeng 916 (2016, first multi-socket Arm, used in TaiShan 100) or Kunpeng 920 (2019, first 7nm data center Arm, used in TaiShan 200).

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`02-Exercise-Kunpeng-920-Die-Cluster-Core-and-HCCS-Lab.html`](./02-Exercise-Kunpeng-920-Die-Cluster-Core-and-HCCS-Lab.html)** (or [`02-Exercise-Kunpeng-920-Die-Cluster-Core-and-HCCS-Lab.md`](./02-Exercise-Kunpeng-920-Die-Cluster-Core-and-HCCS-Lab.md)) to apply this concept in an interactive lab workbench!
