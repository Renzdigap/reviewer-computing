# 📖 Logging In, CLI vs. GUI Desktops, Virtual Consoles & Bash Shortcuts

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 01 — OS for the AI Era & Getting Started with openEuler (Sprint 4 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `08-Exercise-Session-Switching-and-Bash-Shortcuts-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.02, pp. 47–52 & Ch.03, p. 62

---

## 🎯 Learning Objectives
- Compare CLI vs. GUI and identify the 5 optional desktop environments supported on openEuler (GNOME, UKUI, DDE, Kiran, XFCE)
- Perform local virtual console switching (Ctrl+Alt+F1..F6 / Alt+F1..F6) and remote SSH login (PuTTY, Xshell)
- Master shell prompts (# vs. $), user switching (su - username, id), and Bash keyboard shortcuts (Tab, history, Ctrl+A/E/C/L)

---

### 1. CLI vs. GUI and Optional Desktop Environments on openEuler
* **CLI (Command Line Interface):** Text-based UI driven by keyboard commands, options, and arguments; low resource overhead, scriptable, and the **default interface** after openEuler installation.
* **GUI (Graphical User Interface):** Visual UI driven by mouse interactions (buttons, menus, dialogs) for ease of use. While openEuler installs in CLI mode by default, users can optionally install **five desktop environments**:
  1. **GNOME:** Official desktop of the GNU Project; comprehensive and user-friendly.
  2. **UKUI:** Lightweight, agile Linux desktop developed by the **Kylin Software** team based on GTK and QT with minimal component dependencies.
  3. **DDE (Deepin Desktop Environment):** Powerful desktop environment developed by the **UnionTech Software** team.
  4. **Kiran:** Secure, stable, efficient desktop developed by the **Hunan Kylin Information Security** team; supports both **x86 and AArch64**.
  5. **XFCE:** Lightweight Linux desktop updated from GTK2 to GTK3 and GDBus with Object Introspection (GI).

---

### 2. Local Virtual Consoles, Remote Login & Shell Prompts
* **Local Login & Virtual Consoles:**
  * A typical Linux system provides **six virtual consoles (`tty1` to `tty6`)** and one graphical console.
  * Press **`Ctrl+Alt+F[1–6]`** (or **`Alt+F1` to `Alt+F6`** in text mode) to switch between the 6 independent virtual consoles. If a program deadlocks on one console, you can switch to another virtual console to kill it.
* **Remote Login:** Enabled by default via SSH using terminal clients like **PuTTY** or **Xshell**.
* **Shell & System Prompt:**
  * A **Shell** (compiled in C) acts as the bridge between the user and the Linux kernel. Common shells include **`bash`** (default on openEuler), `sh`, `csh`, and `ksh`.
  * Prompt format: `[Current login user@Host name Current location]#/$`
  * **`#` (Hash/Pound):** Indicates the **root** superuser (`[root@openEuler ~]#`).
  * **`$` (Dollar sign):** Indicates a **common (regular) user** (`[user@openEuler ~]$`).
  * Use **`su - username`** to switch users, and **`id`** to check the current user's UID/GID.

---

### 3. Essential Bash Shell Keyboard Shortcuts
| Shortcut / Command | Function in Bash Shell |
| :--- | :--- |
| **`Tab`** | **Automatically supplements (auto-completes) commands, parameters, or file names** (Ch.02 Quiz Q2!). Press **`Tab` twice** on an empty line to list all available commands. |
| **`↑` and `↓`** | Quickly browse previously executed historical commands. |
| **`history` / `!n`** | `history` lists recorded commands; `history n` (or `!n`) executes historical command `n`. |
| **`Home` or `Ctrl+A`** | Moves the cursor to the **beginning** of the current line. |
| **`End` or `Ctrl+E`** | Moves the cursor to the **end** of the current line. |
| **`Ctrl+C`** | Immediately **stops/terminates** the currently running foreground program. |
| **`clear` or `Ctrl+L`** | Quickly **clears the terminal screen**. |

---

## 🔑 Key Takeaways
- **openEuler uses the CLI and the bash shell by default; if a GUI is needed, GNOME, UKUI, DDE, Kiran, or XFCE can be installed.**
- **The root user prompt ends with '#', whereas a common user prompt ends with '$'. Switch users with 'su - username' and verify identity with 'id'.**
- **Pressing 'Tab' quickly auto-completes commands and parameters (Ch.02 Quiz Q2); Ctrl+A jumps to the start of the line, Ctrl+E jumps to the end, Ctrl+C aborts the current program, and Ctrl+L (or clear) clears the screen.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.02 Quiz Q2): 'Tab' is used to quickly supplement commands and parameters—do NOT confuse it with Ctrl+L (clear screen) or Up/Down arrows (command history).

> [!WARNING]
> EXAM TRAP: Note the slight typo on Slide 26 of Ch.02 ('Generally, the last prompt of the root user and common users is #') vs. Slide 28 of Ch.02 ('the command prompt of the root user generally ends with #, while that of a common user generally ends with $'). Slide 28 is the standard Unix/Linux rule tested on exams!

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`08-Exercise-Session-Switching-and-Bash-Shortcuts-Lab.html`](./08-Exercise-Session-Switching-and-Bash-Shortcuts-Lab.html)** (or [`08-Exercise-Session-Switching-and-Bash-Shortcuts-Lab.md`](./08-Exercise-Session-Switching-and-Bash-Shortcuts-Lab.md)) to apply this concept in an interactive lab workbench!
