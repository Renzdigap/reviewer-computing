# 💻 Hands-On Lab: Generating a WDR Performance Report & Diagnosing Blocked Sessions

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 04 — openGauss High Security, Easy O&M & AI Capabilities (DBMind) (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `05-Lecture-Easy-OM-WDR-Reports-Slow-SQL-and-Session-Diagnosis`  
**Interactive Workbench:** Open **[`06-Exercise-WDR-Snapshot-and-Session-Diagnosis-Lab.html`](./06-Exercise-WDR-Snapshot-and-Session-Diagnosis-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
A DBA notices intermittent latency spikes. Manually take a WDR snapshot, generate a WDR report between snapshot IDs 1 and 2, and query `DBE_PERF.local_active_session` to identify any blocked sessions and their `final_block_sessionid`.

### 📋 Step-by-Step Instructions
1. Step 1: Call `SELECT create_wdr_snapshot();` to create a manual WDR snapshot.
2. Step 2: Call `SELECT generate_wdr_report(1, 2, 'all', 'cluster', null);` to generate a cluster-wide WDR report between snapshots 1 and 2.
3. Step 3: Query `SELECT sessionid, block_sessionid, final_block_sessionid FROM DBE_PERF.local_active_session;`.

### 📝 Starter Workspace (`postgres=#`)
```bash
-- Step 1: Manually create a WDR performance snapshot
SELECT ____();

-- Step 2: Generate a WDR report between snapshot 1 and snapshot 2
SELECT ____(1, 2, 'all', 'cluster', null);

-- Step 3: Check blocked sessions and final blocker in local_active_session
SELECT sessionid, block_sessionid, final_block_sessionid
FROM DBE_PERF.____;
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- The function to manually take a WDR snapshot is `create_wdr_snapshot()`.
- The function to generate the report is `generate_wdr_report(...)`.
- Active session samples are stored in `DBE_PERF.local_active_session`.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
SELECT create_wdr_snapshot();

SELECT generate_wdr_report(1, 2, 'all', 'cluster', null);

SELECT sessionid, block_sessionid, final_block_sessionid
FROM DBE_PERF.local_active_session;
```

#### Expected Console / Query Output:
```text
create_wdr_snapshot           
-----------------------------------------
 WDR snapshot request has been submitted
(1 row)

 generate_wdr_report 
---------------------
 <html lang="en">...WDR Cluster Report (Snap 1 -> Snap 2)...</html>
(1 row)

   sessionid    | block_sessionid | final_block_sessionid 
----------------+-----------------+-----------------------
 14021983741696 |  14021983745792 |        14021983749888
(1 row)
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**What are the prerequisites for generating a Workload Diagnosis Report (WDR) in openGauss?**

- A. `enable_wdr_snapshot` is set to `off`, and at least 1 snapshot exists
- B. `enable_wdr_snapshot` is set to `on`, and the number of snapshots is greater than or equal to 2
- C. The database must be stopped first using `gs_om -t stop`
- D. Only a common user without `sysadmin` privileges can run `create_wdr_snapshot()`

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 03 (p. 230), the prerequisites for WDR generation are that `enable_wdr_snapshot` is set to `on` (it is `off` by default) and the number of snapshots is greater than or equal to 2. Only a `sysadmin` user can manually run `create_wdr_snapshot()`.
</details>

### Question 2 [Single-Choice]
**In openGauss Slow SQL Diagnosis, which GUC parameter specifies the execution duration threshold above which a SQL statement is recorded as a slow SQL statement, and in which database must `statement_history` be queried?**

- A. `session_timeout`; queried in `template1`
- B. `log_min_duration_statement`; queried in `postgres`
- C. `wdr_snapshot_interval`; queried in any user database
- D. `lock_wait_timeout`; queried in `template0`

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 03 (pp. 236, 238), Slow SQL diagnosis records jobs exceeding `log_min_duration_statement`, and `statement_history` (or `dbe_perf.standby_statement_history` on standby) contains data only when queried in the `postgres` database.
</details>

### Question 3 [True / False]
**In `gsql`, the meta-commands `\a \t \o /path/report.html` switch output to unaligned mode, tuples-only mode, and redirect query output to the specified HTML file.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** True (Ch.03 p. 231). `\a` toggles unaligned mode, `\t` toggles tuples-only mode (hiding column headers and row count footer), and `\o <file>` redirects query results to the server file.
</details>
