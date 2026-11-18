# 📖 Primitive, Mechanical, and Electronic Computing Eras

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 01 — History of Computing & Industry Trends (Sprint 1 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `02-Exercise-Computing-Eras-and-Generations-Lab` (8 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.01, pp. 5–28

---

## 🎯 Learning Objectives
- Trace computing tools from digits, stones, Inca Quipu knotted strings, counting rods, abacus, and Napier's Bones to logarithmic slide rules
- Understand mechanical calculators including Blaise Pascal's Pascaline (sautoir carry mechanism) and Dorr Eugene Felt's Comptometer
- Differentiate the four generations of electronic computers, Edison effect, Fleming's vacuum diode, Lee de Forest's vacuum triode, ABC, ENIAC, TRADIC, Altair 8800, Apple II/Lisa, and supercomputers

---

### 1. Primitive Computing Era (pp. 8–15)
Computing is the process of symbol transformation based on mathematical rules. As human counting demands exceeded fingers/toes (digits) and stones, specialized tools emerged:

| Tool | Historical Period / Inventor | Key Mechanism & Exam Facts |
| :--- | :--- | :--- |
| **Knotted Strings (Quipu)** | Ancient Inca (South America) | Woven alpaca/llama hair strings tied to a thicker horizontal string. Place value is determined by distance from the horizontal string: **farthest = Ones place**, **closest = Tens of thousands place (largest)** — covers Ones, Tens, Hundreds, Thousands, and Tens of thousands (**Tens of hundreds** in Ch.01 Quiz Q2). |
| **Tally Sticks & Counting Rods** | Spring & Autumn / Warring States (770–221 BCE), Han to Sui Dynasties | Bamboo sticks; **Ones place = vertical**, **Tens place = horizontal**, **Hundreds = vertical** (alternating vertical and horizontal). Changed from round (0.23 cm × 14 cm in Han) to triangular/quadrangular for positive/negative numbers and shorter (0.59 cm × 8.85 cm in Sui). |
| **Abacus** | Pre-Arabic numerals to modern era | Fast arithmetic (addition, subtraction, multiplication, division, exponentiation, root extraction) using bead manipulation rules. |
| **Napier's Bones (1617)** | John Napier (*Rabdologiae*) | A board (left border marked 1–9) and **10 rods** (top marked 0–9, nine front squares split by a diagonal line separating tens and ones places). Replaces multi-digit multiplication with addition and single-digit multiplication (and division with subtraction). |
| **Logarithms & Slide Rule** | John Napier & Henry Briggs | Napier invented logarithms (*Mirifici Logarithmorum Canonis Descriptio*); **Henry Briggs** compiled the first base-10 logarithm table ($\lg X$). Combining two logarithmic scales created linear and circular **slide rules**. |

---

### 2. Mechanical Computing Era (pp. 16–18)
- **Pascal's Adder (Pascaline)**: Invented by French mathematician **Blaise Pascal**. Uses rotary dials for input and small windows above dials for output. Its centerpiece carry mechanism is the **sautoir**, which carries `1` to the next dial when a dial transitions from `9` to `0`. Early models only performed addition; later editions performed subtraction by reversing dial rotation. Marks the transition from **manual to automatic** computing tools.
- **Key-Driven Calculator (Comptometer, 1886)**: Invented by American engineer **Dorr Eugene Felt**. Resembles a typewriter in a square box with a clearing handle on the right. Each key displays two numbers whose **sum is 9**: the **larger number** is used for addition/multiplication, and the **smaller number** (9's complement) transforms subtraction into addition while blocking carry (e.g., $500 - 427$ is computed by pressing `500` and `426` on smaller numbers $= 500 + 573 = 73$ with carry blocked).

---

### 3. Electronic Computing Era & Four Generations (pp. 19–28)
- **Vacuum Tubes**: In 1883, Thomas Edison discovered the **Edison effect** (electrons flowing from a heated filament to a cooler metal plate in vacuum). In **1904**, British scientist **John Ambrose Fleming** invented the two-electrode **vacuum diode** (converting AC to DC). In **1906**, **Lee de Forest** added a fence-shaped third electrode to create the **vacuum triode**, enabling signal amplification and high-speed electronic switching.

| Milestone / Generation | Year / Inventor | Core Architecture & Specifications |
| :--- | :--- | :--- |
| **Electromechanical Tabulator** | 1889 (Herman Hollerith) | Punch-card tabulating machine for storing accounting data. |
| **Analog Computer** | 1930 (Vannevar Bush) | World's first analog electronic computer with some digital components. |
| **ABC (Atanasoff–Berry Computer)** | 1937 | **World's first electronic digital computer**, designed to solve linear equations (not general-purpose/programmable). |
| **1st Gen: ENIAC** | 1946 (John Mauchly team, Univ. of Pennsylvania) | **Second electronic computer** and **first general-purpose programmable electronic computer**. 30+ m long, 6+ m wide, 2+ m high, **30+ tons**, **17,000+ electron tubes**, **7,000+ crystal diodes**; **5,000 additions/s** or **400 multiplications/s**. |
| **Von Neumann Parallel Computer** | 1950 | First parallel computer using **von Neumann architecture** (binary format and stored programs). |
| **2nd Gen: Transistors** | 1947 / 1954 / 1958 | First germanium transistor made in **1947** by **Shockley, Bardeen, and Brattain** at Bell Labs. **TRADIC (1954)** at Bell Labs used ~800 transistors (< 100 W). **RCA 501 (1958)** reached hundreds of thousands of ops/s. |
| **3rd Gen: Integrated Circuits (IC)** | 1958–1959 / 1970 | **Jack Kilby** (TI, 1958, germanium IC) and **Robert Noyce** (Fairchild, 1959, monolithic silicon IC) solved the "tyranny of numbers". **IBM System/370 (1970)** replaced magnetic core storage with LSI circuits and applied virtual memory, separating software from hardware. |
| **4th Gen: Microprocessors & PCs** | 1971–1983 | **Intel 4004 (1971, Marcian Hoff)**: first microprocessor (2,000+ transistors, 4-bit, 50,000 ops/s, $12\text{ cm}^2$). **Altair 8800 (1974/1975, MITS)**: world's first microcomputer based on **Intel 8080** (metal box with LED indicators, no monitor/keyboard/mouse). **Apple II (1977)**: MOS 6502 8-bit CPU, 4 KB RAM, color graphics, built-in BASIC, first batch-manufactured PC. **Apple Lisa (1983)**: world's first PC with both a **GUI and mouse**. |
| **Supercomputers** | 21st Century | **Sunway TaihuLight** delivers **90 PFLOPS** sustained and **120+ PFLOPS** peak performance. Classified into dedicated (astrophysics, cryptography) and general-purpose (meteorology, finance, medical care). |

---

## 🔑 Key Takeaways
- **Inca Quipu knots represent Ones (farthest from main horizontal string) up to Tens of thousands (closest to horizontal string); Chinese counting rods alternate vertical (ones, hundreds) and horizontal (tens, thousands).**
- **Edison discovered the Edison effect (1883); Fleming invented the vacuum diode (1904); Lee de Forest invented the vacuum triode (1906) by adding a grid/fence electrode for amplification and switching.**
- **ABC (1937) is the first electronic computer; ENIAC (1946) is the second electronic computer and first general-purpose programmable electronic computer (17,000+ tubes, 5,000 additions/s).**
- **TRADIC (1954) is Bell Labs' first transistorized computer; IBM System/370 (1970) separated hardware and software; MITS Altair 8800 (Intel 8080) is the first microcomputer.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.01 Quiz Q2): In the Inca knot counting method (Quipu), the places represented are Ones, Tens, Hundreds, Thousands, and Tens of thousands ('Tens of hundreds' in the official option list) — NEVER 'Hundreds of thousands'!

> [!WARNING]
> EXAM TRAP: Do not confuse ABC (1937, world's first electronic computer for linear equations) with ENIAC (1946, second electronic computer and world's first general-purpose programmable computer).

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`02-Exercise-Computing-Eras-and-Generations-Lab.html`](./02-Exercise-Computing-Eras-and-Generations-Lab.html)** (or [`02-Exercise-Computing-Eras-and-Generations-Lab.md`](./02-Exercise-Computing-Eras-and-Generations-Lab.md)) to apply this concept in an interactive lab workbench!
