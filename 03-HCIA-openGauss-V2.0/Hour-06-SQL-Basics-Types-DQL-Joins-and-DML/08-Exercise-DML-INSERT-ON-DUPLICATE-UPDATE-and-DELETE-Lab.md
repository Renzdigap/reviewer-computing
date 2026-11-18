# Hands-On Lab: Executing Upsert (`ON DUPLICATE KEY UPDATE`), `UPDATE`, and `DELETE`

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 06 — SQL Basics — Classification, Data Types, DQL, Joins & DML (Sprint 4 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `07-Lecture-DML-Statements-INSERT-UPDATE-and-DELETE`  
**Interactive Workbench:** Open **[`08-Exercise-DML-INSERT-ON-DUPLICATE-UPDATE-and-DELETE-Lab.html`](./08-Exercise-DML-INSERT-ON-DUPLICATE-UPDATE-and-DELETE-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
Execute the three high-yield DML operations from Chapter 05: perform an upsert on `bank_card` using `ON DUPLICATE KEY UPDATE`, increment all employees' ages by 5 in `STAFFS`, and delete all students in class `cid = 6` from `student`.

### Step-by-Step Instructions
1. Step 1: Insert `('6222021302020000001', 'Credit Card', 1)` into `bank_card` and update `b_type = 'Savings Card'` on duplicate key.
2. Step 2: Increase the `AGE` column in the `STAFFS` table by 5 years using `UPDATE STAFFS SET AGE = AGE + 5;`.
3. Step 3: Delete all records from `student` where `cid = 6` using `DELETE FROM student WHERE cid = 6;`.

### Starter Workspace (`openGauss=#`)
```bash
-- Step 1: Upsert into bank_card using ON DUPLICATE KEY UPDATE
INSERT INTO bank_card VALUES ('6222021302020000001', 'Credit Card', 1)
____ ____ ____ UPDATE b_type = 'Savings Card';

-- Step 2 (Ch.05 Quiz Q1): Increase AGE in STAFFS by 5 years
UPDATE STAFFS ____ AGE = ____;

-- Step 3 (Ch.05 Quiz Q3): Delete students with cid = 6
____ ____ student ____ cid = 6;
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `ON DUPLICATE KEY UPDATE b_type = 'Savings Card'`.
- Use `UPDATE STAFFS SET AGE = AGE + 5;`.
- Use `DELETE FROM student WHERE cid = 6;` (do not put `*` after `DELETE`).

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
INSERT INTO bank_card VALUES ('6222021302020000001', 'Credit Card', 1)
ON DUPLICATE KEY UPDATE b_type = 'Savings Card';

UPDATE STAFFS SET AGE = AGE + 5;

DELETE FROM student WHERE cid = 6;
```

#### Expected Console / Query Output:
```text
INSERT 0 1
UPDATE 42
DELETE 8
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**(Official Ch.05 Quiz p. 405 Q1) Which of the following SQL commands can be used to increase the value of the `AGE` column in the `STAFFS` table by five years?**

- A. UPDATE SET AGE WITH AGE+5
- B. UPDATE AGE WITH AGE+5
- C. UPDATE STAFFS SET AGE = AGE+5
- D. UPDATE STAFFS AGE WITH AGE+5

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `C`
- **Explanation:** Per Chapter 05 (p. 401 & p. 405), the correct `UPDATE` syntax is `UPDATE table_name SET column_name = expression`, so `UPDATE STAFFS SET AGE = AGE+5` is correct.
</details>

### Question 2 [Single-Choice]
**(Official Ch.05 Quiz p. 406 Q3) Which of the following SQL statements will delete records for all students whose class ID (specified by `cid`) is 6 from the `student` table?**

- A. delete FROM student where cid = 6;
- B. delete * FROM student where cid = 6;
- C. delete FROM student on cid = 6;
- D. delete * FROM student on cid = 6;

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** Per Chapter 05 (p. 403 & p. 406), the `DELETE` syntax is `DELETE FROM table_name WHERE condition;`. Putting `*` after `DELETE` or using `ON` instead of `WHERE` is invalid.
</details>

### Question 3 [True / False]
**In openGauss, the `IGNORE` keyword in `INSERT IGNORE INTO ...` can be used together with the `ON DUPLICATE KEY UPDATE` clause in the same `INSERT` statement.**

- A. True
- B. False

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False (Ch.05 p. 398). `IGNORE` ignores records that cause duplicate key errors and CANNOT be used together with `ON DUPLICATE KEY UPDATE`.
</details>
