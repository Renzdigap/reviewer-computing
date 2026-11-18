# Hands-On Lab: Auditing Resource Pooling Components, Protocols & Constraints

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 03 — openGauss Architecture, Resource Pooling & High Performance (Sprint 2 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `03-Lecture-Resource-Pooling-Architecture-DMS-and-DSS`  
**Interactive Workbench:** Open **[`04-Exercise-Resource-Pooling-DMS-DSS-Architecture-Lab.html`](./04-Exercise-Resource-Pooling-DMS-DSS-Architecture-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You are designing an openGauss Resource Pooling deployment on Huawei OceanStor Dorado storage. Record the exact component names (`DMS`, `DSS`), required SCSI3 protocols (`PR`, `CAW`), and maximum standby node count (`7`) into an architecture verification query.

### Step-by-Step Instructions
1. Step 1: Complete the `SELECT` verification query specifying `'DSS'` as the storage service component and `'DMS'` as the memory service component.
2. Step 2: Specify `'RDMA'` as the low-latency page exchange protocol (reducing latency by >= 20% over TCP) and `7` as the maximum number of standby nodes supported.

### Starter Workspace (`openGauss=#`)
```bash
-- Complete the Resource Pooling architecture specification query:
SELECT
    '____' AS storage_component,     -- Distributed Storage Service
    '____' AS memory_component,      -- Distributed Memory Service
    '____' AS fast_interconnect,     -- OCK low-latency network protocol
    ____   AS max_standby_nodes;     -- Maximum standby nodes with 1 primary
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Distributed Storage Service is abbreviated `DSS`, and Distributed Memory Service is abbreviated `DMS`.
- Page exchange between primary and standby nodes is accelerated over `RDMA` (OCK RDMA with CX5 NIC), and resource pooling supports 1 primary + `7` standby nodes.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
SELECT
    'DSS' AS storage_component,
    'DMS' AS memory_component,
    'RDMA' AS fast_interconnect,
    7 AS max_standby_nodes;
```

#### Expected Console / Query Output:
```text
storage_component | memory_component | fast_interconnect | max_standby_nodes 
-------------------+------------------+-------------------+-------------------
 DSS               | DMS              | RDMA              |                 7
(1 row)
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**In the openGauss Resource Pooling architecture, which component is responsible for transmitting page data over TCP/RDMA networks and pooling memory between primary and standby nodes to ensure real-time consistent reads?**

- A. DSS (Distributed Storage Service)
- B. DMS (Distributed Memory Service)
- C. SPQ (Shared-Everything Parallel Query)
- D. GTM (Global Transaction Manager)

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 03 (p. 147), DMS (Distributed Memory Service) is a dynamic library integrated into the database that transmits page data over TCP/RDMA networks and pools memory between primary and standby nodes.
</details>

### Question 2 [Multiple-Choice (Select ALL)]
**Which of the following are restrictions or limitations of the openGauss Resource Pooling architecture?**

- A. Supports a maximum of 1 primary node and 7 standby nodes deployed on the same disk array
- B. Supports only segment-page tables, and Ceph storage is not supported
- C. Global temporary tables, hash indexes, and cascaded standby nodes are not supported
- D. Requires continuous WAL log replication between primary and standby nodes within the same cluster to read committed data

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Options A, B, and C are exact specifications/limitations (Ch.03 pp. 150–151). Option D is false: log replication is NOT required between primary and standby nodes in the same resource-pooled cluster; real-time page exchange via DMS is used instead (p. 149).
</details>

### Question 3 [True / False]
**In openGauss Resource Pooling, using the OCK RDMA dynamic library with a CX5 NIC reduces the latency of consistent reads on the standby node by at least 20% compared with TCP.**

- A. True
- B. False

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** True (Ch.03 p. 148). Compared to TCP, the latency of consistent reads on the standby node over OCK RDMA is reduced by at least 20%.
</details>
