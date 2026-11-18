# 💻 Hands-On Lab: Shell Inspection, `chmod +x`, `nohup` Backgrounding & Redirection

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 07 — Shell Scripting, Variables, Control Flow & Automation (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `01-Lecture-Shell-Basics-Execution-Redirection-and-Pipes`  
**Interactive Workbench:** Open **[`02-Exercise-Script-Execution-Nohup-and-Redirection-Lab.html`](./02-Exercise-Script-Execution-Nohup-and-Redirection-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
You are deploying a monitoring script `my_script.sh` on openEuler. Inspect the system's available shells (`/etc/shells`) and current shell (`$SHELL`), grant execute permission to `my_script.sh`, run it persistently in the background using `nohup`, and append directory listings to `dir_log`.

### 📋 Step-by-Step Instructions
1. Step 1: View all installed shells in `/etc/shells` (`cat /etc/shells`) and print the current user's default shell (`echo $SHELL`).
2. Step 2: Grant execute permission to `my_script.sh` (`chmod +x my_script.sh`) and run it persistently in the background using `nohup ./my_script.sh &`.
3. Step 3: Append the output of `ls` to `dir_log` using `ls >> dir_log`.

### 📝 Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: View installed shells and current user's default login shell
<cat_shells_command>
<echo_shell_command>

# Step 2: Grant execute permission to my_script.sh and run with nohup in background
<chmod_x_command>
<nohup_command>

# Step 3: Append ls output to dir_log
<append_redirect_command>
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Use `cat /etc/shells` and `echo $SHELL` (Ch.06 p.328).
- Use `chmod +x my_script.sh` and `nohup ./my_script.sh &` (Ch.06 p.334, 336).
- Use `ls >> dir_log` to append output (Ch.06 p.339).

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: View installed shells and current user's default login shell
cat /etc/shells
echo $SHELL

# Step 2: Grant execute permission to my_script.sh and run with nohup in background
chmod +x my_script.sh
nohup ./my_script.sh &

# Step 3: Append ls output to dir_log
ls >> dir_log
```

#### Expected Console / Query Output:
```text
/bin/sh
/bin/bash
/usr/bin/sh
/usr/bin/bash
/bin/bash

[1] 14920
nohup: ignoring input and appending output to 'nohup.out'
[root@openEuler ~]# cat dir_log
my_script.sh
nohup.out
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**When running a long-running shell script in the background, which command ensures the script continues running even after you exit the shell, and where are its standard output and standard error redirected by default?**

- A. `./my_script.sh &`; redirected to `/dev/null`
- B. `nohup ./my_script.sh &`; redirected to `nohup.out`
- C. `bg ./my_script.sh`; redirected to `/var/log/messages`
- D. `jobs ./my_script.sh`; redirected to `stdout.log`

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.06 (p.336), running `nohup ./my_script.sh &` ensures the script keeps running after you exit the shell, and redirects its standard output and standard error streams to the `nohup.out` file.
</details>

### Question 2 [Single-Choice]
**Who developed the Bourne Again Shell (`bash`) in 1989 for the GNU Project as a free software replacement for the Bourne shell?**

- A. Ken Thompson
- B. Bill Joy
- C. Brian Fox
- D. David Korn

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `C`
- **Explanation:** Per Ch.06 (p.327), in 1989, Brian Fox developed the Bourne again shell (Bash) for the open source GNU project.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about shell redirection and pipes in openEuler are TRUE?**

- A. Every Linux process has three text stream interfaces enabled when started: standard input, standard output, and standard error.
- B. `ls > dir_log` overwrites the file's previous contents, whereas `ls >> dir_log` appends to the end of the file.
- C. `command << marker` (such as `EOF`) performs inline input redirection, and the `marker` itself is not included in the standard input.
- D. A pipe (`|`) is an inter-process communication (IPC) mechanism that connects the output of one command to the input of another.

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.06 (pp.338–341), all four statements match the official Huawei training material.
</details>
