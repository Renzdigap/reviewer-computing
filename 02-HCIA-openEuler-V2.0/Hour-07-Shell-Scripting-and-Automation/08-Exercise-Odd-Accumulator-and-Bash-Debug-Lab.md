# Hands-On Lab: Odd Accumulator Script (`{1..100..2}`), `bash -x` Debugging & `$?` Exit Code Check

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 07 — Shell Scripting, Variables, Control Flow & Automation (Sprint 4 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `07-Lecture-Shell-Loops-Debugging-and-Best-Practices`  
**Interactive Workbench:** Open **[`08-Exercise-Odd-Accumulator-and-Bash-Debug-Lab.html`](./08-Exercise-Odd-Accumulator-and-Bash-Debug-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
Implement the official Odd Accumulator script (`adder.sh`) from Ch.06 (p.361) using `for i in {1..100..2}` and `let "sum+=i"`, run it in debug trace mode using `bash -x adder.sh`, and print the exit status code using `echo $?`.

### Step-by-Step Instructions
1. Step 1: Complete the `for i in {1..100..2}` loop and accumulate odd numbers using `let "sum+=i"`.
2. Step 2: Execute `adder.sh` in Bash debugging mode using `bash -x adder.sh`.
3. Step 3: Print the exit status code of the last executed command using `echo $?`.

### Starter Workspace (`root@openEuler:~#`)
```bash
#!/bin/bash
# Step 1: Odd Accumulator from 1 to 100
sum=0
for i in <odd_brace_range>
do
    let "sum+=i"
done
echo "sum=$sum"

# Step 2: Run adder.sh in debugging mode
<bash_debug_command>

# Step 3: Check exit status code
<echo_exit_code_command>
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `{1..100..2}` for odd numbers from 1 to 100 (Ch.06 p.361).
- Use `bash -x adder.sh` to run in debug mode (Ch.06 p.371).
- Use `echo $?` to check the exit code (Ch.06 p.372).

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
#!/bin/bash
# Step 1: Odd Accumulator from 1 to 100
sum=0
for i in {1..100..2}
do
    let "sum+=i"
done
echo "sum=$sum"

# Step 2: Run adder.sh in debugging mode
bash -x adder.sh

# Step 3: Check exit status code
echo $?
```

#### Expected Console / Query Output:
```text
+ sum=0
+ for i in {1..100..2}
+ let sum+=i
...
+ echo sum=2500
sum=2500
0
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**In a Bash loop, what is the difference between the `break` statement and the `continue` statement?**

- A. `break` skips the current round and enters the next round; `continue` exits the entire loop.
- B. `break` interrupts and exits the entire loop; `continue` skips the current loop round and enters the next round.
- C. `break` exits the operating system; `continue` restarts the script from line 1.
- D. Both `break` and `continue` terminate the shell process.

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.06 (pp.363–364), `break` is used to interrupt and exit the entire loop when a condition is met, whereas `continue` is used to skip the current loop round and enter the next round.
</details>

### Question 2 [Single-Choice]
**Which option can be added to `#!/bin/bash` or the `bash` CLI command to activate script debugging mode (printing each command and expanded variables before execution), and which variable stores the exit status code of the last command?**

- A. `-v` and `$0`
- B. `-x` and `$?`
- C. `-d` and `$$`
- D. `-e` and `$!`

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.06 (pp.370–372), adding `-x` (`#!/bin/bash -x` or `bash -x script.sh`) activates debugging mode, and `echo $?` retrieves the exit status code of the previous command.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following shell loop headers correctly iterate over even or odd number sequences in openEuler Bash?**

- A. `for i in {1..100..2}; do ... done` (odd numbers from 1 to 99)
- B. `for EVEN in $(seq 2 2 8); do ... done` (even numbers 2, 4, 6, 8)
- C. `while (( i <= 100 )); do ... done` (pre-test while loop)
- D. `until (( i > 100 )); do ... done` (until loop that exits when `i > 100`)

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.06 (pp.360–366), all four loop syntaxes are official examples in the Huawei HCIA-openEuler V2.0 training material.
</details>
