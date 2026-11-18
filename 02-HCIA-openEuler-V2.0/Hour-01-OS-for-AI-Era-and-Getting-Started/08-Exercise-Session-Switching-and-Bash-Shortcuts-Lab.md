# Hands-On Lab: Identity Verification, Shell Inspection & History Navigation

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 01 — OS for the AI Era & Getting Started with openEuler (Sprint 4 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `07-Lecture-CLI-vs-GUI-Login-and-Bash-Shortcuts`  
**Interactive Workbench:** Open **[`08-Exercise-Session-Switching-and-Bash-Shortcuts-Lab.html`](./08-Exercise-Session-Switching-and-Bash-Shortcuts-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You are logged into openEuler via SSH as `root`. Verify your current UID/GID identity, display recent command history, switch to the common user `openeuler` using a login shell, and exit back to `root`.

### Step-by-Step Instructions
1. Step 1: Run the `id` command to display the current user's UID, GID, and group memberships.
2. Step 2: Run the `history` command to view previously executed shell commands.
3. Step 3: Switch to the user `openeuler` with a full login environment using `su - openeuler`.

### Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: View current user UID and GID
<command_1>

# Step 2: View historical commands
<command_2>

# Step 3: Switch to user 'openeuler' with login environment
<command_3>
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- The `id` command prints the current user's UID and GID.
- The `history` command lists the recorded bash command history.
- Use `su - openeuler` to switch to the `openeuler` account.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: View current user UID and GID
id

# Step 2: View historical commands
history

# Step 3: Switch to user 'openeuler' with login environment
su - openeuler
```

#### Expected Console / Query Output:
```text
uid=0(root) gid=0(root) groups=0(root)
    1  cat /etc/os-release
    2  uname -r
    3  id
    4  history
Last login: Tue Nov 17 09:15:02 CST 2026 on pts/0
[openeuler@openEuler ~]$
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**[Official Ch.02 Quiz Q2] Which of the following keys can be used to quickly supplement commands and parameters?**

- A. Ctrl+L
- B. ↑ and ↓
- C. tab
- D. Space

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `C`
- **Explanation:** Official Ch.02 Quiz Q2 (p.52): C. The Tab key is used to automatically supplement (auto-complete) commands, file names, and parameters.
</details>

### Question 2 [Single-Choice]
**In the Bash shell on openEuler, which keyboard shortcut moves the cursor to the beginning of the current command line, and which moves it to the end?**

- A. Ctrl+C and Ctrl+L
- B. Ctrl+A (or Home) and Ctrl+E (or End)
- C. Alt+F1 and Alt+F6
- D. Ctrl+Z and Ctrl+D

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.02 (p.50) and Ch.03 (p.62), Home or Ctrl+A moves the cursor to the beginning of the line, while End or Ctrl+E moves the cursor to the end of the line.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following graphical desktop environments can be installed on openEuler if a GUI is required?**

- A. GNOME and XFCE
- B. UKUI (developed by Kylin Software)
- C. DDE (developed by UnionTech Software)
- D. Kiran (developed by Hunan Kylin Information Security)

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.02 (p.47), openEuler uses the CLI by default, and supports installing GNOME, UKUI, DDE, Kiran, or XFCE desktop environments as needed.
</details>
