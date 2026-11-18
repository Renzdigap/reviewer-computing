# `systemd` Service Architecture, Unit Files & `journald` Log Management

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 05 — Software Packages, systemd Services, Processes & Scheduled Tasks (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (7 mins) - Followed immediately by `06-Exercise-Systemctl-and-Journalctl-Service-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.04, pp. 215–223

---

## Learning Objectives
- Explain `systemd` (PID 1) advantages over SysVinit, its 3 invoked kernel modules (`cgroups`, `autofs`, `kdbus`), and its 12 Unit types
- Parse the 3 sections of a `systemd` unit file (`[Unit]`, `[Service]`, `[Install]`) and key directives (`After=`, `Requires=`, `Wants=`, `ExecStart=`, `WantedBy=`)
- Control service lifecycle with `systemctl` and query centralized service logs with `journalctl -u <service>`

---

### 1. `systemd` Architecture (PID 1) & Unit Types
* **What is `systemd`?** **`systemd`** is the **first system program (`PID 1`)** loaded by the Linux kernel at boot. Compared with legacy `SysVinit`, `systemd` provides fast parallel activation, on-demand activation, process lifecycle tracking via **cgroups**, mount/automount management, transactional dependency management, backwards compatibility with SysVinit scripts, and system snapshots/restoration.
* **Three Kernel Modules Directly Invoked by `systemd` (Ch.04, p.217):**
  1. **`cgroups`**: Resource control and restriction.
  2. **`autofs`**: Automatic file system mounting.
  3. **`kdbus`**: Kernel message passing.
* **12 `systemd` Unit Types:**
  * **`service`** (system service), **`target`** (group of units / runlevel, e.g., `multi-user.target`, `graphical.target`), **`automount`**, **`device`**, **`mount`**, **`path`**, **`scope`** (externally created process), **`snapshot`**, **`slice`** (hierarchical cgroup process tree), **`socket`** (IPC socket), **`swap`**, and **`timer`**.

---

### 2. Anatomy of a `systemd` Unit File (3 Sections)
A complete `.service` unit file consists of **three sections** (Ch.04, p.219):

| Section | Key Directives & Meaning |
| :--- | :--- |
| **`[Unit]`** | Defines service metadata, startup order, and dependencies:<br>• **`Description=`**: Brief description shown in `systemctl status`.<br>• **`After=`**: Ordering rule—start this unit *after* the specified unit starts.<br>• **`Requires=`**: **Hard dependency**—startup fails if the required dependency is missing/fails.<br>• **`Wants=`**: **Soft dependency**—if the dependency is missing/fails, this service **can still start**. |
| **`[Service]`** | Defines service execution behavior:<br>• **`ExecStart=` (Mandatory):** Command to start the service.<br>• **`ExecStop=`**: Command to stop the service.<br>• **`Restart=`**: Auto-restart policy (`always`, `on-failure`, etc.).<br>• **`User=`**: User account under which the service runs (`root` by default). |
| **`[Install]`** | Defines how `systemctl enable` integrates the service into boot targets:<br>• **`WantedBy=`**: Target unit associated when enabled (e.g., `multi-user.target`). |

---

### 3. `systemctl` Operations & `journald` (`journalctl`)
* **Service Lifecycle Commands (`systemctl`):**
  * **`systemctl start / stop / restart <name>.service`**
  * **`systemctl enable / disable <name>.service`** (enable/disable auto-start at boot)
  * **`systemctl list-units --type service`** (add **`-all`** to view all active and inactive services)
  * **`systemctl status <name>.service`**: Displays `Loaded` (path & enabled state), `Active` (running status & timestamp), `Main PID`, `CGroup`, and recent log fragments.
* **Centralized Log Management (`journald` & `journalctl`):**
  * `journald` is a subsystem of `systemd` that automatically records all service logs.
  * While `systemctl status <service>` shows only recent log fragments, **`journalctl -u <service_name>`** displays the **complete service logs**!

---

## Key Takeaways
- **systemd is PID 1 and directly invokes 3 kernel modules: cgroups (resource control), autofs (auto-mounting), and kdbus (message passing).**
- **A systemd unit file has 3 sections: [Unit] (Description, After, Requires [hard dependency], Wants [soft dependency]), [Service] (ExecStart [mandatory], ExecStop, Restart, User), and [Install] (WantedBy).**
- **Use 'systemctl start/stop/restart/enable/disable/status <name>.service' to manage services, and 'journalctl -u <service>' to view complete service logs.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: In the [Unit] section, 'Requires=' declares a HARD dependency (service fails if dependency is missing), whereas 'Wants=' declares a SOFT dependency (service still starts if dependency is missing)!

> [!WARNING]
> EXAM TRAP: 'systemctl status <service>' displays only service log fragments; use 'journalctl -u <service>' to display complete service logs.

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-Systemctl-and-Journalctl-Service-Lab.html`](./06-Exercise-Systemctl-and-Journalctl-Service-Lab.html)** (or [`06-Exercise-Systemctl-and-Journalctl-Service-Lab.md`](./06-Exercise-Systemctl-and-Journalctl-Service-Lab.md)) to apply this concept in an interactive lab workbench!
