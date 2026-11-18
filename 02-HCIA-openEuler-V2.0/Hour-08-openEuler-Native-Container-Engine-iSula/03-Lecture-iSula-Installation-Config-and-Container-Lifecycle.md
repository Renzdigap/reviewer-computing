# iSula Installation, Configuration Priority & Container Lifecycle Operations

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 08 — openEuler Native Container Engine iSula (iSulad) (Sprint 2 of 4)  
**Format:** Bite-Sized Lecture (7 mins) - Followed immediately by `04-Exercise-iSula-Container-Lifecycle-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.07, pp. 399–417, 439

---

## Learning Objectives
- Install `iSulad` via `yum`/`rpm` and apply the configuration priority order (`CLI > /etc/isulad/daemon.json > default code configurations`)
- Identify the 4 official container states (`Created`, `Up`, `Paused`, `Exited` — Official Ch.07 Quiz Q1!)
- Execute `isula` container lifecycle commands: `create`, `start`, `run` (`-d`, `-it`, `-p`, `-e`, `--workdir`, `--name`, `--dns`, `--restart`, `--rm`), `pause`/`unpause`, `exec`, `ps`, `inspect`, `logs`, `restart`, and `rm`

---

### 1. Installing & Configuring `iSulad` (Configuration Priority Rule!)
* **Installation:**
  * Recommended (auto-resolves dependencies): **`yum install -y iSulad`** (installs iSula 2.0.11 by default on openEuler 22.03 LTS).
  * Offline RPM (must manually install all dependency RPMs): `rpm -ihv iSulad-xx.aarch64.rpm`.
* **Configuration Priority (Highest to Lowest — Ch.07, p.401):**
  $CLI (`isulad --xxx)` > Configuration file (`/etc/isulad/daemon.json)` > Default configurations in code$
  * **CLI Configuration:** e.g., **`isulad -l DEBUG`** (takes effect immediately without restarting; if managed by `systemd`, modifying `OPTIONS` in **`/etc/sysconfig/iSulad`** is equivalent to CLI configuration).
  * **Config File (`/etc/isulad/daemon.json`):** Modifying `/etc/isulad/daemon.json` **requires restarting `iSulad`** (**`systemctl restart isulad`**) to take effect!

---

### 2. Container Lifecycle & 4 Official Container States (Ch.07 Quiz Q1!)
* **Official Ch.07 Quiz Q1 (p.439):** Which of the following are container states?
  * **`A. Created`** (newly created via `isula create nginx`, not yet started)
  * **`B. Exited`** (stopped container)
  * **`C. Up`** (running container after `isula start` or `isula run`)
  * **`D. Paused`** (suspended via `isula pause`) -> **Answer: `ABCD`!**

---

### 3. Complete `isula` Container Lifecycle Commands
| Command | Key Options & Usage Examples (Ch.07, pp. 405–417) |
| :--- | :--- |
| **`isula create <image>`** | Creates a container in `Created` state; returns a 64-hex-digit Container ID (first **12 digits** shown in `isula ps`; can use unambiguous prefix like `e` or `7a`). |
| **`isula start <ID>`** | Starts a `Created` or `Exited` container -> status changes to **`Up`**. |
| **`isula run [opts] <img >`** | Creates and starts a container in one step:<br>• **`-d`**: Run in background.<br>• **`-it`**: Interactive (`-i`) + allocate pseudo-TTY (`-t`), e.g., `isula run -it nginx /bin/bash`.<br>• **`-p hostPort:containerPort[/udp]`**: Port mapping (can pass multiple `-p`, e.g., `isula run -d -p 8081:80 -p 5000:5000 nginx`).<br>• **`-e KEY=VAL`**: Set environment variable(s) (`-e A=100 -e B=200`).<br>• **`--workdir /tmp`**: Set container working directory.<br>• **`--name test`**: Assign container name.<br>• **`--dns 114.114.114.114`**: Set container DNS server.<br>• **`--restart <policy>`**: Auto-restart policy: **`no`** (default), **`on-failure[:N]`**, **`always`**, **`unless-stopped`**.<br>• **`--rm`**: Automatically delete container when it stops. |
| **`isula pause / unpause`** | `isula pause <ID>` pauses a running container (`Paused`); `isula unpause <ID>` resumes it (`Up`). |
| **`isula exec` vs. `attach`** | **`isula exec [-it] <ID> <cmd>`** creates a new terminal to run commands cleanly (**recommended**; `attach` may cause errors and is not recommended). |
| **`isula ps`** | Lists running containers. **`-a`** (all containers), **`-q`** (only IDs), **`-n 2`** (latest 2 created containers). |
| **`isula inspect / logs`** | **`isula inspect [--format="{{json .NetworkSettings}}"] <ID>`** (Go template format by default); **`isula logs <ID>`**. |
| **`isula restart / rm`** | **`isula restart <ID>`**; **`isula rm <ID>`** deletes stopped containers (**`isula rm -f <ID>`** forcibly deletes a running container!). |

---

## Key Takeaways
- **iSulad configuration priority from highest to lowest is: CLI (isulad --xxx or /etc/sysconfig/iSulad OPTIONS) > Configuration file (/etc/isulad/daemon.json) > Default code configurations.**
- **All four states—Created, Exited, Up, and Paused—are valid iSula container states (Official Ch.07 Quiz Q1: ABCD).**
- **isula rm can only delete stopped containers by default; use 'isula rm -f <ID>' to forcibly delete a running container, or '--rm' on 'isula run' to auto-delete upon exit.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Official Ch.07 Quiz Q1): 'Which of the following are container states? A. Created B. Exited C. Up D. Paused' -> ABCD!

> [!WARNING]
> EXAM TRAP: In 'isula run -p 8081:80 nginx', the FIRST number (8081) is the HOST port and the SECOND number (80) is the CONTAINER port!

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`04-Exercise-iSula-Container-Lifecycle-Lab.html`](./04-Exercise-iSula-Container-Lifecycle-Lab.html)** (or [`04-Exercise-iSula-Container-Lifecycle-Lab.md`](./04-Exercise-iSula-Container-Lifecycle-Lab.md)) to apply this concept in an interactive lab workbench!
