# 💻 Hands-On Lab: Creating Tables with Numeric, Serial, Character (`CLOB`), and Date/Time Types

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 06 — SQL Basics — Classification, Data Types, DQL, Joins & DML (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `01-Lecture-SQL-Classification-and-Data-Types`  
**Interactive Workbench:** Open **[`02-Exercise-SQL-Data-Types-and-Storage-Sizes-Lab.html`](./02-Exercise-SQL-Data-Types-and-Storage-Sizes-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
Create a table `type_audit` that tests `TINYINT` (1B), `INTEGER` (4B), `BIGINT` (8B), `DECIMAL(10,4)`, `CLOB` (large text object), and `SMALLDATETIME` (minute-rounded timestamp), insert a test row, and query it.

### 📋 Step-by-Step Instructions
1. Step 1: Complete `CREATE TABLE type_audit` with columns `a TINYINT`, `b INTEGER`, `c BIGINT`, `d DECIMAL(10,4)`, `e CLOB`, and `f SMALLDATETIME`.
2. Step 2: Insert `(100, 1000, 10000, 123456.1223, 'Large text description', '2003-04-12 04:05:06')` into `type_audit` and run `SELECT * FROM type_audit;`.

### 📝 Starter Workspace (`openGauss=#`)
```bash
-- Step 1: Create table type_audit with exact data types
CREATE TABLE type_audit (
    a TINYINT,
    b INTEGER,
    c ____,          -- 8-byte integer type
    d DECIMAL(10,4),
    e ____,          -- Large object data of the TEXT type
    f SMALLDATETIME
);

-- Step 2: Insert a test record and query
INSERT INTO type_audit VALUES (100, 1000, 10000, 123456.1223, 'Large text description', '2003-04-12 04:05:06');
SELECT * FROM type_audit;
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- The 8-byte integer type is `BIGINT`.
- The large text object alias of `TEXT` is `CLOB`.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
CREATE TABLE type_audit (
    a TINYINT,
    b INTEGER,
    c BIGINT,
    d DECIMAL(10,4),
    e CLOB,
    f SMALLDATETIME
);

INSERT INTO type_audit VALUES (100, 1000, 10000, 123456.1223, 'Large text description', '2003-04-12 04:05:06');
SELECT * FROM type_audit;
```

#### Expected Console / Query Output:
```text
CREATE TABLE
INSERT 0 1
  a  |  b   |   c   |      d      |           e            |          f          
-----+------+-------+-------------+------------------------+---------------------
 100 | 1000 | 10000 | 123456.1223 | Large text description | 2003-04-12 04:05:00
(1 row)
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [True / False]
**(Official Ch.05 Quiz p. 372 Q1) `BIGINT` occupies four bytes.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False (Ch.05 p. 362 & p. 372). `BIGINT` (`INT8`) occupies eight (8) bytes. `INTEGER` (`INT4`) occupies four bytes.
</details>

### Question 2 [True / False]
**(Official Ch.05 Quiz p. 372 Q2) `CLOB` is used to store large object data of the `TEXT` type.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** True (Ch.05 p. 366 & p. 372). `CLOB` is the alias of the `TEXT` type (up to 1 GB minus 1 byte) and is used to store large text objects.
</details>

### Question 3 [Single-Choice]
**(Official Ch.05 Quiz p. 405 Q2) Which of the following four groups of SQL commands belong to the DML commands?**

- A. CREATE, DROP, UPDATE
- B. INSERT, UPDATE, DELETE
- C. INSERT, DROP, ALTER
- D. UPDATE, DELETE, ALTER

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 05 (p. 359 & p. 405), `INSERT`, `UPDATE`, and `DELETE` are Data Manipulation Language (DML) commands, whereas `CREATE`, `DROP`, and `ALTER` are DDL commands.
</details>
