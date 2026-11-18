# 💻 Hands-On Lab: openEuler Intelligence Entries, RAG & Diagnostic Agents Verification

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 01 — OS for the AI Era & Getting Started with openEuler (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `01-Lecture-OS-for-AI-Era-and-openEuler-Intelligence`  
**Interactive Workbench:** Open **[`02-Exercise-openEuler-Intelligence-Architecture-Lab.html`](./02-Exercise-openEuler-Intelligence-Architecture-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
You are deploying openEuler Intelligence for an enterprise O&M team. Complete the architecture verification manifest below to specify the two interaction entries, the three Intelligent Diagnosis agents, and the three Intelligent Container Image tiers.

### 📋 Step-by-Step Instructions
1. Step 1: Set `INTERACTION_ENTRIES` to the two official access entries supported by the openEuler intelligent platform (`web` and `intelligent shell`).
2. Step 2: Set `DIAGNOSIS_AGENTS` to the three diagnostic agents in execution order (`Inspection`, `Demarcation`, `Detection`) and specify `TOP_ROOT_CAUSE_METRICS=3`.
3. Step 3: Set `CONTAINER_TIERS` to include the Huawei Ascend SDK (`CANN`), framework (`PyTorch`), and LLM (`chatglm2-13b` or `llama2-7b`).

### 📝 Starter Workspace (`root@openEuler:~#`)
```bash
# openEuler Intelligence Architecture Verification Manifest
INTERACTION_ENTRIES="<entry1>, <entry2>"
DIAGNOSIS_AGENTS="<agent1> -> <agent2> -> <agent3>"
TOP_ROOT_CAUSE_METRICS=<number>
CONTAINER_TIERS="SDK(CUDA/<sdk>) -> Framework(TensorFlow/<framework>) -> LLM(<model>)"
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Recall Ch.01 Quiz Q1: The openEuler intelligent platform supports two entries: web entry and intelligent shell entry.
- In Intelligent Diagnosis, the Inspection Agent checks IPs/containers, the Demarcation Agent outputs the top 3 root cause metrics, and the Detection Agent profiles stack hotspots.
- The SDK layer encapsulates CUDA and CANN; the LLM layer includes llama2-7b and chatglm2-13b.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# openEuler Intelligence Architecture Verification Manifest
INTERACTION_ENTRIES="web, intelligent shell"
DIAGNOSIS_AGENTS="Inspection -> Demarcation -> Detection"
TOP_ROOT_CAUSE_METRICS=3
CONTAINER_TIERS="SDK(CUDA/CANN) -> Framework(TensorFlow/PyTorch) -> LLM(llama2-7b/chatglm2-13b)"
```

#### Expected Console / Query Output:
```text
[OK] openEuler Intelligence Entries Verified: Web Entry + Intelligent Shell Entry
[OK] RAG Multi-Channel Retrieval Active: Vector + Keyword + Chat2DB
[OK] Intelligent Diagnosis Pipeline: Inspection Agent -> Demarcation Agent (Top 3 Root Causes) -> Detection Agent (Stack Profiling)
[OK] Intelligent Container Image Tiers: SDK (CUDA/CANN) | Framework (TensorFlow/PyTorch) | LLM (llama2-7b/chatglm2-13b)
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [True / False]
**[Official Ch.01 Quiz Q1] The openEuler intelligent platform currently supports two entries: web entry and intelligent shell entry.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** Official Ch.01 Quiz Q1 (p.20): True. openEuler Intelligence is accessible via two entries: the Web entry and the Intelligent shell entry.
</details>

### Question 2 [Single-Choice]
**In the Intelligent Diagnosis function of openEuler Intelligence, which agent analyzes an abnormality selected from the inspection result and outputs the top 3 root cause metrics?**

- A. Inspection Agent
- B. Demarcation Agent
- C. Detection Agent
- D. Orchestration Agent

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.01 (p.15), the Inspection Agent checks for abnormalities of designated IP addresses; the Demarcation Agent analyzes and demarcates an abnormality and outputs the top 3 root cause metrics; the Detection Agent performs profiling location on the root cause metrics.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following capabilities are part of Corpus Governance in openEuler Intelligence's RAG technology?**

- A. Fragment relationship extraction
- B. Fragment derivative construction (digests)
- C. Optical Character Recognition (OCR) for hybrid image and text scenarios
- D. Kernel space memory paging

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Ch.01 (pp.10–11), Corpus Governance imports corpuses into the knowledge base through fragment relationship extraction, fragment derivative construction, and OCR.
</details>
