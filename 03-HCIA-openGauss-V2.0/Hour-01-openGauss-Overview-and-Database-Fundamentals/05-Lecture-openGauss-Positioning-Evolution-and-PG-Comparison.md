# openGauss Positioning, Evolution & Differences from PostgreSQL

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 01 — openGauss Overview & Database Fundamentals (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (7 mins) - Followed immediately by `06-Exercise-openGauss-vs-PostgreSQL-Architecture-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.01, pp. 42–50

---

## Learning Objectives
- Trace openGauss's evolution from internal incubation (2001) to open-source release (June 30, 2020) under Mulan PSL v2
- Explain the 4 core value pillars of openGauss: High Performance, High Availability, High Security, and Easy O&M
- Contrast openGauss and PostgreSQL across process/thread model, concurrency control, checkpoints, NUMA, and storage engines

---

### 1. openGauss Positioning, License & Evolution Timeline
**openGauss** is an enterprise-grade, multi-core-optimized open-source relational database developed by Huawei with global partners.
- **Open-Source License**: Released under **Mulan Permissive Software License v2 (Mulan PSL v2)** — allowing code to be freely modified, used, and referenced commercially.
- **4 Milestones in openGauss History (p. 44)**:
  1. **2001–2011 (Internal Incubation)**: Enterprise in-memory database used across Huawei telecom carrier products.
  2. **2011–2019 (Productization & Joint Innovation)**: Commercialized on HUAWEI CLOUD DWS and major banks; **GaussDB globally released on May 15, 2019**; openGauss open-source announced on **September 19, 2019**.
  3. **June 30, 2020 (Official Open Source)**: Source code officially opened at `https://gitee.com/opengauss`.
  4. **2021–Future (Ecosystem Building)**: Community governance via Technical Committee (**TC**), **SIGs** (SQL Engine, Storage Engine, Connectors, Docs, Infra, Security), **Maintainers**, **Committers**, and **Contributors**.

---

### 2. Core Value Pillars of openGauss (p. 46)
1. **High Performance**: **1.5 million tpmC** on 2-socket Kunpeng 920 (128 cores); NUMA-aware data structures; **SQL-Bypass** intelligent fast path; in-memory **MOT** engine.
2. **High Availability (HA)**: Hitless primary/standby switchover and Parallel Redo **Ultimate RTO < 10s**.
3. **High Security**: End-to-end protection including **Fully-Encrypted Equality Query** (TEE/secGear), Dynamic Data Masking, RBAC, RLS, Unified Auditing, and TDE.
4. **Easy O&M**: Built-in **DBMind AI** (parameter tuning, slow SQL diagnosis, index recommendation, workload time prediction) and WDR snapshots.

---

### 3. Architectural Comparison: openGauss vs. PostgreSQL (pp. 48–49)

| Differentiation Dimension | openGauss | PostgreSQL |
| :--- | :--- | :--- |
| **Execution Model** | **Single-process multi-threaded (`gaussdb`)** with thread pool | **Multi-process (`postgres`)** — one process per client connection |
| **Transaction ID & Concurrency** | **64-bit Transaction ID (XID)** + **CSN (Commit Sequence Number)**; eliminates XID wraparound & resolves the "five big locks" bottleneck | 32-bit XID wraparound causes periodic VACUUM FREEZE performance drops; "five big locks" limit multi-core scaling |
| **Logs & Checkpoints** | **Incremental checkpoint**, keeping performance fluctuation **< 5%** | **Full checkpoint**, causing short-term performance fluctuation **> 15%** |
| **Kunpeng NUMA Scaling** | NUMA data structure reconstruction, cache-line padding, ARMv8.1 native `casal` spin-lock (**1.5M tpmC** on 2-socket Kunpeng) | Weak NUMA multi-core capability (**< 600,000 tpmC** on dual-socket server) |
| **Storage Engines** | **Multi-engine**: Row-store (Astore/Ustore in-place update), Column-store, and **MOT (Memory-Optimized Table)** | **Row-store only** (append-only MVCC) |
| **Optimizer & SQL** | CBO + **ABO (AI-Based Optimizer)**; SQL92/99/2003/2011 + enterprise extensions | Standard CBO; average performance in complex enterprise queries |

---

## Key Takeaways
- **openGauss uses a single-process multi-threaded architecture (`gaussdb`), whereas PostgreSQL uses a multi-process architecture.**
- **openGauss uses 64-bit transaction IDs with Commit Sequence Numbers (CSNs) and incremental checkpoints (< 5% fluctuation), solving PostgreSQL's 32-bit XID wraparound and full checkpoint (> 15% fluctuation) bottlenecks.**
- **openGauss officially went open source on June 30, 2020 under the Mulan PSL v2 license.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: PostgreSQL supports only row-store natively, whereas openGauss supports Row-store, Column-store, and Memory-Optimized Table (MOT) engines.

> [!WARNING]
> EXAM TRAP: On 2-socket Kunpeng 920 (128 cores), openGauss achieves 1.5 million tpmC (1.5x higher than x86 alternatives), with RTO < 10s.

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-openGauss-vs-PostgreSQL-Architecture-Lab.html`](./06-Exercise-openGauss-vs-PostgreSQL-Architecture-Lab.html)** (or [`06-Exercise-openGauss-vs-PostgreSQL-Architecture-Lab.md`](./06-Exercise-openGauss-vs-PostgreSQL-Architecture-Lab.md)) to apply this concept in an interactive lab workbench!
