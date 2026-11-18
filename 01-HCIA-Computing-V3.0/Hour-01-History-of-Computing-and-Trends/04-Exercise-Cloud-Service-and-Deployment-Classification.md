# Hands-On Lab: Cloud Service Model & Architecture Classifier

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 01 — History of Computing & Industry Trends (Sprint 2 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `03-Lecture-Cloud-Computing-Architecture-and-Service-Models`  
**Interactive Workbench:** Open **[`04-Exercise-Cloud-Service-and-Deployment-Classification.html`](./04-Exercise-Cloud-Service-and-Deployment-Classification.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
An enterprise is migrating from Traditional IT to Huawei Cloud. Complete the architecture mapping configuration defining Cloud 1.0/2.0/3.0 focus areas and IaaS/PaaS/SaaS management boundaries.

### Step-by-Step Instructions
1. Set `cloud_1_focus` to `'virtualization-centric'`, `cloud_2_focus` to `'resource-centric'`, and `cloud_3_focus` to `'application-centric'`.
2. Set `iaas_user_manages_os` to `True` and `paas_user_manages_os` to `False`.
3. Specify the two layers managed by the user in PaaS as `'applications'` and `'data'`.

### Starter Workspace (`architect@huawei-cloud:~#`)
```bash
# Huawei Cloud Migration Matrix Configuration
cloud_evolution:
  cloud_1_focus: "___"
  cloud_2_focus: "___"
  cloud_3_focus: "___"

service_models:
  iaas_user_manages_os: ___
  paas_user_manages_os: ___
  paas_user_managed_layers:
    - "___"
    - "___"
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Cloud 1.0 is virtualization-centric, Cloud 2.0 is resource-centric, and Cloud 3.0 is application-centric.
- In PaaS, the cloud provider manages the OS, middleware, and runtime environment; users only focus on applications and data.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Huawei Cloud Migration Matrix Configuration
cloud_evolution:
  cloud_1_focus: "virtualization-centric"
  cloud_2_focus: "resource-centric"
  cloud_3_focus: "application-centric"

service_models:
  iaas_user_manages_os: True
  paas_user_manages_os: False
  paas_user_managed_layers:
    - "applications"
    - "data"
```

#### Expected Console / Query Output:
```text
[VALIDATED] Cloud Evolution & Service Model Matrix:
- Cloud 1.0: Virtualization-centric (KVM, ESXi, Xen, Hyper-V)
- Cloud 2.0: Resource-centric (OpenStack)
- Cloud 3.0: Application-centric (Docker, Cloud Foundry)
- PaaS User Responsibility: Applications + Data only.
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**In the Platform as a Service (PaaS) cloud computing model, which layers do users need to focus on and manage?**

- A. OS, middleware, data, and applications
- B. Applications and data only
- C. Virtualization, servers, storage, and networks
- D. Users only use applications and manage no layers

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** In PaaS (Ch.01, p.36), the cloud platform provides and maintains the infrastructure (servers, storage, networks, virtualization) and application deployment environment (OS, middleware, operating environment). Users only need to focus on applications and data.
</details>

### Question 2 [Single-Choice]
**Which phase of cloud computing evolution is characterized as 'resource-centric' for infrastructure migration to the cloud and standardized, automated services (represented by OpenStack)?**

- A. Cloud 1.0
- B. Cloud 2.0
- C. Cloud 3.0
- D. First Platform

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Cloud 1.0 is virtualization-centric; Cloud 2.0 is resource-centric (OpenStack); Cloud 3.0 is application-centric (Docker, Cloud Foundry, Cloud Native) (Ch.01, p.34).
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following are included among the five core benefits of cloud computing defined in HCIA-Computing?**

- A. On-demand self-service
- B. Widespread network access
- C. Resource pooling
- D. Quick deployment and auto scaling
- E. Metered services

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCDE`
- **Explanation:** All five (On-demand self-service, Widespread network access, Resource pooling, Quick deployment and auto scaling, and Metered services) are the five core benefits of cloud computing (Ch.01, p.33).
</details>
