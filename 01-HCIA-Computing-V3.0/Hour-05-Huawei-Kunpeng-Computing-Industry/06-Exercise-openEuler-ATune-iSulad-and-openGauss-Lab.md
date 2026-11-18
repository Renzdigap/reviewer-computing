# Hands-On Lab: openEuler A-Tune/iSulad & openGauss Feature Verification

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 05 — Huawei Kunpeng Processors, TaiShan Servers, openEuler/openGauss & HPC (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `05-Lecture-Kunpeng-Software-Ecosystem-openEuler-and-openGauss`  
**Interactive Workbench:** Open **[`06-Exercise-openEuler-ATune-iSulad-and-openGauss-Lab.html`](./06-Exercise-openEuler-ATune-iSulad-and-openGauss-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
Configure the Kunpeng base software manifest verifying openEuler 22.03 LTS and openGauss technical specifications.

### Step-by-Step Instructions
1. Set `openeuler_2203_kernel` to `'5.10'`, `ai_tuning_engine` to `'A-Tune'`, and `container_engine` to `'iSulad'`.
2. Set `opengauss_license` to `'Mulan PSL v2'` and `opengauss_2p_tpmc` to `1500000`.
3. Set `opengauss_failover_seconds` to `10`.

### Starter Workspace (`root@openeuler-2203:~#`)
```bash
# openEuler & openGauss Technical Manifest
openeuler_specs:
  open_source_year: 2019
  foundation: "OpenAtom Foundation"
  openeuler_2203_kernel: "___"
  ai_tuning_engine: "___"
  container_engine: "___"
  automated_install_tool: "kickstart"

opengauss_specs:
  open_source_date: "2020-06-30"
  opengauss_license: "___"
  opengauss_2p_tpmc: ___
  opengauss_failover_seconds: ___
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- openEuler 22.03 LTS uses Linux kernel 5.10, A-Tune for AI tuning, and iSulad for lightweight containers.
- openGauss uses Mulan PSL v2, reaches 1,500,000 tpmC on 2-socket Kunpeng, and promotes standby to primary within 10 seconds.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# openEuler & openGauss Technical Manifest
openeuler_specs:
  open_source_year: 2019
  foundation: "OpenAtom Foundation"
  openeuler_2203_kernel: "5.10"
  ai_tuning_engine: "A-Tune"
  container_engine: "iSulad"
  automated_install_tool: "kickstart"

opengauss_specs:
  open_source_date: "2020-06-30"
  opengauss_license: "Mulan PSL v2"
  opengauss_2p_tpmc: 1500000
  opengauss_failover_seconds: 10
```

#### Expected Console / Query Output:
```text
[OK] Kunpeng Software Ecosystem Manifest Verified:
- openEuler 22.03 LTS: Linux Kernel 5.10 | A-Tune (Sensing/Decision/Execution) | iSulad (Moby/Kata/System) | BiSheng Compiler
- openGauss: Open-sourced June 30, 2020 (Mulan PSL v2) | 1.5M tpmC (2P Kunpeng) | NUMA-aware + SQL Bypass | <10s Failover.
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**Which AI-driven automatic optimization system in openEuler uses non-intrusive system profiling (Sensing, Decision making, and Execution) to match optimal resource models to service workloads in real time?**

- A. iSulad
- B. A-Tune
- C. BiSheng Compiler
- D. Kickstart

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.04 p.261, A-Tune is openEuler's AI-driven automatic optimization system that operates through Sensing, Decision making, and Execution.
</details>

### Question 2 [Multiple-Choice (Select ALL)]
**Which of the following statements about the openGauss enterprise-class open-source database are true?**

- A. openGauss went open source on June 30, 2020 under the Mulan Permissive Software License v2.
- B. It uses NUMA-aware data structures and SQL bypass technology, achieving 1,500,000 tpmC on 2-socket Kunpeng servers.
- C. It supports data page CRC checks (restoring damaged pages via the standby node) and promotes a standby node to primary within 10 seconds.
- D. It supports fully-encrypted computing, dynamic data masking, and AI-based parameter tuning and slow SQL diagnosis.

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** All four statements accurately describe openGauss features in Ch.04 pp. 266–269.
</details>

### Question 3 [Single-Choice]
**In openEuler's iSulad container solution, which upstream project is integrated to implement 'secure containers' (VMs whose interfaces are encapsulated as container interfaces)?**

- A. Moby 18.09
- B. Kata Containers 1.7
- C. Cloud Foundry
- D. OpenStack Nova

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.04 p.262, openEuler integrates Moby 18.09 for application containers and Kata Containers 1.7 for secure containers (which are essentially VMs with container interfaces).
</details>
