# Hands-On Lab: Redfish RESTful Operations & SNMP/iBMC Diagnostic Check

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 04 — RAID Arrays, PCIe Bus, NICs/iNICs, GPU/NPU, Power/Cooling & Server Software (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (7 mins) — Paired with `05-Lecture-Server-Management-Protocols-IPMI-Redfish-SNMP-and-iBMC`  
**Interactive Workbench:** Open **[`06-Exercise-Redfish-RESTful-API-and-SNMP-Architecture-Lab.html`](./06-Exercise-Redfish-RESTful-API-and-SNMP-Architecture-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You are configuring out-of-band server management using Redfish HTTPS calls and verifying SNMP and iBMC Kbox parameters.

### Step-by-Step Instructions
1. Complete the `curl` command using the HTTPS protocol and `GET` method to query the Redfish `/redfish/v1/Systems` endpoint on iBMC.
2. Specify the four Redfish HTTP methods (`GET, POST, PATCH, DELETE`) in the verification variable.
3. Specify the iBMC black box name (`Kbox`) and its parsing tool (`HWKbox`).

### Starter Workspace (`admin@mgmt-station:~#`)
```bash
# 1. Query Redfish Systems endpoint via HTTPS GET:
curl -k -X ___ https://192.168.2.100/redfish/v1/Systems -u Administrator:Admin@9000

# 2. Verify Redfish methods & iBMC Black Box tools:
REDFISH_METHODS="GET, POST, ___, ___"
IBMC_BLACKBOX="___"
IBMC_PARSER="___"
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Redfish uses GET, POST, PATCH, and DELETE over HTTPS.
- On page 202, the iBMC black box is Kbox and the parsing tool is HWKbox.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# 1. Query Redfish Systems endpoint via HTTPS GET:
curl -k -X GET https://192.168.2.100/redfish/v1/Systems -u Administrator:Admin@9000

# 2. Verify Redfish methods & iBMC Black Box tools:
REDFISH_METHODS="GET, POST, PATCH, DELETE"
IBMC_BLACKBOX="Kbox"
IBMC_PARSER="HWKbox"
```

#### Expected Console / Query Output:
```text
{
  "@odata.context": "/redfish/v1/$metadata#ComputerSystemCollection.ComputerSystemCollection",
  "@odata.id": "/redfish/v1/Systems",
  "Name": "Computer System Collection",
  "Members": [{"@odata.id": "/redfish/v1/Systems/1"}]
}
[OK] Redfish HTTPS RESTful API (GET/POST/PATCH/DELETE) and iBMC Kbox/HWKbox verified.
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [True / False]
**(Official Ch.03 Quiz Q2) The baseboard management controller (BMC) complies with the Intelligent Platform Management Interface (IPMI) specification. It collects, processes, and stores sensor signals, and monitors the operating status of components.**

- A. True
- B. False

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** True. This is the exact definition of the BMC in Ch.03 p.201 and Official Quiz Q2 on p.220.
</details>

### Question 2 [Single-Choice]
**Which standard organization maintains the Redfish specification, and which four HTTP operations are registered by the Redfish service in iBMA/iBMC?**

- A. IEEE; GET, PUT, CONNECT, TRACE
- B. DMTF; GET, POST, PATCH, DELETE
- C. IETF; SNMP-GET, SNMP-SET, TRAP, WALK
- D. NIST; SELECT, INSERT, UPDATE, DELETE

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.03 pp. 194 and 196, DMTF (www.dmtf.org) maintains Redfish, and the Redfish service provides GET, POST, PATCH, and DELETE operations over HTTPS.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following are the four basic components of the Simple Network Management Protocol (SNMP) architecture?**

- A. Network Management System (NMS)
- B. Agent process
- C. Managed Object (MO)
- D. Management Information Base (MIB)
- E. Serial Presence Detect (SPD)

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** According to Ch.03 p.198, basic SNMP components include the NMS, agent process, managed object (MO), and management information base (MIB).
</details>
