# 💻 Hands-On Lab: Computing Evolution & Architecture Milestones Verification

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 01 — History of Computing & Industry Trends (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `01-Lecture-Primitive-Mechanical-and-Electronic-Computing`  
**Interactive Workbench:** Open **[`02-Exercise-Computing-Eras-and-Generations-Lab.html`](./02-Exercise-Computing-Eras-and-Generations-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
You are preparing a verification script for the Huawei ICT Competition Computing Track study group that validates historical computing milestones, vacuum tube physics, and electronic computer generation specs.

### 📋 Step-by-Step Instructions
1. Set `quipu_largest_place` to `'tens_of_thousands'` (the knot closest to the horizontal string in Inca Quipu).
2. Set `first_general_electronic_computer` to `'ENIAC'` and `first_microcomputer` to `'Altair 8800'` (powered by `'Intel 8080'`).
3. Set `software_hardware_separation_system` to `'IBM System/370'` and `sunway_peak_pflops` to `120`.

### 📝 Starter Workspace (`python3@kunpeng-lab:~$`)
```bash
# Complete the historical milestone dictionary for HCIA-Computing Ch.01:
milestones = {
    "quipu_largest_place": "___",
    "first_electronic_computer_1937": "ABC",
    "first_general_electronic_computer": "___",
    "first_transistor_computer_1954": "TRADIC",
    "software_hardware_separation_system": "___",
    "first_microcomputer": "___",
    "sunway_peak_pflops": ___
}
print(milestones)
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Inca Quipu knots closest to the horizontal cord represent the tens of thousands place.
- ENIAC (1946) was the first general-purpose programmable electronic computer; MITS Altair 8800 was the first microcomputer.
- IBM System/370 (1970) introduced virtual memory and separated software from hardware.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Complete the historical milestone dictionary for HCIA-Computing Ch.01:
milestones = {
    "quipu_largest_place": "tens_of_thousands",
    "first_electronic_computer_1937": "ABC",
    "first_general_electronic_computer": "ENIAC",
    "first_transistor_computer_1954": "TRADIC",
    "software_hardware_separation_system": "IBM System/370",
    "first_microcomputer": "Altair 8800",
    "sunway_peak_pflops": 120
}
print(milestones)
```

#### Expected Console / Query Output:
```text
{'quipu_largest_place': 'tens_of_thousands', 'first_electronic_computer_1937': 'ABC', 'first_general_electronic_computer': 'ENIAC', 'first_transistor_computer_1954': 'TRADIC', 'software_hardware_separation_system': 'IBM System/370', 'first_microcomputer': 'Altair 8800', 'sunway_peak_pflops': 120}
[OK] All Computing Era milestones verified against HCIA-Computing V3.0 Ch.01.
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Multiple-Choice (Select ALL)]
**(Official Ch.01 Quiz Q2) Which of the following places can be represented in the knot counting method of the Inca people?**

- A. Hundreds
- B. Tens of hundreds
- C. Hundreds of thousands
- D. Thousands

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `ABD`
- **Explanation:** In the Inca Quipu knot counting method (Ch.01 p.10 & p.62 Quiz Q2), knots represent Ones (farthest), Tens, Hundreds, Thousands, and Tens of thousands (written as 'Tens of hundreds' in option B of the official quiz). 'Hundreds of thousands' (C) exceeds the Quipu place limit.
</details>

### Question 2 [Single-Choice]
**Which electronic device was invented by Lee de Forest in 1906 by adding a fence-shaped third electrode to control current and amplify signals, serving as a high-speed switch for early electronic computers?**

- A. Vacuum diode
- B. Vacuum triode
- C. Germanium transistor
- D. Monolithic silicon IC

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** John Ambrose Fleming invented the vacuum diode in 1904 based on the Edison effect. In 1906, Lee de Forest added a third fence-shaped electrode to create the vacuum triode, which amplifies electrical signals and functions as a fast electronic switch (Ch.01, p.22).
</details>

### Question 3 [True / False]
**ENIAC (1946) was the world's first electronic digital computer, whereas the Atanasoff-Berry Computer (ABC) was the second electronic computer.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False. According to Ch.01 p.23, the Atanasoff–Berry Computer (ABC, 1937) is the world's first electronic computer (designed to solve linear equations), while ENIAC (1946) is the second electronic computer and the first general-purpose programmable electronic computer.
</details>
