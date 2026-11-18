# Hands-On Lab: Vim Command-Line Configuration, Global Substitution & Crash Recovery

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 03 — Vim Editor & Text Processing Utilities (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `01-Lecture-Vim-Text-Editor-Modes-and-Operations`  
**Interactive Workbench:** Open **[`02-Exercise-Vim-Navigation-Search-and-Replace-Lab.html`](./02-Exercise-Vim-Navigation-Search-and-Replace-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You are configuring `/etc/vimrc` and automating a Vim batch script for server configuration files. Specify the exact Vim commands to display line numbers, enable search highlighting, replace all occurrences of `word1` with `word2` case-insensitively across the entire file, and forcibly save and exit.

### Step-by-Step Instructions
1. Step 1: Write the Vim command to display line numbers (`:set nu`) and highlight search results (`:set hlsearch`).
2. Step 2: Write the Vim substitution command to replace all occurrences of `word1` with `word2` across the entire file case-insensitively (`:%s/word1/word2/gi`).
3. Step 3: Write the Vim command to forcibly save and exit (`:wq!`).

### Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Enable line numbers and search highlighting in Vim
<vim_line_numbers>
<vim_highlight_search>

# Step 2: Global case-insensitive replacement of word1 with word2
<vim_global_replace>

# Step 3: Forcibly save and exit Vim
<vim_force_save_exit>
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `:set nu` to show line numbers and `:set hlsearch` to highlight search matches.
- Use `:%s/word1/word2/gi` for full-file (`%`), global (`g`), case-insensitive (`i`) replacement.
- Use `:wq!` to forcibly save and exit.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Enable line numbers and search highlighting in Vim
:set nu
:set hlsearch

# Step 2: Global case-insensitive replacement of word1 with word2
:%s/word1/word2/gi

# Step 3: Forcibly save and exit Vim
:wq!
```

#### Expected Console / Query Output:
```text
1 hello
  2 openEuler
  3 word2 (replaced from word1)
  4 WORD2 (replaced from WORD1 - case-insensitive)
"test.txt" 4L, 42B written
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**When starting Vim from the command line, which option opens a file in strict read-only mode and does NOT allow you to forcibly save the file?**

- A. vim -R
- B. vim -M
- C. vim -r
- D. vim -c

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.03 (p.124), `-R` opens a file in read-only mode but allows you to forcibly save the file, whereas `-M` opens a file in read-only mode and does NOT allow you to forcibly save the file.
</details>

### Question 2 [Single-Choice]
**In Vim Normal mode, which key combination redoes the last operation that was undone with `u`?**

- A. U
- B. Ctrl+R
- C. Ctrl+O
- D. yy

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.03 (p.132), `u` undoes the latest change, `U` undoes all changes on the current line, and `Ctrl+R` redoes the last undo operation.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about Vim search, replacement, and configuration are TRUE?**

- A. `:set nu` displays line numbers, while `:set nonu` hides line numbers.
- B. Adding `set hlsearch` to `/etc/vimrc` permanently enables search result highlighting.
- C. `:1,5s/word1/word2/g` replaces all occurrences of `word1` with `word2` in lines 1 to 5.
- D. Pressing `gg` moves the cursor to the last line of the file, while `G` moves it to the first line.

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Ch.03 (pp.126–130), A, B, and C are true. Option D is reversed: `gg` moves the cursor to the first line of the file, and `G` moves it to the last line.
</details>
