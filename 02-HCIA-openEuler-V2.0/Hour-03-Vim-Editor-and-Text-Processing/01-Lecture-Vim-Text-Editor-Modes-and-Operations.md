# Vim Text Editor Modes, Navigation, Editing & Search/Replace

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 03 — Vim Editor & Text Processing Utilities (Sprint 1 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `02-Exercise-Vim-Navigation-Search-and-Replace-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.03, pp. 118–133

---

## Learning Objectives
- Distinguish Vi vs. Vim (Bram Moolenaar, 1991) and navigate its basic modes (Normal, Insert, Visual, Select, Command-line, Ex) and derivative modes
- Execute Vim CLI launch options (`-c`, `-R`, `-M`, `-r`, `+num`, `-`, `-t`, `-q`) and Normal-mode cursor/data commands (`gg`, `G`, `yy`, `dd`, `p`, `u`, `U`, `Ctrl+R`)
- Perform Command-line mode operations: line numbering (`:set nu`/`nonu`), search highlighting (`:set hlsearch`), regex substitution (`:%s/old/new/gi`), and saving/exiting (`:wq`, `:q!`)

---

### 1. Vi vs. Vim and Editor Modes
* **Vi & Vim Evolution:** **Vi** is the universal standard Unix text editor with three basic modes (Command, Insert, Visual). **Vim** was released in **1991 by Bram Moolenaar** (initially *Vi IMitation*, later renamed **Vi IMproved**). Note: After a minimal openEuler installation, you may need to manually install `vim`.
* **Vim Modes:**
  * **6 Basic Modes:** **Normal** (default startup mode for cursor movement and operator commands), **Insert** (entered via `i` or `a`; press `ESC` to return to Normal mode), **Visual** (highlights characters/lines/blocks for operators), **Select** (Windows-like selection where typing replaces highlighted text and enters Insert mode), **Command-line** (`:`, `/`, `?`, `!`), and **Ex** (batch command mode; exit with `:visual`).
  * **5 Derivative Modes:** **Operator-pending** (waiting for text object like `aw` word, `as` sentence, `ap` paragraph), **Insert Normal** (`Ctrl+O` in Insert mode executes one Normal command then returns to Insert), **Insert Visual**, **Insert Select**, and **Replace** (press **`R`** in Normal mode to overwrite characters).
  * **Other:** **eVim** (`evim` or `vim -y` — modeless GUI mode staying in Insert mode).

---

### 2. Vim CLI Launch Options & Normal Mode Keybindings
* **CLI Syntax & Options (`vim [options] [file]...`):**
  * **`+num`**: Opens file with cursor at line `num`.
  * **`-R` vs. `-M`**: **`-R`** opens in read-only mode (can still force save with `:w!`); **`-M`** opens in strict read-only mode (**does not allow forcible saving**).
  * **`-r`**: Recovers a crashed session (swap file).
  * **`-c <cmd>`**: Runs specified command before opening file; **`-`** reads from `stdin`; **`-t tag`** jumps to tag definition; **`-q [errorfile]`** jumps to first error.

| Category | Normal / Command-Line Mode Keybindings |
| :--- | :--- |
| **Cursor Movement** | `k` (up), `j` (down), `h` (left), `l` (right); **`0`** (beginning of line); **`g0`** (leftmost character on screen); **`gg`** (first line of file); **`G`** (last line of file); **`:n`** (jump to line `n`). |
| **Copy, Cut & Paste** | **`yy` or `Y`** (copy entire line); **`y[n]w`** (copy `n` words); **`[n]dd`** (delete/cut `n` lines; `2dd` equals `dj`); **`d[n]w`** (delete `n` words); **`p`** (paste below line / after cursor); **`P`** (paste above line / before cursor). |
| **Undo & Redo** | **`u`** (undo latest change); **`U`** (undo **all changes on the current line** since cursor arrived on it); **`Ctrl+R`** (redo last undo). |

---

### 3. Line Numbers, Search/Replace & Saving/Exiting
* **Line Numbers & Search Highlighting:**
  * **`:set nu`** (display line numbers) / **`:set nonu`** (hide line numbers).
  * **`:set hlsearch`** (temporarily highlight search matches; add `set hlsearch` to **`/etc/vimrc`** for permanent configuration).
* **Find & Replace:**
  * **`/word`** (search forwards) and **`?word`** (search backwards). Press **`n`** for next match, **`N`** for previous match.
  * **`:1,5s/word1/word2/g`**: Replaces all `word1` with `word2` in lines 1 to 5 (without `g`, only the first match per line is replaced).
  * **`:%s/word1/word2/gi`**: Replaces all occurrences across the entire file (`%`), case-insensitively (`i`).
* **Saving & Exiting:** **`:w`** (save), **`:q`** (quit), **`:wq`** (save and quit), **`:q!`** (force quit without saving), **`:wq!`** (force save and quit).

---

## Key Takeaways
- **Vim starts in Normal mode by default; press 'i' or 'a' to enter Insert mode, 'R' for Replace mode, 'Ctrl+O' in Insert mode for one-shot Insert Normal mode, and 'ESC' to return to Normal mode.**
- **In Normal mode: 'gg' = first line, 'G' = last line, 'yy' = copy line, '[n]dd' = delete n lines, 'u' = undo last change, 'U' = undo all changes on current line, 'Ctrl+R' = redo.**
- **In Command-line mode: ':set nu' shows line numbers, ':set hlsearch' highlights matches (persisted in /etc/vimrc), and ':%s/old/new/gi' replaces globally and case-insensitively.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Distinguishing 'vim -R' vs. 'vim -M': '-R' opens a file in read-only mode but allows forcible saving (:wq!), whereas '-M' opens in read-only mode and DOES NOT allow forcible saving!

> [!WARNING]
> EXAM TRAP: In Vim, lowercase 'u' undoes the single latest change, whereas uppercase 'U' undoes ALL changes made on the current line, and 'Ctrl+R' redoes an undone change.

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`02-Exercise-Vim-Navigation-Search-and-Replace-Lab.html`](./02-Exercise-Vim-Navigation-Search-and-Replace-Lab.html)** (or [`02-Exercise-Vim-Navigation-Search-and-Replace-Lab.md`](./02-Exercise-Vim-Navigation-Search-and-Replace-Lab.md)) to apply this concept in an interactive lab workbench!
