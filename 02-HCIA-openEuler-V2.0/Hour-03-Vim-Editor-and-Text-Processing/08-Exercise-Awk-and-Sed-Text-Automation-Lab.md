# Hands-On Lab: Pipeline Slicing with `awk` and In-Place Editing with `sed -i`

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 03 — Vim Editor & Text Processing Utilities (Sprint 4 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `07-Lecture-Stream-Processing-with-awk-and-sed`  
**Interactive Workbench:** Open **[`08-Exercise-Awk-and-Sed-Text-Automation-Lab.html`](./08-Exercise-Awk-and-Sed-Text-Automation-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You are automating log and configuration maintenance on openEuler. Use `last` piped to `awk` to extract the usernames of the last 5 logins, use `sed -n` to print only lines 1 to 3 of `/etc/passwd`, and use `sed -i` to directly replace `enabled=0` with `enabled=1` in `local.repo`.

### Step-by-Step Instructions
1. Step 1: Display the first column (account names) of the last 5 login records using `last -n 5 | awk '{print $1}'`.
2. Step 2: Quietly print only lines 1 to 3 of `/etc/passwd` by canceling default output with `sed -n '1,3p' /etc/passwd`.
3. Step 3: Directly edit `local.repo` in place to replace `enabled=0` with `enabled=1` using `sed -i 's/enabled=0/enabled=1/g' local.repo`.

### Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Display the last 5 login account names using last and awk
<last_awk_command>

# Step 2: Print only lines 1 to 3 of /etc/passwd using sed
<sed_print_command>

# Step 3: Directly modify local.repo in place using sed -i
<sed_inplace_command>
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `last -n 5 | awk '{print $1}'` (exact example from Ch.03 p.144).
- Use `sed -n '1,3p' /etc/passwd` so `-n` cancels default output.
- Use `sed -i 's/enabled=0/enabled=1/g' local.repo` to edit the file in place.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Display the last 5 login account names using last and awk
last -n 5 | awk '{print $1}'

# Step 2: Print only lines 1 to 3 of /etc/passwd using sed
sed -n '1,3p' /etc/passwd

# Step 3: Directly modify local.repo in place using sed -i
sed -i 's/enabled=0/enabled=1/g' local.repo
```

#### Expected Console / Query Output:
```text
root
openeuler
reboot
root
root

root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin

[root@openEuler ~]# grep enabled local.repo
enabled=1
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**By default, what separator does `awk` use to slice each input line into fields, and which variable represents the entire current line?**

- A. Colon (:); `$1`
- B. Spaces (whitespace); `$0`
- C. Comma (,); `$ALL`
- D. Semicolon (;); `$#`

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.03 (p.144), `awk` reads files or standard input by line, uses spaces as the default separator to slice each line, and uses `0` to represent the entire line (`awk '{print 0}' test.txt`).
</details>

### Question 2 [Single-Choice]
**When using the `sed` command, which option must be specified to directly modify the original file on disk instead of only editing the copied text in the memory buffer?**

- A. -n
- B. -e
- C. -i
- D. -r

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `C`
- **Explanation:** Per Ch.03 (p.150), `sed` only changes the copied text stored in buffers by default. To edit the original file directly, use the `-i` option.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following accurately describe `sed` command options in openEuler?**

- A. `-n` cancels the default output.
- B. `-e` specifies multipoint editing so multiple subcommands can be executed.
- C. `-f` reads editing commands from a script file.
- D. `-r` uses extended regular expressions in a script.

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.03 (p.150), `-n`, `-e`, `-f`, `-i`, `-l`, and `-r` are the six core options of `sed`.
</details>
