# Hands-On Lab: openGauss HA Cluster Pre-Install & Installation Commands

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 07 — OS Compatibility, openEuler 22.03 LTS Installation, Drivers/Firmware & Service Deployment (Sprint 4 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `07-Lecture-Deploying-openGauss-Database-on-TaiShan-openEuler`  
**Interactive Workbench:** Open **[`08-Exercise-openGauss-XML-gs-preinstall-and-gs-install-Lab.html`](./08-Exercise-openGauss-XML-gs-preinstall-and-gs-install-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You are deploying an openGauss HA cluster on TaiShan 200 servers running openEuler 22.03 LTS using an XML configuration file (`/opt/software/openGauss/cluster_config.xml`). Complete the deployment commands and HA limits.

### Step-by-Step Instructions
1. Use `gs_preinstall` to initialize the installation environment with `-U omm -G dbgrp -X /opt/software/openGauss/cluster_config.xml`.
2. Use `gs_install` (as user `omm`) to install openGauss with `-X /opt/software/openGauss/cluster_config.xml`.
3. Set `MAX_HA_STANDBY_SERVERS` to `8`.

### Starter Workspace (`root@taishan-db:~#`)
```bash
# 1. Initialize the openGauss installation environment (as root):
/opt/software/openGauss/script/___ -U omm -G dbgrp -X /opt/software/openGauss/cluster_config.xml

# 2. Switch to omm and perform the openGauss installation:
su - omm -c "___ -X /opt/software/openGauss/cluster_config.xml"

# 3. Verify maximum number of standby servers in HA mode:
MAX_HA_STANDBY_SERVERS=___
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- `gs_preinstall` prepares and initializes the installation environment; `gs_install` performs the installation.
- In HA deployment (Ch.05, p.344), one primary server and at least 1 (up to 8) standby servers are deployed.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# 1. Initialize the openGauss installation environment (as root):
/opt/software/openGauss/script/gs_preinstall -U omm -G dbgrp -X /opt/software/openGauss/cluster_config.xml

# 2. Switch to omm and perform the openGauss installation:
su - omm -c "gs_install -X /opt/software/openGauss/cluster_config.xml"

# 3. Verify maximum number of standby servers in HA mode:
MAX_HA_STANDBY_SERVERS=8
```

#### Expected Console / Query Output:
```text
Parsing the configuration file.
Successfully checked OSivo status.
Preinstallation succeeded.
Installing the database...
Successfully started cluster.
Successfully installed application.
[OK] openGauss HA cluster deployed (gs_preinstall -> gs_install, supports 1 primary + up to 8 standby nodes).
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**During openGauss installation on openEuler (Ch.05, p. 345), which command is used to initialize and prepare the installation environment after decompressing the software package, and which command performs the actual installation?**

- A. gs_initdb (initialize environment) and gs_ctl (install)
- B. gs_preinstall (initialize environment) and gs_install (install)
- C. yum install (initialize environment) and rpm -ivh (install)
- D. gsql (initialize environment) and gs_om (install)

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.05 p.345, you use the `gs_preinstall` command to prepare/initialize the installation environment, and then use the `gs_install` command to install openGauss.
</details>

### Question 2 [Single-Choice]
**In openGauss High Availability (HA) deployment mode, how many primary and standby servers can be deployed?**

- A. Two primary servers and no standby servers
- B. One primary server and at least one (up to eight) standby servers
- C. One primary server and at most one standby server
- D. Up to 64 primary servers in a peer-to-peer ring

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.05 p.344, in HA deployment, one primary server and at least one (up to eight) standby servers are deployed.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about openGauss deployment modes and configuration files are true?**

- A. Standalone deployment is not recommended for production due to data loss risks.
- B. openGauss provides a script for deploying one database instance on a single server, while CLI commands are recommended if you need to deploy multiple database instances on a single server.
- C. The XML configuration file contains information about the server where openGauss will be deployed, including the installation path, IP address, and port.
- D. Setting the standby node to readable is an optional post-installation step to meet data consistency and read requirements.

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** All four statements come directly from Ch.05 pp. 344–345.
</details>
