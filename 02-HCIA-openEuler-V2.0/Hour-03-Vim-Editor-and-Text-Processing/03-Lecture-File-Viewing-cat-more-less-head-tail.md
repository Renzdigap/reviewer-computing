# File Viewing & Extraction (`cat`, `more`, `less`, `head`, `tail`)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 03 — Vim Editor & Text Processing Utilities (Sprint 2 of 4)  
**Format:** Bite-Sized Lecture (7 mins) - Followed immediately by `04-Exercise-Viewing-and-Extracting-Files-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.03, pp. 96–104, 135–142, 151

---

## Learning Objectives
- View and concatenate files with `cat` (`-n`, `-b`, `-s`, `-E`, `-A`)
- Compare paginated viewers `more` (loads entire file upfront) vs. `less` (loads on demand, bidirectional scrolling & search)
- Extract file headers and tails using `head` (first 10 lines by default — Ch.03 Quiz!) and `tail` (last 10 lines by default, `-f` real-time log tracking)

---

### 1. Viewing & Combining Files with `cat`
`cat` reads entire files to standard output, creates files (`cat > filename`), or combines files (`cat file1 file2 > file3`):
* **`-n` (`--number`):** Numbers **all** output lines starting from 1.
* **`-b` (`--number-nonblank`):** Numbers **only non-empty (non-blank)** lines starting from 1.
* **`-s`:** Squeezes multiple consecutive blank lines into a single blank line.
* **`-E` (`--show-ends`):** Appends **`$`** at the end of each line.
* **`-A` (`--show-all`):** Equivalent to **`-vET`**; displays all non-printable characters (tabs, line endings).

---

### 2. Paginated Viewing: `more` vs. `less`
| Feature / Key | `more [options] <file>` | `less [option] file` |
| :--- | :--- | :--- |
| **Loading Mechanism** | Reads from front to back and **loads the entire file from the very start**. | **Does NOT load the entire file** before displaying; faster on huge logs and more flexible (Vim-like UI). |
| **CLI Options** | **`+n`** (start at line `n`), **`-n`** (set screen size to `n` lines), **`-c`** (clear screen from top), **`-s`** (squeeze blank lines), **`+/pattern`** (search pattern before displaying). | **`-N`** (show line numbers), **`-i`** (ignore case in search), **`-s`** (squeeze blank lines), **`-f`** (force open special/binary file), **`-o <file>`** (save output to file), **`-g`** (highlight only last match). |
| **Interactive Keys** | `Space` / `Ctrl+F` (next page), `Enter` (next line), `b` / `Ctrl+B` (previous page), **`=`** (print current line number), **`:f`** (print filename & line number), **`v`** (invoke `vi`), **`!cmd`** (run shell cmd), **`q`** (quit). | `/string` (search down), `?string` (search up), `n`/`N` (repeat search), `b`/`PageUp` (prev page), `d` (down half page), `u` (up half page), `y` (prev line), `h` (help), `q`/`Q` (quit). |

---

### 3. Extracting File Beginnings (`head`) and Ends (`tail`)
* **`head [option]... [file]...`:**
  * **Default Behavior (Official Ch.03 Quiz Q1!):** Displays the **first 10 lines** of a file by default!
  * **`-n num` / `-c num`:** Displays the first `num` lines / bytes (`head -n 3 /etc/passwd`).
  * **Negative Count (`head -n -num` / `head -c -num`):** Displays **all lines/bytes EXCEPT the last `num` lines/bytes** (e.g., `head -n -40 /etc/passwd` outputs everything except the last 40 lines!).
  * **`-q` / `-v`:** Hide (`-q`, default for single file) or display (`-v`) the filename header.
* **`tail [option]... [file]...`:**
  * **Default Behavior:** Displays the **last 10 lines** of a file by default.
  * **`-n num` / `-c num`:** Displays the last `num` lines / bytes (`tail -n 3 /etc/passwd`).
  * **Plus Offset (`tail -n +num` / `tail -c +num`):** Reads data **starting from the `num`-th line/byte to the end of the file** (`tail -n +3 file`).
  * **`-f`:** **Reads log files cyclically in real time** (traces growing log files like `tail -f ping.log`).

---

## Key Takeaways
- **By default, both 'head' and 'tail' display 10 lines (the first 10 lines and last 10 lines, respectively — Ch.03 Quiz Q1).**
- **head -n -3 file reads all lines EXCEPT the last 3 lines; tail -n +3 file reads from line 3 to the end of the file; tail -f cyclically follows real-time log updates.**
- **cat -n numbers all lines including blank lines, whereas cat -b numbers only non-blank lines; less does not load the entire file into memory upfront, unlike more.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Official Ch.03 Quiz Q1): 'How many lines of a file are displayed by default when using the head command?' -> 10 lines (Option B)!

> [!WARNING]
> EXAM TRAP: Watch the sign in head/tail! 'head -n -20 file' excludes the last 20 lines, whereas 'tail -n +3 file' starts outputting from line 3 to the end.

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`04-Exercise-Viewing-and-Extracting-Files-Lab.html`](./04-Exercise-Viewing-and-Extracting-Files-Lab.html)** (or [`04-Exercise-Viewing-and-Extracting-Files-Lab.md`](./04-Exercise-Viewing-and-Extracting-Files-Lab.md)) to apply this concept in an interactive lab workbench!
