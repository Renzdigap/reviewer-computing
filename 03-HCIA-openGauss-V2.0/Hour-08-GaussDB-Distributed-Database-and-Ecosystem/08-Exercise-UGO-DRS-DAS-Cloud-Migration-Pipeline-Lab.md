# 💻 Hands-On Lab: Auditing the 6 Core Functions of UGO & Huawei Cloud Ecosystem Tools

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 08 — GaussDB Enterprise Distributed Database & Cloud Ecosystem (Sprint 4 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `07-Lecture-GaussDB-Ecosystem-Tools-UGO-DRS-DAS-and-Security`  
**Interactive Workbench:** Open **[`08-Exercise-UGO-DRS-DAS-Cloud-Migration-Pipeline-Lab.html`](./08-Exercise-UGO-DRS-DAS-Cloud-Migration-Pipeline-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
You are planning an Oracle-to-GaussDB migration on Huawei Cloud. Complete the SQL verification query listing the 6 official core functions of UGO (Ch.06 Quiz Q2) and matching `DAS`, `DRS`, `CTS`, `CES`, and `DBSS` to their roles.

### 📋 Step-by-Step Instructions
1. Step 1: Fill in the missing keywords in the 6 official UGO core functions (`profiling`, `recommendation`, `compatibility`, `workload`, `structure`, `Application SQL`).
2. Step 2: Match `'DRS'` (real-time data migration/sync), `'DAS'` (web console management), and `'DBSS'` (bypass-mode database security audit).

### 📝 Starter Workspace (`GaussDB=#`)
```bash
-- Step 1 (Ch.06 Quiz Q2): Verify the 6 core functions of UGO
SELECT
    'Source database ____'                                      AS ugo_fn_1,
    'Destination database selection and specification ____'     AS ugo_fn_2,
    'Destination database ____ analysis'                        AS ugo_fn_3,
    'Migration ____ evaluation'                                 AS ugo_fn_4,
    'Database ____ migration'                                   AS ugo_fn_5,
    '____ migration'                                            AS ugo_fn_6;

-- Step 2: Match Huawei Cloud ecosystem services
SELECT '____' AS data_replication_service,
       '____' AS web_admin_console,
       '____' AS db_security_service;
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- The 6 UGO functions are: Source database `profiling`, Destination DB selection and specification `recommendation`, Destination DB `compatibility` analysis, Migration `workload` evaluation, Database `structure` migration, and `Application SQL` migration.
- Data Replication Service = `DRS`, Data Admin Service = `DAS`, Database Security Service = `DBSS`.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
SELECT
    'Source database profiling'                                          AS ugo_fn_1,
    'Destination database selection and specification recommendation'    AS ugo_fn_2,
    'Destination database compatibility analysis'                        AS ugo_fn_3,
    'Migration workload evaluation'                                      AS ugo_fn_4,
    'Database structure migration'                                       AS ugo_fn_5,
    'Application SQL migration'                                          AS ugo_fn_6;

SELECT 'DRS' AS data_replication_service,
       'DAS' AS web_admin_console,
       'DBSS' AS db_security_service;
```

#### Expected Console / Query Output:
```text
ugo_fn_1          |                            ugo_fn_2                             |                  ugo_fn_3                   |           ugo_fn_4            |           ugo_fn_5           |         ugo_fn_6          
---------------------------+-----------------------------------------------------------------+---------------------------------------------+-------------------------------+------------------------------+---------------------------
 Source database profiling | Destination database selection and specification recommendation | Destination database compatibility analysis | Migration workload evaluation | Database structure migration | Application SQL migration
(1 row)

 data_replication_service | web_admin_console | db_security_service 
--------------------------+-------------------+---------------------
 DRS                      | DAS               | DBSS
(1 row)
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Multiple-Choice (Select ALL)]
**(Official Ch.06 Quiz Q2) Which of the following belong to the 6 core functions of UGO (Database and Application Migration UGO)?**

- A. Source database profiling & Destination database selection and specification recommendation
- B. Destination database compatibility analysis & Migration workload evaluation
- C. Database structure migration & Application SQL migration
- D. Bypass-mode SQL injection firewall & 7-day ECS trace recording

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 06 (p. 512 & p. 527), the 6 core functions of UGO are: Source database profiling, Destination database selection and specification recommendation, Destination database compatibility analysis, Migration workload evaluation, Database structure migration, and Application SQL migration. Option D describes DBSS and CTS.
</details>

### Question 2 [Single-Choice]
**Which Huawei Cloud service provides a database security audit function deployed in bypass mode to generate real-time alarms for SQL injection, risky operations, and Sarbanes-Oxley compliance reports?**

- A. DAS (Data Admin Service)
- B. DRS (Data Replication Service)
- C. CES (Cloud Eye Service)
- D. DBSS (Database Security Service)

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `D`
- **Explanation:** Per Chapter 06 (pp. 517–520), Database Security Service (DBSS) provides database security audit in bypass mode, detecting SQL injection, blacklist/whitelist hits, and generating compliance reports.
</details>

### Question 3 [True / False]
**In DRS (Data Replication Service), Backup Migration allows you to migrate data by uploading source database backup files to OBS and restoring them to the destination database without exposing the source database's IP address or connecting to it directly.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** True (Ch.06 p. 508). DRS Backup Migration stages backup files via OBS so data migration is completed without exposing or directly connecting to the source database.
</details>
