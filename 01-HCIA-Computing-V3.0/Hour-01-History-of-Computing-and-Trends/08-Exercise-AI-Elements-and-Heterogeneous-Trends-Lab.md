# 💻 Hands-On Lab: AI Ecosystem Elements & Computing Workload Audit

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 01 — History of Computing & Industry Trends (Sprint 4 of 4)  
**Format:** Immediate Hands-On Exercise (7 mins) — Paired with `07-Lecture-Artificial-Intelligence-and-Computing-Trends`  
**Interactive Workbench:** Open **[`08-Exercise-AI-Elements-and-Heterogeneous-Trends-Lab.html`](./08-Exercise-AI-Elements-and-Heterogeneous-Trends-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
Complete the Python audit script verifying the four basic elements of AI applications, AI historical phases, and workload mapping between integer and floating-point computations.

### 📋 Step-by-Step Instructions
1. Define `ai_basic_elements` as the exact 4 elements from Ch.01 (`'data'`, `'algorithms'`, `'computing power'`, `'scenarios'`), and set `not_an_ai_element` to `'talent'`.
2. Set `text_and_bigdata_compute_type` to `'integer'` and `scientific_compute_type` to `'floating-point'`.
3. Set `cloud_edge_pattern` to `'central training + edge inference'` and `dc_ai_power_percentage` to `80`.

### 📝 Starter Workspace (`python3@kunpeng-ai:~$`)
```bash
# Audit script for Ch.01 AI & Computing Trends
ai_basic_elements = ["data", "algorithms", "computing power", "___"]
not_an_ai_element = "___"
text_and_bigdata_compute_type = "___"
scientific_compute_type = "___"
cloud_edge_pattern = "___"
dc_ai_power_percentage = ___

print("AI Elements:", ai_basic_elements, "| Excluded:", not_an_ai_element)
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- The four basic elements on page 48 and page 51 are data, algorithms, computing power, and scenarios. Talent is the distractor in Ch.01 Quiz Q1.
- Integer computing excels at text processing and big data; floating-point excels at scientific computing.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Audit script for Ch.01 AI & Computing Trends
ai_basic_elements = ["data", "algorithms", "computing power", "scenarios"]
not_an_ai_element = "talent"
text_and_bigdata_compute_type = "integer"
scientific_compute_type = "floating-point"
cloud_edge_pattern = "central training + edge inference"
dc_ai_power_percentage = 80

print("AI Elements:", ai_basic_elements, "| Excluded:", not_an_ai_element)
```

#### Expected Console / Query Output:
```text
AI Elements: ['data', 'algorithms', 'computing power', 'scenarios'] | Excluded: talent
Workload Mapping: Integer -> Text/Storage/Big Data | Floating-Point -> Scientific/Video
Cloud-Edge Synergy: central training + edge inference (AI accounts for 80% of DC compute).
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**(Official Ch.01 Quiz Q1) Which of the following is not a basic element of AI applications?**

- A. Data
- B. Scenario
- C. Computing power
- D. Talent

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `D`
- **Explanation:** Data, algorithms, computing power, and scenarios are the four basic elements of AI applications (Ch.01, pp. 48, 51, 61 Quiz Q1). Talent is not one of the basic elements.
</details>

### Question 2 [Single-Choice]
**During which period of AI development did expert systems with logical rule inference become popular and fifth-generation computers emerge?**

- A. The first peak (1956–1976)
- B. The first trough (1976–1982)
- C. The second peak (1982–1987)
- D. The recovery period (1997–2010)

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `C`
- **Explanation:** During the second peak (1982–1987), decision tree models, multi-layer neural networks, expert systems with logical rule inference, and fifth-generation computers emerged, before the Lisp machine market collapsed in 1987 (Ch.01, p.49).
</details>

### Question 3 [True / False]
**Floating-point computing is outstanding in text processing, storage, and big data analysis, whereas integer computing is mainly used for scientific computing.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False. According to Ch.01 p.57, integer computing is outstanding in text processing, storage, and big data analysis, whereas floating-point computing is excellent in scientific computing and video processing.
</details>
