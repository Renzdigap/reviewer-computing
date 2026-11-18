# GaussDB Distributed Components — CN, DN, GTM, CMS & ETCD

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 08 — GaussDB Enterprise Distributed Database & Cloud Ecosystem (Sprint 2 of 4)  
**Format:** Bite-Sized Lecture (7 mins) - Followed immediately by `04-Exercise-Distributed-Query-Flow-and-Components-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.06, pp. 487–495, 527

---

## Learning Objectives
- Memorize the exact role of every GaussDB distributed component: CN, DN, GTM, CM/CMS/CMA, OM/OMA, ETCD, WLM, GDS Loader, and Storage (Ch.06 Quiz Q1: D!)
- Trace the 5-step distributed parallel SQL execution flow across CNs and DNs
- Distinguish the 3 inter-DN data stream operators (`Broadcast`, `Gather`, `Redistribution`)

---

### 1. GaussDB Distributed Architecture Components (pp. 487, 495, Ch.06 Quiz Q1!)

| Component | Full Name | Official Responsibility in GaussDB (p. 495) |
| :--- | :--- | :--- |
| **`CN`** | **Coordinator Node** | Receives SQL access requests from applications, uses the optimizer to **generate distributed execution plans**, breaks down tasks and distributes fragments to DNs for parallel processing, and **summarizes/returns final results** to the client. |
| **`DN`** | **Data Node** | Stores service data (in row, column, or hybrid mode), executes data query tasks assigned by CNs, and returns result sets to CNs. |
| **`GTM`** | **Global Transaction Manager** | Generates and maintains globally unique transaction information: **global transaction ID (`GXID`), transaction snapshot, timestamp, and sequence**. |
| **`ETCD`** | **Editable Text Configuration Daemon** | Distributed key-value store (Raft consensus) **used for sharing configurations and discovering services (service registration and search) — Exact Ch.06 Quiz Q1: D!** |
| **`CM` (`CMS` + `CMA`)** | **Cluster Manager** | Manages and monitors the running status of functional units and physical resources across the distributed system, driving automatic failover. |
| **`OM` (`OMA`)** | **Operation Manager** | Provides management interfaces and tools for routine O&M and configuration management of the cluster. |
| **`Storage`** | **Local Storage** | Server's local storage resources used to store data permanently (Shared-Nothing architecture). |
| **`GDS Loader` & `WLM`** | **Gauss Data Service / Workload Manager** | High-speed parallel data loading direct to DNs (`GDS`) and workload resource management (`WLM`). |

> **Roles Perceived by the Management Plane (p. 495)**: **`DN`**, **`CN`**, **`GTM`**, **`ETCD`**, and **`CMS`**.

---

### 2. Five-Step Fully Parallel Distributed Execution Flow (p. 487)
1. **Step 1 (SQL Submission)**: The service application sends an SQL statement (`SELECT`, `INSERT`, `UPDATE`, `DELETE`/`DROP`) to a **CN**.
2. **Step 2 (Plan Generation & Dispatch)**: The **CN** uses its query optimizer to generate a distributed execution plan and dispatches plan fragments to the **DNs** (acquiring global snapshot/CSN from **GTM**).
3. **Step 3 (Inter-DN Stream Exchange)**: Because data is evenly distributed across DNs via consistent hashing, DNs exchange intermediate data when needed using **three types of Streams**:
   - **`Broadcast` Stream**: Broadcasts a small table's rows to all DNs.
   - **`Redistribution` Stream**: Re-hashes rows by join/group key across DNs.
   - **`Gather` Stream**: Collects results from DNs back to the CN.
4. **Step 4 (Result Return to CN)**: Each **DN** executes its fragment in multi-threaded parallel mode and returns its partial result set to the **CN**.
5. **Step 5 (Final Aggregation)**: The **CN** summarizes/merges the results and sends the final response to the service application.

---

### 3. Additional High-Performance Engines in GaussDB (pp. 489–490)
- **High-Speed Parallel Data Loading (`GDS`)**: **CNs** only plan and deliver tasks while **DNs** directly import data in parallel (`CSV`, `TEXT`, or `FIXED` format), fully utilizing all nodes' I/O and network bandwidth.
- **LLVM Dynamic Compilation (JIT)**: Moves determination of the actual execution path from the executor phase to the **execution initialization phase**, eliminating function-call overhead and branch mispredictions on expression evaluation.
- **Adaptive Compression**: Automatically selects the optimal compression algorithm by data type (**`RLE`**, **`DELTA`**, **`BYTEPACK`/`BITPACK`**, **`LZ4`**, **`ZLIB`**, **`LOCAL DICTIONARY`**).

---

## Key Takeaways
- **In GaussDB's distributed architecture, `ETCD` is used for sharing configurations and service discovery (service registration and search) — exact Ch.06 Quiz Q1: D!**
- **`CN` parses SQL, generates distributed plans, dispatches tasks to DNs, and aggregates final results; `DN` stores data and executes query fragments; `GTM` manages global transaction IDs, snapshots, timestamps, and sequences.**
- **GaussDB provides three Stream operators to exchange data among DNs: `Broadcast`, `Gather`, and `Redistribution`.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.06 Quiz Q1): 'In the GaussDB distributed architecture, which component is used for sharing configuration and service discovery (service registration and search)?' -> D. `ETCD`! Do not confuse `ETCD` with `GTM` (global transaction info) or `CM` (cluster status monitoring).

> [!WARNING]
> EXAM TRAP: During high-speed parallel data loading in GaussDB, does table data pass through the CN? No! CNs are only responsible for task planning and delivery, while DNs import data directly in parallel (Ch.06 p. 489).

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`04-Exercise-Distributed-Query-Flow-and-Components-Lab.html`](./04-Exercise-Distributed-Query-Flow-and-Components-Lab.html)** (or [`04-Exercise-Distributed-Query-Flow-and-Components-Lab.md`](./04-Exercise-Distributed-Query-Flow-and-Components-Lab.md)) to apply this concept in an interactive lab workbench!
