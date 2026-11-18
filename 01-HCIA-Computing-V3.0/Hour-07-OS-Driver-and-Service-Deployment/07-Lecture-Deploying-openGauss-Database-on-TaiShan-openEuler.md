# Deploying openGauss Database on TaiShan / openEuler

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 07 — OS Compatibility, openEuler 22.03 LTS Installation, Drivers/Firmware & Service Deployment (Sprint 4 of 4)  
**Format:** Bite-Sized Lecture (8 mins) - Followed immediately by `08-Exercise-openGauss-XML-gs-preinstall-and-gs-install-Lab` (8 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.05, pp. 343–349

---

## Learning Objectives
- Compare openGauss Standalone deployment vs. HA deployment (1 primary + 1 to 8 standby servers)
- Understand when to use the installation script vs. CLI commands for single vs. multiple instances
- Master the exact 8-step openGauss installation workflow (`XML` config, `gs_preinstall`, `gs_install`, standby readable)

---

### 1. openGauss Deployment Modes: Standalone vs. HA (p. 344)
openGauss supports two deployment modes on openEuler / TaiShan servers:
1. **Standalone Deployment**:
   - One or multiple database instances are deployed on a **single host**.
   - **Not recommended** for production due to **data loss risks** if the single host fails.
   - **Script vs. CLI Rule (p. 344)**: openGauss provides a **script** for deploying **one database instance** on a single server, whereas **CLI commands are recommended** if you need to deploy **multiple database instances** on a single server.
2. **HA (High Availability) Deployment**:
   - Deploys **one primary server** and **at least one (up to eight) standby servers** (`1 Primary + 1..8 Standby`).

---

### 2. Eight-Step openGauss Installation & Deployment Procedure (p. 345)
Look closely at the official flowchart and step descriptions on **Ch.05 Page 345**:
1. **Preparing for the installation**: Prepare the hardware and software environments (OS parameters, dependencies, firewall/SELinux).
2. **Obtaining and verifying the software package**: Download the openGauss installation package from the official website and verify its integrity.
3. **Configuring the XML file**: Create the cluster configuration **XML file**, which specifies the **server information, installation path, IP address, and port** where openGauss will be deployed.
4. **Uploading the software package and XML file**: Upload both to the target server(s).
5. **Decompressing the software package**: Extract the installation tarball.
6. **Initializing the installation environment (`gs_preinstall`)**: Run the **`gs_preinstall`** command (as `root`) to prepare and initialize the OS installation environment based on the XML file.
7. **Performing the installation (`gs_install`)**: Switch to the database O&M user (e.g., `omm`) and run the **`gs_install`** command with the XML file to install openGauss.
8. **(Optional) Setting the standby node to readable**: Configure the standby node to be readable to meet read-scalability and data consistency requirements.

---

## Key Takeaways
- **openGauss supports Standalone deployment (not recommended due to data loss risk; use script for 1 instance, CLI commands for multiple instances on 1 server) and HA deployment (1 primary + 1 to 8 standby servers).**
- **The openGauss XML configuration file defines the server hostname/IP address, installation path, and database port.**
- **Use `gs_preinstall` to initialize the installation environment, and then use `gs_install` to perform the actual database installation.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: In openGauss HA deployment, a single primary server supports at least 1 and UP TO 8 standby servers (p. 344)!

> [!WARNING]
> EXAM TRAP: Do not reverse `gs_preinstall` and `gs_install`: `gs_preinstall` initializes the installation environment BEFORE `gs_install` installs openGauss!

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`08-Exercise-openGauss-XML-gs-preinstall-and-gs-install-Lab.html`](./08-Exercise-openGauss-XML-gs-preinstall-and-gs-install-Lab.html)** (or [`08-Exercise-openGauss-XML-gs-preinstall-and-gs-install-Lab.md`](./08-Exercise-openGauss-XML-gs-preinstall-and-gs-install-Lab.md)) to apply this concept in an interactive lab workbench!
