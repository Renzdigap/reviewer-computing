# 📖 DQL Queries — Filtering (`WHERE`), Sorting (`ORDER BY`) & Pagination (`LIMIT`/`OFFSET`)

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 06 — SQL Basics — Classification, Data Types, DQL, Joins & DML (Sprint 2 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `04-Exercise-WHERE-ORDER-BY-and-LIMIT-OFFSET-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.05, pp. 373–395

---

## 🎯 Learning Objectives
- Write `SELECT` queries with column/table aliases (`AS` or space) and `WHERE` conditions (`Position = 'Engineer' AND Salary > 6000`, `BETWEEN ... AND ...`)
- Sort results with `ORDER BY` using column names, 1-based column positions (`ORDER BY 2 DESC, 3 ASC` — Ch.05 Quiz!), or expressions, plus `NULLS FIRST | LAST`
- Paginate queries using `LIMIT count OFFSET start`, `OFFSET start LIMIT count`, and `LIMIT offset, count`

---

### 1. Relational Operations & Conditional Filtering (`WHERE`, pp. 374–382, 394)
- **3 Relational Algebra Operations in `SELECT` (p. 374)**:
  1. **`SELECT` (Selection)**: Filters rows (tuples) that satisfy a condition.
  2. **`PROJECT` (Projection)**: Selects specific columns (attributes) and filters out others.
  3. **`JOIN`**: Combines rows from multiple tables.
- **Conditional Query Rules (`WHERE`, pp. 380–382, Ch.05 p. 394 Quizzes!)**:
  - **String & Date Literals**: Single quotation marks (`'...'`) are optional for numbers but **mandatory for character strings and dates**!
    - **Ch.05 p. 394 Quiz Q1**: Searching for records whose position is an engineer and salary > 6000 is **`Position = 'Engineer' AND Salary > 6000`** (Option D — `'Engineer'` must be in single quotes and joined with `AND`!).
  - **Range Predicate (`BETWEEN ... AND ...`)**: Inclusive on both bounds!
    - **Ch.05 p. 394 Quiz Q2**: **`age BETWEEN 20 AND 30`** is strictly equivalent to **`age >= 20 AND age <= 30`** (Option A!).
  - **Logical Operator Precedence & Three-Valued Logic (`TRUE`, `FALSE`, `NULL`)**:
    - Priority order: **`NOT` > `AND` > `OR`**.
    - Truth table with `NULL` (Unknown):
      - **`TRUE OR NULL` -> `TRUE`**; **`FALSE OR NULL` -> `NULL`**.
      - **`FALSE AND NULL` -> `FALSE`**; **`TRUE AND NULL` -> `NULL`**.
      - **`NOT NULL` -> `NULL`**.

---

### 2. Data Sorting (`ORDER BY`, pp. 390–391, 395)
```sql
ORDER BY { column_name | number | expression } [ ASC | DESC ] [ NULLS FIRST | NULLS LAST ] [, ...]
```
- **Default Order**: **`ASC`** (ascending) is the default when neither `ASC` nor `DESC` is specified!
- **Sorting by Column Position (`number`)**: `1` refers to the 1st column in the `SELECT` list, `2` refers to the 2nd column, etc.
  - **Ch.05 p. 395 Quiz Q3 (Answer: AC!)**: To query `name, age, score` from `student` sorted by `age` descending and then `score` ascending:
    - **Option A**: `SELECT name, age, score FROM student order by age desc, score;` (valid because `score` defaults to `ASC`!)
    - **Option C**: `SELECT name, age, score FROM student order by 2 desc, 3 asc;` (valid because `2` is `age` and `3` is `score`!)
- **Default `NULL` Placement (p. 390)**:
  - For **`ASC`**, **`NULLS FIRST`** is the default in openGauss (per slide 38, p. 390).
  - For **`DESC`**, **`NULLS LAST`** is the default.

---

### 3. Data Limit & Pagination (`LIMIT` and `OFFSET`, pp. 392–393)
- **`LIMIT count`**: Maximum number of rows to return.
- **`OFFSET start`**: Number of initial rows to skip before returning rows.
- **Three Equivalent Syntax Forms in openGauss (p. 392)**:
  - **`LIMIT 5, 20`** $\equiv$ **`LIMIT 20 OFFSET 5`** $\equiv$ **`OFFSET 5 LIMIT 20`**
  - All three mean: **skip the first 5 rows, and return at most 20 rows**!

---

## 🔑 Key Takeaways
- **String literals in `WHERE` must be enclosed in single quotes (`Position = 'Engineer' AND Salary > 6000`), and `age BETWEEN 20 AND 30` is equivalent to `age >= 20 AND age <= 30` (Ch.05 p. 394 Q1 & Q2).**
- **In `ORDER BY`, `ASC` is the default direction, and you can reference `SELECT` columns by their 1-based position (`ORDER BY 2 DESC, 3 ASC` is equivalent to `ORDER BY age DESC, score` for `SELECT name, age, score` — Ch.05 p. 395 Q3: AC).**
- **`LIMIT 5, 20`, `LIMIT 20 OFFSET 5`, and `OFFSET 5 LIMIT 20` are all equivalent and output 20 rows after skipping 5 rows.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.05 p. 395 Quiz Q3): Both `SELECT name, age, score FROM student order by age desc, score;` (A) and `SELECT name, age, score FROM student order by 2 desc, 3 asc;` (C) are correct! Don't forget that omitting `ASC` after `score` defaults to ascending order.

> [!WARNING]
> EXAM TRAP: In `LIMIT 5, 20` (comma syntax), the FIRST number (`5`) is the offset (rows skipped) and the SECOND number (`20`) is the row count, whereas in `LIMIT 20 OFFSET 5`, `20` is the count and `5` is the offset!

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`04-Exercise-WHERE-ORDER-BY-and-LIMIT-OFFSET-Lab.html`](./04-Exercise-WHERE-ORDER-BY-and-LIMIT-OFFSET-Lab.html)** (or [`04-Exercise-WHERE-ORDER-BY-and-LIMIT-OFFSET-Lab.md`](./04-Exercise-WHERE-ORDER-BY-and-LIMIT-OFFSET-Lab.md)) to apply this concept in an interactive lab workbench!
