# Hands-On Lab: Managing Services (`systemctl`) and Querying Complete Logs (`journalctl -u`)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 05 — Software Packages, systemd Services, Processes & Scheduled Tasks (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `05-Lecture-systemd-Service-and-Journald-Log-Management`  
**Interactive Workbench:** Open **[`06-Exercise-Systemctl-and-Journalctl-Service-Lab.html`](./06-Exercise-Systemctl-and-Journalctl-Service-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You are administering the `sshd` and `k3s` services on openEuler. Restart and enable `sshd.service`, list all running service units using `systemctl list-units --type service`, and query the complete service logs of `k3s` using `journalctl -u k3s`.

### Step-by-Step Instructions
1. Step 1: Restart `sshd.service` (`systemctl restart sshd.service`) and enable it to start at boot (`systemctl enable sshd.service`).
2. Step 2: Display all running service units using `systemctl list-units --type service`.
3. Step 3: View the complete logs of the `k3s` service using `journalctl -u k3s`.

### Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Restart and enable sshd.service
<systemctl_restart_command>
<systemctl_enable_command>

# Step 2: List running service units
<systemctl_list_units_command>

# Step 3: View complete logs of the k3s service
<journalctl_command>
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `systemctl restart sshd.service` and `systemctl enable sshd.service`.
- Use `systemctl list-units --type service` (Ch.04 p.221).
- Use `journalctl -u k3s` (Ch.04 p.223).

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Restart and enable sshd.service
systemctl restart sshd.service
systemctl enable sshd.service

# Step 2: List running service units
systemctl list-units --type service

# Step 3: View complete logs of the k3s service
journalctl -u k3s
```

#### Expected Console / Query Output:
```text
UNIT          LOAD   ACTIVE SUB     DESCRIPTION
atd.service   loaded active running Deferred execution scheduler
crond.service loaded active running Command Scheduler
sshd.service  loaded active running OpenSSH server daemon

Jul 28 17:05:18 vbox systemd[1]: Starting Lightweight Kubernetes...
Jul 28 17:05:19 vbox k3s[76]: time="2026-07-28T17:05:19+08:00" level=info msg="Starting k3s v1.30.2+k3s1"
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**In a `systemd` `.service` unit file, which directive in the `[Service]` section is mandatory, and which directive in `[Unit]` declares a soft dependency that allows the service to start even if the dependency is missing?**

- A. `ExecStart=` (mandatory); `Wants=` (soft dependency)
- B. `ExecStop=` (mandatory); `Requires=` (soft dependency)
- C. `WantedBy=` (mandatory); `After=` (soft dependency)
- D. `Description=` (mandatory); `User=` (soft dependency)

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** Per Ch.04 (p.219), `ExecStart=` is mandatory in `[Service]`, while in `[Unit]`, `Requires=` is a hard dependency and `Wants=` declares a soft dependency (the service can still start if the dependency is missing).
</details>

### Question 2 [Single-Choice]
**Which command displays the complete logs recorded by `journald` for a specific `systemd` service such as `k3s`?**

- A. `systemctl status k3s`
- B. `journalctl -u k3s`
- C. `dmesg -s k3s`
- D. `last -f k3s`

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.04 (p.223), `systemctl status <Service name>` displays only service log fragments, whereas `journalctl -u <Service name>` displays complete service logs.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which three kernel modules are directly invoked by `systemd` according to the openEuler `systemd` architecture?**

- A. `cgroups` (for resource control and restriction)
- B. `autofs` (for automatic mounting)
- C. `kdbus` (for kernel message passing)
- D. `ext2fs` (for floppy formatting)

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Ch.04 (p.217), three key modules in the kernel are directly invoked by `systemd`: `cgroups` for resource control and restriction, `autofs` for automatic mounting, and `kdbus` for kernel message passing.
</details>
