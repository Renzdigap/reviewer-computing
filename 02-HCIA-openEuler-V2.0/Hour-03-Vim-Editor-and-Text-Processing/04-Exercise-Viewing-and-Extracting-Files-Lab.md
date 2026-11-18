# 💻 Hands-On Lab: Numbering Non-Blank Lines (`cat -b`), `head` Offsets & `tail -f` Log Tracing

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 03 — Vim Editor & Text Processing Utilities (Sprint 2 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `03-Lecture-File-Viewing-cat-more-less-head-tail`  
**Interactive Workbench:** Open **[`04-Exercise-Viewing-and-Extracting-Files-Lab.html`](./04-Exercise-Viewing-and-Extracting-Files-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
You are inspecting system configuration and log files on openEuler. Number all non-blank lines of `/etc/profile`, extract the first 3 lines of `/etc/passwd`, extract `/etc/passwd` excluding the last 40 lines, and view the last 3 lines of `/etc/passwd`.

### 📋 Step-by-Step Instructions
1. Step 1: View `/etc/profile` and number only non-blank lines starting from 1 using `cat -b /etc/profile`.
2. Step 2: Display the first 3 lines of `/etc/passwd` using `head -n 3 /etc/passwd`, and display `/etc/passwd` excluding the last 40 lines using `head -n -40 /etc/passwd`.
3. Step 3: Display the last 3 lines of `/etc/passwd` using `tail -n 3 /etc/passwd`.

### 📝 Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Display /etc/profile with non-blank line numbers
<cat_nonblank_command>

# Step 2: Display first 3 lines of /etc/passwd, then all except last 40 lines
<head_first_3_command>
<head_exclude_last_40_command>

# Step 3: Display last 3 lines of /etc/passwd
<tail_last_3_command>
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Use `cat -b /etc/profile` to number only non-blank lines.
- Use `head -n 3 /etc/passwd` and `head -n -40 /etc/passwd`.
- Use `tail -n 3 /etc/passwd`.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Display /etc/profile with non-blank line numbers
cat -b /etc/profile

# Step 2: Display first 3 lines of /etc/passwd, then all except last 40 lines
head -n 3 /etc/passwd
head -n -40 /etc/passwd

# Step 3: Display last 3 lines of /etc/passwd
tail -n 3 /etc/passwd
```

#### Expected Console / Query Output:
```text
1	# /etc/profile
     2	# System wide environment and startup programs

root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin

tcpdump:x:72:72::/:/sbin/nologin
dbus:x:978:978:System Message Bus:/:/usr/sbin/nologin
openeuler:x:1000:1000:openEuler:/home/openeuler:/bin/bash
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**[Official Ch.03 Quiz Q1] How many lines of a file are displayed by default when using the `head` command?**

- A. 5
- B. 10
- C. 15
- D. 20

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Official Ch.03 Quiz Q1 (p.151): B (10). By default, both `head` and `tail` display 10 lines of a file.
</details>

### Question 2 [Single-Choice]
**Which command reads data from the 3rd line to the end of `file`, and which command reads all lines of `file` EXCEPT the last 3 lines?**

- A. `tail -n +3 file` and `head -n -3 file`
- B. `head -n +3 file` and `tail -n -3 file`
- C. `tail -f 3 file` and `head -c 3 file`
- D. `more +3 file` and `less -3 file`

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** Per Ch.03 (p.97 & p.101), `tail -n +3 file` reads data from the 3rd line to the end of the file, while `head -n -3 file` reads all lines except the last three.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about `cat`, `more`, `less`, and `tail` are TRUE?**

- A. `cat -b` numbers only non-empty lines starting from 1, whereas `cat -n` numbers all lines.
- B. `cat -E` adds a `$` symbol at the end of each output line.
- C. Unlike `more` (which loads the entire file from the start), `less` can scroll both upwards and downwards and does not load the entire file before displaying.
- D. `tail -f` reads log files cyclically for real-time log monitoring.

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.03 (pp.101–104, 135–142), all four statements are accurate.
</details>
