# 📖 Loop Statements (`for`, `while`, `until`), `break`/`continue`, Debugging (`bash -x`) & Best Practices

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 07 — Shell Scripting, Variables, Control Flow & Automation (Sprint 4 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `08-Exercise-Odd-Accumulator-and-Bash-Debug-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.06, pp. 358–380

---

## 🎯 Learning Objectives
- Write `for` (shell-style & C-style), `while`, and `until` loops, including the official Odd Accumulator (`{1..100..2}`) and 9×9 Multiplication Table scripts
- Control loop execution with `break` (exit entire loop) and `continue` (skip current round to next iteration)
- Debug shell scripts using `#!/bin/bash -x` / `bash -x`, evaluate `$?` exit status codes (`0` vs. `2` for missing file in `ls`), and apply shell coding style best practices

---

### 1. Loop Statements: `for`, `while`, and `until`
Bash provides three loop constructs (**`for`**, **`while`**, **`until`**), all using **`do ... done`** for the loop body, plus **`break`** and **`continue`**:

| Loop / Control | Syntax & Official Examples (Ch.06, pp. 359–367) |
| :--- | :--- |
| **`for` (Shell style)** | `for var in list; do commands; done`<br>• List forms: `host1 host2 host3`, brace range **`host{1..3}`**, step range **`{1..100..2}`**, command substitution **`$(seq 2 2 8)`** or **`$(ls)`**. |
| **`for` (C style)** | `for (( i = 1; i <= 9; i++ )); do ... done` (used in the 9×9 Multiplication Table script). |
| **`while` Loop** | Pre-test loop that repeats **while the condition is TRUE**:<br>`sum=0; i=1; while (( i <= 100 )); do let "sum+=i"; let "i += 2"; done` |
| **`until` Loop** | Repeats **until the exit condition becomes TRUE** (runs while condition is FALSE):<br>`sum=0; i=1; until (( i > 100 )); do let "sum+=i"; let "i += 2"; done` |
| **`break` vs. `continue`** | • **`break`**: Immediately **interrupts and exits the entire loop** (e.g., find first number divisible by 5: `if (( i % 5 == 0 )); then break; fi`).<br>• **`continue`**: **Skips the rest of the current iteration** and starts the next round of the loop (e.g., skip numbers divisible by 3: `if (( i % 3 == 0 )); then continue; fi`). |

* **Official Odd Accumulator Script (`1 + 3 + 5 + ... + 99 = 2500` — Ch.06, p.361):**
  ```bash
  #!/bin/bash
  sum=0
  for i in {1..100..2}
  do
      let "sum+=i"
  done
  echo "sum=$sum"
  ```

---

### 2. Debugging Mode (`-x`) & Exit Status Codes (`$?`)
* **Activating Bash Debugging Mode (2 Ways — Ch.06, pp. 370–371):**
  1. Add **`-x`** to the shebang line inside the script: **`#!/bin/bash -x`**
  2. Invoke `bash` with **`-x`** from the CLI: **`bash -x adder.sh`**
  * *Effect:* Prints each command and expanded variable values in real time (prefixed with `+`) before executing it!
* **Evaluating Exit Status Codes (`$?` — Ch.06, pp. 372–373):**
  * Every command returns an exit code stored in **`$?`**.
  * **`0`** indicates success (`ls /etc/hosts` -> `echo $?` outputs **`0`**).
  * Non-zero indicates an error (`ls /etc/nofile` -> `echo $?` outputs **`2`**).
  * Use **`exit <N>`** (e.g., `exit 1`) inside a script to terminate immediately and return exit code `<N>` to the caller.

---

### 3. Shell Coding Style Best Practices (Ch.06, pp. 374–376)
* Break long one-liners into readable multi-line steps using descriptive intermediate variables (`PACKAGETYPE=kernel`, `INSTALLEPOCH=...`, `INSTALLDATETIME=...`).
* Align `if/fi` and `do/done`, indent nested blocks, add comments (`#`), and use blank lines to separate logical sections.

---

## 🔑 Key Takeaways
- **while (( i <= 100 )) loops while the condition is true; until (( i > 100 )) loops until the condition becomes true.**
- **break exits the entire loop immediately, whereas continue skips only the current iteration and proceeds to the next loop round.**
- **Enable script trace debugging with '#!/bin/bash -x' or 'bash -x script.sh'; check the previous command's exit status code with 'echo $?' (0 = success).**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Do not confuse 'while' and 'until' conditions! For the Odd Accumulator (1 to 100), 'while' uses 'while (( i <= 100 ))', whereas 'until' uses the opposite termination condition 'until (( i > 100 ))'!

> [!WARNING]
> EXAM TRAP: When 'ls' fails because a file does not exist ('ls /etc/nofile'), 'echo $?' outputs 2 (Ch.06 p.372).

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`08-Exercise-Odd-Accumulator-and-Bash-Debug-Lab.html`](./08-Exercise-Odd-Accumulator-and-Bash-Debug-Lab.html)** (or [`08-Exercise-Odd-Accumulator-and-Bash-Debug-Lab.md`](./08-Exercise-Odd-Accumulator-and-Bash-Debug-Lab.md)) to apply this concept in an interactive lab workbench!
