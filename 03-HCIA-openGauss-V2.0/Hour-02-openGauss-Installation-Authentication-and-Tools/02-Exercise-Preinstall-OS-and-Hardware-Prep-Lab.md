# 💻 Hands-On Lab: Preparing openEuler OS Configurations for openGauss

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 02 — openGauss Installation, Authentication & O&M Tools (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `01-Lecture-Deployment-Modes-Prerequisites-and-OS-Config`  
**Interactive Workbench:** Open **[`02-Exercise-Preinstall-OS-and-Hardware-Prep-Lab.html`](./02-Exercise-Preinstall-OS-and-Hardware-Prep-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
You are preparing a Kunpeng 920 (ARM64) server running openEuler 20.03 LTS for openGauss installation. Disable firewalld, disable `RemoveIPC`, set the ARM64 recommended MTU (8192) on `eth0`, and create the `dbgrp` group and `omm` user.

### 📋 Step-by-Step Instructions
1. Step 1: Disable and stop `firewalld.service` using `systemctl`.
2. Step 2: Configure `RemoveIPC=no` in `/etc/systemd/logind.conf` and restart `systemd-logind`.
3. Step 3: Set the `eth0` MTU to `8192` (recommended for ARM64) and create group `dbgrp` and user `omm` (`groupadd dbgrp && useradd -g dbgrp omm`).

### 📝 Starter Workspace (`root@opengauss:~#`)
```bash
# Step 1: Disable and stop firewalld
systemctl disable ____
systemctl stop firewalld.service

# Step 2: Set RemoveIPC=no and reload systemd-logind
sed -i 's/.*RemoveIPC.*/____/' /etc/systemd/logind.conf
systemctl daemon-reload && systemctl restart systemd-logind

# Step 3: Set ARM64 MTU (8192) on eth0 and create dbgrp/omm
ifconfig eth0 mtu ____
groupadd ____ && useradd -g dbgrp ____
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- On openEuler, `RemoveIPC=no` must be set so systemd does not clean up IPC semaphores/shared memory when `omm` logs out.
- For ARM (Kunpeng), the recommended NIC MTU is 8192 (for x86 it is 1500).
- The standard OS group is `dbgrp` and the OS user is `omm`.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
systemctl disable firewalld.service
systemctl stop firewalld.service
sed -i 's/.*RemoveIPC.*/RemoveIPC=no/' /etc/systemd/logind.conf
systemctl daemon-reload && systemctl restart systemd-logind
ifconfig eth0 mtu 8192
groupadd dbgrp && useradd -g dbgrp omm
```

#### Expected Console / Query Output:
```text
Removed /etc/systemd/system/multi-user.target.wants/firewalld.service.
RemoveIPC=no
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 8192
uid=1000(omm) gid=1000(dbgrp) groups=1000(dbgrp)
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Multiple-Choice (Select ALL)]
**(Official Ch.03 Quiz Q1) Which of the following are the openGauss deployment modes?**

- A. Single-node deployment
- B. Deployment with one primary and one standby
- C. Deployment with one primary and multiple standbys
- D. Deployment with dual primary nodes

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 02 (p. 77) and Chapter 03 Quiz Q1 (p. 268), openGauss supports single-node deployment, one primary and one standby, and one primary and multiple standbys. Dual-primary deployment is NOT supported.
</details>

### Question 2 [Single-Choice]
**When configuring the network interface card (NIC) MTU on openGauss database nodes, what are the recommended MTU values for x86 and ARM (Kunpeng) architectures respectively?**

- A. 1500 for x86; 1500 for ARM
- B. 1500 for x86; 8192 for ARM
- C. 8192 for x86; 1500 for ARM
- D. 9000 for x86; 4096 for ARM

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 02 (p. 89), for x86 the recommended MTU value is 1500, and for ARM (Kunpeng) the recommended MTU value is 8192.
</details>

### Question 3 [True / False]
**In openGauss one-primary-two-standby deployment, the primary and standby nodes can be deployed on the same physical machine in production to save hardware costs.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False (Ch.02 p. 81). The primary and standby nodes cannot be deployed on the same physical machine because a single physical host failure would take down multiple copies.
</details>
