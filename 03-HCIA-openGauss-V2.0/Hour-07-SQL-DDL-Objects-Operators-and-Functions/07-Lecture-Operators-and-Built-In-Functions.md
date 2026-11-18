# Operators & Built-in Functions (String, Numeric, Date/Time, Pattern Matching, Geometric)

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 07 — SQL DDL Objects, Sequences, Operators & Built-in Functions (Sprint 4 of 4)  
**Format:** Bite-Sized Lecture (7 mins) - Followed immediately by `08-Exercise-String-Numeric-Date-and-Geometric-Functions-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.05, pp. 448–469

---

## Learning Objectives
- Master Logical Operators (`and`, `or`, `not` — Ch.05 Quiz Q3: ABC!) and the 3 Pattern Matching approaches (`LIKE`, `SIMILAR TO`, `POSIX regular expressions` — Ch.05 Quiz Q4: ACD!)
- Evaluate Character Functions (`instr`, `overlay`, `insert`, `substring`, `replace`, `lpad`/`rpad`), Arithmetic Operators (`!!`, `@`, `|/`, `||/`, `^`, `&`, `#`, `~`, `<<`, `>>`) & Functions (`sin`, `round`, `bitand`, `ceil`, `floor` — Ch.05 Quiz Q2: BC!)
- Compute Date/Time Arithmetic (`SELECT date '2021-4-28' + integer '7'` — Ch.05 Quiz Q1!), Type Conversions (`cast`, `to_char`, `to_date`, `to_number`), and Geometric Operators/Functions

---

### 1. Logical Operators, Pattern Matching & Character Functions (pp. 449–454, 469)
- **Logical Operators (Ch.05 p. 469 Quiz Q3: ABC!)**:
  - **`and`**, **`or`**, and **`not`** (Priority: `NOT` > `AND` > `OR`). *(`not or` is NOT a logical operator!)*
- **Three Separate Approaches to Pattern Matching (Ch.05 p. 469 Quiz Q4: ACD!)**:
  1. **`LIKE`** (traditional SQL wildcard matching with `%` and `_`).
  2. **`SIMILAR TO`** (SQL:1999 regular expressions).
  3. **`POSIX regular expressions`** (`~`, `~*`, `!~`, `!~*`). *(Option B `Same` is NOT a pattern matching method!)*
- **High-Yield Character Processing Functions (pp. 451–454)**:
  - **`instr(str1, str2, pos, nth)`**: Searches `str1` starting at `pos` for the `nth` occurrence of `str2` and returns the 1-based character index from the start of `str1` (or `0` if not found).
    - Example: `SELECT instr('abcdabcdabcd', 'bcd', 2, 2);` -> Starts at pos 2 (`'bcdabcdabcd'`), 1st match is at pos 2, **2nd match is at pos `6`**!
  - **`overlay(str PLACING newstr FROM pos [FOR len])`**: Replaces `len` chars starting at `pos`.
    - Example: `SELECT overlay('hello' PLACING 'world' FROM 2 FOR 3);` -> Replaces `'ell'` with `'world'` -> **`'hworldo'`**.
  - **`insert(str, pos, len, newstr)`**: `insert('quadratic', 5, 2, 'what')` \\equiv `replace('quadratic', 'ra', 'what')` -> `'quadwhattic'`.
  - **`substring('Thomas' FROM 2 FOR 3)`** -> **`'hom'`**; **`replace('abcdefabcdef', 'cd', 'XXX')`** -> **`'abXXXefabXXXef'`**.
  - **`lpad('hi', 5, 'xyza')`** -> **`'xyzhi'`**; **`rpad('hi', 5, 'xy')`** -> **`'hixyx'`**; **`reverse('abcde')`** -> **`'edcba'`**.
  - **`char_length('hello')`** (char count) vs. **`lengthb('hello')`** (byte count); **`ascii(str)`**; **`concat`** / **`concat_ws`** (max 8000 bytes).

---

### 2. Arithmetic Operators & Functions (pp. 455–458, 468)
- **Special Arithmetic & Bitwise Operators (p. 455)**:
  - **`!!`**: Factorial (prefix); **`@`**: Absolute value (`@ -5.0` = `5.0`); **`|/`**: Square root (`|/ 25.0` = `5`); **`||/`**: Cubic root; **`^`**: Power (`2.0^3.0` = `8.0`); **`|`**: Bitwise OR; **`&`**: Bitwise AND (`91 & 15` = `11`); **`#`**: Bitwise XOR (`17 # 5` = `20`); **`~`**: Bitwise NOT; **`<<` / `>>`**: Left/Right shift (`1 << 4` = `16`).
  - *Priority*: Four arithmetic ops (`* / % + -`) > Shift (`<< >>`) > Bitwise AND (`&`) > Bitwise XOR (`#`) > Bitwise OR (`|`).
  - *Decimal rounding difference*: Bitwise operators (`&`, `|`, `#`) **round off** decimal inputs first, whereas functions **`BITAND`**, **`BITOR`**, **`BITXOR`** **truncate (round down)** decimal inputs first!
- **Arithmetic Functions (pp. 456–458, Ch.05 p. 468 Quiz Q2: BC!)**:
  - **`sin(n)`**, **`cos(n)`**, **`acos(n)`**, **`asin(n)`**, **`abs(n)`**.
  - **`round(number [, decimals])`**: `round(1234.5678, -2)` -> **`1200`**; `round(1234.5678, 2)` -> **`1234.57`**.
  - **`bitand(29, 15)`** -> **`13`** (11101_2 \land 01111_2 = 01101_2 = 13).
  - **`ceil(-42.8)`** -> **`-42`** (smallest integer \≥ x); **`floor(-42.8)`** -> **`-43`** (largest integer \≤ x); **`trunc(42.8)`** -> **`42`**; **`div(9,4)`** -> **`2`**; **`mod(9,4)`** -> **`1`**; **`cbrt(27.0)`** -> **`3`**; **`log(100.0)`** -> **`2`**.
  - *(Note: `length(str)` and `hex(p1)` are character/string functions, so in Ch.05 p. 468 Quiz Q2 only **`B. sin(n)`** and **`C. round(v numeric, s int)`** are arithmetic functions!)*

---

### 3. Date/Time Operators, Type Conversions & Geometric Operators (pp. 459–468)
- **Date/Time Arithmetic (pp. 459–462, Ch.05 p. 468 Quiz Q1!)**:
  - Slide 106 (p. 459): `SELECT date '2021-5-28' + integer '7' AS RESULT;` outputs **`2021-06-04 00:00:00`** in openGauss (where `DATE` in A-compatibility mode includes `00:00:00` time).
  - **Ch.05 p. 468 Quiz Q1**: `SELECT date '2021-4-28' + integer '7' AS RESULT;` -> Adding 7 days to April 28 (April has 30 days) yields **May 5 (`2021-05-05` / `2021-05-05 00:00:00`)**! *(Note: The official slide 115 answer key prints `A` [`2021-05-05`], while openGauss `gsql` in default Oracle compatibility mode prints `2021-05-05 00:00:00` [Option C]. Know both why April 28 + 7 days = May 5 and the slide key `A` / runtime `C`!)*
  - **`justify_days(interval '35 days')`** -> **`1 mon 5 days`** (30-day month); **`last_day(...)`** -> last day of month.
- **Type Conversions**: `cast(x AS y)`, `to_char`, `to_clob`, `to_date`, `to_number`, `to_timestamp`, `to_bigint`, `hextoraw`, `rawtohex`, `numtoday`.
- **Geometric Operators & Functions (pp. 465–467)**:
  - Operators: `+` / `-` (translation), `*` / `/` (scaling/rotation), **`#`** (intersection), **`@-@`** (length/circumference), **`@@`** (center), **`<->`** (distance), **`&&`** (overlaps), **`<<` / `>>`** (strictly left/right of), **`<^` / `>^`** (below/above).
  - Functions: `area(obj)`, `center(obj)`, `diameter(circle)`, `radius(circle)`, `height(box)`, `width(box)`, `length(obj)`, `npoints(path/polygon)`, `isclosed(path)`, `isopen(path)`, `pclose(path)`, `popen(path)`.

---

## Key Takeaways
- **The arithmetic functions in Ch.05 Quiz Q2 are `B. sin(n)` and `C. round(v numeric, s int)` (`BC`); the logical operators in Quiz Q3 are `and`, `or`, `not` (`ABC`); the 3 pattern matching approaches in Quiz Q4 are `LIKE`, `SIMILAR TO`, and `POSIX regular expressions` (`ACD`).**
- **`instr('abcdabcdabcd', 'bcd', 2, 2)` returns `6`; `overlay('hello' placing 'world' from 2 for 3)` returns `'hworldo'`; `round(1234.5678, -2)` returns `1200`; `bitand(29, 15)` returns `13`.**
- **`SELECT date '2021-4-28' + integer '7' AS RESULT;` adds 7 days to April 28 (30-day month) to produce May 5 (`2021-05-05` in the Ch.05 slide answer key A, or `2021-05-05 00:00:00` in openGauss A-mode runtime C).**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.05 p. 469 Quiz Q4): 'Which three separate approaches to pattern matching are provided by a database?' -> `A. LIKE`, `C. SIMILAR TO`, `D. POSIX regular expressions` (`ACD`). `B. Same` does not exist!

> [!WARNING]
> EXAM TRAP: Watch negative numbers in `ceil(-42.8)` (`-42`, notsmaller integer) vs. `floor(-42.8)` (`-43`, not larger integer) vs. `round(1234.5678, -2)` (`1200`, rounds two digits to the left of the decimal point)!

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`08-Exercise-String-Numeric-Date-and-Geometric-Functions-Lab.html`](./08-Exercise-String-Numeric-Date-and-Geometric-Functions-Lab.html)** (or [`08-Exercise-String-Numeric-Date-and-Geometric-Functions-Lab.md`](./08-Exercise-String-Numeric-Date-and-Geometric-Functions-Lab.md)) to apply this concept in an interactive lab workbench!
