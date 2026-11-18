# 💻 Hands-On Lab: Testing String, Arithmetic, Bitwise & Date/Time Functions in openGauss

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 07 — SQL DDL Objects, Sequences, Operators & Built-in Functions (Sprint 4 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `07-Lecture-Operators-and-Built-In-Functions`  
**Interactive Workbench:** Open **[`08-Exercise-String-Numeric-Date-and-Geometric-Functions-Lab.html`](./08-Exercise-String-Numeric-Date-and-Geometric-Functions-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
Run a diagnostic SQL query in openGauss that tests `instr`, `overlay`, `bitand`, `round` with negative and positive scale, `ceil`/`floor` on negative numbers, and date + integer addition.

### 📋 Step-by-Step Instructions
1. Step 1: Compute `instr('abcdabcdabcd', 'bcd', 2, 2)` and `overlay('hello' PLACING 'world' FROM 2 FOR 3)`.
2. Step 2: Compute `bitand(29, 15)`, `round(1234.5678, -2)`, `ceil(-42.8)`, and `floor(-42.8)`.
3. Step 3: Compute `SELECT date '2021-4-28' + integer '7' AS RESULT;`.

### 📝 Starter Workspace (`openGauss=#`)
```bash
-- Step 1: String functions instr and overlay
SELECT ____('abcdabcdabcd', 'bcd', 2, 2) AS pos,
       ____('hello' PLACING 'world' FROM 2 FOR 3) AS replaced;

-- Step 2: Arithmetic functions bitand, round, ceil, floor
SELECT ____(29, 15) AS b_and,
       ____(1234.5678, -2) AS rnd_hundreds,
       ceil(-42.8) AS c_val,
       floor(-42.8) AS f_val;

-- Step 3 (Ch.05 Quiz Q1): Add 7 days to 2021-4-28
SELECT date '2021-4-28' + ____ '7' AS RESULT;
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Use `instr(...)` and `overlay(...)` in Step 1.
- Use `bitand(29, 15)` and `round(1234.5678, -2)` in Step 2.
- Use `integer '7'` in Step 3.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
SELECT instr('abcdabcdabcd', 'bcd', 2, 2) AS pos,
       overlay('hello' PLACING 'world' FROM 2 FOR 3) AS replaced;

SELECT bitand(29, 15) AS b_and,
       round(1234.5678, -2) AS rnd_hundreds,
       ceil(-42.8) AS c_val,
       floor(-42.8) AS f_val;

SELECT date '2021-4-28' + integer '7' AS RESULT;
```

#### Expected Console / Query Output:
```text
pos | replaced 
-----+----------
   6 | hworldo
(1 row)

 b_and | rnd_hundreds | c_val | f_val 
-------+--------------+-------+-------
    13 |         1200 |   -42 |   -43
(1 row)

       result        
---------------------
 2021-05-05 00:00:00
(1 row)
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Multiple-Choice (Select ALL)]
**(Official Ch.05 Quiz p. 468 Q2) Which of the following are arithmetic functions in openGauss?**

- A. length(str)
- B. sin(n)
- C. round(v numeric, s int)
- D. hex(p1)

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `BC`
- **Explanation:** Per Chapter 05 (pp. 456–457 & p. 468), `sin(n)` (sine value) and `round(v numeric, s int)` (rounding a numeric value) are arithmetic functions. `length(str)` and `hex(p1)` are character/string functions.
</details>

### Question 2 [Multiple-Choice (Select ALL)]
**(Official Ch.05 Quiz p. 469 Q4) Which three separate approaches to pattern matching are provided by an openGauss database?**

- A. LIKE
- B. Same
- C. SIMILAR TO
- D. POSIX regular expressions

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `ACD`
- **Explanation:** Per Chapter 05 (p. 469), the three pattern matching approaches are `LIKE`, `SIMILAR TO`, and `POSIX regular expressions`.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**(Official Ch.05 Quiz p. 469 Q3) Which of the following are logical operators in openGauss?**

- A. and
- B. or
- C. not
- D. not or

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 05 (p. 449 & p. 469), the logical operators in openGauss are `and`, `or`, and `not`.
</details>
