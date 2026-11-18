# Process Management (`ps`, `top`, `nice`, `kill`) & Scheduled Tasks (`at`, `crontab`)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 05 — Software Packages, systemd Services, Processes & Scheduled Tasks (Sprint 4 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `08-Exercise-Top-Nice-Kill-At-and-Crontab-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.04, pp. 224–250

---

## Learning Objectives
- Explain the 5 Linux process memory segments, Copy-on-Write (`fork`/`exec`/`exit`/`wait`) lifecycle, and 5 kernel process states
- Monitor and control processes with `ps`, `top` (dynamically checks host resource usage — Ch.04 Quiz!), `nice`/`renice` (`PRI` vs. `NI`), `&`/`jobs`/`fg`/`bg`, and `kill`/`killall` signals
- Schedule one-time tasks with `at` (`atq`, `atrm`) and recurring periodic tasks with `crontab` (5-field syntax `min hour dom month dow`)

---

### 1. Process Memory, Lifecycle & States
* **5 Virtual Address Space Segments (Low to High Address):** **Code segment** (read-only executable code/constants) -> **Data segment** (initialized static/global variables) -> **BSS segment** (uninitialized static/global variables) -> **Heap** (dynamic memory) -> **Stack** (local variables).
* **Lifecycle & Copy-on-Write (COW):** Parent calls **`fork()`** (shares address space via COW) -> Child calls **`exec()`** (loads new program; kernel allocates new physical pages on write) -> Child calls **`exit()`** and becomes a **Zombie process** until the parent reaps it via **`wait()`**.
* **5 Process States (Ch.04, p.227):**
  * **`TASK_RUNNING` (`running/0`):** Running in user/kernel space or ready in the run queue.
  * **`TASK_INTERRUPTIBLE` (`interruptible/1`):** Sleeping; can be woken by resources, signals, or clock interrupts.
  * **`TASK_UNINTERRUPTIBLE` (`uninterruptible/2`):** Sleeping on hardware I/O; **cannot** be woken by signals.
  * **`TASK_ZOMBIE` (`zombie/3`):** Terminated, but process control block (PCB) is not yet released by parent `wait()`.
  * **`TASK_STOPPED` (`stopped/4`):** Stopped (e.g., by debugger or `SIGSTOP`/`SIGTSTP`).

---

### 2. Priority (`PRI`/`NI`), Monitoring (`ps`/`top`), Job Control & Signals
* **Priority (`PRI` vs. `NI`):** Internal kernel priority is **`0–139`** (`0–99` real-time, `100–139` non-real-time; **smaller value = higher priority**). **`NI` (nice value)** ranges from **`-20` (highest priority)** to **`19` (lowest priority)** (default `0`). Formula: **`PRI(new) = PRI(old) + nice`**. Only **`root`** can set a negative `nice` value!
  * Launch with nice: `nice -n -18 vi &`
  * Modify running process: `renice -n 12 -p 9700` (supports `-p` PID, `-g` group, `-u` user; or press `r` inside `top`).
* **Static vs. Dynamic Monitoring (Official Ch.04 Quiz Q1!):**
  * **`ps aux` / `ps -ef` / `ps -l`:** **Statically** lists process snapshot at a single point in time.
  * **`top`:** **Dynamically checks host resource usage and processes in real time** (Ch.04 Quiz Q1!).
* **Foreground/Background & Signals (`kill` / `killall`):**
  * **`&`** (run in background), **`Ctrl+Z`** (suspend foreground job to background), **`jobs`** (list background jobs), **`fg`** (bring to foreground), **`bg`** (resume in background).
  * **Key Signals:** **`1` (`HUP` - Hangup/reload)**, **`2` (`INT` - `Ctrl+C` interrupt)**, **`3` (`QUIT`)**, **`9` (`KILL` - unconditional termination)**, **`11` (`SEGV` - segment error)**, **`15` (`TERM` - default termination signal of `kill PID`)**, **`17` (`STOP`)**, **`18` (`TSTP` - `Ctrl+Z`)**, **`19` (`CONT` - continue)**. Note: `killall python*` supports wildcards by process name!

---

### 3. Scheduled Tasks: One-Time (`at`) vs. Periodic (`cron` / `crontab`)
* **One-Time Task (`at` — managed by `atd` daemon checking `/var/spool/at`):**
  * Controlled by `/etc/at.allow` and `/etc/at.deny`.
  * Interactive: `at 16:30` -> enter commands -> press **`Ctrl+D`** to submit; or script file: **`at -f example.sh 15:00`**.
  * Relative time examples: `at now+4 hours`, `at now+240 minutes`, `at 4:30pm`, `at teatime` (`16:00`).
  * Queue inspection & removal: **`atq`** (view job queue) and **`atrm <job_ID>`** (delete job).
* **Periodic Task (`cron` — wakes up every minute to read `/var/spool/cron/<user>` and `/etc/crontab`):**
  * Commands: **`crontab -e`** (edit), **`crontab -l`** (list), **`crontab -r`** (remove), **`crontab -u <user>`** (root only). **No need to restart `crond` after editing!**
  * **5 Time Fields:** `minute(0-59)  hour(0-23)  day-of-month(1-31)  month-of-year(1-12)  day-of-week(0-6, 0=Sunday)  command`
  * Special symbols: **`*`** (all values), **`/`** (step, e.g., `*/5`), **`-`** (range), **`,`** (discrete list). Example: `00 08 * * 1 commands` (every Monday at 08:00 AM). In `/etc/crontab`, **`run-parts`** executes all scripts inside a directory (`/etc/cron.hourly`, `/etc/cron.daily`, etc.).

---

## Key Takeaways
- **top dynamically checks host resource usage in real time (Ch.04 Quiz Q1), whereas ps lists a static snapshot.**
- **PRI(new) = PRI(old) + nice, where nice ranges from -20 (highest priority, root only) to 19 (lowest priority); kill sends signal 15 (TERM) by default, while signal 9 (KILL) forces unconditional termination.**
- **at schedules one-time tasks (atq lists, atrm deletes, Ctrl+D ends interactive input); crontab (-e/-l/-r/-u) schedules periodic tasks using 'minute hour day-of-month month-of-year day-of-week command'.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Official Ch.04 Quiz Q1): 'Which of the following commands can be used to dynamically check the host resource usage?' -> B. top (ps, free, and lscpu are static snapshots)!

> [!WARNING]
> EXAM TRAP: Do NOT restart the cron service after modifying a crontab file—the cron daemon wakes up every minute and automatically re-reads /etc/crontab and /var/spool/cron (Ch.04 p.247)!

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`08-Exercise-Top-Nice-Kill-At-and-Crontab-Lab.html`](./08-Exercise-Top-Nice-Kill-At-and-Crontab-Lab.html)** (or [`08-Exercise-Top-Nice-Kill-At-and-Crontab-Lab.md`](./08-Exercise-Top-Nice-Kill-At-and-Crontab-Lab.md)) to apply this concept in an interactive lab workbench!
