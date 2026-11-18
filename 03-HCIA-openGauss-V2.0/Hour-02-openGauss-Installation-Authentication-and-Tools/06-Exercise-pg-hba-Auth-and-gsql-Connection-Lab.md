# 💻 Hands-On Lab: Configuring `pg_hba.conf` via `gs_guc` and Connecting with `gsql`

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 02 — openGauss Installation, Authentication & O&M Tools (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `05-Lecture-Client-Authentication-pg-hba-and-gsql-Connections`  
**Interactive Workbench:** Open **[`06-Exercise-pg-hba-Auth-and-gsql-Connection-Lab.html`](./06-Exercise-pg-hba-Auth-and-gsql-Connection-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
You need to allow remote client `10.252.95.191/32` to connect to all databases as user `testuser` using `sha256` authentication without restarting the database, then connect to the default `postgres` database on port `8000` using `gsql`.

### 📋 Step-by-Step Instructions
1. Step 1: Check detailed cluster node status and data directory using `gs_om -t status --detail`.
2. Step 2: Use `gs_guc reload -N all -I all -h "host all testuser 10.252.95.191/32 sha256"` to add and immediately reload the client authentication rule.
3. Step 3: Connect to the `postgres` database on port `8000` using `gsql -d postgres -p 8000`.

### 📝 Starter Workspace (`omm@opengauss:~$`)
```bash
# Step 1: Query detailed cluster instance status
gs_om -t status ____

# Step 2: Dynamically add and reload pg_hba.conf rule for testuser with sha256
gs_guc ____ -N all -I all -h "host all testuser 10.252.95.191/32 ____"

# Step 3: Connect to the default postgres database on port 8000
____ -d postgres -p 8000
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Use `--detail` with `gs_om -t status` to display the node IP and instance data directory.
- Use `gs_guc reload` (instead of `set`) so semaphores are sent to reload `pg_hba.conf` immediately, and specify `sha256`.
- Use `gsql -d postgres -p 8000` to connect.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
gs_om -t status --detail
gs_guc reload -N all -I all -h "host all testuser 10.252.95.191/32 sha256"
gsql -d postgres -p 8000
```

#### Expected Console / Query Output:
```text
[   DBnode State   ]
node    node_ip         instance                                 state
-----------------------------------------------------------------------------
1 plat1 192.168.0.11    5001 /srv/BigData/gaussdb/data1/dbnode   Normal

Total instances: 1. Failed instances: 0.
Success to perform gs_guc!

gsql ((openGauss 2.0.0 build 78689da9) compiled at 2021-03-31 21:03:52 commit 0 last mr)
Non-SSL connection (SSL connection is recommended when requiring high-security)
Type "help" for help.
postgres=#
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**What is the difference between `gs_guc set` and `gs_guc reload` when modifying openGauss parameters?**

- A. `set` modifies `pg_hba.conf`, while `reload` modifies `postgresql.conf`
- B. `set` modifies only the configuration file, while `reload` modifies the configuration file and sends semaphores to the database process to reload it immediately
- C. `set` is executed by `root`, while `reload` is executed by `omm`
- D. `set` restarts the database cluster automatically, while `reload` stops the cluster

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 02 (p. 96), `set` modifies only parameters in the configuration file, whereas `reload` modifies the parameters in the configuration file and sends semaphores to the database process for reloading the configuration file.
</details>

### Question 2 [Single-Choice]
**When connecting to openGauss via `gsql`, what does the prompt `postgres=#` versus `postgres=>` indicate?**

- A. `=#` indicates an SSL connection; `=>` indicates a Non-SSL connection
- B. `=#` indicates login as database administrator (`omm`); `=>` indicates login as a common user
- C. `=#` indicates the primary node; `=>` indicates the standby node
- D. `=#` indicates interactive mode; `=>` indicates script batch mode

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 02 (p. 98), if you log in as administrator `omm`, `DBNAME=#` is displayed; if you log in as a common user, `DBNAME=>` is displayed.
</details>

### Question 3 [True / False]
**In openGauss `pg_hba.conf`, remote hosts can be configured with the `trust` authentication option to allow passwordless remote connections.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False (Ch.02 p. 96 & p. 118). Remote hosts are NOT allowed to access openGauss in `trust` mode for security reasons.
</details>
