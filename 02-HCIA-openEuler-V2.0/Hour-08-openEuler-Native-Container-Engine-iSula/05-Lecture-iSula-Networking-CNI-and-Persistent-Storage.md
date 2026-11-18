# 📖 iSula Container Networking (CNI) & Persistent Storage (`-v`)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 08 — openEuler Native Container Engine iSula (iSulad) (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `06-Exercise-iSula-Network-and-Volume-Mount-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.07, pp. 418–426

---

## 🎯 Learning Objectives
- Explain how `iSulad` integrates with Container Network Interface (CNI) plugins and configure CNI in `/etc/isulad/daemon.json`
- Distinguish the 3 iSula CNI plugins (`bridge`, `portmap`, `firewall`) and manage networks via `isula network create/ls/inspect` and `--net`
- Implement container persistent storage by mounting host files/directories with `isula run -v /host:/container[:rw|:ro]`

---

### 1. How `iSulad` Implements Container Networking with CNI
* **Runtime & Network Flow:** `User -> iSula -> Runtime (LCR by default) / CNI / CSI -> Container`.
* Because `iSulad` does not bundle a built-in network stack, it uses **CNI (Container Network Interface)** binary plugins (v0.9.0+ recommended, v1.3.0 available from `github.com/containernetworking/plugins`).
* **Supported Network Mode:** While CNI specifications support bridge, VLAN, Flannel, and Calico, **currently `iSula` only supports the `bridge` mode** (Ch.07, p.420), where containers connected to the same Linux bridge communicate directly with each other and with the host.
* **Enabling CNI in `/etc/isulad/daemon.json` (Ch.07, p.422):**
  * **`"network-plugin": "cni"`** (can be set to `cni` or left empty by default).
  * **`"cni-bin-dir": "/opt/cni/bin"`** (default directory storing compiled CNI plugin binaries).
  * **`"cni-conf-dir": "/etc/cni/net.d"`** (default directory storing CNI network configuration files).

---

### 2. Three iSula Network Plugins & `isula network` Commands
When you create a bridge network in iSula, three CNI plugins work together (Ch.07, p.423):
1. **`bridge` plugin:** Creates a Linux bridge device, connects container virtual NICs to the bridge, and assigns IP addresses via the **`host-local` IPAM** plugin.
2. **`portmap` plugin:** Implements **NAT port forwarding** between container ports and host ports.
3. **`firewall` plugin:** Uses **`iptables`** to control ingress/egress container traffic and enforce port-mapping security rules.
* **iSula Network CLI Operations:**
  ```bash
  isula network create cni0
  isula network ls
  isula network inspect cni0
  isula run --net cni0 -d -it isulad/busybox sleep 99d
  ```

---

### 3. Container Persistent Storage (`-v` Host Bind Mounts & SCI)
By default, modifications inside a container are written only to its **temporary read/write container layer** and are lost when the container is deleted!
* **Two Persistent Storage Methods:**
  1. **Mount host files or directories into the container (`-v`).**
  2. **Use a third-party storage plugin** (invoked via **SCI**).
* **Mounting Syntax & Permissions (`-v` on `isula create` or `isula run`):**
  ```bash
  isula run -it -n storage \
    -v /root/test1.txt:/tmp/test1.txt:rw \
    -v /root/test2.txt:/tmp/test2.txt:ro \
    oepkgs/test/nginx:latest /bin/bash
  ```
  * **`rw` (Default):** Container has **read-write** permission on the mounted host file/directory.
  * **`ro`:** Container has **read-only** permission (writing inside the container returns `Read-only file system`).

---

## 🔑 Key Takeaways
- **iSulad uses LCR as its default runtime and CNI for networking; currently, iSula only supports the 'bridge' network mode.**
- **In /etc/isulad/daemon.json, CNI is configured with 'network-plugin': 'cni', 'cni-bin-dir': '/opt/cni/bin' (default), and 'cni-conf-dir': '/etc/cni/net.d' (default), utilizing the bridge, portmap, and firewall plugins.**
- **Use 'isula run -v /host/path:/container/path[:rw|:ro]' for persistent storage; 'rw' (read-write) is the default mount permission.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Do not confuse cni-bin-dir and cni-conf-dir defaults in /etc/isulad/daemon.json! cni-bin-dir defaults to '/opt/cni/bin', whereas cni-conf-dir defaults to '/etc/cni/net.d'.

> [!WARNING]
> EXAM TRAP: Currently, iSula only supports the 'bridge' network mode in CNI (Ch.07 p.420).

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-iSula-Network-and-Volume-Mount-Lab.html`](./06-Exercise-iSula-Network-and-Volume-Mount-Lab.html)** (or [`06-Exercise-iSula-Network-and-Volume-Mount-Lab.md`](./06-Exercise-iSula-Network-and-Volume-Mount-Lab.md)) to apply this concept in an interactive lab workbench!
