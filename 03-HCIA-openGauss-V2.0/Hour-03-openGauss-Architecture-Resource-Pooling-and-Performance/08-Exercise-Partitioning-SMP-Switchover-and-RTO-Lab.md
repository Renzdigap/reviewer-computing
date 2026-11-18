# Hands-On Lab: Executing Primary/Standby Switchover & Configuring Ultimate RTO

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 03 — openGauss Architecture, Resource Pooling & High Performance (Sprint 4 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `07-Lecture-Partitioning-Kunpeng-NUMA-SMP-and-HA-Ultimate-RTO`  
**Interactive Workbench:** Open **[`08-Exercise-Partitioning-SMP-Switchover-and-RTO-Lab.html`](./08-Exercise-Partitioning-SMP-Switchover-and-RTO-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You need to enable Ultimate RTO parallel recovery (`recovery_parse_workers = 4`, `recovery_parallelism = 4`), perform a planned primary/standby switchover on standby node `/home/omm/cluster/dn1/`, and persist the new cluster role topology.

### Step-by-Step Instructions
1. Step 1: Set `recovery_parse_workers=4` and `recovery_parallelism=4` using `gs_guc set`.
2. Step 2: Promote standby `/home/omm/cluster/dn1/` via planned switchover using `gs_ctl switchover -D /home/omm/cluster/dn1/`.
3. Step 3: Persist the updated dynamic primary/standby configuration using `gs_om -t refreshconf`.

### Starter Workspace (`omm@opengauss:~$`)
```bash
# Step 1: Configure Ultimate RTO parallel recovery workers
gs_guc set -N all -I all -c "____=4"
gs_guc set -N all -I all -c "recovery_parallelism=4"

# Step 2: Perform planned primary/standby switchover on standby dn1
gs_ctl ____ -D /home/omm/cluster/dn1/

# Step 3: Record the updated primary/standby roles in the dynamic config file
gs_om -t ____
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Ultimate RTO requires both `recovery_parse_workers` and `recovery_parallelism` to be greater than 1.
- Use `gs_ctl switchover -D /home/omm/cluster/dn1/` for planned maintenance switchover.
- Always run `gs_om -t refreshconf` after a switchover or failover.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
gs_guc set -N all -I all -c "recovery_parse_workers=4"
gs_guc set -N all -I all -c "recovery_parallelism=4"
gs_ctl switchover -D /home/omm/cluster/dn1/
gs_om -t refreshconf
```

#### Expected Console / Query Output:
```text
Total instances: 2. Failed instances: 0.
Success to perform gs_guc!
[2026-11-17 14:20:01.102][24810][][gs_ctl]: gs_ctl switchover ,datadir is /home/omm/cluster/dn1/
[2026-11-17 14:20:03.450][24810][][gs_ctl]: switchover completed (/home/omm/cluster/dn1/)
Generating dynamic configuration file for all nodes.
Successfully generated dynamic configuration file.
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**On Kunpeng 920 (ARMv8.1) processors, which atomic instruction does openGauss use to replace the 4-instruction `ldxr`/`stlxr` loop for Compare-and-Swap (CAS), improving TPC-C throughput by over 10%?**

- A. cmpxchg8b
- B. casal
- C. dmb ish
- D. yield

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 03 (p. 184), openGauss uses the ARMv8.1 LSE `casal` atomic instruction to implement CAS in 1 instruction instead of 4 (`ldxr` and `stlxr`), increasing throughput from 1.34M to 1.51M tpmC.
</details>

### Question 2 [Single-Choice]
**After performing a primary/standby switchover (`gs_ctl switchover`) or failover (`gs_ctl failover`), which command must be executed to update the dynamic configuration file with the current primary and standby roles?**

- A. gs_om -t generateconf
- B. gs_om -t refreshconf
- C. gs_guc reload
- D. gs_ctl build

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 02 (p. 120) and Chapter 03 (p. 193), `gs_om -t refreshconf` must be executed after a failover or switchover to record the updated primary and standby node roles in the dynamic configuration file.
</details>

### Question 3 [True / False]
**RPO (Recovery Point Objective) is application-oriented and measures the maximum tolerable service downtime, whereas RTO (Recovery Time Objective) is data-oriented and measures the amount of lost data.**

- A. True
- B. False

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False (Ch.03 pp. 195–196). The definitions are swapped: RTO (Recovery Time Objective) is application-oriented and measures acceptable downtime, whereas RPO (Recovery Point Objective) is data-oriented and measures acceptable data loss over time.
</details>
