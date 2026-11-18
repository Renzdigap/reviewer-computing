# 💻 Hands-On Lab: Remote Console & BIOS/PXE Boot Automation

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 06 — Computing Product Deployment: Equipment Room, iBMC, BIOS & RAID Configuration (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (7 mins) — Paired with `05-Lecture-Remote-Virtual-Console-KVM-and-BIOS-Configuration`  
**Interactive Workbench:** Open **[`06-Exercise-BIOS-POST-Boot-Order-and-PXE-Configuration-Lab.html`](./06-Exercise-BIOS-POST-Boot-Order-and-PXE-Configuration-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
Configure the Remote Virtual Console concurrency parameters and the BIOS boot/PXE settings for automated UEFI PXE network installation.

### 📋 Step-by-Step Instructions
1. Set `shared_console_max_local_users` to `2` and `shared_console_max_vnc_users` to `5`.
2. Set `bios_entry_keys` to `'Delete or F4'` and `bios_save_exit_key` to `'F10'`.
3. Set `lom_pxe_menu_path` to `'Advanced > LOM Configuration > PXE Configuration'`.

### 📝 Starter Workspace (`bios-setup@taishan-2280:~#`)
```bash
# Remote Console & BIOS/PXE Configuration
remote_console:
  private_console_max_users: 1
  shared_console_max_local_users: ___
  shared_console_max_vnc_users: ___

bios_settings:
  bios_entry_keys: "___"
  boot_order_adjust_keys: "+ or -"
  bios_save_exit_key: "___"
  lom_pxe_menu_path: "___"
  pxe_boot_capabilities:
    - "UEFI: IPv4"
    - "UEFI: IPv6"
    - "UEFI: IPv4/IPv6"
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Shared remote console supports up to 2 local users or 5 VNC users.
- Enter BIOS with Delete or F4; save and exit with F10; onboard PXE is under Advanced > LOM Configuration > PXE Configuration.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Remote Console & BIOS/PXE Configuration
remote_console:
  private_console_max_users: 1
  shared_console_max_local_users: 2
  shared_console_max_vnc_users: 5

bios_settings:
  bios_entry_keys: "Delete or F4"
  boot_order_adjust_keys: "+ or -"
  bios_save_exit_key: "F10"
  lom_pxe_menu_path: "Advanced > LOM Configuration > PXE Configuration"
  pxe_boot_capabilities:
    - "UEFI: IPv4"
    - "UEFI: IPv6"
    - "UEFI: IPv4/IPv6"
```

#### Expected Console / Query Output:
```text
[OK] Remote Console & BIOS Configuration Validated:
- HTML5/Java Console: Private (1 user) | Shared (2 local users or 5 VNC users)
- BIOS Hotkeys: Entry = Delete / F4 | Move Boot Option = + / - | Save & Exit = F10
- Onboard PXE: Advanced > LOM Configuration > PXE Configuration (UEFI: IPv4 / IPv6 / IPv4/IPv6).
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**How many simultaneous users can access the server when using the HTML5 Integrated Remote Console (Shared) mode on the iBMC WebUI?**

- A. Only 1 local user or 1 VNC user
- B. Up to 2 local users or 5 VNC users
- C. Up to 10 local users or 20 VNC users
- D. Unlimited local and VNC users

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.05 p.310, Private mode allows only 1 local user or VNC user, while Shared mode (Java or HTML5) allows up to 2 local users or 5 VNC users simultaneously.
</details>

### Question 2 [Single-Choice]
**Which keys are pressed during server startup to enter the TaiShan 200 BIOS Setup utility, and which key saves configuration changes and exits the BIOS?**

- A. Press Ctrl+Alt+Del to enter BIOS; press Esc to save and exit
- B. Press Delete or F4 to enter BIOS; press F10 to save and exit
- C. Press F1 to enter BIOS; press F5 to save and exit
- D. Press Tab to enter BIOS; press Alt+F4 to save and exit

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.05 pp. 298, 311, and 315, press Delete or F4 when the boot menu is displayed to enter the BIOS, use + or - to change boot order, and press F10 to save configuration changes and exit.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**In the BIOS Power-On Self-Test (POST) sequence (Ch.05, p. 312), which of the following steps occur BEFORE the BIOS attempts OS startup?**

- A. Initialization of the data bus and control bus
- B. CPU self-check and Memory self-check
- C. Graphics card self-check and Self-check of drives and other peripheral devices
- D. Result presentation in the form of beep codes or on-screen messages

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** All four steps occur in that exact sequence during POST before the BIOS hands over control to OS startup (Ch.05, p.312).
</details>
