# 📖 Server Protocols (IPMI, Redfish, SNMP), iBMA & Huawei iBMC

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 04 — RAID Arrays, PCIe Bus, NICs/iNICs, GPU/NPU, Power/Cooling & Server Software (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `06-Exercise-Redfish-RESTful-API-and-SNMP-Architecture-Lab` (7 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.03, pp. 191–202, 220

---

## 🎯 Learning Objectives
- Trace the evolution of IPMI (1.0 -> 1.5 -> 2.0) and understand how BMC uses IPMI independently of the OS (Ch.03 Quiz Q2!)
- Master Redfish HTTPS/RESTful interfaces (GET, POST, PATCH, DELETE) and iBMA 2.0 in-band/out-of-band BOB mapping
- Explain SNMP architecture (NMS, Agent, MO, MIB over UDP) and Huawei iBMC (Hi1710, Kbox/HWKbox)

---

### 1. IPMI & Baseboard Management Controller (BMC) (pp. 193, 201–202 — Official Quiz Q2!)
- **IPMI (Intelligent Platform Management Interface, p. 193)**: Open-standard hardware management interface specification created by **Intel, HP, NEC, Dell, and SuperMicro** that operates **independently of the OS** via the **BMC**:
  - **1998 (IPMI 1.0)**: Remote monitoring of temperature and voltage over the network.
  - **2001 (IPMI 1.5)**: Added **PCI Management Bus** function.
  - **2004 (IPMI 2.0)**: Backward compatible with 1.0/1.5; added **Console Redirection (Serial over LAN)**, remote management via ports/modems/LANs, enhanced security, **VLAN**, and **blade server support**.
- **BMC & Huawei iBMC (pp. 201–202 — Ch.03 Quiz Q2!)**:
  - The **BMC** uses the **IPMI specification** to collect, process, and store sensor signals, and monitor the operating status of components.
  - **Huawei iBMC** runs on the Huawei-developed **Hi1710** management chip and provides **CLI, WebUI, IPMI, SNMP, and Redfish** interfaces:
    - **Status monitoring**: CPU, memory, drive, SSD, PCIe, RAID, fan, PSU, temperature, voltage.
    - **Fault diagnosis**: CPU CATERR event, PSU failure, overtemperature alarm, sub-healthy fan, storage medium fault.
    - **Running records**: Power-on/off recording, serial port voice/data recording, breakdown screenshot & breakdown video recording.
    - **Diagnosis assistance**: Black box (**Kbox**) and parsing tool (**HWKbox**).

---

### 2. Redfish & iBMA 2.0 Architecture (pp. 194–196)
- **Redfish (p. 194)**: Maintained by **DMTF (`www.dmtf.org`)** to solve security and horizontal-scalability limitations of IPMI. Based on **HTTPS/SSL** and uses **RESTful APIs** (`JSON`).
- **Four Redfish HTTP Operations & Plugin Methods (p. 196)**:
  - `GET` \rightarrow `getAllInfo` (query resources)
  - `POST` \rightarrow `postRequest` (create/action)
  - `PATCH` \rightarrow `patchRequest` (update/modify parameters)
  - `DELETE` \rightarrow `deleteRequest` (remove resource)
- **iBMA 2.0 (In-Band Management Agent, p. 195)**: Runs inside the host OS to obtain in-band metrics unavailable to out-of-band BMC (process info, CPU performance, RAID controller details) and integrates with **iBMC** via **vNIC** and **BOB** (*Baseboard Management Controller Out-of-Band*).

---

### 3. Simple Network Management Protocol (SNMP) (pp. 197–200)
SNMP is an application-layer TCP/IP network management protocol carried over **UDP packets** using a polling + trap notification model:
- **Four Basic SNMP Components (p. 198)**:
  1. **NMS (Network Management System)**: Runs on NMS servers; sends `GET`/`SET` requests to agents and receives **Traps**.
  2. **Agent**: Process running on the managed device; queries/updates the **MIB** and sends **Traps** when faults/events occur.
  3. **Managed Object (MO)**: Hardware or software configuration parameters on a managed device (one device can have multiple MOs).
  4. **MIB (Management Information Base)**: Hierarchical database schema defining the variables maintained by the agent.

---

## 🔑 Key Takeaways
- **IPMI evolution: 1998 (v1.0), 2001 (v1.5, PCI Management Bus), 2004 (v2.0, Console Redirection, VLAN, Blade server support).**
- **BMC complies with the IPMI specification to collect, process, and store sensor signals and monitor component status independently of the OS (Ch.03 Quiz Q2).**
- **Redfish (DMTF) uses HTTPS RESTful APIs supporting GET (getAllInfo), POST (postRequest), PATCH (patchRequest), and DELETE (deleteRequest).**
- **SNMP runs over UDP and consists of 4 basic components: NMS, Agent, Managed Object (MO), and MIB.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: SNMP packets are carried over UDP (User Datagram Protocol), whereas Redfish is based on HTTPS/SSL (TCP)!

> [!WARNING]
> EXAM TRAP: In Huawei iBMC diagnosis assistance, the black box is called 'Kbox' and its parsing tool is called 'HWKbox'.

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-Redfish-RESTful-API-and-SNMP-Architecture-Lab.html`](./06-Exercise-Redfish-RESTful-API-and-SNMP-Architecture-Lab.html)** (or [`06-Exercise-Redfish-RESTful-API-and-SNMP-Architecture-Lab.md`](./06-Exercise-Redfish-RESTful-API-and-SNMP-Architecture-Lab.md)) to apply this concept in an interactive lab workbench!
