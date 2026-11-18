# 💻 Hands-On Lab: Variable Brace Expansion (`${FIRST}_LAST`) & Shell Arithmetic (`[...]`) Time Calculation

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 07 — Shell Scripting, Variables, Control Flow & Automation (Sprint 2 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `03-Lecture-Shell-Variables-Quoting-and-Arithmetic`  
**Interactive Workbench:** Open **[`04-Exercise-Variables-Braces-and-Arithmetic-Lab.html`](./04-Exercise-Variables-Braces-and-Arithmetic-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
Complete the official openEuler shell script exercises from Ch.06 (pp. 347–350): use `${FIRST}_LAST` to output `john_Doe`, and calculate the number of seconds in a day (`86400`) using `[ SEC_PER_MIN * MIN_PER_HR * $HR_PER_DAY ]`.

### 📋 Step-by-Step Instructions
1. Step 1: Assign `FIRST=john` and `LAST=Doe` (no spaces around `=`), and echo `${FIRST}_$LAST`.
2. Step 2: Define `SEC_PER_MIN=60`, `MIN_PER_HR=60`, and `HR_PER_DAY=24`.
3. Step 3: Compute `SEC_PER_DAY=[ SEC_PER_MIN * MIN_PER_HR * HR_PER_DAY ]` and echo the result.

### 📝 Starter Workspace (`root@openEuler:~#`)
```bash
#!/bin/bash
# Step 1: Assign FIRST=john, LAST=Doe and print john_Doe using brace expansion
FIRST=john
LAST=Doe
echo <brace_expansion>

# Step 2 & 3: Calculate seconds per day using $[ ... ]
SEC_PER_MIN=60
MIN_PER_HR=60
HR_PER_DAY=24
SEC_PER_DAY=<arithmetic_expression>
echo "There are $SEC_PER_DAY seconds in a day"
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Use `echo ${FIRST}_$LAST` (Ch.06 p.347).
- Use `SEC_PER_DAY=[ SEC_PER_MIN * MIN_PER_HR * HR_PER_DAY ]` (Ch.06 p.350).
- Remember `*` is the multiplication operator in shell expressions.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
#!/bin/bash
# Step 1: Assign FIRST=john, LAST=Doe and print john_Doe using brace expansion
FIRST=john
LAST=Doe
echo ${FIRST}_$LAST

# Step 2 & 3: Calculate seconds per day using $[ ... ]
SEC_PER_MIN=60
MIN_PER_HR=60
HR_PER_DAY=24
SEC_PER_DAY=[ SEC_PER_MIN * MIN_PER_HR * HR_PER_DAY ]
echo "There are $SEC_PER_DAY seconds in a day"
```

#### Expected Console / Query Output:
```text
john_Doe
There are 86400 seconds in a day
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**[Official Ch.06 Quiz Q1] Which of the following is the meaning of `*` in a shell script expression?**

- A. Summation
- B. Multiplication
- C. Subtraction
- D. Division

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Official Ch.06 Quiz Q1 (p.379): B (Multiplication). In shell arithmetic expressions (p.351), `*` denotes multiplication and `**` denotes exponentiation.
</details>

### Question 2 [True / False]
**[Official Ch.06 Quiz Q2] An administrator can run the `name==Tom` command to assign value Tom to variable name.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Official Ch.06 Quiz Q2 (p.379): False. Variable assignment in the shell uses a single equals sign with no spaces (`name=Tom`), not `==`.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about shell variables, quoting, and increments in openEuler are TRUE?**

- A. `printenv` views global environment variables, while `set` views all variables (local, global, user-defined) and functions in the process.
- B. Single quotes (`'`) preserve literal characters without expanding variables, whereas double quotes (`"`) expand variables and commands.
- C. A shell variable name must start with a letter or underscore (`_`) and cannot contain spaces around `=` during assignment.
- D. If `i=3`, running `echo [++i]` outputs `4`, and then running `echo [i++]` also outputs `4` (leaving `i` equal to `5`).

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.06 (pp.345–353), all four statements are directly from the official Huawei training slides.
</details>
