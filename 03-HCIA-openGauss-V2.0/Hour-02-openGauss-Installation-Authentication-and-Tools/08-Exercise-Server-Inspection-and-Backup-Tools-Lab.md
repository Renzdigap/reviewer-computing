# 💻 Hands-On Lab: Running `gs_checkos`, `gs_checkperf`, `gs_check`, and `gs_ssh`

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 02 — openGauss Installation, Authentication & O&M Tools (Sprint 4 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `07-Lecture-openGauss-Client-and-Server-OM-Tools`  
**Interactive Workbench:** Open **[`08-Exercise-Server-Inspection-and-Backup-Tools-Lab.html`](./08-Exercise-Server-Inspection-and-Backup-Tools-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
Perform a routine pre-upgrade and performance inspection of an openGauss server: check OS parameters as `root` using `gs_checkos`, check SSD read/write performance as `root` using `gs_checkperf`, and run a health scenario check as `omm` using `gs_check`.

### 📋 Step-by-Step Instructions
1. Step 1: As `root`, run `gs_checkos -i A` to check all 14 OS parameters (A1–A14) without modifying them.
2. Step 2: As `root`, run `gs_checkperf -U omm -i SSD` to measure SSD read/write performance.
3. Step 3: As `omm`, run `gs_check -e health` to execute the health inspection scenario.

### 📝 Starter Workspace (`root@opengauss:~#`)
```bash
# Step 1 (as root): Check OS parameters (A1..A14) using gs_checkos
gs_checkos -i ____

# Step 2 (as root): Check SSD performance using gs_checkperf
gs_checkperf -U omm -i ____

# Step 3 (as omm): Run gs_check for the 'health' inspection scenario
su - omm -c "gs_check -e ____"
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- In `gs_checkos`, `-i A` checks OS items A1 to A14, whereas `-i B` sets OS parameters B1 to B8.
- In `gs_checkperf`, `-i SSD` checks SSD performance and requires `root`.
- In `gs_check`, `-e` specifies a scenario name such as `health`, `inspect`, `upgrade`, or `install`.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
gs_checkos -i A
gs_checkperf -U omm -i SSD
su - omm -c "gs_check -e health"
```

#### Expected Console / Query Output:
```text
Checking items:
    A1. [ OS version status ]                                   : Normal
    A2. [ Kernel version status ]                               : Normal
    A6. [ System control parameters status ]                    : Normal
    A9. [ Disk configuration status ]                           : Normal
Total numbers:14. Abnormal numbers:0. Warning numbers:0.

Cluster statistics information:
    SSD Write Performance                                       : 540.25 MB/s
    SSD Read Performance                                        : 685.80 MB/s

Parsing the check items config file successfully.
The scenario [health] check completed. Result: All 28 items passed.
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**(Official Ch.02 Quiz Q1) Which of the following is NOT an openGauss server tool?**

- A. gs_check
- B. gs_guc
- C. gsql
- D. gs_collector

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `C`
- **Explanation:** Per Chapter 02 (p. 102 & p. 126), `gsql` is a Client tool, whereas `gs_check`, `gs_guc`, and `gs_collector` are Server tools.
</details>

### Question 2 [Single-Choice]
**(Official Ch.02 Quiz Q2) When the `gs_checkperf` tool is used to check system performance, which of the following can be viewed ONLY by user `root`?**

- A. openGauss level
- B. Host level
- C. Session/Process level
- D. SSD performance

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `D`
- **Explanation:** Per Chapter 02 (p. 109, p. 110 & p. 126), SSD read/write performance (`gs_checkperf -U USER -i SSD`) can be viewed ONLY by user `root`.
</details>

### Question 3 [True / False]
**In `gs_checkos`, items A1 to A14 are used to check OS parameters without modifying them, whereas items B1 to B8 set system parameters to expected values, and A and B items cannot be set simultaneously.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** True (Ch.02 p. 107). Items A1–A14 check OS parameters, items B1–B8 set system parameters, and A and B cannot be specified at the same time.
</details>
