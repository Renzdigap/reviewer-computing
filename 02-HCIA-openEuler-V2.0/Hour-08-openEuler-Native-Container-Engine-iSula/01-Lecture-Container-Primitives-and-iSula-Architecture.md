# Container Fundamentals (Namespaces, `cgroups`) & iSula Architecture

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 08 — openEuler Native Container Engine iSula (iSulad) (Sprint 1 of 4)  
**Format:** Bite-Sized Lecture (7 mins) - Followed immediately by `02-Exercise-Namespaces-Cgroups-and-iSula-Specs-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.07, pp. 387–398

---

## Learning Objectives
- Distinguish the two core Linux kernel container features: Namespaces (resource isolation across 6 types) and `cgroups` (resource limitation in `/sys/fs/cgroup`)
- Explain what `iSula` (`iSulad`) is, why it is written in C/C++ instead of Go, and its Northbound (CLI/CRI) and Southbound (OCI: LCR, runC, Kata) architecture
- Quantify iSula's Lightweight (68%+ less memory), Fast (35% faster startup, 75% faster download, 15% faster `isula-build`), Easy-to-Use (`isula-transform`), and Flexible (REST vs. gRPC) advantages

---

### 1. Core Linux Kernel Container Primitives: Namespaces vs. `cgroups`
Container technology evolved from `chroot` (1982), FreeBSD `Jail` (1998), `Linux-VServer` (2001), `Solaris Zone` (2004), `OpenVZ` (2005), **`cgroups` & `Namespaces` (2007)**, `LXC` (2008), to `Docker`, **`iSula`**, and `Kubernetes` (2011–now).
* **Namespaces — Function: Resource Isolation (Ch.07, p.391):**
  Encapsulates global kernel resources so processes in different namespaces are isolated from each other:

| Namespace Type | System Call Parameter | Isolated Resource | Kernel Version |
| :--- | :--- | :--- | :--- |
| **PID namespace** | `CLONE_NEWPID` | Process IDs | Linux 2.6.24 |
| **Mount namespace** | `CLONE_NEWNS` | File system mount points | Linux 2.6.19 |
| **Network namespace** | `CLONE_NEWNET` | Network devices, IP addresses, ports | Linux 2.6.24–2.6.29 |
| **User namespace** | `CLONE_NEWUSER` | User IDs (UIDs) and Group IDs (GIDs) | Linux 2.6.23–3.8 |
| **UTS namespace** | `CLONE_NEWUTS` | **Host names and domain names** | Linux 2.6.19 |
| **IPC namespace** | `CLONE_NEWIPC` | Semaphores, message queues, shared memory | Linux 2.6.19 |

* **`cgroups` (Linux Control Groups) — Function: Resource Limitation (Ch.07, p.392):**
  * **Limits system resources** (CPU, memory, block I/O) available to a set of processes, controls process priorities, and suspends/restores processes.
  * Organized as files and directories in **`/sys/fs/cgroup`**.

---

### 2. What is `iSula` / `iSulad` & Its Unified Architecture
* **Why `iSula`?** Mainstream engines like Docker and containerd are written in **Go**, which incurs high memory overhead in resource-constrained edge computing, IoT, and high-density server scenarios. **`iSula`** is openEuler's native container solution implemented in **C/C++**, featuring a unified architecture for CT and IT fields (system, secure, common, and embedded containers).
* **iSulad Architecture (Ch.07, p.394):**
  * **Northbound Interfaces:** **CLI (`isula`)** and **CRI** (for Kubernetes orchestration).
  * **Communication Modes:** **Lightweight mode (REST interface)** and **Performance mode (gRPC interface)**.
  * **Core Daemon (`iSulad`):** Image Service, Execution Service, Content Service, and Rootfs Service (separated to isolate operations).
  * **Southbound OCI Runtimes:** Interconnects with OCI-compliant runtimes: **LCR (Lightweight Container Runtime — default, written in C)**, **`runC`**, and **`Kata`**.

---

### 3. Four Advantages of iSula (Lightweight, Fast, Easy-to-Use, Flexible)
1. **Lightweight:** **>68% lower stable memory usage** for 100 containers compared to Docker (C/C++, LCR, simplified monitor process).
2. **Fast:**
   * **35% faster concurrent startup** (100 containers) using `fork/exec` + direct function calls and separated rootfs/image services.
   * **75% faster image download** via smart on-demand loading.
   * **15% faster image building (`isula-build`)** via **DAG-based building** (unlike `docker build`, `isula-build` does **not** start a container for every Dockerfile instruction—only for necessary instructions like `RUN`).
3. **Easy-to-Use Toolkit:** **`isula-build`** (Dockerfile image builder) and **`isula-transform`** (cold/live migration tool converting Docker containers to iSulad).

---

## Key Takeaways
- **Namespaces provide resource ISOLATION (6 types: PID, Mount, Network, User, UTS [host/domain names], IPC), whereas cgroups (/sys/fs/cgroup) provide resource LIMITATION (CPU, memory, block I/O).**
- **iSula (iSulad) is written in C/C++ (unlike Go-based Docker), uses LCR as its default OCI runtime, and supports Lightweight mode (REST) and Performance mode (gRPC).**
- **Compared with Docker, iSula reduces 100-container memory usage by >68%, speeds up concurrent startup by 35%, accelerates smart image downloads by 75%, and speeds up DAG-based image builds (isula-build) by 15%.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Do not confuse Namespaces vs. cgroups! Namespaces = Resource Isolation (what a container can SEE); cgroups = Resource Limitation (how much CPU/RAM/I/O a container can USE).

> [!WARNING]
> EXAM TRAP: UTS namespace (CLONE_NEWUTS) isolates host names and domain names, whereas IPC namespace (CLONE_NEWIPC) isolates semaphores, message queues, and shared memory.

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`02-Exercise-Namespaces-Cgroups-and-iSula-Specs-Lab.html`](./02-Exercise-Namespaces-Cgroups-and-iSula-Specs-Lab.html)** (or [`02-Exercise-Namespaces-Cgroups-and-iSula-Specs-Lab.md`](./02-Exercise-Namespaces-Cgroups-and-iSula-Specs-Lab.md)) to apply this concept in an interactive lab workbench!
