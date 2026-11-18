# Hands-On Lab: CPU Control Unit Registers & Kunpeng 920 SKU Inspector

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 03 — Server Hardware Architecture: CPU, Memory, Mainboard & Storage Drives (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (7 mins) — Paired with `01-Lecture-CPU-Architecture-Parameters-and-Multi-Socket-Topologies`  
**Interactive Workbench:** Open **[`02-Exercise-CPU-Instruction-Cycle-and-Kunpeng-920-SKU-Lab.html`](./02-Exercise-CPU-Instruction-Cycle-and-Kunpeng-920-SKU-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
Write a Python hardware inspection script that maps CPU Control Unit registers (PC, IR, ID, OC) and calculates clock cycle period and total physical cores on a 2-socket TaiShan 200 (2280) server.

### Step-by-Step Instructions
1. Set `next_instruction_address_register` to `'PC'` and `current_instruction_register` to `'IR'`.
2. Calculate `clock_period_ns_at_100mhz` as `10` (since 1 / 100 MHz = 10 ns).
3. Map the core counts for Kunpeng 920 models: `7260` -> `64`, `5250` -> `48`, `5220` -> `32`, `3210` -> `24`.

### Starter Workspace (`python3@taishan-2280:~$`)
```bash
# CPU Architecture & Kunpeng 920 SKU Verification
control_unit = {
    "next_instruction_address_register": "___",
    "current_instruction_register": "___",
    "decoder": "ID",
    "signal_generator": "OC"
}
clock_period_ns_at_100mhz = ___
kunpeng_920_cores = {
    "7260": ___,
    "5250": ___,
    "5220": ___,
    "3210": ___
}
print(control_unit, clock_period_ns_at_100mhz, kunpeng_920_cores)
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- PC (Program Counter) holds the address of the next instruction; IR (Instruction Register) holds the current instruction.
- Kunpeng 920 core counts on p. 141 are 64 (7260), 48 (5250), 32 (5220), and 24 (3210).

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# CPU Architecture & Kunpeng 920 SKU Verification
control_unit = {
    "next_instruction_address_register": "PC",
    "current_instruction_register": "IR",
    "decoder": "ID",
    "signal_generator": "OC"
}
clock_period_ns_at_100mhz = 10
kunpeng_920_cores = {
    "7260": 64,
    "5250": 48,
    "5220": 32,
    "3210": 24
}
print(control_unit, clock_period_ns_at_100mhz, kunpeng_920_cores)
```

#### Expected Console / Query Output:
```text
{'next_instruction_address_register': 'PC', 'current_instruction_register': 'IR', 'decoder': 'ID', 'signal_generator': 'OC'} 10 {'7260': 64, '5250': 48, '5220': 32, '3210': 24}
[OK] CPU Control Unit registers and Kunpeng 920 SKU table verified.
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**Within the Control Unit of a CPU, which component stores the memory address of the NEXT instruction to be executed, and which stores the instruction CURRENTLY being executed?**

- A. Instruction Register (next address) and Program Counter (current instruction)
- B. Program Counter (next address) and Instruction Register (current instruction)
- C. Instruction Decoder (next address) and Operation Controller (current instruction)
- D. ALU (next address) and L1 Cache (current instruction)

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.03 pp. 138 and 224, the Program Counter (PC) stores the memory address of the next instruction to be executed, while the Instruction Register (IR) stores the instruction currently being executed.
</details>

### Question 2 [Multiple-Choice (Select ALL)]
**Which of the following are the four basic functions of a CPU defined in Chapter 03 (p. 139)?**

- A. Instruction control
- B. Operation control
- C. Time control
- D. Data processing
- E. Permanent nonvolatile storage

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** The four basic functions of a CPU are Instruction control, Operation control, Time control, and Data processing (Ch.03, p.139).
</details>

### Question 3 [Single-Choice]
**How many cores and what clock frequency does a single Kunpeng 920 5250 processor provide in a TaiShan 200 (model 2280) server?**

- A. 64 cores at 2.6 GHz
- B. 48 cores at 2.6 GHz
- C. 32 cores at 2.6 GHz
- D. 24 cores at 2.6 GHz

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** On a TaiShan 200 (model 2280), Kunpeng 920 7260 = 64-core 2.6 GHz, 5250 = 48-core 2.6 GHz, 5220 = 32-core 2.6 GHz, and 3210 = 24-core 2.6 GHz (Ch.03, p.141).
</details>
