# 💻 Hands-On Lab: Inspecting openEuler Release, Kernel Version & Community Workflow

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 01 — OS for the AI Era & Getting Started with openEuler (Sprint 2 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `03-Lecture-Linux-History-Open-Source-Licenses-and-openEuler`  
**Interactive Workbench:** Open **[`04-Exercise-openEuler-Releases-and-Licenses-Lab.html`](./04-Exercise-openEuler-Releases-and-Licenses-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
You have logged into a freshly provisioned openEuler server. Verify the OS release file, inspect the kernel release and processor architecture using `uname`, and check the `LICENSES` directory.

### 📋 Step-by-Step Instructions
1. Step 1: View the openEuler release version information stored in `/etc/os-release` using `cat /etc/os-release`.
2. Step 2: Display the running Linux kernel version and hardware architecture using `uname -r` or `uname -a`.
3. Step 3: Echo the release cycles (`LTS=2_years`, `Innovation=6_months`) to confirm openEuler lifecycle compliance.

### 📝 Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Display OS release details
<command_to_view_os_release>

# Step 2: Check kernel version
<command_to_check_kernel>

# Step 3: Verify release cadence
echo "LTS=2_years, Innovation=6_months"
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Use `cat /etc/os-release` or `cat /etc/openEuler-release` to inspect the distribution release.
- Use `uname -r` or `uname -a` to print the kernel version.
- Keep the echo statement in Step 3 intact.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Display OS release details
cat /etc/os-release

# Step 2: Check kernel version
uname -r

# Step 3: Verify release cadence
echo "LTS=2_years, Innovation=6_months"
```

#### Expected Console / Query Output:
```text
NAME="openEuler"
VERSION="24.03 (LTS)"
ID="openEuler"
VERSION_ID="24.03"
PRETTY_NAME="openEuler 24.03 (LTS)"
ANSI_COLOR="0;31"

6.6.0-28.0.0.34.oe2403.aarch64
LTS=2_years, Innovation=6_months
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**Which open source license allows commercial software to reference and link to an open-source class library without requiring the commercial software's own source code to be open-sourced?**

- A. GPL
- B. LGPL
- C. Proprietary EULA
- D. Copyfree Only

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.02 (p.30), LGPL (Lesser GPL) is designed for class libraries and allows commercial software to use the LGPL library in link mode without open-sourcing the commercial software code.
</details>

### Question 2 [Single-Choice]
**What are the standard release intervals for openEuler Innovation releases and Long-Term Support (LTS) releases, respectively?**

- A. Every 3 months; Every 1 year
- B. Every half a year (6 months); Every 2 years
- C. Every 1 year; Every 5 years
- D. Every 2 years; Every 6 months

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.02 (p.34), an openEuler Innovation release is generally released every half a year (6 months), whereas an LTS release is usually released every two years.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which five major aspects are covered by China's Mulan open source license?**

- A. Copyright license and Patent license
- B. Non-trademark license
- C. Distribution restriction
- D. Disclaimer and liability limitation

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.02 (p.29), the Mulan license involves five major aspects: copyright license, patent license, non-trademark license, distribution restriction, and disclaimer and liability limitation.
</details>
