# 📖 Shell Conditional Statements (`if-then-elif-else-fi` and `case-in-esac`)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 07 — Shell Scripting, Variables, Control Flow & Automation (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `06-Exercise-If-Then-and-Case-Branching-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.06, pp. 354–357

---

## 🎯 Learning Objectives
- Explain how Bash `if` evaluates command exit status codes (`0` = True/Success, non-zero = False)
- Write `if-then-fi`, `if-then-else-fi`, and `elif` conditional blocks using numeric, string, and file tests
- Construct multi-branch `case ... in ... esac` statements using `|` pattern alternation, `;;` terminators, and `*` default wildcards

---

### 1. How `if-then-fi` Works in Bash (Exit Status Code `0`)
Unlike C or Java (where `if` evaluates a boolean `true`/`false` expression), **the Bash `if` statement executes the command following `if` and checks its exit status code (`$?`)**:
* **If the exit status code is `0` (Success):** Bash executes the commands inside the **`then`** block!
* **If the exit status code is non-zero (Failure):** Bash skips the `then` block (and evaluates `elif` / `else`, or moves to the next statement after `fi`).

```bash
if command
then
    commands
fi
```
* **Common Test Conditions (`[ ... ]` / `test` / `(( ... ))`):**
  * **Numeric comparisons:** `-eq` (equal), `-ne` (not equal), `-gt` (greater than), `-ge` (greater or equal), `-lt` (less than), `-le` (less or equal), or C-style `(( i % 5 == 0 ))`.
  * **String comparisons:** `=` / `==` (equal), `!=` (not equal), `-z` (empty string), `-n` (non-empty string).
  * **File checks:** `-e` (exists), `-f` (regular file), `-d` (directory), `-r` (readable), `-w` (writable), `-x` (executable).

---

### 2. Multi-Branch Judgment with `case ... in ... esac`
When checking a single variable against multiple distinct values/patterns, a **`case`** statement is cleaner and more readable than deeply nested `if-then-elif-else` blocks (Ch.06, p.357):

```bash
case variable in
pattern1 | pattern2)
    commands1
    ;;
pattern3)
    commands2
    ;;
*)
    default commands
    ;;
esac
```

---

### 3. Key Syntax Rules for `case` Statements
* **Opening & Closing Keywords:** Starts with **`case variable in`** and closes with **`esac`** (`case` spelled backwards!).
* **Pattern Alternation (`|`):** Multiple patterns sharing the same branch are separated by a **vertical bar (`|`)**, followed by a closing parenthesis **`)`**.
* **Branch Terminator (`;;`):** Every pattern branch (except optionally the last) must end with a **double semicolon (`;;`)**.
* **Default Catch-All (`*)`):** The asterisk **`*)`** matches **all values that do not match the known patterns** (equivalent to `default:` in C/Java).

---

## 🔑 Key Takeaways
- **In a Bash 'if command; then ... fi' statement, the 'then' block executes ONLY when the command following 'if' returns an exit status code of 0!**
- **A multi-branch 'case' statement starts with 'case $var in' and ends with 'esac'.**
- **In 'case', multiple patterns are separated by '|', each branch ends with ';;', and '*)' serves as the default catch-all branch.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: In C/Python, 0 is False and 1 is True; in Bash 'if command', exit status code 0 means SUCCESS (True, executes 'then'), while any non-zero exit code (1–255) means FAILURE (False)!

> [!WARNING]
> EXAM TRAP: Do not forget ';;' at the end of each pattern block and 'esac' at the end of a 'case' statement.

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-If-Then-and-Case-Branching-Lab.html`](./06-Exercise-If-Then-and-Case-Branching-Lab.html)** (or [`06-Exercise-If-Then-and-Case-Branching-Lab.md`](./06-Exercise-If-Then-and-Case-Branching-Lab.md)) to apply this concept in an interactive lab workbench!
