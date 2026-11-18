# 📖 Deployment Modes, Hardware/OS Prerequisites & XML Configuration

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 02 — openGauss Installation, Authentication & O&M Tools (Sprint 1 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `02-Exercise-Preinstall-OS-and-Hardware-Prep-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.02, pp. 77–91

---

## 🎯 Learning Objectives
- Compare the 3 official openGauss deployment modes: Standalone, Primary/Standby, and One Primary + Multiple Standbys
- Verify hardware (RAM, CPU, Disk, NIC MTU) and software/OS prerequisites (openEuler, Python 3.7, libaio-devel)
- Configure OS settings prior to installation: SELinux, firewalld, RemoveIPC=no, locale/timezone, NIC MTU, root SSH, and `dbgrp`/`omm`

---

### 1. Three Official openGauss Deployment Modes (pp. 77–81, Ch.03 Quiz Q1!)

| Deployment Mode | Data Copies | HA / RPO / RTO | Key Characteristics & Target Scenario |
| :--- | :--- | :--- | :--- |
| **1. Standalone (Single-node)** | **1 copy** | No HA; RTO & RPO uncontrollable | Single instance; lost instance data can only be restored from physical backup. For **trial use, learning, and sandbox testing** (not production). |
| **2. Primary/Standby (1 Primary + 1 Standby)** | **2 copies** | **RPO = 0**, Instance fault **RTO < 10s** | Primary supports Read/Write; Standby receives/replays WAL logs and supports **Read-only**. Protects against instance failure. |
| **3. One Primary + Multiple Standbys (Quorum)** | **2 to 4 copies** (typically 1P + 2S = **3 copies**; up to 8 standbys in v2.0+) | **RPO = 0**, Instance fault **RTO < 10s**, **99.99% reliability** | Quorum replication synchronizes data to at least one standby node for max performance. Primary and standby nodes **cannot** be on the same physical machine. |

> **CRITICAL EXAM NOTE (Ch.03 Quiz Q1)**: openGauss supports **Single-node**, **One primary + one standby**, and **One primary + multiple standbys**. It **DOES NOT** support "Dual primary nodes" deployment!

---

### 2. Hardware & Software Requirements (pp. 84–85)
- **Memory**: **>= 32 GB** for function debugging; **>= 128 GB** for commercial/performance testing; **4 GB min (8 GB recommended)** for individual developers.
- **CPU**: At least one 8-core 2.0 GHz CPU (debugging) or 16-core 2.0 GHz CPU (commercial); 2 cores min (4 cores recommended) for individual developers. Supports **Kunpeng (ARM64)** and **x86_64**.
- **Disk**: At least **1 GB** for application installation, **>= 300 MB** per host for data, and **> 70% free space** reserved for data storage. Recommended: **RAID 1 for system disk**, **4 groups of RAID 5 for data disks**, Disk Cache Policy = **Disabled**.
- **Network**: >= 300 Mbit/s Ethernet (bond 2 NICs recommended). Recommended **MTU**: **1500 for x86**, **8192 for ARM (Kunpeng)**.
- **OS & Software Dependencies**:
  - **OS**: Arm (`openEuler 20.03/22.03 LTS`, `KylinOS`); x86 (`openEuler 20.03/22.03 LTS`, `CentOS 7.6`).
  - **File system**: Remaining inodes **> 1.5 billion**.
  - **Python**: **Python 3.7.x** on openEuler/KylinOS; **Python 3.6.x** on CentOS 7.6.
  - **Packages**: `bzip2`, `libaio-devel` (0.3.109-13), `readline-devel` (7.0-13), `expect`.

---

### 3. Mandatory OS Configuration Changes & User Planning (pp. 86–91)
1. **Disable SELinux & Firewall**: Set `SELINUX=disabled` in `/etc/selinux/config`, reboot, and run `systemctl disable firewalld.service && systemctl stop firewalld.service`.
2. **Locale & Timezone**: Add `export LANG=en_US.UTF-8` to `/etc/profile`; copy `/usr/share/zoneinfo/Locale/Timezone` to `/etc/localtime` and sync time with `date -s`. Optional: `swapoff -a` to prevent buffer eviction.
3. **Disable `RemoveIPC` (Critical on openEuler!)**: Set `RemoveIPC=no` in **both** `/etc/systemd/logind.conf` and `/usr/lib/systemd/system/systemd-logind.service`, then run `systemctl daemon-reload && systemctl restart systemd-logind`.
4. **Enable Root SSH & Disable Banner**: In `/etc/ssh/sshd_config`, set `PermitRootLogin yes` and comment out `#Banner XXXX` (welcome banners interfere with remote installation scripts).
5. **User & Group (`dbgrp` and `omm`)**: Create group `dbgrp` (`-G dbgrp`) and OS user `omm` (`-U omm`). During `gs_install`, a database superuser `omm` with the same name is created.

---

## 🔑 Key Takeaways
- **openGauss deployment modes are Single-node, One primary + one standby, and One primary + multiple standbys (up to 8 standbys; typically 1 primary + 2 standbys for 99.99% availability). Dual-primary is NOT supported.**
- **On openEuler (ARM64), set RemoveIPC=no in both logind.conf and systemd-logind.service, disable SELinux and firewalld, comment out SSH Banner, and set NIC MTU to 8192 (1500 on x86).**
- **System disk should use RAID 1, data disks should use 4 groups of RAID 5 with Disk Cache Policy Disabled, and remaining inodes should exceed 1.5 billion.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.03 Quiz Q1): 'Which of the following are the openGauss deployment modes?' -> A. Single-node, B. One primary and one standby, C. One primary and multiple standbys (ABC). D. Dual primary nodes is FALSE!

> [!WARNING]
> EXAM TRAP: Why comment out `Banner` in `/etc/ssh/sshd_config`? Because welcome banner text interferes with automated remote SSH operations during `gs_preinstall` and `gs_install`!

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`02-Exercise-Preinstall-OS-and-Hardware-Prep-Lab.html`](./02-Exercise-Preinstall-OS-and-Hardware-Prep-Lab.html)** (or [`02-Exercise-Preinstall-OS-and-Hardware-Prep-Lab.md`](./02-Exercise-Preinstall-OS-and-Hardware-Prep-Lab.md)) to apply this concept in an interactive lab workbench!
