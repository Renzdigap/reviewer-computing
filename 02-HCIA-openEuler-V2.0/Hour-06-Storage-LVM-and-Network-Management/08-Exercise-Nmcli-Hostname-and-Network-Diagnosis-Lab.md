# Hands-On Lab: Configuring Connections & Static Routes with `nmcli`, Hostname & `ss` Diagnostics

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 06 — openEuler Disk Partitioning, LVM & Network Management (Sprint 4 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `07-Lecture-Network-Configuration-and-Diagnosis`  
**Interactive Workbench:** Open **[`08-Exercise-Nmcli-Hostname-and-Network-Diagnosis-Lab.html`](./08-Exercise-Nmcli-Hostname-and-Network-Diagnosis-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You are configuring networking on an openEuler server (following Ch.05 pp. 305–317). Permanently set the hostname to `openEuler01`, create and activate an Ethernet connection named `Demo` on `enp4s0`, add a static route `192.168.122.0/24` via `10.10.10.1` to `enp3s0`, and inspect listening TCP sockets with `ss -talnp`.

### Step-by-Step Instructions
1. Step 1: Set the permanent hostname to `openEuler01` using `hostnamectl set-hostname openEuler01`.
2. Step 2: Create connection `Demo` on `enp4s0` (`nmcli connection add con-name 'Demo' type Ethernet ifname enp4s0`) and activate it (`nmcli connection up 'Demo'`).
3. Step 3: Add a static route on `enp3s0` (`nmcli connection modify enp3s0 +ipv4.routes "192.168.122.0/24 10.10.10.1"`) and check listening sockets with `ss -talnp`.

### Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Permanently set hostname to openEuler01
<hostnamectl_command>

# Step 2: Create connection 'Demo' on enp4s0 and bring it up
<nmcli_add_command>
<nmcli_up_command>

# Step 3: Add static route to enp3s0 and inspect listening TCP sockets
<nmcli_route_command>
<ss_command>
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `hostnamectl set-hostname openEuler01` (Ch.05 p.305).
- Use `nmcli connection add con-name 'Demo' type Ethernet ifname enp4s0` and `nmcli connection up 'Demo'` (Ch.05 p.310).
- Use `nmcli connection modify enp3s0 +ipv4.routes "192.168.122.0/24 10.10.10.1"` (Ch.05 p.313) and `ss -talnp` (Ch.05 p.317).

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Permanently set hostname to openEuler01
hostnamectl set-hostname openEuler01

# Step 2: Create connection 'Demo' on enp4s0 and bring it up
nmcli connection add con-name 'Demo' type Ethernet ifname enp4s0
nmcli connection up 'Demo'

# Step 3: Add static route to enp3s0 and inspect listening TCP sockets
nmcli connection modify enp3s0 +ipv4.routes "192.168.122.0/24 10.10.10.1"
ss -talnp
```

#### Expected Console / Query Output:
```text
Connection 'Demo' (789c723b-cd60-4515-99fc-5074b6f38498) successfully added.
Connection successfully activated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/16)

State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port  Process
LISTEN  0       128     0.0.0.0:22           0.0.0.0:*          users:(("sshd",pid=60,fd=3))
LISTEN  0       128     [::]:22              [::]:*             users:(("sshd",pid=60,fd=4))
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [True / False]
**[Official Ch.05 Quiz Q1] The `route` command can view or configure host route information. Configured route information will remain valid permanently.**

- A. True
- B. False

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Official Ch.05 Quiz Q1 (p.318): False (`F`). Route information configured via the `route` command is temporary and lost upon system reboot.
</details>

### Question 2 [Single-Choice]
**In openEuler's Predictable Network Interface Naming scheme (`systemd/udev`), what does the interface name `enp0s3` signify?**

- A. `en` = Wireless LAN; `p0` = USB port 0; `s3` = Serial port 3
- B. `en` = Ethernet; `p0` = PCIe bus 0; `s3` = slot 3
- C. `en` = WWAN; `p0` = Onboard port 0; `s3` = MAC address 3
- D. `en` = Virtual bridge; `p0s3` = VLAN ID 3

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.05 (p.306), `en` indicates Ethernet (`wl` is Wireless, `ww` is WWAN), `p` indicates PCIe bus, and `s` indicates slot number (`0s3` = slot 3 on bus 0).
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about NetworkManager (`nmcli`/`nmtui`) and network diagnostic tools in openEuler are TRUE?**

- A. In NetworkManager, a device (network interface) may have multiple connections, but only one connection can remain active at a time.
- B. After modifying an active connection with `nmcli con mod`, you must run `nmcli con up <name>` for the changes to take effect.
- C. `tracepath` displays hop counts, measures RTT per hop, and detects changes in the Maximum Transmission Unit (MTU) along a path.
- D. `ss` (Socket Statistics) works faster than `netstat` by accessing data directly from the kernel.

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.05 (pp.308–317), all four statements are explicitly taught in the official HCIA-openEuler V2.0 material.
</details>
