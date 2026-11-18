#!/usr/bin/env python3
"""
Progress Manager for Huawei ICT Competition National Stage Study Reviewer
Handles loading, merging, atomic saving of progress.json, and Git synchronization.
"""
import datetime
import json
import os
import subprocess

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PROGRESS_FILE = os.path.join(ROOT_DIR, "progress.json")


def get_progress():
    """Load progress data from progress.json. If missing, initializes default."""
    if not os.path.exists(PROGRESS_FILE):
        return {
            "version": 1,
            "last_synced": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "progress": {}
        }
    try:
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if "progress" not in data:
                data = {"version": 1, "last_synced": "", "progress": data}
            return data
    except Exception as e:
        print(f"[ProgressManager] Warning loading progress.json: {e}")
        return {"version": 1, "last_synced": "", "progress": {}}


def merge_and_save(incoming_prog):
    """
    Merge incoming progress dictionary with disk progress.json.
    Incoming format: { "unit_uid": { "completed": true, "ts": ... }, ... }
    """
    current = get_progress()
    curr_prog = current.get("progress", {})

    for uid, info in incoming_prog.items():
        if uid.endswith("_mock_exam"):
            # Mock exam merging: retain highest score
            if uid in curr_prog:
                old_score = curr_prog[uid].get("score", 0)
                new_score = info.get("score", 0)
                if new_score >= old_score:
                    curr_prog[uid] = info
            else:
                curr_prog[uid] = info
        else:
            # Regular unit: mark completed
            if uid in curr_prog:
                if info.get("completed"):
                    curr_prog[uid]["completed"] = True
                    curr_prog[uid]["ts"] = max(curr_prog[uid].get("ts", 0), info.get("ts", 0))
            else:
                curr_prog[uid] = info

    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
    current["version"] = 1
    current["last_synced"] = now_iso
    current["progress"] = curr_prog

    # Atomic write to progress.json
    temp_file = PROGRESS_FILE + ".tmp"
    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(current, f, indent=2, ensure_ascii=False)
    os.replace(temp_file, PROGRESS_FILE)

    return current


def git_sync_progress(message=None):
    """
    Automatically stage progress.json, commit with timestamp, and push to origin/main.
    Returns (success: bool, message: str)
    """
    if not os.path.exists(PROGRESS_FILE):
        return False, "progress.json does not exist yet."

    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = message or f"feat(progress): sync study progress ({now_str})"

    try:
        # Check git status for progress.json
        subprocess.run(["git", "add", "progress.json"], cwd=ROOT_DIR, check=True, capture_output=True, text=True)

        status_res = subprocess.run(["git", "status", "--porcelain", "progress.json"], cwd=ROOT_DIR, capture_output=True, text=True)
        if not status_res.stdout.strip():
            return True, "No new progress changes to commit (already in sync with git)."

        commit_res = subprocess.run(["git", "commit", "-m", commit_msg], cwd=ROOT_DIR, capture_output=True, text=True)
        if commit_res.returncode != 0:
            return False, f"Git commit failed: {commit_res.stderr.strip()}"

        push_res = subprocess.run(["git", "push", "origin", "main"], cwd=ROOT_DIR, capture_output=True, text=True)
        if push_res.returncode != 0:
            return False, f"Git push failed: {push_res.stderr.strip()}"

        return True, f"Successfully pushed progress to GitHub ({commit_msg})!"
    except Exception as e:
        return False, f"Git sync error: {str(e)}"


if __name__ == "__main__":
    # Test initialization
    curr = get_progress()
    print("Loaded progress entries:", len(curr.get("progress", {})))
