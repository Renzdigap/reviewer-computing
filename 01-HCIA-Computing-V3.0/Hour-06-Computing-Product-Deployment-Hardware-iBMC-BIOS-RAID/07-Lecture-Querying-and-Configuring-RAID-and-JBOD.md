# Querying & Configuring RAID and JBOD (BIOS & iBMC WebUI)

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 06 — Computing Product Deployment: Equipment Room, iBMC, BIOS & RAID Configuration (Sprint 4 of 4)  
**Format:** Bite-Sized Lecture (8 mins) - Followed immediately by `08-Exercise-Avago-MegaRAID-9460-and-iBMC-Storage-Lab` (8 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.05, pp. 318–325

---

## Learning Objectives
- Query RAID controller card models on iBMC (`System > System Info > Others`) and understand Avago MegaRAID SAS 9460-8i drive/span limits
- Explain JBOD (Just a Bunch of Drives) drive passthrough
- Configure hardware RAID via VNC/BIOS (`Advanced > Avago MegaRAID > Main Menu > Configuration Management > Create Virtual Drive`) and via iBMC WebUI (`System > Storage Management`)

---

### 1. Querying RAID Info & Avago MegaRAID SAS 9460-8i Specifications (pp. 319–320)
- **Querying RAID Card Model in iBMC WebUI (p. 319)**: Choose **`System > System Info`**, then click the **`Others`** tab page to view the model of the RAID controller card.
- **Avago MegaRAID SAS 9460-8i Supported RAID Levels & Drive Quantities (p. 320)**:
  - **RAID 00 is NOT supported!**

| RAID Level | Total Drives Supported | Spans | Drives per Span | Allowed Failed Drives (p. 320) |
| :--- | :--- | :---: | :---: | :--- |
| **RAID 0** | **1 to 32** | N/A | N/A | **0** |
| **RAID 1** | **Even numbers from 2 to 32** | N/A | N/A | **Half the number of drives** |
| **RAID 5** | **3 to 32** | N/A | N/A | **1** |
| **RAID 6** | **3 to 32** (controller table) | N/A | N/A | **2** |
| **RAID 10** | **Even numbers from 4 to 240** | **2 to 8** RAID 1 | Even numbers **2 to 32** | **Number of spans** (1 per span) |
| **RAID 50** | **6 to 240** | **2 to 8** RAID 5 | **3 to 32** | **Number of spans** (1 per span) |
| **RAID 60** | **6 to 240** | **2 to 8** RAID 6 | **3 to 32** | **Twice the number of spans** (2 per span) |

---

### 2. JBOD Drive Passthrough (p. 321)
- **JBOD (*Just a Bunch of Drives*, pp. 321, 349)**: Also known as **drive passthrough** or **transparent transmission**.
- **Mechanism**: Bypasses RAID array processing so the RAID controller card transmits user commands directly to connected physical drives, allowing upper-layer services, SDS (like Ceph/FusionStorage), or OS installers to directly access raw physical drives.
- **OS Installation Impact**: If a RAID controller card **does NOT support passthrough (JBOD)**, you **cannot** install an OS directly on raw physical drives mounted to the card — you **must first configure a virtual drive (RAID)** under the controller card!

---

### 3. Configuring RAID via VNC (BIOS) and via iBMC WebUI (pp. 322–325)
- **Method 1 — Using VNC / BIOS Configuration Utility (pp. 322–323)**:
  1. In BIOS **`Advanced`** tab, select the Avago RAID controller card \rightarrow **`Main Menu > Configuration Management > Create Virtual Drive`**.
  2. Configure parameters:
     - **Select RAID Level** (e.g., RAID 1)
     - **Select Drives From**: **`Unconfigured Capacity`** (free drives not in any virtual drive) or **`Free Capacity`** (unused space in an existing drive group)
     - **Select Drives**: Use arrow keys and **`Space` bar** to select member drives \rightarrow **`Apply Changes`**
     - **Access Policy**: **`Read/Write`**, **`Read Only`**, or **`Blocked`**
- **Method 2 — Using iBMC WebUI (pp. 324–325)**:
  1. Choose **`System > Storage Management`**, expand **`PCIe Card`**, and click **`Add`** next to the RAID card to open **Create Logical Drive**.
  2. Example (p. 325): Set **Name** = `Data`, **Initialization State** = `Quick Init`, **RAID Level** = `5`. With **four 8 TB SATA HDDs** installed, each 8 TB decimal HDD has an actual binary available capacity of about **`7.2 TB`** in Storage Management (so a 4-drive RAID 5 provides 3 × 7.2 TB ≈ 21.6 TB).

---

## Key Takeaways
- **View the RAID controller card model in iBMC WebUI under System > System Info > Others; configure RAID in iBMC WebUI under System > Storage Management.**
- **Avago MegaRAID SAS 9460-8i supports up to 32 drives for single arrays (RAID 0/1/5/6) and up to 240 drives across 2 to 8 spans for spanned arrays (RAID 10/50/60). RAID 00 is NOT supported.**
- **JBOD (Just a Bunch of Drives) is drive passthrough. If a RAID card does NOT support passthrough, you can only install an OS on virtual drives (RAID volumes) configured on the card.**
- **In the BIOS RAID utility (Advanced > Avago MegaRAID > Main Menu > Configuration Management > Create Virtual Drive), press the Space bar to select drives, and note that an 8 TB decimal HDD shows ~7.2 TB actual capacity.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: If a RAID controller card does not have JBOD (passthrough) enabled or supported, the OS installer will see ZERO disks until you create a Virtual Drive / Logical Drive!

> [!WARNING]
> EXAM TRAP: In the BIOS RAID utility, 'Unconfigured Capacity' refers to free physical drives not added to any virtual drive, whereas 'Free Capacity' refers to unused space within an existing drive group (p. 322).

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`08-Exercise-Avago-MegaRAID-9460-and-iBMC-Storage-Lab.html`](./08-Exercise-Avago-MegaRAID-9460-and-iBMC-Storage-Lab.html)** (or [`08-Exercise-Avago-MegaRAID-9460-and-iBMC-Storage-Lab.md`](./08-Exercise-Avago-MegaRAID-9460-and-iBMC-Storage-Lab.md)) to apply this concept in an interactive lab workbench!
