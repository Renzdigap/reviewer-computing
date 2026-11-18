# Container Image Architecture (UnionFS, AUFS, OverlayFS) & Image Management (`isula images/pull/tag/rmi`)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 08 — openEuler Native Container Engine iSula (iSulad) (Sprint 4 of 4)  
**Format:** Bite-Sized Lecture (7 mins) - Followed immediately by `08-Exercise-iSula-Image-Pull-Tag-Inspect-Rmi-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.07, pp. 427–438

---

## Learning Objectives
- Explain the layered container image structure (read-only `rootfs` image layers up to 128 layers + read/write container layer) and Copy-on-Write (CoW)
- Compare UnionFS implementations: AUFS (`aufs/diff` & `aufs/mnt`) vs. OverlayFS (`lowerdir`, `upperdir`, `merged`, `workdir`, `copy_up`, and whiteout/opaque files)
- Parse image naming (`[registry/][path/]<imagename>[:tag]`) and manage images with `isula images`, `isula inspect`, `isula pull`, `isula tag`, and `isula rmi`

---

### 1. Container Image Architecture, Layer Limit & Copy-on-Write (CoW)
* **What is in a Container Image?** A container image is an immutable template containing a complete operating system **`rootfs` (files and directories)** plus the application and its dependencies.
  * **Shared Host Kernel:** All containers share the **host OS kernel** and **cannot modify the host kernel**.
  * **Layer Limit:** An image is immutable and **cannot exceed 128 layers** (Ch.07, p.428).
* **Image Layers vs. Container Layer & Copy-on-Write (CoW — Ch.07, pp. 429–430):**
  * **Image layers (Read-Only / R/O):** Shared across containers; enables incremental pulls/storage.
  * **Container layer (Thin Read/Write / R/W layer):** Mounted on top when a container starts.
  * **4 File Operations under CoW:**
    1. **Creating a file:** Added directly to the top R/W **container layer**.
    2. **Reading a file:** Searched from top layer (`upperdir`/container layer) down to lower image layers (`lowerdir`).
    3. **Modifying a file:** Looked up from top to bottom; when modified for the first time, the file is **copied from the read-only image layer up to the container layer (`copy_up`)** and modified there (**Copy-on-Write**).
    4. **Deleting a file/directory:** Because image layers are read-only, UnionFS creates a **whiteout file** (or **opaque directory** in OverlayFS) in the R/W container layer to hide the underlying file/directory!

---

### 2. UnionFS Drivers: AUFS vs. OverlayFS
**UnionFS** mounts multiple directories (branches/layers) onto a single unified virtual mount point:
* **AUFS (Advanced Multi-Layered Unification Filesystem — Ch.07, p.432):**
  * Stores each image layer and container layer in `/var/lib/xxx/aufs/diff/<ID>`, and presents the unified working directory at **`/var/lib/xxx/aufs/mnt`**.
* **OverlayFS (`overlay` / `overlay2` — Ch.07, p.433):**
  * Simpler deployment and higher performance than AUFS; built on top of `ext4` or `xfs` using **four directories**:
    1. **`lowerdir`:** Read-only image layers (`lowerdir1`, `lowerdir2`...).
    2. **`upperdir`:** Read-write container layer (stores new, `copy_up`-modified, and whiteout/opaque files).
    3. **`merged`:** Unified view presented to the user/container.
    4. **`workdir`:** Internal working directory (**invisible to users**).

---

### 3. Container Image Naming & `isula` Image Commands
* **Image Naming Format:** **`[registry/][path/]<imagename>[:tag]`**
  * If `registry/` is omitted, the configured default public/mirror registry is used.
  * If `:tag` is omitted, **`latest`** is used by default!
* **`isula` Image Management Commands (Ch.07, pp. 435–438):**
  * **`isula images`:** Lists local images on the host.
  * **`isula inspect <image:tag>`:** Views detailed JSON metadata (e.g., `isula inspect nginx:latest`).
  * **`isula pull <image>`:** Pulls an image from a registry (`isula pull openeuler/busybox:latest`).
    * **CRITICAL EXAM TRAP (Ch.07, p.436):** **`iSula` supports the `pull` command and does NOT support the `push` command!**
  * **`isula tag <source_image:tag> <target_image:tag>`:** Creates a new tag alias referring to the same `IMAGE ID` (e.g., `isula tag openeuler/busybox:latest busybox:test`).
  * **`isula rmi <image:tag>`:** Deletes an image from the host (`isula rmi busybox:test`).

---

## Key Takeaways
- **Container images encapsulate the OS rootfs and app dependencies while sharing the host OS kernel; an image is read-only/immutable and cannot exceed 128 layers.**
- **OverlayFS uses four directories: lowerdir (R/O image layers), upperdir (R/W container layer), merged (unified container view), and workdir (invisible to users), using copy_up (CoW) for modifications and whiteout files / opaque directories for deletions.**
- **In '[registry/][path/]<imagename>[:tag]', the default tag is 'latest'; manage images with 'isula images', 'isula pull', 'isula tag', 'isula inspect', and 'isula rmi' (Note: iSula does NOT support 'push'!).**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.07 p.436): iSula supports 'isula pull', but DOES NOT support 'isula push'!

> [!WARNING]
> EXAM TRAP: Deleting a file inside a container does NOT delete it from the read-only image layer (lowerdir)—instead, AUFS/OverlayFS creates a 'whiteout' file (or 'opaque' directory) in the container layer (upperdir) to mask it.

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`08-Exercise-iSula-Image-Pull-Tag-Inspect-Rmi-Lab.html`](./08-Exercise-iSula-Image-Pull-Tag-Inspect-Rmi-Lab.html)** (or [`08-Exercise-iSula-Image-Pull-Tag-Inspect-Rmi-Lab.md`](./08-Exercise-iSula-Image-Pull-Tag-Inspect-Rmi-Lab.md)) to apply this concept in an interactive lab workbench!
