# 📖 Shell Variables, Quoting, `read` & Arithmetic Operations (`$[...]`, `++i` vs. `i++`)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 07 — Shell Scripting, Variables, Control Flow & Automation (Sprint 2 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `04-Exercise-Variables-Braces-and-Arithmetic-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.06, pp. 342–353, 379

---

## 🎯 Learning Objectives
- Distinguish special characters (`#`, `'`, `\`, `/`, `!`), environment vs. user-defined variables, and `printenv` vs. `set`
- Apply strict variable assignment rules (`variable=value` — NO spaces, `name==Tom` is FALSE [Ch.06 Quiz Q2!]), single vs. double quotes, `${VAR}` brace expansion, and `read`
- Evaluate integer arithmetic using `$[expression]` (`*` = Multiplication [Ch.06 Quiz Q1!], operator precedence, and `++i` vs. `i++`)

---

### 1. Special Characters & Variable Scopes (`printenv` vs. `set`)
* **5 Key Shell Special Characters (Ch.06, p.343):**
  * **`#` (Hashtag/Remarks):** Comments out lines (`#!` is shebang; `#` inside `'...'` or `"..."` is a literal `#`, not a comment!).
  * **`'` (Single Quote / Full Quoting):** Preserves the **exact literal value** of every character inside; **does NOT expand variables or commands**.
  * **`"` (Double Quote):** **Expands variables (`$VAR`) and commands** inside the quotes.
  * **`\` (Backslash / Escape):** Removes special meaning from the next character, or escapes a newline at the end of a line for line continuation.
  * **`/` (Forward Slash):** Root directory / path separator, or **division** in arithmetic (`a=4/2`).
  * **`!` (Bang / Negation):** Negates a test/exit status, `!=` (not equal), or character range negation (`ls a[!0-9]`).
* **Variable Types & Inspection (Ch.06, p.345):**
  * **Environment vs. User-defined**, scoped as **Global** (current shell + subshells; persisted via `export` in `.bash_profile` or `.bashrc`) or **Local**.
  * **`printenv` (or `env`):** Views **global environment variables**.
  * **`set`:** Built-in shell command that displays **ALL variables in a process** (local, global, user-defined, and shell functions).

---

### 2. Variable Naming, Assignment, Brace Expansion & `read`
* **Naming Rules:** Consists of letters, digits, and underscores (`_`); **must start with a letter or underscore (`_`)**; cannot use shell keywords.
* **Assignment Rule (Official Ch.06 Quiz Q2!):**
  * Syntax: **`variable=value`** (e.g., `name=Tom`).
  * **NO spaces are allowed on the left or right of `=`!**
  * **Official Ch.06 Quiz Q2 Trap:** *"An administrator can run the `name==Tom` command to assign value Tom to variable name."* -> **False!** (`==` is equality comparison, NOT assignment!).
* **Brace Expansion (`${VAR}` — Ch.06, p.347):**
  * If `FIRST=john`, `FIRST_=Jane`, and `LAST=Doe`, then `echo FIRST_LAST` outputs **`Doe`** (because bash looks up `FIRST_` + `LAST`? Wait: if `FIRST_` was unset it would output `Doe`; on Slide 27, when you want `FIRST` followed by `_` and `LAST`, you **must use braces**: **`echo ${FIRST}_$LAST` -> `john_Doe`**!).
* **`read <var>`:** Waits for user keyboard input and assigns it to `<var>`.

---

### 3. Arithmetic Operations (`$[...]`), Precedence & `++i` vs. `i++`
* **Syntax:** **`[expression]`** (e.g., `echo [1+1]` -> `2`, `echo $[2*2]` -> `4`).
* **Official Ch.06 Quiz Q1:** In a shell script arithmetic expression, **`*` means Multiplication**!
* **Arithmetic Operator Precedence (Highest to Lowest — Ch.06, p.352):**
  1. **`<VAR>++`, `<VAR>--`** (Post-increment / Post-decrement)
  2. **`++<VAR>`, `--<VAR>`** (Pre-increment / Pre-decrement)
  3. **`-`, `+`** (Unary minus / plus)
  4. **`**`** (Exponentiation)
  5. **`*`, `/`, `%`** (Multiplication, Division, Remainder)
  6. **`+`, `-`** (Addition, Subtraction)
* **`++i` vs. `i++` (Ch.06, p.353):**
  * `i++` creates a temporary variable to save the old value of `i`, returns that old value, and then increments `i` by 1.
  * `++i` directly adds 1 to `i`'s memory space and returns the new value without creating temporary space (higher performance).
  * **Slide 33 Example:** If `i=3`, `echo [++i]` outputs **`4`** (`i` becomes 4); then `echo [i++]` outputs **`4`** (returns old value 4, while `i` becomes 5); then `echo $i` outputs **`5`**!

---

## 🔑 Key Takeaways
- **Variable assignment is 'variable=value' with NO spaces around '='; 'name==Tom' is NOT a valid assignment (Ch.06 Quiz Q2 = False).**
- **Single quotes ('') preserve literal characters without variable expansion, whereas double quotes ("") expand variables and commands; use ${FIRST}_$LAST to disambiguate variable boundaries.**
- **In a shell arithmetic expression ($[...]), '*' means Multiplication (Ch.06 Quiz Q1); printenv displays global variables, whereas 'set' displays all local, global, and user-defined variables.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Official Ch.06 Quiz Q1): 'Which of the following is the meaning of * in a shell script expression?' -> B. Multiplication!

> [!WARNING]
> EXAM TRAP (Official Ch.06 Quiz Q2): 'An administrator can run the name==Tom command to assign value Tom to variable name.' -> False!

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`04-Exercise-Variables-Braces-and-Arithmetic-Lab.html`](./04-Exercise-Variables-Braces-and-Arithmetic-Lab.html)** (or [`04-Exercise-Variables-Braces-and-Arithmetic-Lab.md`](./04-Exercise-Variables-Braces-and-Arithmetic-Lab.md)) to apply this concept in an interactive lab workbench!
