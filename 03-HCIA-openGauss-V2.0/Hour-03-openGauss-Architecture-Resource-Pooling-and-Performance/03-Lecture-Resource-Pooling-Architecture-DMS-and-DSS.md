# 📖 Resource Pooling Architecture (DMS, DSS & Shared Storage)

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 03 — openGauss Architecture, Resource Pooling & High Performance (Sprint 2 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `04-Exercise-Resource-Pooling-DMS-DSS-Architecture-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.03, pp. 145–159

---

## 🎯 Learning Objectives
- Explain how openGauss Resource Pooling decouples Compute, Memory (DMS), and Storage (DSS)
- List the hardware/protocol requirements (OceanStor Dorado SAN, SCSI3 PR & CAW, CX5 NIC, OCK RDMA) and feature limitations
- Describe the 6 advanced Resource Pooling enhancements (Standby visibility/Xmin/snapshot caching, Transparent write forwarding, DSS thread pool/blackbox/NoF+, Operator offloading/NDP, Dual-cluster DR, On-demand replay, and SPQ multi-node parallel query)

---

### 1. Core Components of openGauss Resource Pooling (pp. 146–149)
Resource pooling innovates HA deployment by allowing **1 Read/Write Primary node and up to 7 Read-Only Standby nodes** to **share a single copy of underlying storage** while pooling memory across nodes for **real-time consistent reads** on standby nodes (`RPO = 0`, no delayed read under Read Committed):
1. **DSS (Distributed Storage Service)**:
   - Consists of **DSS Server** (an independent process that directly manages raw LUN devices of disk arrays like **OceanStor Dorado** and provides distributed file system semantics) and **DSS API** (a dynamic library integrated into `gaussdb` communicating with DSS Server via shared memory).
   - System catalog storage is switched from page mode to **segment-page mode** (supports **only segment-page tables**).
2. **DMS (Distributed Memory Service)**:
   - A dynamic library integrated into the database that pools memory and exchanges hot data pages in real time between primary and standby shared buffer pools over **TCP** (default) or **OCK RDMA** (with **CX5 NIC**, reducing standby consistent-read latency by **>= 20%**).
   - Log replication is **not** required between primary and standby nodes during normal operation because pages are exchanged directly via DMS!

---

### 2. Hardware Requirements & Feature Limitations (pp. 150–151)
- **Hardware Prerequisites**:
  - Disk array (e.g., **OceanStor Dorado 5000**) with **UltraPath** multipath software installed (**Ceph is NOT supported**).
  - LUNs must support **SCSI3 PR (`PR OUT`, `PR IN`, `INQUIRY`)** for cluster **I/O FENCE**, and **SCSI3 `CAW` (Compare and Write)** for shared disk locks.
  - Supports at most **1 primary node + 7 standby nodes** on the same disk array.
- **Feature Limitations in Resource Pooling Mode (p. 151)**:
  - **NOT supported**: Global temporary tables, Hash indexes, Cascaded standby nodes, Logical replication publication/subscription (`T_CreatePublicationStmt`, etc.), `gs_xlogdump_*` / `gs_repair_page` functions, and converting between traditional and resource-pooling deployments.

---

### 3. Seven Resource Pooling Performance & HA Enhancements (pp. 152–159)
1. **Standby Visibility & Snapshot Optimization (v5.1.0+, +50%–80% sysbench read perf)**:
   - Standby caches `XID -> CSN` mappings in its local L2 cache; Primary locally caches cluster `oldest Xmin` (standbys send local `oldest Xmin` periodically via background thread); Primary can broadcast latest snapshots to standbys.
2. **Transparent Write Forwarding on Standby (`write-on-standby`)**: Inside an explicit transaction (`BEGIN ... END`) on a standby node, read statements execute locally on the standby while write statements are transparently forwarded to the primary node.
3. **DSS Enhancements**: Thread pools for DSS Server, crash **black box logs** (`_LOG_LEVEL=0` to disable), and **NoF/NoF+** storage networking APIs.
4. **Operator Offloading / Near-Data Processing (NDP)**: Offloads `SeqScan`, `Filter`, `Projection`, and `Agg` operators to storage nodes to filter data before network transmission.
5. **Dual-Cluster DR**: Synchronizes Xlogs between a Primary Cluster and Standby Cluster via **Network Streaming Replication** (v6.0.0-RC1) or **OceanStor Dorado Synchronous Replication** (v5.1.0, intra-city 100 km, `RPO = 0`, `RTO < 30s`).
6. **On-Demand Replay for Ultimate RTO**: Because standbys in resource pooling do not continuously replay primary WAL logs, upon primary failure the promoted standby rebuilds only essential metadata so services resume immediately, replaying remaining logs on-demand in the background.
7. **Multi-Node Parallelism (SPQ — Shared-Everything Parallel Query, v6.0.0-RC1)**: Integrates the **ORCA optimizer** to distribute a single large OLAP query across all read nodes in parallel using virtual Node-Groups.

---

## 🔑 Key Takeaways
- **Resource Pooling relies on DSS (Distributed Storage Service — DSS Server process + DSS API dynamic library) for shared disk array storage and DMS (Distributed Memory Service) for real-time TCP/RDMA page exchange.**
- **Resource Pooling supports up to 1 Primary + 7 Standby nodes, requires SCSI3 PR (for I/O Fence) and SCSI3 CAW (for shared disk locks) on disk arrays like OceanStor Dorado, and supports ONLY segment-page tables.**
- **Global temporary tables, hash indexes, and cascaded standby nodes are NOT supported in resource pooling mode.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Do not confuse DMS (Distributed Memory Service, a dynamic library inside the database for cross-node page exchange) with DSS (Distributed Storage Service, which includes an independent DSS Server process managing raw LUNs).

> [!WARNING]
> EXAM TRAP: In Resource Pooling mode, standby nodes do NOT replay logs during normal operation — they exchange pages via DMS and use On-Demand Replay during failover to achieve Ultimate RTO.

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`04-Exercise-Resource-Pooling-DMS-DSS-Architecture-Lab.html`](./04-Exercise-Resource-Pooling-DMS-DSS-Architecture-Lab.html)** (or [`04-Exercise-Resource-Pooling-DMS-DSS-Architecture-Lab.md`](./04-Exercise-Resource-Pooling-DMS-DSS-Architecture-Lab.md)) to apply this concept in an interactive lab workbench!
