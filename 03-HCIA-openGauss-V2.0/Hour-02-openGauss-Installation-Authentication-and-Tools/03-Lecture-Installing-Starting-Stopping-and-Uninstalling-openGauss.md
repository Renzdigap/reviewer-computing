# Installing (`install.sh` / `gs_preinstall` / `gs_install`), Starting/Stopping & Uninstalling openGauss

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 02 — openGauss Installation, Authentication & O&M Tools (Sprint 2 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `04-Exercise-Installation-Lifecycle-and-Uninstallation-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.02, pp. 82–94, 124–127

---

## Learning Objectives
- Verify all 4 official prerequisites for single-node openGauss installation (Ch.02 Quiz Q3)
- Execute both Simplified Single-Node Installation (`sh install.sh -w`) and Standard Enterprise XML Installation (`gs_preinstall` + `gs_install`)
- Start and stop openGauss (`gs_om -t start/stop`) and cleanly uninstall (`gs_uninstall --delete-data` + `gs_postuninstall`)

---

### 1. Single-Node Installation Prerequisites & Procedure (pp. 92–93, Ch.02 Quiz Q3!)
Before installing openGauss on a single node, **four prerequisites** must be met (exact **Ch.02 Quiz Q3: ABCD**):
1. **Users & OS/Network**: A user group and a common user have been created, and all server OSs and networks are functioning properly.
2. **Directory Permissions**: Common users must have **read, write, and execute (`rwx`)** permissions on the database package decompression directory and installation directory, and the **installation directory must be empty**.
3. **Package Permission**: Common users have the **execution permission** for the downloaded openGauss package.
4. **Port Check**: Before installation, check whether the specified openGauss port is occupied. If occupied, change the port number or stop the process using the port.

#### Simplified Single-Node Installation Procedure (`simpleInstall/install.sh`):
```bash
# 1. Decompress as common user (omm)
tar -jxf openGauss-2.0.0-openEuler-64bit.tar.bz2 -C /opt/software/openGauss
# 2. Go to simpleInstall directory and run install.sh
cd /opt/software/openGauss/simpleInstall
sh install.sh -w Huawei@123 -p 5432
```
- **`-w`**: Initializes the database password (passed to `gs_initdb`). **Mandatory** for security!
- **`-p`**: Specifies the openGauss port (**default is `5432`** if not specified).
- After installation, the default instance name is **`sgnode`**, and the data directory is `/opt/software/openGauss/data/single_node`.
- **Verification**:
  - `ps ux | grep gaussdb`
  - `gs_ctl query -D /opt/software/openGauss/data/single_node` (shows `local_role: Normal`, `db_state: Normal`).

---

### 2. Standard Enterprise XML Installation & Start/Stop Lifecycle (pp. 82, 94)
1. **Standard Flow**: Prepare OS -> Obtain package -> Configure **XML file** -> Decompress -> Run **`gs_preinstall`** (as `root` to initialize environment, check permissions, and create `omm`/`dbgrp`) -> Switch to `omm` and run **`gs_install -X clusterconfig.xml`** -> (Optional) Set standby node to readable.
2. **Starting and Stopping openGauss (as `omm`)**:
   - **Start cluster**: `gs_om -t start` (default timeout is **300s**; customize via `gs_om -t start --time-out=300`).
   - **Stop cluster**: `gs_om -t stop`
   - *Note*: An HA cluster must be started in HA mode. If started in standalone mode, restore the HA relationship using `gs_ctl build`.

---

### 3. Uninstalling openGauss & Cleaning Up the Environment (pp. 124–125)
Uninstallation is a two-phase process:
1. **Phase 1 — Uninstall openGauss Application (as OS user `omm`)**:
   - Cluster-wide uninstallation: `gs_uninstall --delete-data`
   - Local single-node uninstallation: `gs_uninstall --delete-data -L`
   - Logs are saved to `$GAUSSLOG/om/gs_uninstall-YYYY-MM-DD_HHMMSS.log`.
2. **Phase 2 — One-Click Environment Cleanup (as user `root` ONLY)**:
   - Run **`gs_postuninstall -U omm -X clusterconfig.xml --delete-user --delete-group`** to clean up the OS environment settings made by `gs_preinstall`.

---

## Key Takeaways
- **All 4 items in Ch.02 Quiz Q3 (user/group & OS/network, rwx on decompression & empty install dir, execute permission on package, and checking if the port is occupied) are mandatory prerequisites for single-node installation.**
- **In simplified single-node installation (`sh install.sh -w <password>`), `-w` is mandatory, `-p` defaults to 5432, the database name is `sgnode`, and the data directory is `data/single_node`.**
- **Uninstallation requires `gs_uninstall --delete-data` run as `omm`, followed by `gs_postuninstall` run as `root`.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.02 Quiz Q3): All four options (A, B, C, D) are correct prerequisites for installing openGauss on a single node!

> [!WARNING]
> EXAM TRAP: Only `root` is authorized to run `gs_preinstall`, `gs_checkos`, and `gs_postuninstall`, whereas `omm` runs `gs_install`, `gs_om`, and `gs_uninstall`.

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`04-Exercise-Installation-Lifecycle-and-Uninstallation-Lab.html`](./04-Exercise-Installation-Lifecycle-and-Uninstallation-Lab.html)** (or [`04-Exercise-Installation-Lifecycle-and-Uninstallation-Lab.md`](./04-Exercise-Installation-Lifecycle-and-Uninstallation-Lab.md)) to apply this concept in an interactive lab workbench!
