# Hands-On Lab: Auditing GaussDB Distributed Cluster Capacity & HA/DR Specifications

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 08 — GaussDB Enterprise Distributed Database & Cloud Ecosystem (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `01-Lecture-GaussDB-Positioning-and-HA-DR-Topologies`  
**Interactive Workbench:** Open **[`02-Exercise-GaussDB-vs-openGauss-and-DR-Topologies-Lab.html`](./02-Exercise-GaussDB-vs-openGauss-and-DR-Topologies-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You are architecting a financial-grade GaussDB deployment. Record the official GaussDB scale-out limits (4 PB max storage, 256 max shards, 100,000 concurrent connections) and Dual-Cluster Remote DR RPO/RTO metrics.

### Step-by-Step Instructions
1. Step 1: Specify `4` (PB) as the maximum storage capacity, `256` as the maximum number of shards/DNs in a single large cluster, and `100000` as the cluster concurrent connections.
2. Step 2: Specify `'10 seconds'` as the RPO and `'10 minutes'` as the RTO for Dual-Cluster Remote DR.

### Starter Workspace (`GaussDB=#`)
```bash
-- Complete the GaussDB enterprise specification verification query:
SELECT
    ____         AS max_storage_pb,            -- Max petabytes of data (p. 478)
    ____         AS max_shards_per_cluster,    -- Max shards/DNs per cluster (p. 487/494)
    ____         AS max_cluster_connections,   -- Max concurrent connections per cluster (p. 494)
    '____'       AS remote_dr_rpo,             -- Dual-cluster Remote DR RPO (p. 486)
    '____'       AS remote_dr_rto;             -- Dual-cluster Remote DR RTO (p. 486)
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- GaussDB supports 4 PB of data, up to 256 shards/DNs per large cluster, and > 100,000 (`100000`) concurrent connections per cluster.
- Dual-Cluster Remote DR (p. 486) achieves RPO of `'10 seconds'` and RTO of `'10 minutes'`.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
SELECT
    4          AS max_storage_pb,
    256        AS max_shards_per_cluster,
    100000     AS max_cluster_connections,
    '10 seconds' AS remote_dr_rpo,
    '10 minutes' AS remote_dr_rto;
```

#### Expected Console / Query Output:
```text
max_storage_pb | max_shards_per_cluster | max_cluster_connections | remote_dr_rpo | remote_dr_rto 
----------------+------------------------+-------------------------+---------------+---------------
              4 |                    256 |                  100000 | 10 seconds    | 10 minutes
(1 row)
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**What is the key architectural difference between openGauss and GaussDB?**

- A. openGauss supports distributed Shared-Nothing deployment, whereas GaussDB supports only standalone deployment
- B. openGauss is an open-source database supporting standalone and primary/standby deployments, whereas GaussDB is a commercial cloud database supporting both distributed and centralized deployments
- C. openGauss is developed in Java, whereas GaussDB is developed in Python
- D. openGauss supports only x86 processors, whereas GaussDB supports only ARM processors

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 06 (p. 478), openGauss is open-source and uses standalone and primary/standby architectures, whereas GaussDB is a commercial cloud service supporting both distributed and centralized systems.
</details>

### Question 2 [Single-Choice]
**In GaussDB Primary/Standby deployment, how do `1+1 (maximum availability)` and `1+2 (maximum protection)` differ when a network problem prevents synchronous replication?**

- A. `1+1` switches to asynchronous replication until network recovery; `1+2` requires synchronous confirmation from a standby node before returning to the client
- B. `1+1` shuts down the primary node immediately; `1+2` deletes all standby logs
- C. `1+1` requires 3 AZs; `1+2` requires only 1 AZ
- D. Both `1+1` and `1+2` discard all uncommitted and committed transactions

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** Per Chapter 06 (p. 481), in `1+1 (maximum availability)`, if synchronous replication cannot be completed due to network problems, asynchronous replication is used until recovery. In `1+2 (maximum protection)`, synchronous confirmation from the standby node is required before returning to the client.
</details>

### Question 3 [True / False]
**In a GaussDB cluster, ETCD uses the Raft algorithm at the bottom layer to ensure consistency, and there must be three or more ETCD instances with an odd total number.**

- A. True
- B. False

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** True (Ch.06 p. 482). ETCD uses the Raft algorithm for consistency, and a cluster must have 3 or more ETCDs in an odd number (Leader and Follower roles).
</details>
