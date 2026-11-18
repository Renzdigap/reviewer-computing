# 💻 Hands-On Lab: Server Form Factor, Timeline & ISA Verification

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 02 — Computing System Overview, System Software & Virtualization (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (7 mins) — Paired with `01-Lecture-Computing-System-Architecture-and-Server-Classification`  
**Interactive Workbench:** Open **[`02-Exercise-Server-Classification-and-Instruction-Set-Lab.html`](./02-Exercise-Server-Classification-and-Instruction-Set-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
Write a verification script that checks the chronological evolution of servers, rack unit dimensions, and instruction set mappings.

### 📋 Step-by-Step Instructions
1. Complete `server_timeline` in chronological order: `'mainframes'`, `'midrange'`, `'microcomputers'`, `'general-purpose'`.
2. Set `one_u_cm` to `4.45` and `rack_width_inches` to `19`.
3. Set `kunpeng_isa` to `'RISC'` and `first_standard_x86_server` to `'SystemPro'`.

### 📝 Starter Workspace (`python3@kunpeng-lab:~$`)
```bash
# Server Hardware & ISA Verification
server_timeline = ["mainframes", "___", "microcomputers", "___"]
one_u_cm = ___
rack_width_inches = ___
kunpeng_isa = "___"
first_standard_x86_server = "___"
print(server_timeline, one_u_cm, rack_width_inches, kunpeng_isa, first_standard_x86_server)
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Servers evolved from mainframes -> midrange -> microcomputers -> general-purpose servers.
- 1U is 4.45 cm (1.75 in) in a 19-inch (48.26 cm) cabinet; Compaq SystemPro was the first standard x86 server.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Server Hardware & ISA Verification
server_timeline = ["mainframes", "midrange", "microcomputers", "general-purpose"]
one_u_cm = 4.45
rack_width_inches = 19
kunpeng_isa = "RISC"
first_standard_x86_server = "SystemPro"
print(server_timeline, one_u_cm, rack_width_inches, kunpeng_isa, first_standard_x86_server)
```

#### Expected Console / Query Output:
```text
['mainframes', 'midrange', 'microcomputers', 'general-purpose'] 4.45 19 RISC SystemPro
[OK] Server timeline, 1U (4.45 cm) / 19-inch rack dimensions, and RISC ISA verified.
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [True / False]
**(Official Ch.02 Quiz Q1) Servers are developed from midrange computers to general-purpose servers and then to mainframe servers.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False. According to Ch.02 p.76 and p.124 Quiz Q1, servers evolved from Mainframes (1940s–1950s) -> Midrange computers (1960s–1970s) -> Microcomputers (1970s–1980s) -> General-purpose servers (1980s–1990s).
</details>

### Question 2 [Single-Choice]
**Which of the following statements about CISC and RISC processor instruction sets is FALSE?**

- A. CISC uses complex instructions of varying lengths and is beneficial for compiler development.
- B. RISC uses a simplified instruction set with fixed instruction length and has higher requirements on compiler design.
- C. Huawei Kunpeng processors use the Arm architecture based on RISC.
- D. Software compiled for the CISC architecture can run directly on a RISC platform without modification or translation.

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `D`
- **Explanation:** According to Ch.02 p.83, software developed based on the CISC architecture cannot directly run on a RISC platform (and vice versa) because instruction formats and encoding modes differ.
</details>

### Question 3 [Single-Choice]
**What are the standard height of 1U and the standard width of a data center rack cabinet?**

- A. 1U = 4.45 cm; cabinet width = 19 inches (48.26 cm)
- B. 1U = 2.54 cm; cabinet width = 24 inches (60.96 cm)
- C. 1U = 8.90 cm; cabinet width = 19 inches (48.26 cm)
- D. 1U = 4.45 cm; cabinet width = 10 inches (25.40 cm)

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** 1U is 1.75 inches (4.45 cm), 2U is 8.9 cm, 4U is 17.8 cm, and standard rack servers are installed in 19-inch (48.26 cm) cabinets (Ch.02, p.80).
</details>
