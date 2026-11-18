# 💻 Hands-On Lab: Resolving Symlink Paths (`pwd -P`) and Time-Sorted Directory Listings

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 02 — openEuler CLI Basics & File Operations (Sprint 2 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `03-Lecture-Linux-Directory-Structure-and-Navigation`  
**Interactive Workbench:** Open **[`04-Exercise-FHS-and-Directory-Navigation-Lab.html`](./04-Exercise-FHS-and-Directory-Navigation-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
You are auditing `/var/run` (which is a symbolic link to `/run`) and `/usr/local`. Navigate into `/var/run`, print both its logical and physical paths, list all files (including hidden files, human-readable sizes, sorted by time) in `/usr/local`, and inspect the `/etc` directory entry itself without listing its contents.

### 📋 Step-by-Step Instructions
1. Step 1: Change directory to `/var/run` using `cd /var/run` and display the physical path (resolving symlinks) using `pwd -P`.
2. Step 2: List all files (including hidden files) in `/usr/local` in human-readable long format sorted by time using `ls -ahlt /usr/local`.
3. Step 3: Display the attributes of the `/etc` directory itself (not its contents) using `ls -ld /etc`.

### 📝 Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Enter /var/run and print the physical path without symlinks
cd /var/run
<pwd_physical_command>

# Step 2: List all files in /usr/local with human-readable sizes sorted by time
<ls_usr_local_command>

# Step 3: Display the directory entry of /etc itself
<ls_etc_dir_itself_command>
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Use `pwd -P` to print the physical working directory without symbolic links.
- Combine `-a`, `-h`, `-l`, and `-t` in `ls -ahlt /usr/local`.
- Use `ls -ld /etc` so `-d` shows the directory entry itself.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Enter /var/run and print the physical path without symlinks
cd /var/run
pwd -P

# Step 2: List all files in /usr/local with human-readable sizes sorted by time
ls -ahlt /usr/local

# Step 3: Display the directory entry of /etc itself
ls -ld /etc
```

#### Expected Console / Query Output:
```text
/run

total 48K
drwxr-xr-x. 12 root root 4.0K Jul 28 14:00 ..
drwxr-xr-x. 12 root root 4.0K Jul 28 14:00 .
drwxr-xr-x.  5 root root 4.0K Jul 28 14:00 share
drwxr-xr-x.  2 root root 4.0K Mar 24 05:34 bin
drwxr-xr-x.  2 root root 4.0K Mar 24 05:34 etc
drwxr-xr-x.  2 root root 4.0K Mar 24 05:34 lib64
drwxr-xr-x.  2 root root 4.0K Mar 24 05:34 sbin

drwxr-xr-x. 102 root root 8192 Nov 17 09:00 /etc
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**Which directory in the Linux file system hierarchy is a virtual directory that serves as a mapping of system memory (RAM)?**

- A. /opt
- B. /proc
- C. /var
- D. /boot

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.03 (p.80), `/proc` is a virtual directory which is the mapping of the system memory. You can obtain system information by directly accessing this directory.
</details>

### Question 2 [Single-Choice]
**If `/tmp/link3` is a chain of symbolic links pointing to the physical directory `/tmp/d1`, and you run `cd /tmp/link3`, what is the output of `pwd -P`?**

- A. /tmp/link3
- B. /tmp/d1
- C. /tmp
- D. An error message

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.03 (p.83), `pwd -L` (default) outputs the symbolic link connection path (`/tmp/link3`), whereas `pwd -P` resolves all symlinks and outputs the physical path (`/tmp/d1`).
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about the `ls` and `cd` commands are TRUE?**

- A. `ls -A` displays hidden files and directories, excluding `.` and `..`.
- B. `ls -ld /etc` displays the directory attributes of `/etc` itself rather than the files inside `/etc`.
- C. `cd -` switches the working directory to the previous directory.
- D. `ls -t` sorts files alphabetically by file extension.

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Ch.03 (pp.84–86), A, B, and C are correct. Option D is false because `ls -t` sorts by creation/modification time (`ls -X` sorts by extension).
</details>
