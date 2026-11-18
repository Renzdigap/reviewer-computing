# Hands-On Lab: Writing `if-then-fi` and Multi-Branch `case ... in ... esac` Scripts

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 07 — Shell Scripting, Variables, Control Flow & Automation (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `05-Lecture-Shell-Conditional-Statements-if-and-case`  
**Interactive Workbench:** Open **[`06-Exercise-If-Then-and-Case-Branching-Lab.html`](./06-Exercise-If-Then-and-Case-Branching-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You are writing a service controller script on openEuler. Use an `if` statement to check whether `/etc/hosts` exists (`ls /etc/hosts`), and use a `case` statement on `$ACTION` to handle `start|run`, `stop`, and default `*` branches.

### Step-by-Step Instructions
1. Step 1: Complete the `if` statement that checks `ls /etc/hosts` and closes with `fi`.
2. Step 2: Complete the `case $ACTION in` statement using `start | run)` for the first branch and `;;` to terminate branches.
3. Step 3: Use `*)` for the default branch and close the `case` block with `esac`.

### Starter Workspace (`root@openEuler:~#`)
```bash
#!/bin/bash
# Step 1: Check if /etc/hosts exists using if-then-fi
if ls /etc/hosts
then
    echo "/etc/hosts is present"
<close_if>

# Step 2 & 3: Multi-branch case statement
ACTION="start"
case $ACTION in
<start_or_run_pattern>)
    echo "Starting service..."
    ;;
stop)
    echo "Stopping service..."
    ;;
<default_pattern>)
    echo "Usage: start|stop"
    ;;
<close_case>
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Close an `if` statement with `fi`.
- Separate multiple patterns in `case` with a vertical bar: `start | run)`.
- Use `*)` for the default pattern and close `case` with `esac`.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
#!/bin/bash
# Step 1: Check if /etc/hosts exists using if-then-fi
if ls /etc/hosts
then
    echo "/etc/hosts is present"
fi

# Step 2 & 3: Multi-branch case statement
ACTION="start"
case $ACTION in
start | run)
    echo "Starting service..."
    ;;
stop)
    echo "Stopping service..."
    ;;
*)
    echo "Usage: start|stop"
    ;;
esac
```

#### Expected Console / Query Output:
```text
/etc/hosts
/etc/hosts is present
Starting service...
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**In a Bash `if command; then commands; fi` structure, under what condition does the Bash shell execute the commands inside the `then` block?**

- A. When the command following `if` returns an exit status code of `1`
- B. When the command following `if` returns an exit status code of `0`
- C. When the command following `if` outputs a non-empty error message to stderr
- D. Only when `esac` is specified

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.06 (p.356), the Bash shell executes the command following `if` first. If the exit status code is `0`, the Bash shell continues to execute the commands in `then`.
</details>

### Question 2 [Single-Choice]
**In a shell `case` statement, which symbol separates multiple patterns in the same branch, and which symbol represents the default catch-all branch?**

- A. `,` (comma) and `default:`
- B. `|` (vertical bar) and `*)`
- C. `&&` (double ampersand) and `?)`
- D. `;` (semicolon) and `#)`

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.06 (p.357), in a `case` statement, multiple patterns can be separated by vertical bars (`|`), and the asterisk (`*`) indicates all values that do not match the known patterns.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following keywords are used to close an `if` statement and a `case` statement in Bash respectively?**

- A. `fi` closes an `if` statement
- B. `esac` closes a `case` statement
- C. `done` closes a `case` statement
- D. `endif` closes an `if` statement

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `AB`
- **Explanation:** Per Ch.06 (pp.356–357), `if` closes with `fi` and `case` closes with `esac` (`do` loops close with `done`).
</details>
