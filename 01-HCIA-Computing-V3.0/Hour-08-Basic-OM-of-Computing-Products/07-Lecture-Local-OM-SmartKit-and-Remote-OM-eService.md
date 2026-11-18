# Local O&M (SmartKit) & Remote O&M (eService / Call Home)

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 08 — Basic O&M of Computing Products: iBMA, iBMC, Smart Provisioning, FusionDirector, eSight, SmartKit & eService (Sprint 4 of 4)  
**Format:** Bite-Sized Lecture (8 mins) → Followed immediately by `08-Exercise-SmartKit-and-eService-Call-Home-Scenario-Lab` (8 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.06, pp. 415–443

---

## Learning Objectives
- Master SmartKit's features (50 parallel tasks, plugin-based, white-box customizable), 4-step local O&M process, and 6 O&M scenarios
- Understand SmartKit IP/IES config (link-local L2 restriction), 2 OS deployment channels, Atlas CANN deployment, Burn-in test (V5/TS200 via SP vs. V3 via FTK.iso), and In-band vs. Out-of-band firmware upgrade
- Master eService Remote O&M functions (Remote Inspection, Log Collection, Fault Diagnosis FMA, Health Evaluation, Call Home) and solve Ch.06 Quiz Q1!

---

### 1. SmartKit: Local O&M Toolbox for Service Engineers (pp. 416–420)
**SmartKit** is Huawei's lightweight, wizard-based, plugin-based local O&M toolbox installed on **frontline engineers' laptops**, supporting FusionServer, Kunpeng/TaiShan, Atlas, storage, machine vision, and cloud products:
- **Key Highlights (pp. 416, 418)**: Processes **up to 50 tasks in parallel**, supports **online updates** from **HOUP**, interconnects with **eService**, and supports **white-box customization** for Kunpeng OEM/ecosystem partners.
- **Four-Step SmartKit Local O&M Process (p. 417)**:
  1. **Prepare**: Upgrade tool to latest version, prepare O&M documents (firmware, drivers, templates, scripts, operation guides).
  2. **Authorize & Connect**: **Obtain customer authorization**, suspend services & back up data if needed, connect to network, and **add devices**.
  3. **Configure**: Obtain device information and set task parameters.
  4. **Execute & Restore**: Execute the task and restore customer services.
- **Six SmartKit Scenarios & Sub-Functions (p. 419)**:
  1. **Device Management**: Add/manage **iBMC, HMM, OS, CMC, IES, TCE** (prerequisite for all other functions).
  2. **Site Deployment Delivery**: **IP address configuration**, **IES configuration** (Atlas 500), **Hardware configuration** (iBMC, BIOS, RAID, HMM), **OS deployment**, One-click site deployment, **Atlas batch deployment**.
  3. **Routine Maintenance**: **Health check** (formerly **"inspection" in uMate**), **Power control**, **Configuration check** (compares against a **baseline device** or **baseline file**).
  4. **Troubleshooting**: **Log collection** (One-click, E9000/TCE custom, or **OS log collection script package** when customer denies service network access), **Burn-in test**, **Hardware diagnosis**, **Device repair**.
  5. **Upgrade / Patch Installation**: **Firmware upgrade**, E9000/TCE upgrade, Device change, **Software package management** (creates local HOUP repositories), Server bundle upgrade, **Batch distribution** (delivers **IPMI, SNMP, Redfish, SSH commands, and files** in batches).
  6. **Parts Replacement**: **Electronic label (ELabel) modification**.

---

### 2. Deep-Dive into Key SmartKit Functions (pp. 421–432)
- **IP Address & IES Configuration (pp. 421–422)**:
  - *Scenario 1*: Configure new IPv4/IPv6/hostname (or Atlas 500 partition/IEF certificate in IES) using known **MAC address or SN** (*Note*: Uses **link-local address**, so **PC and server CANNOT be connected across routes / L3**!).
  - *Scenario 2*: Configure new IP using known **IPv4/IPv6 address** (supports cross-route L3 connection).
- **Two SmartKit OS Deployment Channels (p. 424)**: Deploys OSs in batches over the **management network** (no PXE server or service network required!):
  1. **Onboard Smart Provisioning**: Deploys the **OS and driver at the same time**.
  2. **Direct deployment through image mounting**: **Faster speed** and independent of Smart Provisioning, **but you must install the driver separately after installing the OS**.
- **Atlas Batch Deployment (p. 425)**: Connects to the **service plane (OS) via SSH** to deploy **CANN** software for Atlas series products.
- **Burn-In Test (p. 429)**: Stress-tests **CPU, memory, and disks** after installation to detect transport damage:
  - **V5 and TaiShan 200 servers**: Use **iBMC to deliver commands to Smart Provisioning** for stress tests.
  - **V3 servers**: Mount **`FTK.iso`** (*FusionServer Tools Toolkit*) through iBMC for stress tests.
- **Firmware Upgrade Classification (p. 430)**:
  - **Out-of-band parts**: **iBMC, BIOS, and Smart Provisioning** (upgraded directly via iBMC).
  - **In-band firmware**: **PCIe card firmware and drive firmware** (upgraded after entering the service OS or external mini-memory system).

---

### 3. eService: 24/7 Remote O&M Platform & Call Home (pp. 433–438 — Official Quiz Q1!)
**eService** provides remote O&M for customers via **eServiceClient** deployed in the customer's equipment room (backed by SQL/NoSQL + HDFS + Elasticsearch + DataCompass):
- **Four Core eService Functions (pp. 435–437)**:
  1. **Remote Inspection and Log Collection**: 24/7 secure remote inspection and log package collection.
  2. **Fault Diagnosis (FMA)**: Analyzes device faults and risks based on collected logs.
  3. **Health Evaluation**: Outputs device health reports based on logs or inspection reports.
  4. **Call Home (p. 437)**: Automatic fault reporting method that **automatically sends hardware alarms** generated by Huawei devices via `eServiceClient` to the **Huawei technical support center**, **automatically creates trouble tickets**, and pushes expert inspection reports within hours.
- **Official Ch.06 Quiz Q1 (p. 438)**: Which tools can configure RAIDs on bare-metal TaiShan 200 (2280) servers during project delivery?
  - **Answer: `ABC` — A. Smart Provisioning, B. SmartKit, C. iBMC!** (**D. eService** is for remote monitoring/inspection/Call Home and **cannot** configure RAID!).

---

## Key Takeaways
- **SmartKit runs on engineers' laptops, processes up to 50 parallel tasks, and covers 6 scenarios: Device Management, Site Deployment Delivery, Routine Maintenance, Troubleshooting, Upgrade/Patch Installation, and Parts Replacement (Electronic label modification).**
- **SmartKit OS deployment uses the management network via two channels: (1) Onboard Smart Provisioning (deploys OS + driver simultaneously) or (2) Direct image mounting (faster, independent of SP, install driver after OS).**
- **SmartKit Burn-in Test stress-tests CPU, memory, and disk: V5/TaiShan 200 uses Smart Provisioning, whereas V3 mounts FTK.iso.**
- **Out-of-band firmware includes iBMC, BIOS, and Smart Provisioning; In-band firmware includes PCIe card firmware and drive firmware.**
- **To configure RAID on bare-metal TaiShan 200 2280 servers, you can use Smart Provisioning, SmartKit, or iBMC (ABC) — NOT eService (Ch.06 Quiz Q1)!**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.06 Quiz Q1): eService is a remote O&M platform (Remote Inspection, Log Collection, Fault Diagnosis, Health Evaluation, Call Home automatic trouble ticket creation) — it CANNOT configure RAID or install OSs on bare-metal servers! Only Smart Provisioning (A), SmartKit (B), and iBMC (C) can configure RAID.

> [!WARNING]
> EXAM TRAP: When SmartKit configures device IP addresses based on MAC address or SN (Scenario 1, pp. 421–422), it uses link-local addresses, so the PC and server CANNOT be connected across routes!

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`08-Exercise-SmartKit-and-eService-Call-Home-Scenario-Lab.html`](./08-Exercise-SmartKit-and-eService-Call-Home-Scenario-Lab.html)** (or [`08-Exercise-SmartKit-and-eService-Call-Home-Scenario-Lab.md`](./08-Exercise-SmartKit-and-eService-Call-Home-Scenario-Lab.md)) to apply this concept in an interactive lab workbench!
