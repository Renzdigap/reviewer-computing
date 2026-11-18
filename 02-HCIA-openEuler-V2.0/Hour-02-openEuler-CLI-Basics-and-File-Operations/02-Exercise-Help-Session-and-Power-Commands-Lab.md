# Hands-On Lab: Querying Manual Sections, Session Logs & Safe Shutdown

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 02 — openEuler CLI Basics & File Operations (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `01-Lecture-CLI-Syntax-Help-and-Power-Management`  
**Interactive Workbench:** Open **[`02-Exercise-Help-Session-and-Power-Commands-Lab.html`](./02-Exercise-Help-Session-and-Power-Commands-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
As the system administrator on an openEuler node, you need to look up the manual page for the `/etc/passwd` file format (Section 5), check the brief description of `ls`, inspect the last 5 login records including system shutdowns, and send a simulated shutdown warning.

### Step-by-Step Instructions
1. Step 1: View the manual page for the `passwd` configuration file format (Section 5) using `man 5 passwd` and query the brief description of `ls` using `whatis ls`.
2. Step 2: Display the last 5 login/shutdown records using `last -n 5 -x`.
3. Step 3: Send a simulated shutdown warning to all logged-in users without actually shutting down using `shutdown -k now`.

### Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: View Section 5 manual for passwd and one-line summary of ls
<man_command>
<whatis_command>

# Step 2: Check last 5 login and shutdown records
<last_command>

# Step 3: Broadcast a simulated shutdown warning without powering off
<shutdown_warning_command>
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Specify the section number before the topic: `man 5 passwd`, and use `whatis ls`.
- Combine `-n 5` and `-x` with the `last` command: `last -n 5 -x`.
- Use the `-k` option of `shutdown` (`shutdown -k now`) to send a warning without shutting down.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: View Section 5 manual for passwd and one-line summary of ls
man 5 passwd
whatis ls

# Step 2: Check last 5 login and shutdown records
last -n 5 -x

# Step 3: Broadcast a simulated shutdown warning without powering off
shutdown -k now
```

#### Expected Console / Query Output:
```text
PASSWD(5)                     Linux Programmer's Manual                    PASSWD(5)
NAME
       passwd - the password file
ls (1)               - list directory contents

root     pts/0        192.168.110.1    Tue Nov 17 09:15   still logged in
runlevel (to lvl 3)   6.6.0-28.0.0.34  Tue Nov 17 09:10   still running
reboot   system boot  6.6.0-28.0.0.34  Tue Nov 17 09:10   still running
shutdown system down  6.6.0-28.0.0.34  Tue Nov 17 09:09 - 09:10  (00:01)

Broadcast message from root@openEuler (pts/0) (Tue Nov 17 09:20:00 2026):
The system is going down for maintenance NOW! (Warning only - shutdown cancelled)
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**On openEuler, command packages and their documentation packages are separated to streamline the OS. Which package must be additionally installed to enable the `man` command to access detailed help documentation for core utilities?**

- A. man-pages-gui
- B. coreutils-help
- C. bash-doc
- D. info-db

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.03 (p.66), on openEuler, to enable the man command to access detailed help documentation, you must additionally install the `coreutils-help` package.
</details>

### Question 2 [Single-Choice]
**In the Linux `man` manual classification (Sections 1 to 9), what do Sections 1, 5, and 8 represent respectively?**

- A. 1: Kernel routines; 5: Games; 8: C library functions
- B. 1: User shell commands/programs; 5: File formats and conventions; 8: System management commands (root only)
- C. 1: System calls; 5: Device files in /dev; 8: Miscellaneous macros
- D. 1: File formats; 5: User commands; 8: Games

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.03 (p.65), Section 1 covers commands/programs operated by users in the shell; Section 5 covers file formats and conventions; Section 8 covers system management commands (applicable only to the root user).
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about `shutdown`, `halt`, and `/var/log/wtmp` are TRUE?**

- A. `shutdown -h` powers off the server after it is shut down, while `shutdown -r` restarts the server.
- B. `shutdown -k` sends a warning signal to each user without actually shutting down the computer.
- C. `/var/log/wtmp` is a binary file that records user login times and durations, queried via the `last` command.
- D. `halt -w` immediately cuts power to the motherboard without writing to `/var/log/wtmp`.

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Ch.03 (pp.73–77), A, B, and C are true. Option D is false because `halt -w` only writes a record to `/var/log/wtmp` without restarting or shutting down the system.
</details>
