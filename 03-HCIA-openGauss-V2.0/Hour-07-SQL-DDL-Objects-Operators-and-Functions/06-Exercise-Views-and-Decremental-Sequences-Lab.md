# 💻 Hands-On Lab: Creating Views & Ascending/Decremental Sequences (`nextval`, `OWNED BY`)

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 07 — SQL DDL Objects, Sequences, Operators & Built-in Functions (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `05-Lecture-DDL-Views-and-Sequences`  
**Interactive Workbench:** Open **[`06-Exercise-Views-and-Decremental-Sequences-Lab.html`](./06-Exercise-Views-and-Decremental-Sequences-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
Create or replace view `privilege_view`, create the official Ch.05 Quiz Q3 decremental sequence `seq_1` (starting at 400, step -4, minvalue 100, cycling), fetch its first value using `nextval('seq_1')`, and associate it with `bank_card.b_c_id`.

### 📋 Step-by-Step Instructions
1. Step 1: Create or replace view `privilege_view` as `SELECT b_number, b_type FROM bank_card;`.
2. Step 2: Create decremental sequence `seq_1` using `CREATE SEQUENCE seq_1 START WITH 400 MINVALUE 100 MAXVALUE 400 INCREMENT BY -4 CYCLE;`.
3. Step 3: Call `SELECT nextval('seq_1');` and bind the sequence using `ALTER SEQUENCE seq_1 OWNED BY bank_card.b_c_id;`.

### 📝 Starter Workspace (`openGauss=#`)
```bash
-- Step 1: Create or replace view privilege_view
CREATE OR ____ VIEW privilege_view AS SELECT b_number, b_type FROM bank_card;

-- Step 2 (Ch.05 Quiz Q3): Create decremental sequence seq_1 (400 down to 100, step -4, cycle)
CREATE SEQUENCE seq_1 START WITH 400 ____ 100 ____ 400 INCREMENT BY -4 ____;

-- Step 3: Fetch next value and associate seq_1 with bank_card.b_c_id
SELECT ____('seq_1');
ALTER SEQUENCE seq_1 ____ BY bank_card.b_c_id;
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Use `CREATE OR REPLACE VIEW` to create or update a view.
- For a decremental sequence starting at 400, you must specify `MINVALUE 100 MAXVALUE 400 INCREMENT BY -4 CYCLE`.
- Use `nextval('seq_1')` and `OWNED BY bank_card.b_c_id`.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
CREATE OR REPLACE VIEW privilege_view AS SELECT b_number, b_type FROM bank_card;

CREATE SEQUENCE seq_1 START WITH 400 MINVALUE 100 MAXVALUE 400 INCREMENT BY -4 CYCLE;

SELECT nextval('seq_1');
ALTER SEQUENCE seq_1 OWNED BY bank_card.b_c_id;
```

#### Expected Console / Query Output:
```text
CREATE VIEW
CREATE SEQUENCE
 nextval 
---------
     400
(1 row)

ALTER SEQUENCE
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Multiple-Choice (Select ALL)]
**(Official Ch.05 Quiz p. 447 Q3) Create a decremental sequence named `seq_1`. The starting value is 400, the step is –4, and the minimum value is 100. When the sequence reaches the minimum value, it can be cyclically executed. Which of the following statements are correct?**

- A. CREATE SEQUENCE seq_1 START WITH 400 MAXVALUE 100 INCREMENT BY -4 CYCLE;
- B. CREATE SEQUENCE seq_1 MAXVALUE 400 MINVALUE 100 INCREMENT BY -4 CYCLE;
- C. CREATE SEQUENCE seq_1 START WITH 400 MINVALUE 100 INCREMENT BY -4 CYCLE;
- D. CREATE SEQUENCE seq_1 START WITH 400 MINVALUE 100 MAXVALUE 400 INCREMENT BY -4 CYCLE;

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `BD`
- **Explanation:** Per Chapter 05 (p. 442 & p. 447), for a descending sequence (`INCREMENT BY -4`), the default `MAXVALUE` is `-1` and the default `START WITH` is `maxvalue`. Thus `MAXVALUE 400` is mandatory (making C fail), while `START WITH 400` defaults to `MAXVALUE 400` when omitted (making both B and D valid).
</details>

### Question 2 [Single-Choice]
**In openGauss `CREATE SEQUENCE`, if `MAXVALUE` is not specified for a descending sequence (`INCREMENT < 0`), what is its default `MAXVALUE`?**

- A. 1
- B. 0
- C. -1
- D. 2^63 - 1

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `C`
- **Explanation:** Per Chapter 05 (p. 442), if `MAXVALUE` is not specified (or `NO MAXVALUE` is specified), the default value for an ascending sequence is `2^63 - 1`, and for a descending sequence is `-1`.
</details>

### Question 3 [True / False]
**When `OWNED BY table_name.column_name` is specified on a sequence, dropping that column or table automatically deletes the associated sequence.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** True (Ch.05 p. 442 & p. 444). `OWNED BY` associates a sequence with a specified table column so that the sequence is automatically deleted when the column or table is dropped.
</details>
