# 💻 Hands-On Lab: FusionCompute Cluster Readiness Check

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 02 — Computing System Overview, System Software & Virtualization (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `05-Lecture-Cloud-OS-and-Huawei-FusionCompute-Virtualization`  
**Interactive Workbench:** Open **[`06-Exercise-FusionCompute-Cluster-Hardware-Planning-Lab.html`](./06-Exercise-FusionCompute-Cluster-Hardware-Planning-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
You are validating a server bill-of-materials (BOM) before deploying Huawei FusionCompute VRM and CNA compute nodes.

### 📋 Step-by-Step Instructions
1. Set `vrm_min_system_disk_gb` to `270` and `compute_node_min_system_disk_gb` to `150`.
2. Set `recommended_system_raid` to `'RAID 1'`, `min_memory_gb` to `8`, and `recommended_memory_gb` to `48`.
3. Set `backup_component` to `'eBackup'` and `dr_component` to `'UltraVR'`.

### 📝 Starter Workspace (`admin@fusioncompute-vrm:~#`)
```bash
# FusionCompute Pre-Deployment Check
cluster_requirements:
  vrm_min_system_disk_gb: ___
  compute_node_min_system_disk_gb: ___
  recommended_system_raid: "___"
  min_memory_gb: ___
  recommended_memory_gb: ___
  max_network_load_percent: 60

suite_components:
  backup_component: "___"
  dr_component: "___"
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- On page 115, VRM system drive >= 270 GB, compute node system drive >= 150 GB, minimum memory is 8 GB (48 GB recommended), and two SAS drives in RAID 1 are recommended.
- eBackup provides CBT-based VM backup; UltraVR provides DR management.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# FusionCompute Pre-Deployment Check
cluster_requirements:
  vrm_min_system_disk_gb: 270
  compute_node_min_system_disk_gb: 150
  recommended_system_raid: "RAID 1"
  min_memory_gb: 8
  recommended_memory_gb: 48
  max_network_load_percent: 60

suite_components:
  backup_component: "eBackup"
  dr_component: "UltraVR"
```

#### Expected Console / Query Output:
```text
[PASS] FusionCompute Cluster BOM Validated:
- VRM Disk >= 270 GB | Compute Disk >= 150 GB (SAS RAID 1)
- Memory: 8 GB min / 48 GB+ recommended | Network load <= 60%
- Suite: FusionCompute + FusionStorage Block + eBackup (CBT) + UltraVR (DR).
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**When deploying Huawei FusionCompute on physical servers, what are the minimum system drive capacities required for the Virtual Resource Manager (VRM) node and each compute node?**

- A. VRM >= 150 GB; Compute node >= 270 GB
- B. VRM >= 270 GB; Compute node >= 150 GB
- C. VRM >= 500 GB; Compute node >= 300 GB
- D. VRM >= 100 GB; Compute node >= 100 GB

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.02 p.115, the system drive on the VRM node must be >= 270 GB, and the system drive on each compute node must be >= 150 GB.
</details>

### Question 2 [Single-Choice]
**In the FusionCompute virtualization suite, which component works with snapshots and Changed Block Tracking (CBT) to back up VM data, and which provides Disaster Recovery (DR) via SAN asynchronous remote replication?**

- A. UltraVR (backup) and eBackup (DR)
- B. eBackup (backup) and UltraVR (DR)
- C. FusionStorage (backup) and FusionAccess (DR)
- D. DVS (backup) and VRM (DR)

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** eBackup works with FusionCompute snapshots and CBT to back up VM data, whereas UltraVR is disaster recovery (DR) management software using SAN asynchronous remote replication (Ch.02, pp. 107–108).
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about FusionCompute virtual networking and virtual storage are true?**

- A. A Distributed Virtual Switch (DVS) connects to VMs via virtual ports and to physical NICs on hosts via uplinks.
- B. Virtual storage supports snapshots, thin provisioning, QoS, and online resizing, which physical drives alone cannot provide.
- C. Before virtualization, typical server utilization is 5% to 10%; after virtualization, it can reach 60% or higher.
- D. Servers in the same FusionCompute cluster can freely mix Intel x86 and Kunpeng Arm CPUs in a single live-migration pool.

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** A, B, and C are true (Ch.02, pp. 110–113). D is false because CPUs on servers in the same cluster must be of the same model and support hardware virtualization (Ch.02, p.115).
</details>
