# GaussDB Positioning, Full-Stack Architecture & High-Availability Topologies

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 08 — GaussDB Enterprise Distributed Database & Cloud Ecosystem (Sprint 1 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `02-Exercise-GaussDB-vs-openGauss-and-DR-Topologies-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.06, pp. 474–486

---

## Learning Objectives
- Contrast openGauss (open-source standalone & primary/standby) with GaussDB (commercial cloud-native distributed & centralized HTAP database)
- Memorize GaussDB scale specifications (> 1,000 nodes scale-out, 4 PB storage, up to 256 shards/DNs, > 100,000 cluster concurrent connections)
- Compare GaussDB deployment topologies: Centralized 1+1 vs 1+2, Intra-City Active-Active, Intra-City 3-AZ Multi-Active, 3DC Geo-Redundant, and Dual-Cluster Remote DR

---

### 1. GaussDB Positioning & Differences from openGauss (pp. 478–480)
**GaussDB** is Huawei's commercial enterprise-level distributed relational database based on the openGauss ecosystem and full-stack Kunpeng hardware/software co-design:

| Dimension | openGauss | GaussDB |
| :--- | :--- | :--- |
| **Delivery Model** | **Open-source** software (Mulan PSL v2) | **Commercial enterprise database / Cloud service** |
| **Architecture** | **Standalone** & **Primary/Standby** (1P + up to 8S) | **Distributed (Shared-Nothing MPP)** & **Centralized (Primary/Standby)** |
| **Scale & Capacity** | Single-node up to 10,000 concurrent connections; 32 TB/table | Scale-out of **> 1,000 nodes** (up to **256 shards/DNs** per large cluster), **4 PB** storage, **> 100,000 concurrent connections** per cluster (10,000 per node) |
| **Workload Focus** | Enterprise OLTP & HTAP on single cluster | Massive distributed transaction expansion + HTAP across regions/AZs |

---

### 2. Primary/Standby Replication Modes: `1+1` vs. `1+2` (p. 481)
- **`1+1` (Maximum Availability)**:
  - Data is synchronously replicated to 1 standby node. However, **if synchronous replication fails due to network issues, it automatically degrades to asynchronous replication** (and resumes synchronous replication when the network recovers). If a switchover occurs while unsynchronized, data loss may occur.
- **`1+2` (Maximum Protection)**:
  - Data is synchronously replicated to 2 standby nodes across up to 3 AZs (5 replicas supported across multiple AZs). **Confirmation from standby is required before returning commit success to the client**, guaranteeing zero data loss (`RPO = 0`).

---

### 3. Distributed High-Availability & Disaster Recovery Topologies (pp. 482–486, 522)
1. **Centralized Cluster Across 3 AZs (p. 482)**: 1 Primary (`DN + CMS + ETCD`) in AZ 1 + 2 Standby (`DN + CMS + ETCD`) in AZ 2 and AZ 3.
2. **Distributed Cluster in Intra-City Active-Active / 3-AZ Multi-Active Mode (pp. 483–484)**:
   - Shards (`DN 1..N`), `CN`s, `GTM`s, `CMS`s, and `ETCD`s are striped across 3 AZs in the same city. Every server runs **`CMA` (Cluster Manager Agent)** and **`OMA` (Operation Manager Agent)**.
3. **Distributed Cluster in Two-Site Three-Center (3DC Geo-Redundant) Mode (p. 485, 522)**:
   - E.g., **Shanghai DC 1 (AZ 1)** + **Shanghai DC 2 (AZ 2)** in intra-city active-active mode + **Beijing Remote DC (AZ 3)**. Single cluster across AZs achieves **`RPO = 0, RTO < 60s`**.
4. **Dual-Cluster Remote DR (via OBS Log Synchronization, p. 486)**:
   - Primary Cluster (AZ 1 + AZ 2 intra-city active-active) ships incremental logs via **OBS** to a remote DR Cluster (AZ 3) for physical log replay.
   - **Specifications**: **`RPO = 10 seconds`**, **`RTO = 10 minutes`**.

---

## Key Takeaways
- **openGauss is open-source (standalone and primary/standby), whereas GaussDB is Huawei's commercial enterprise cloud database supporting both centralized and distributed (Shared-Nothing) deployment up to >1,000 nodes (256 shards), 4 PB data, and >100,000 concurrent connections.**
- **In Primary/Standby deployment, `1+1` is Maximum Availability (falls back to async on network fault) and `1+2` is Maximum Protection (strict sync confirmation).**
- **In Dual-Cluster Remote DR via OBS log synchronization, the specifications are RPO = 10 seconds and RTO = 10 minutes (whereas intra-city active-active / 3DC achieves RPO = 0, RTO < 60s).**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: In GaussDB, what is the difference between `1+1` and `1+2` primary/standby modes? `1+1` is 'Maximum Availability' (switches to async replication on network fault), while `1+2` is 'Maximum Protection' (requires standby confirmation before returning to client, Ch.06 p. 481).

> [!WARNING]
> EXAM TRAP: In an ETCD cluster within GaussDB, there must be **3 or more ETCD instances** and the total number of ETCDs **must be an odd number** (using the Raft consensus algorithm with Leader and Follower roles, Ch.06 p. 482).

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`02-Exercise-GaussDB-vs-openGauss-and-DR-Topologies-Lab.html`](./02-Exercise-GaussDB-vs-openGauss-and-DR-Topologies-Lab.html)** (or [`02-Exercise-GaussDB-vs-openGauss-and-DR-Topologies-Lab.md`](./02-Exercise-GaussDB-vs-openGauss-and-DR-Topologies-Lab.md)) to apply this concept in an interactive lab workbench!
