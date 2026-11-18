# 📖 SQL Classification (DDL, DML, DCL, DQL) & Data Types

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 06 — SQL Basics — Classification, Data Types, DQL, Joins & DML (Sprint 1 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `02-Exercise-SQL-Data-Types-and-Storage-Sizes-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.05, pp. 355–372

---

## 🎯 Learning Objectives
- Classify SQL commands into DDL (`CREATE`, `ALTER`, `DROP`, `TRUNCATE`), DML (`INSERT`, `UPDATE`, `DELETE`), DCL (`COMMIT`, `ROLLBACK`, `GRANT`, `REVOKE`, `LOCK TABLE`), and DQL (`SELECT`)
- Memorize exact storage byte sizes for Integer, Serial, Floating-Point, Arbitrary-Precision, Character, Date/Time, Binary, and Boolean types
- Avoid the classic exam traps on `BIGINT` (8 bytes, NOT 4 bytes — Ch.05 Quiz!) and `CLOB` (large `TEXT` object — Ch.05 Quiz!)

---

### 1. Four-Way SQL Statement Classification (pp. 358–359, Ch.05 Quizzes!)

| Category | Full Name | Core SQL Statements in openGauss |
| :--- | :--- | :--- |
| **DDL** | **Data Definition Language** | **`CREATE`**, **`ALTER`**, **`DROP`**, **`TRUNCATE TABLE`** (defines/modifies databases, tablespaces, tables, indexes, views, sequences, users, roles, functions) — *Ch.05 p. 446 Quiz Q2: C!* |
| **DML** | **Data Manipulation Language** | **`INSERT`**, **`UPDATE`**, **`DELETE`** (plus `LOAD`, `DUMP`, `EXPLAIN PLAN`) — *Ch.05 p. 405 Quiz Q2: B!* |
| **DCL** | **Data Control Language** | **`COMMIT`**, **`ROLLBACK`**, **`GRANT`**, **`REVOKE`**, **`LOCK TABLE`**, **`SHUTDOWN`** |
| **DQL** | **Data Query Language** | **`SELECT`** (and set combinations of multiple `SELECT` statements) |

---

### 2. Numeric, Character, Date/Time, Binary & Boolean Data Types (pp. 361–372)

| Type Family | Data Type | Storage Space | Key Exam Notes & Aliases |
| :--- | :--- | :--- | :--- |
| **Integers** | **`TINYINT` (`INT1`)** | **1 byte** | Whole numbers without decimals |
| | **`SMALLINT` (`INT2`)** | **2 bytes** | Used when range is guaranteed small |
| | **`INTEGER` (`INT4` / `BINARY_INTEGER`)** | **4 bytes** | Best balance of range, size, and speed |
| | **`BIGINT` (`INT8`)** | **8 bytes** | **EXAM TRAP (p. 372 Q1)**: Occupies **8 bytes**, **NOT 4 bytes**! |
| **Serial (Auto-Inc)** | `SMALLSERIAL` / `SERIAL` / `BIGSERIAL` | **2 / 4 / 8 bytes** | Not true types; creates integer col + sequence + `NOT NULL`. Cannot be added via `ALTER TABLE` or used in temp tables. |
| **Arbitrary Precision** | `NUMERIC(p,s)` / `DECIMAL(p,s)` / `NUMBER(p,s)` / `DEC(p,s)` | **2 bytes per 4 decimal digits + 8-byte overhead** | `p` (precision) in `[1, 1000]`, `s` (scale) in `[0, p]` |
| **Floating-Point** | `REAL` (`FLOAT4`) | **4 bytes** | Single-precision inexact float |
| | `DOUBLE PRECISION` (`FLOAT8` / `BINARY_DOUBLE`) | **8 bytes** | Double-precision inexact float (`FLOAT(p)` is 4 or 8B for $p \in [1,53]$) |
| **Character** | `CHAR(n)` / `CHARACTER(n)` / `NCHAR(n)` | Up to **10 MB** | Fixed-length, blank-padded (default $n=1$). ASCII = 1B/char; Unicode = 2B/char. |
| | `VARCHAR(n)` / `VARCHAR2(n)` / `NVARCHAR2(n)` | Up to **10 MB** | Variable-length string without blank padding |
| | **`TEXT` / `CLOB`** | Up to **1 GB – 1 byte** | **`CLOB` is an alias of `TEXT` used to store large text objects (p. 372 Q2: True!)** |
| **Date / Time** | `DATE` | **4 bytes** | Date and time |
| | `TIME [WITHOUT TIME ZONE]` / `TIMESTAMP` / `TIMESTAMPTZ` / `SMALLDATETIME` | **8 bytes** | `SMALLDATETIME` precision is 1 minute (30s–60s rounds up to 1 min!) |
| | `TIME WITH TIME ZONE` / `INTERVAL [FIELDS]` | **12 bytes** | `INTERVAL DAY(l) TO SECOND(p)` occupies **16 bytes** |
| **Binary & Boolean** | `BYTEA` / `RAW` / `BLOB` | Up to **1 GB – 8203 B** | `BOOLEAN` occupies **1 byte** (`TRUE`/`1` or `FALSE`/`0`) |

---

## 🔑 Key Takeaways
- **`TINYINT` = 1 byte, `SMALLINT` = 2 bytes, `INTEGER` (`BINARY_INTEGER`) = 4 bytes, and `BIGINT` = 8 bytes (Ch.05 p. 372 Quiz Q1: `BIGINT occupies four bytes` is FALSE!).**
- **`CLOB` is an alias of `TEXT` (up to 1 GB minus 1 byte) used to store large character/text objects (Ch.05 p. 372 Quiz Q2: TRUE!).**
- **`INSERT, UPDATE, DELETE` are DML commands (p. 405 Quiz Q2), whereas `CREATE, DROP, ALTER` are DDL commands (p. 446 Quiz Q2).**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.05 p. 372 Quiz Q1): '(True or false) BIGINT occupies four bytes.' -> B. False! `BIGINT` (`INT8`) occupies EIGHT (8) bytes (`INTEGER`/`INT4` occupies 4 bytes).

> [!WARNING]
> EXAM TRAP (Ch.05 p. 372 Quiz Q2): '(True or false) CLOB is used to store large object data of the TEXT type.' -> A. True!

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`02-Exercise-SQL-Data-Types-and-Storage-Sizes-Lab.html`](./02-Exercise-SQL-Data-Types-and-Storage-Sizes-Lab.html)** (or [`02-Exercise-SQL-Data-Types-and-Storage-Sizes-Lab.md`](./02-Exercise-SQL-Data-Types-and-Storage-Sizes-Lab.md)) to apply this concept in an interactive lab workbench!
