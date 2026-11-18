# 📖 Advanced Stream Processing with `awk` and `sed`

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 03 — Vim Editor & Text Processing Utilities (Sprint 4 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `08-Exercise-Awk-and-Sed-Text-Automation-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.03, pp. 144, 150

---

## 🎯 Learning Objectives
- Analyze and slice text streams line-by-line using `awk` (`$0`, `$1..$n`, default space separator, `-F` custom field delimiter)
- Understand how `sed` (stream editor) processes lines in a pattern buffer without altering the original file by default
- Apply `sed` options (`-n`, `-e`, `-f`, `-i`, `-l`, `-r`) for non-interactive string replacement and in-place file editing

---

### 1. Column & Pattern Analysis with `awk`
**`awk`** is a powerful text analysis utility that reads files or standard input **line by line**, slices each line into fields using **spaces (whitespace) as the default separator**, and executes actions on each slice.
* **Syntax:** `awk [options] 'action' filename`
* **Positional Field Variables:**
  * **`$0`**: Represents the **entire current line** (e.g., `awk '{print $0}' test.txt`).
  * **`$1`, `$2`, `$3`...**: Represent the 1st, 2nd, 3rd field of the current line.
* **Custom Field Separator (`-F`):**
  * Use `-F` to specify a delimiter other than whitespace, such as `:` for `/etc/passwd`:
    ```bash
    awk -F: '{print $1, $3}' /etc/passwd
    ```
* **Pipeline Example from Official Material (Ch.03, p.144):**
  ```bash
  # Display the last five accounts that have logged in to the system:
  [root@openEuler ~]# last -n 5 | awk '{print $1}'
  ```

---

### 2. Non-Interactive Stream Editing with `sed`
**`sed`** is a streamlined, **non-interactive** stream editor capable of modifying character strings across standard input or files (unlike `tr`, which only performs character-level mapping).
* **Buffer Execution Principle:**
  * When `sed` runs, it reads one line at a time from the input into a **temporary memory buffer (pattern space)**, applies the editing commands to the buffer copy, prints the buffer to `stdout`, and moves to the next line.
  * **Crucial Rule:** By default, **`sed` only modifies the copied text in the buffer and leaves the original file untouched!** To modify the original file directly on disk, you **must pass `-i`**.

---

### 3. Key `sed` Options & Actions
| Option / Action | Description & Usage |
| :--- | :--- |
| **`-n`** | **Cancels default output** (only prints lines explicitly marked with the `p` action, e.g., `sed -n '1,5p' file`). |
| **`-e <script>`** | Specifies **multipoint editing**, allowing multiple `sed` subcommands in a single invocation. |
| **`-f <file>`** | Reads `sed` editing commands from a script file. |
| **`-i`** | **Directly edits the original file in place** (instead of only outputting modified buffer text to `stdout`). |
| **`-l <N>`** | Specifies the line-wrap length for the `l` command. |
| **`-r`** | Uses **extended regular expressions (ERE)** in the script. |
| **`s/old/new/g`** | Substitutes `old` with `new` globally on matched lines; **`d`** deletes matched lines; **`a`/`i`/`c`** appends/inserts/changes lines. |

---

## 🔑 Key Takeaways
- **awk reads input line by line using spaces as the default separator; $0 is the entire line, $1 is the first field, and -F changes the field separator.**
- **sed is a non-interactive stream editor that modifies text in a memory buffer by default without changing the source file on disk.**
- **In sed, -i edits the original file directly in place, -n suppresses default output, -e enables multipoint editing, and -r enables extended regular expressions.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Running 'sed "s/foo/bar/g" file.txt' does NOT modify file.txt on disk—it only prints the modified buffer to standard output! You must use 'sed -i' to edit the original file directly.

> [!WARNING]
> EXAM TRAP: Remember the difference between 'tr' and 'sed': 'tr' performs single-character translation/deletion from stdin, whereas 'sed' modifies character strings and lines.

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`08-Exercise-Awk-and-Sed-Text-Automation-Lab.html`](./08-Exercise-Awk-and-Sed-Text-Automation-Lab.html)** (or [`08-Exercise-Awk-and-Sed-Text-Automation-Lab.md`](./08-Exercise-Awk-and-Sed-Text-Automation-Lab.md)) to apply this concept in an interactive lab workbench!
