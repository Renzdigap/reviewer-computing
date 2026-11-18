# 💻 Hands-On Lab: TaiShan 2280 iBMC Initial Provisioning & Security Hardening

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 06 — Computing Product Deployment: Equipment Room, iBMC, BIOS & RAID Configuration (Sprint 2 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `03-Lecture-TaiShan-2280-Default-Credentials-and-iBMC-Initial-Setup`  
**Interactive Workbench:** Open **[`04-Exercise-iBMC-Default-IP-Credentials-and-WebUI-Navigation-Lab.html`](./04-Exercise-iBMC-Default-IP-Credentials-and-WebUI-Navigation-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
You have just powered on a brand-new TaiShan 200 (model 2280) server. Complete the initialization parameters including default IP, credentials, BIOS lookup path, and SNMP hardening.

### 📋 Step-by-Step Instructions
1. Set `default_ibmc_ip` to `'192.168.2.100'` and `default_subnet_mask` to `'255.255.255.0'`.
2. Set `webui_cli_user` to `'Administrator'`, `webui_cli_password` to `'Admin@9000'`, and `default_root_password` to `'Huawei12#$'`.
3. Set `recommended_snmp_version` to `'SNMPv3'`.

### 📝 Starter Workspace (`iBMC:/->`)
```bash
# TaiShan 200 (2280) iBMC Initialization Parameters
ibmc_defaults:
  default_ibmc_ip: "___"
  default_subnet_mask: "___"
  webui_cli_user: "___"
  webui_cli_password: "___"
  default_root_password: "___"
  login_domain: "Local iBMC"

security_and_menus:
  bios_ip_lookup_path: "Advanced > IPMI iBMC Configuration > iBMC Configuration"
  recommended_snmp_version: "___"
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Default iBMC IP is 192.168.2.100 with mask 255.255.255.0.
- WebUI/CLI user is Administrator (Admin@9000), root password is Huawei12#$, and SNMPv3 is recommended.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# TaiShan 200 (2280) iBMC Initialization Parameters
ibmc_defaults:
  default_ibmc_ip: "192.168.2.100"
  default_subnet_mask: "255.255.255.0"
  webui_cli_user: "Administrator"
  webui_cli_password: "Admin@9000"
  default_root_password: "Huawei12#$"
  login_domain: "Local iBMC"

security_and_menus:
  bios_ip_lookup_path: "Advanced > IPMI iBMC Configuration > iBMC Configuration"
  recommended_snmp_version: "SNMPv3"
```

#### Expected Console / Query Output:
```text
[OK] TaiShan 200 (2280) iBMC Initial Setup Validated:
- URL: https://192.168.2.100 (255.255.255.0) | Domain: Local iBMC
- WebUI/CLI: Administrator / Admin@9000 | Root: root / Huawei12#$ | U-Boot/BIOS: Admin@9000
- Hardening: Password updated under User & Security > Local Users; SNMPv3 enabled under Services > SNMP.
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**What are the default IP address, subnet mask, and WebUI/CLI login user name and password of the iBMC management network port on a TaiShan 200 (model 2280) server?**

- A. 192.168.1.1 / 255.255.255.0; admin / Admin@123
- B. 192.168.2.100 / 255.255.255.0; Administrator / Admin@9000
- C. 10.0.0.100 / 255.0.0.0; root / Huawei@123
- D. 172.16.0.1 / 255.255.0.0; operator / Taishan@2280

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.05 p.297, the default iBMC management port IP is 192.168.2.100, subnet mask is 255.255.255.0, and the default iBMC WebUI or CLI login user/password is Administrator / Admin@9000.
</details>

### Question 2 [Single-Choice]
**If the iBMC management IP address of a used TaiShan 200 (model 2280) server has been changed and is unknown, which BIOS menu path should you navigate to after pressing Delete or F4 during boot?**

- A. Main > System Time > Network Configuration
- B. Advanced > IPMI iBMC Configuration > iBMC Configuration
- C. Boot > Boot Type Order > PXE Configuration
- D. Security > Administrator Password > iBMC IP

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.05 pp. 299 and 313, you check or configure the iBMC management port IP address in the BIOS by choosing Advanced > IPMI iBMC Configuration > iBMC Configuration.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about iBMC WebUI configuration and SNMP versions are true?**

- A. To change the initial user password on the iBMC WebUI, choose User & Security > Local Users.
- B. To upgrade firmware or configure Time Zone & NTP, navigate under the iBMC Settings menu.
- C. SNMPv1 (RFC 1157) and SNMPv2 (RFC 1901) may pose security risks, so SNMPv3 is recommended for security purposes.
- D. The front and rear panels of a TaiShan 200 (model 2280) server provide dedicated purple/green PS/2 keyboard and mouse ports.

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** A, B, and C are true (Ch.05, pp. 303–308). D is false because Ch.05 p.298 explicitly states that the front and rear panels feature a VGA port and USB 3.0 ports, but lack PS/2 ports for keyboard and mouse input.
</details>
