# Hands-On Lab: Filtering, Positional `ORDER BY`, and `LIMIT / OFFSET` Pagination

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 06 — SQL Basics — Classification, Data Types, DQL, Joins & DML (Sprint 2 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `03-Lecture-DQL-Filtering-Sorting-and-Pagination`  
**Interactive Workbench:** Open **[`04-Exercise-WHERE-ORDER-BY-and-LIMIT-OFFSET-Lab.html`](./04-Exercise-WHERE-ORDER-BY-and-LIMIT-OFFSET-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
Write three DQL queries against the `employees` and `student` tables to verify exact Huawei exam syntax for `WHERE` filtering, positional `ORDER BY`, and `LIMIT / OFFSET` pagination.

### Step-by-Step Instructions
1. Step 1: Query all columns from `employees` where `Position = 'Engineer' AND Salary > 6000` and `age BETWEEN 20 AND 30`.
2. Step 2: Query `name, age, score` from `student` sorted by `age` descending and `score` ascending using positional numbers (`ORDER BY 2 DESC, 3 ASC`).
3. Step 3: Add `LIMIT 20 OFFSET 5` to skip 5 rows and return 20 rows.

### Starter Workspace (`openGauss=#`)
```bash
-- Step 1: Filter Engineers with Salary > 6000 and age between 20 and 30
SELECT * FROM employees
WHERE Position = ____ AND Salary > 6000 AND age ____ 20 AND 30;

-- Step 2 & 3: Query student sorted by 2nd col DESC, 3rd col ASC, skipping 5 rows and returning 20
SELECT name, age, score FROM student
ORDER BY ____ DESC, ____ ASC
LIMIT ____ OFFSET ____;
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Enclose `'Engineer'` in single quotes and use the `BETWEEN 20 AND 30` operator.
- In `SELECT name, age, score`, `age` is column `2` and `score` is column `3`.
- To skip 5 rows and return 20 rows, use `LIMIT 20 OFFSET 5`.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
SELECT * FROM employees
WHERE Position = 'Engineer' AND Salary > 6000 AND age BETWEEN 20 AND 30;

SELECT name, age, score FROM student
ORDER BY 2 DESC, 3 ASC
LIMIT 20 OFFSET 5;
```

#### Expected Console / Query Output:
```text
emp_id |  name   | position | salary | age 
--------+---------+----------+--------+-----
    101 | Li Ming | Engineer |   8500 |  26
(1 row)

   name   | age | score 
----------+-----+-------
 Zhang Yi |  22 |    88
 Wang Wu  |  22 |    95
 Zhao Liu |  21 |    91
(3 rows)
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**(Official Ch.05 Quiz p. 394 Q1) Which of the following logical expressions is used to search for records whose position is an engineer and salary is greater than 6000?**

- A. Position = 'Engineer' OR Salary > 6000
- B. Position = Engineer AND Salary > 6000
- C. Position = Engineer OR Salary > 6000
- D. Position = 'Engineer' AND Salary > 6000

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `D`
- **Explanation:** Per Chapter 05 (p. 381 & p. 394), character string literals must be enclosed in single quotation marks (`'Engineer'`), and both conditions must hold simultaneously (`AND`).
</details>

### Question 2 [Single-Choice]
**(Official Ch.05 Quiz p. 394 Q2) In a `WHERE` clause, the expression `age between 20 and 30` is equivalent to:**

- A. age >= 20 and age <= 30
- B. age >= 20 or age <= 30
- C. age > 20 and age < 30
- D. age > 20 or age < 30

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** Per Chapter 05 (p. 394), `BETWEEN 20 AND 30` is inclusive of both endpoints and is equivalent to `age >= 20 and age <= 30`.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**(Official Ch.05 Quiz p. 395 Q3) Assume that you want to query student names, ages, and scores from the `student` table, and want the results sorted in descending order by age. If there are students of the same age, they are sorted in ascending order by score instead. Which of the following SQL statements can be used?**

- A. SELECT name, age, score FROM student order by age desc, score;
- B. SELECT name, age, score FROM student order by age, score asc;
- C. SELECT name, age, score FROM student order by 2 desc, 3 asc;
- D. SELECT name, age, score FROM student order by 1 desc, 2;

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `AC`
- **Explanation:** Per Chapter 05 (p. 390 & p. 395), Option A sorts by `age desc` and `score` (which defaults to `ASC`), and Option C uses 1-based column positions (`2` = `age`, `3` = `score`) with `2 desc, 3 asc`.
</details>
