# GaussDB Enterprise Features — Distributed Storage, `GTM-Lite` & Physical/Logical Backup

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 08 — GaussDB Enterprise Distributed Database & Cloud Ecosystem (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (7 mins) - Followed immediately by `06-Exercise-Distributed-Tables-GTM-Lite-and-Backup-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.06, pp. 496–503

---

## Learning Objectives
- Contrast GaussDB two-layer distributed storage: inter-shard (`Hash distribution` vs `Replication distribution`) and intra-shard (`Quorum multi-copy`)
- Compare `GTM-Lite` (strongly consistent, lock-free CSN) vs. `GTM-Free` (eventually consistent, no central node)
- Distinguish GaussDB Physical Backup (full + incremental to OBS) from Logical Backup (streaming table extract to local disk/OBS in TEXT/CSV)

---

### 1. Two-Layer Distributed Storage: Inter-Shard & Intra-Shard (p. 497)
GaussDB provides a **two-layer distributed storage architecture**:
1. **Layer 1 — Inter-Shard Data Distribution (Between Shards)**:
   - **Hash Distribution (`DISTRIBUTE BY HASH(col)`)**: Applied to **large user tables**. Hashes one or more user-specified distribution keys to spread rows evenly across shards, expanding total capacity and enabling parallel query processing and shard pruning.
   - **Replication Distribution (`DISTRIBUTE BY REPLICATION`)**: Applied to **small dimension/lookup tables**. Stores a complete copy of the table on **every shard**, allowing multi-table joins to execute locally on each DN without cross-node data redistribution!
2. **Layer 2 — Intra-Shard Data Storage (Within Each Shard)**:
   - Uses **quorum-based distributed multi-copy storage** (Primary DN + Standby DNs per shard) with automatic primary/standby switchover, AZ switchover, and forcible promotion to primary.

---

### 2. Distributed Transaction Processing: `GTM-Lite` vs. `GTM-Free` (p. 500)
Traditional distributed databases maintain a global active transaction list on the GTM, which becomes a central bottleneck. Huawei's **`GTM-Lite`** eliminates this bottleneck via three innovations:
1. **CSN Replaces Transaction Lists**: Uses a 64-bit **Commit Sequence Number (`CSN`)** to determine tuple visibility immediately without traversing a global active transaction list.
2. **Lock-Free Atomic Operations**: Assigns CSNs via lock-free atomic instructions so concurrent transactions obtain CSNs simultaneously without single-point contention.
3. **Minimal Network Overhead**: Only a single CSN integer is exchanged during node interactions.

| Transaction Mode | Consistency Level | Central GTM Dependency & Target Scenario |
| :--- | :--- | :--- |
| **`GTM-Lite` Mode** | **Strong Global Consistency** | Connects to lightweight GTM for lock-free CSN snapshots; ideal for general enterprise OLTP requiring real-time cross-shard read consistency. |
| **`GTM-Free` Mode** | **Eventual Consistency** (does not provide real-time cross-node read consistency) | **Does NOT connect to GTM** (zero central node involvement); achieves maximum throughput in **perfectly sharded OLTP scenarios**. |

---

### 3. Distributed Physical Backup vs. Logical Backup (pp. 502–503)
- **Physical Backup (p. 502)**:
  - Backs up data files of each DN across the **entire cluster in parallel to OBS (Object Storage Service)** in internal database format and restores to **homogeneous databases** (supports compression, flow control, and resumable backup).
  - **Full Backup vs. Incremental Backup**:
    - **Full backup**: Backs up all data at a time point (duration proportional to total DB size).
    - **Incremental backup**: Backs up only data modified since the last backup (duration proportional to changed data size). **Restoring a complete database requires BOTH the full backup and subsequent incremental backups** (e.g., Monday Full + Tue–Sun Incrementals).
- **Logical Backup (p. 503)**:
  - Extracts user table records from each DN in parallel streaming mode to **local disk files or OBS in `TEXT` or `CSV` format**, and can restore data into **homogeneous OR heterogeneous databases**.

---

## Key Takeaways
- **Between shards, GaussDB uses Hash distribution for large tables and Replication distribution (a full copy on every shard) for small lookup tables to accelerate multi-table joins.**
- **`GTM-Lite` provides strong global consistency using lock-free CSNs (replacing active transaction lists), whereas `GTM-Free` provides eventual consistency without connecting to GTM for perfectly sharded OLTP.**
- **Physical backup writes internal-format cluster files to OBS for homogeneous restore (Full + Incremental), whereas Logical backup streams user tables in TEXT/CSV to local disk or OBS for homogeneous or heterogeneous restore.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Can you restore a complete database using ONLY an incremental physical backup? No! A complete database can be restored only when BOTH the full backup and incremental backups are used together (Ch.06 p. 502).

> [!WARNING]
> EXAM TRAP: Do not confuse `GTM-Lite` (strongly consistent, uses lock-free CSNs) with `GTM-Free` (eventually consistent, does not connect to GTM).

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-Distributed-Tables-GTM-Lite-and-Backup-Lab.html`](./06-Exercise-Distributed-Tables-GTM-Lite-and-Backup-Lab.html)** (or [`06-Exercise-Distributed-Tables-GTM-Lite-and-Backup-Lab.md`](./06-Exercise-Distributed-Tables-GTM-Lite-and-Backup-Lab.md)) to apply this concept in an interactive lab workbench!
