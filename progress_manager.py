#!/usr/bin/env python3
"""
Local Progress Manager for Huawei ICT Competition National Stage Study Reviewer
Handles loading, merging, and atomic saving of progress.json strictly on the user's local PC.
NOTE: progress.json is ignored by Git so teammates can pull and track their own progress individually.
"""
import datetime
import json
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PROGRESS_FILE = os.path.join(ROOT_DIR, "progress.json")


def get_progress():
    """Load local progress data from progress.json. If missing, initializes default."""
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
        print(f"[ProgressManager] Warning loading local progress.json: {e}")
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

    # Atomic write to progress.json on local PC
    temp_file = PROGRESS_FILE + ".tmp"
    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(current, f, indent=2, ensure_ascii=False)
    os.replace(temp_file, PROGRESS_FILE)

    return current


def reset_local_progress():
    """Reset all local progress back to zero."""
    blank = {
        "version": 1,
        "last_synced": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "progress": {}
    }
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(blank, f, indent=2, ensure_ascii=False)
    return blank


if __name__ == "__main__":
    curr = get_progress()
    print("Loaded local progress entries:", len(curr.get("progress", {})))
