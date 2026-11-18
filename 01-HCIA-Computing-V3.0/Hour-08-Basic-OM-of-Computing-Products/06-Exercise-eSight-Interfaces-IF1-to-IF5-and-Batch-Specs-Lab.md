# 💻 Hands-On Lab: eSight IF1–IF5 Interface & Batch Specification Verification

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 08 — Basic O&M of Computing Products: iBMA, iBMC, Smart Provisioning, FusionDirector, eSight, SmartKit & eService (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (7 mins) — Paired with `05-Lecture-Centralized-Management-eSight-Architecture-and-Features`  
**Interactive Workbench:** Open **[`06-Exercise-eSight-Interfaces-IF1-to-IF5-and-Batch-Specs-Lab.html`](./06-Exercise-eSight-Interfaces-IF1-to-IF5-and-Batch-Specs-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
Configure the eSight integration architecture mapping (`IF1`–`IF5`) and batch operation capacity limits for a large carrier data center.

### 📋 Step-by-Step Instructions
1. Map `southbound_interface` to `'IF1'`, `northbound_oss_interface` to `'IF2'`, and `auth_ldap_radius_sso_interface` to `'IF3'`.
2. Set `excel_batch_import_max` to `500`, `os_deploy_task_max` to `200`, and `os_deploy_concurrent_max` to `40`.
3. Set `fw_upgrade_schedule_max` to `1000`, `profile_bind_max` to `2000`, and `cleared_alarm_bg_color` to `'light green'`.

### 📝 Starter Workspace (`esight-admin@ict-nms:~#`)
```bash
# eSight Architecture & Batch Specification Config
esight_interfaces:
  southbound_interface: "___"
  northbound_oss_interface: "___"
  auth_ldap_radius_sso_interface: "___"
  notification_mail_sms_interface: "IF4"
  user_ui_interface: "IF5"

esight_batch_limits:
  excel_batch_import_max: ___
  os_deploy_task_max: ___
  os_deploy_concurrent_max: ___
  fw_upgrade_schedule_max: ___
  fw_upgrade_concurrent_max: 100
  profile_bind_max: ___
  cleared_alarm_bg_color: "___"
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- IF1 is southbound, IF2 is northbound, and IF3 is external authentication (LDAP/RADIUS/SSO).
- Batch limits: Excel import = 500, OS deploy = 200/task (40 concurrent), FW upgrade = 1000/schedule (100 concurrent), Profile bind = 2000; cleared alarms have a light green background.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# eSight Architecture & Batch Specification Config
esight_interfaces:
  southbound_interface: "IF1"
  northbound_oss_interface: "IF2"
  auth_ldap_radius_sso_interface: "IF3"
  notification_mail_sms_interface: "IF4"
  user_ui_interface: "IF5"

esight_batch_limits:
  excel_batch_import_max: 500
  os_deploy_task_max: 200
  os_deploy_concurrent_max: 40
  fw_upgrade_schedule_max: 1000
  fw_upgrade_concurrent_max: 100
  profile_bind_max: 2000
  cleared_alarm_bg_color: "light green"
```

#### Expected Console / Query Output:
```text
[OK] eSight External Interfaces & Batch Capacities Verified:
- Interfaces: IF1 (Southbound), IF2 (Northbound RESTful/SNMP/FTP/Kafka), IF3 (LDAP/RADIUS/SSO), IF4 (Mail/SMS), IF5 (UI)
- Capacities: Excel Import=500 | OS Deploy=200/task (40 concurrent) | FW Upgrade=1000/schedule (100 concurrent) | Profile=2000 bound (1000 applied)
- Alarms: White background = Uncleared | Light green background = Cleared.
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**Among the five external interfaces of Huawei eSight (Ch.06, p. 404), which interface is the northbound interface used by upper-layer OSS or third-party systems to obtain resources, alarms, and performance data via RESTful, SNMP, FTP, or Kafka?**

- A. IF1
- B. IF2
- C. IF3
- D. IF4

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.06 p.404: IF1 is the southbound interface to managed devices; IF2 is the northbound interface (RESTful, SNMP, FTP, Kafka, Syslog) to upper-layer OSS; IF3 is for external authentication servers (LDAP, RADIUS, SSO); IF4 is for notifications (Mail/SMS); IF5 is the UI.
</details>

### Question 2 [Single-Choice]
**In Huawei eSight OS Deployment (Ch.06, p. 412), what are the maximum number of devices supported per task and the maximum number of devices that can be deployed concurrently?**

- A. Maximum 30 devices per task and 10 devices concurrently
- B. Maximum 200 devices per task and 40 devices concurrently
- C. Maximum 1,000 devices per task and 500 devices concurrently
- D. Maximum 50 devices per task and 50 devices concurrently

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.06 p.412, each eSight OS deployment task supports a maximum of 200 devices and a maximum of 40 devices can be deployed concurrently (requiring servers with Smart Provisioning).
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about eSight Server Management are true?**

- A. Up to 500 devices can be added at a time using an Excel file in Batch Import mode.
- B. On the eSight alarm panel, alarms with a white background are not cleared, whereas alarms with a light green background are cleared.
- C. In Software and Firmware Upgrade, up to 100 devices can be upgraded concurrently and up to 1,000 devices can be selected for an upgrade schedule.
- D. A single eSight Server Profile can be bound to a maximum of 2,000 devices, and up to 1,000 devices can be selected at a time for applying a profile.

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** All four statements match the exact specifications in Ch.06 pp. 406, 410, 413, and 414.
</details>
