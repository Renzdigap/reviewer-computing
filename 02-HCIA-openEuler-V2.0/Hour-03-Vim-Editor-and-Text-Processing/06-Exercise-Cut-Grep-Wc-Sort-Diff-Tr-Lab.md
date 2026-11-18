# 💻 Hands-On Lab: Extracting Usernames (`cut`), Counting Accounts (`wc`), Sorting & `tr` Case Conversion

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 03 — Vim Editor & Text Processing Utilities (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `05-Lecture-Text-Extraction-Filtering-Stats-and-Sorting`  
**Interactive Workbench:** Open **[`06-Exercise-Cut-Grep-Wc-Sort-Diff-Tr-Lab.html`](./06-Exercise-Cut-Grep-Wc-Sort-Diff-Tr-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
You are auditing user accounts in `/etc/passwd`. Extract the first column (usernames) delimited by `:`, count how many lines in `/etc/passwd` match `nologin` using `grep -c`, count total lines in `/etc/passwd` using `wc -l`, and convert lowercase letters in `text.txt` to uppercase using `tr`.

### 📋 Step-by-Step Instructions
1. Step 1: Display the first column of `/etc/passwd` separated by colons (`:`) using `cut -d: -f1 /etc/passwd`.
2. Step 2: Count matching `nologin` lines with `grep -c nologin /etc/passwd` and count total lines with `wc -l /etc/passwd`.
3. Step 3: Pipe `cat text.txt` into `tr a-z A-Z` to convert lowercase letters to uppercase.

### 📝 Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Extract the 1st colon-separated column of /etc/passwd
<cut_command>

# Step 2: Count lines matching 'nologin' and total lines in /etc/passwd
<grep_count_command>
<wc_lines_command>

# Step 3: Convert lowercase to uppercase in text.txt using tr
<tr_command>
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Use `cut -d: -f1 /etc/passwd`.
- Use `grep -c nologin /etc/passwd` and `wc -l /etc/passwd`.
- Use `cat text.txt | tr a-z A-Z`.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Extract the 1st colon-separated column of /etc/passwd
cut -d: -f1 /etc/passwd

# Step 2: Count lines matching 'nologin' and total lines in /etc/passwd
grep -c nologin /etc/passwd
wc -l /etc/passwd

# Step 3: Convert lowercase to uppercase in text.txt using tr
cat text.txt | tr a-z A-Z
```

#### Expected Console / Query Output:
```text
root
bin
daemon
adm
openeuler

28
32 /etc/passwd

HELLO OPENEULER V2.0
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**What is the default field separator of the `cut` command if the `-d` option is not specified?**

- A. Colon (:)
- B. Comma (,)
- C. TAB
- D. Semicolon (;)

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `C`
- **Explanation:** Per Ch.03 (p.143), `-d` specifies a field separator, and the default field separator of `cut` is TAB.
</details>

### Question 2 [Single-Choice]
**Which option of the `sort` command sorts numbers by their numeric value, and which option removes duplicate lines?**

- A. `-n` and `-u`
- B. `-d` and `-r`
- C. `-f` and `-c`
- D. `-b` and `-o`

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** Per Ch.03 (p.147), `sort -n` sorts by numeric value and `sort -u` ignores repeated (duplicate) lines.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about `grep`, `wc`, and `tr` are TRUE?**

- A. `grep -w` prints whole word matches, while `grep -x` prints only results matching the whole line.
- B. `wc -l` displays only the number of lines, and `wc -w` displays only the number of words.
- C. `tr -d` deletes specified characters from standard input.
- D. `tr -s` reduces consecutive repeated characters to a single character.

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.03 (pp.145–149), all four options match the official Huawei HCIA-openEuler V2.0 documentation.
</details>
