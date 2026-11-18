# Hands-On Lab: Creating CNI Bridge Networks (`isula network`) and Read-Only/Read-Write Volumes (`-v`)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 08 — openEuler Native Container Engine iSula (iSulad) (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `05-Lecture-iSula-Networking-CNI-and-Persistent-Storage`  
**Interactive Workbench:** Open **[`06-Exercise-iSula-Network-and-Volume-Mount-Lab.html`](./06-Exercise-iSula-Network-and-Volume-Mount-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You are configuring CNI networking and persistent volumes for `iSula` containers (following Ch.07 pp. 423–426). Create a CNI bridge network named `cni0`, launch a `busybox` container attached to `cni0` using `--net cni0`, and launch a container mounting `/root/test1.txt` as `rw` and `/root/test2.txt` as `ro`.

### Step-by-Step Instructions
1. Step 1: Create the iSula network `cni0` (`isula network create cni0`) and list existing networks (`isula network ls`).
2. Step 2: Start a background container attached to `cni0` using `isula run --net cni0 -d -it isulad/busybox sleep 99d`.
3. Step 3: Mount `/root/test1.txt` (`rw`) and `/root/test2.txt` (`ro`) into `/tmp/` using `-v /root/test1.txt:/tmp/test1.txt:rw -v /root/test2.txt:/tmp/test2.txt:ro`.

### Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Create iSula network cni0 and list networks
<isula_net_create_command>
<isula_net_ls_command>

# Step 2: Run isulad/busybox attached to network cni0
<isula_run_net_command>

# Step 3: Run container with test1.txt (rw) and test2.txt (ro) mounted
isula run -it -n storage <volume_mounts> oepkgs/test/nginx:latest /bin/bash
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `isula network create cni0` and `isula network ls` (Ch.07 p.423).
- Use `isula run --net cni0 -d -it isulad/busybox sleep 99d` (Ch.07 p.424).
- Use `-v /root/test1.txt:/tmp/test1.txt:rw -v /root/test2.txt:/tmp/test2.txt:ro` (Ch.07 p.426).

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Create iSula network cni0 and list networks
isula network create cni0
isula network ls

# Step 2: Run isulad/busybox attached to network cni0
isula run --net cni0 -d -it isulad/busybox sleep 99d

# Step 3: Run container with test1.txt (rw) and test2.txt (ro) mounted
isula run -it -n storage -v /root/test1.txt:/tmp/test1.txt:rw -v /root/test2.txt:/tmp/test2.txt:ro oepkgs/test/nginx:latest /bin/bash
```

#### Expected Console / Query Output:
```text
cni0
NAME    VERSION    PLUGIN
cni0    1.0.0      bridge,portmap,firewall

6a43c0d019609299916ba058886e7a2f0e60465a27a3212ba2982253ed79494c

root@309f333abd89:/tmp# echo "test" >> test1.txt
root@309f333abd89:/tmp# echo "test" >> test2.txt
bash: test2.txt: Read-only file system
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**In `/etc/isulad/daemon.json`, what are the default directories for `cni-bin-dir` (CNI plugin binaries) and `cni-conf-dir` (CNI configuration files)?**

- A. `/usr/bin/cni` and `/etc/isulad/cni`
- B. `/opt/cni/bin` and `/etc/cni/net.d`
- C. `/var/lib/cni` and `/etc/sysconfig/cni`
- D. `/sbin/cni` and `/opt/cni/conf`

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.07 (p.422), the default directory for `cni-bin-dir` is `/opt/cni/bin`, and the default directory for `cni-conf-dir` is `/etc/cni/net.d`.
</details>

### Question 2 [Single-Choice]
**When mounting a host directory into an iSula container using `-v /host/dir:/container/dir`, what is the default access permission if neither `:ro` nor `:rw` is specified?**

- A. Read-only (`ro`)
- B. Read-write (`rw`)
- C. Execute-only (`x`)
- D. No access until `chmod` is run

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.07 (p.425), when using `-v` to mount host files or directories during container creation, `-rw` (read-write permission) is the default.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which three CNI network plugins are used together when `isula network create cni0` creates a container bridge network?**

- A. `bridge` (creates Linux bridge and assigns IPs via `host-local` IPAM)
- B. `portmap` (implements NAT port forwarding between container and host ports)
- C. `firewall` (uses `iptables` to set container network access rules)
- D. `vsftpd` (transfers files over FTP)

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Ch.07 (p.423), iSula network plugins for `cni0` are `bridge,portmap,firewall`.
</details>
