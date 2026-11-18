# Hands-On Lab: Nested Directory Creation, Archive Copy, Rename & Cleanup

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 02 — openEuler CLI Basics & File Operations (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `05-Lecture-File-and-Directory-Creation-Copy-Move-Delete`  
**Interactive Workbench:** Open **[`06-Exercise-File-Lifecycle-Operations-Lab.html`](./06-Exercise-File-Lifecycle-Operations-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You are preparing a backup workspace in `/root`. Create a nested directory `/root/backup/logs`, create two log files (`test01.log` and `test02.log`), recursively copy `/var/log/audit` while preserving attributes into `/root/backup/`, rename `test02.log` to `test03.log`, and forcibly remove `test01.log`.

### Step-by-Step Instructions
1. Step 1: Create the nested directory `/root/backup/logs` using `mkdir -p /root/backup/logs` and create empty files `test01.log` and `test02.log` using `touch test01.log test02.log`.
2. Step 2: Copy `/var/log/audit` recursively into `/root/backup/` using `cp -r /var/log/audit /root/backup/` (or `cp -a`).
3. Step 3: Rename `test02.log` to `test03.log` using `mv test02.log test03.log`, and forcibly delete `test01.log` using `rm -f test01.log`.

### Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Create nested directory and empty log files
<mkdir_command>
<touch_command>

# Step 2: Recursively copy /var/log/audit to /root/backup/
<cp_command>

# Step 3: Rename test02.log to test03.log and forcibly remove test01.log
<mv_command>
<rm_command>
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `mkdir -p /root/backup/logs` and `touch test01.log test02.log`.
- Use `cp -r /var/log/audit /root/backup/` to copy the directory recursively.
- Use `mv test02.log test03.log` and `rm -f test01.log`.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Create nested directory and empty log files
mkdir -p /root/backup/logs
touch test01.log test02.log

# Step 2: Recursively copy /var/log/audit to /root/backup/
cp -r /var/log/audit /root/backup/

# Step 3: Rename test02.log to test03.log and forcibly remove test01.log
mv test02.log test03.log
rm -f test01.log
```

#### Expected Console / Query Output:
```text
[root@openEuler ~]# ls -la /root/backup/
total 12
drwxr-xr-x. 4 root root 4096 Nov 17 09:30 .
dr-xr-x---. 6 root root 4096 Nov 17 09:30 ..
drwx------. 2 root root 4096 Nov 17 09:30 audit
drwxr-xr-x. 2 root root 4096 Nov 17 09:30 logs
[root@openEuler ~]# ls -l test*
-rw-r--r--. 1 root root 0 Nov 17 09:30 test03.log
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**Which option of the `mkdir` command enables automatic creation of non-existent parent directories without reporting an error if the directory already exists?**

- A. -r
- B. -p
- C. -f
- D. -a

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.03 (p.88), the `-p` option enables `mkdir` to report no error if a directory already exists and automatically creates any parent directories that do not exist.
</details>

### Question 2 [Single-Choice]
**When running `mv` or `rm` in the Bash shell, if both `-i` (interactive) and `-f` (force) options are provided on the command line (e.g., `rm -i -f file1`), which option takes effect?**

- A. Always `-i`
- B. Always `-f`
- C. The option on the right (the last option specified)
- D. The command fails with a syntax error

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `C`
- **Explanation:** Per Ch.03 (pp.92, 94), if both `-i` and `-f` are provided on `mv` or `rm`, the option on the right takes effect.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about the `touch` and `cp` commands are TRUE?**

- A. `touch -a file` changes only the file access time.
- B. `touch -m file` changes the file content modification time.
- C. `cp -a` copies directories while retaining links, file attributes, and special device/pipe files.
- D. `cp -s /etc/passwd passwd_link` creates a symbolic (soft) link to `/etc/passwd`.

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.03 (pp.89–91), all four statements are explicitly documented in the official training material.
</details>
