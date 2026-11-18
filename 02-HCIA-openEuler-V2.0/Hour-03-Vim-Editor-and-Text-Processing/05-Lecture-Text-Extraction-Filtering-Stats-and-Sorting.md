# Text Extraction, Filtering, Statistics & Sorting (`cut`, `grep`, `wc`, `sort`, `diff`, `tr`)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 03 — Vim Editor & Text Processing Utilities (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `06-Exercise-Cut-Grep-Wc-Sort-Diff-Tr-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.03, pp. 143–149

---

## Learning Objectives
- Slice columns and character ranges using `cut` (`-b`, `-c`, `-d`, `-f` with ranges `N-`, `N-M`, `-M`)
- Filter lines with `grep` (`-c`, `-i`, `-w`, `-x`) and compute line/word/byte counts with `wc` (`-l`, `-w`, `-c`)
- Sort, deduplicate, compare, and translate text streams using `sort` (`-n`, `-r`, `-u`, `-o`), `diff` (`-B`, `-c`, `-i`, `-r`, `-w`), and `tr` (`-c`, `-d`, `-s`, `-t`)

---

### 1. Column Extraction (`cut`) & Keyword Filtering (`grep`)
* **`cut [option]... [file]` (Extract columns/fields):**
  * **`-d <char>`:** Specifies the field separator (**default separator is `TAB`**). Example: `cut -d: -f1 /etc/passwd`.
  * **`-f [range]`:** Selects fields (multiple fields separated by commas `,`).
  * **`-b [range]` / `-c [range]`:** Selects bytes (`-b`) or characters (`-c`).
  * **Range Syntax:** **`N-`** (from `N`-th to end), **`N-M`** (from `N`-th to `M`-th inclusive), **`-M`** (from 1st to `M`-th inclusive).
* **`grep [option] pattern [file]...` (Regular expression line search):**
  * Enclose multi-word patterns in single or double quotes so words after the first aren't misinterpreted as filenames!
  * **`-c`:** Prints only the **count** of matching lines.
  * **`-i`:** Ignores case sensitivity.
  * **`-w`:** Matches **whole words** only.
  * **`-x`:** Matches only results spanning the **whole line**.

---

### 2. Text Statistics (`wc`) & Sorting (`sort`)
* **`wc [option]... [file]...` (Word/Line/Byte Count):**
  * Reads from `stdin` if no file or `-` is given.
  * **`-l` (`--lines`):** Displays only the number of **lines**.
  * **`-w` (`--words`):** Displays only the number of **words**.
  * **`-c` (`--bytes` / `--chars`):** Displays only the number of **bytes**.
* **`sort [option]... [file]...` (Line Sorting):**
  * **`-n`:** Sorts **numerically** by value (instead of ASCII character order).
  * **`-r`:** Sorts in **reverse** (descending) order.
  * **`-u`:** Ignores repeated lines (**unique**).
  * **`-o <file>`:** Saves sorted output directly to `<file>`.
  * **`-b`** (ignore leading spaces), **`-c`** (check if already sorted), **`-d`** (letters, digits, spaces only), **`-f`** (fold lowercase into uppercase).

---

### 3. File Comparison (`diff`) & Character Translation (`tr`)
* **`diff [option]... file1 file2` (Line-by-line Comparison):**
  * If directories are specified, `diff` compares files with the same name in those directories (non-recursively unless `-r` is passed).
  * **`-B`** (ignore blank lines), **`-c`** (context format marking differences), **`-i`** (ignore case), **`-r`** (compare subdirectories recursively), **`-w`** (ignore all whitespace).
* **`tr [option]... set1 [set2]` (Character Translation/Deletion from `stdin`):**
  * Reads **only from standard input (`stdin`)**, converts or deletes characters, and writes to `stdout` (e.g., `cat text.txt | tr a-z A-Z`).
  * **`-d`:** **Deletes** characters in `set1`.
  * **`-s`:** **Squeezes** consecutive repeated characters into a single character.
  * **`-c`:** Inverts (complements) `set1` (processes characters *not* in `set1`).
  * **`-t`:** Truncates `set1` to the length of `set2`.

---

## Key Takeaways
- **In 'cut', the default delimiter is TAB; use '-d:' and '-f1' to extract the first colon-separated column of /etc/passwd.**
- **grep -c counts matching lines, -i ignores case, -w matches whole words, and -x matches whole lines; wc -l, -w, -c count lines, words, and bytes.**
- **sort -n sorts numerically, -r reverses order, -u removes duplicate lines; tr reads from stdin (e.g., cat file | tr a-z A-Z) and uses -d to delete characters.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: The default field separator of 'cut' is TAB, whereas the default field separator of 'awk' is spaces/whitespace!

> [!WARNING]
> EXAM TRAP: 'tr' does NOT accept a filename as a command-line argument—it reads from standard input (stdin) via a pipe ('|') or input redirection ('<').

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-Cut-Grep-Wc-Sort-Diff-Tr-Lab.html`](./06-Exercise-Cut-Grep-Wc-Sort-Diff-Tr-Lab.html)** (or [`06-Exercise-Cut-Grep-Wc-Sort-Diff-Tr-Lab.md`](./06-Exercise-Cut-Grep-Wc-Sort-Diff-Tr-Lab.md)) to apply this concept in an interactive lab workbench!
