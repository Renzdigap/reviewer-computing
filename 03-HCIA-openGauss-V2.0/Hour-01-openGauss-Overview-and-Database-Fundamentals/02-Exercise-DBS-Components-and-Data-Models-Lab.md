# 💻 Hands-On Lab: Auditing DBS Components, Data Management Stages & Models

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 01 — openGauss Overview & Database Fundamentals (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `01-Lecture-Data-Management-Evolution-DBS-and-Data-Models`  
**Interactive Workbench:** Open **[`02-Exercise-DBS-Components-and-Data-Models-Lab.html`](./02-Exercise-DBS-Components-and-Data-Models-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
You are onboarding junior DBAs onto an openGauss environment. Create a reference relational table `dbs_audit` that models a normalized relational structure (with indivisible attributes) and records the three historical data management stages and their characteristics.

### 📋 Step-by-Step Instructions
1. Step 1: Write a `CREATE TABLE dbs_audit` statement with columns `stage_id INT PRIMARY KEY`, `stage_name VARCHAR(30)`, `manager VARCHAR(20)`, and `independence VARCHAR(40)`.
2. Step 2: Insert the three official stages (`'Manual management'`, `'File system'`, and `'DBS'`) using `INSERT INTO dbs_audit VALUES ...`.
3. Step 3: Query all records ordered by `stage_id ASC` using `SELECT * FROM dbs_audit ORDER BY stage_id;`.

### 📝 Starter Workspace (`openGauss=#`)
```bash
-- Step 1: Create the normalized relational table dbs_audit
CREATE TABLE dbs_audit (
    stage_id INT PRIMARY KEY,
    stage_name VARCHAR(30),
    manager VARCHAR(20),
    independence VARCHAR(40)
);

-- Step 2: Complete the INSERT statement with the 3 official stages
INSERT INTO dbs_audit VALUES
    (1, '____', 'User/Program', 'Poor'),
    (2, '____', 'File system', 'Physical only'),
    (3, '____', 'DBMS', 'Physical and Logical');

-- Step 3: Query the table
____ * FROM dbs_audit ORDER BY stage_id;
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Recall Ch.01 Quiz Q3: The three stages of data management are 'Manual management', 'File system', and 'DBS'.
- Use SELECT * FROM dbs_audit ORDER BY stage_id; to retrieve the rows.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
CREATE TABLE dbs_audit (
    stage_id INT PRIMARY KEY,
    stage_name VARCHAR(30),
    manager VARCHAR(20),
    independence VARCHAR(40)
);

INSERT INTO dbs_audit VALUES
    (1, 'Manual management', 'User/Program', 'Poor'),
    (2, 'File system', 'File system', 'Physical only'),
    (3, 'DBS', 'DBMS', 'Physical and Logical');

SELECT * FROM dbs_audit ORDER BY stage_id;
```

#### Expected Console / Query Output:
```text
CREATE TABLE
INSERT 0 3
 stage_id |    stage_name     |   manager    |     independence     
----------+-------------------+--------------+----------------------
        1 | Manual management | User/Program | Poor
        2 | File system       | File system  | Physical only
        3 | DBS               | DBMS         | Physical and Logical
(3 rows)
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**(Official Ch.01 Quiz Q1) Which of the following is NOT a component of a database system (DBS)?**

- A. Database
- B. DBMS
- C. Database application
- D. Database storage medium

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `D`
- **Explanation:** Per Chapter 01 (p. 9 & p. 67), a DBS consists of three parts: Database, DBMS, and Database application. The database storage medium is hardware and not one of the three logical DBS components.
</details>

### Question 2 [Multiple-Choice (Select ALL)]
**(Official Ch.01 Quiz Q3) Which of the following phases are involved in the development of data management technologies?**

- A. Manual management
- B. File system
- C. DBS
- D. AI management

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 01 (p. 10 & p. 68), data management technologies went through three stages: Manual management, File system, and DBS.
</details>

### Question 3 [True / False]
**In the hierarchical database model, all nodes except the root node can have multiple parent nodes.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False. In the hierarchical model, all nodes except the root node have ONLY ONE parent node. It is the network model that allows a node to have more than one parent.
</details>
