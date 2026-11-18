#!/usr/bin/env python3
"""
Interactive Terminal Study Reviewer & Mock Exam Runner
Pillar: HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)
Run with: py practice_cli.py
"""
import json
import os
import re
import webbrowser

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(HERE, "curriculum_data.json")


def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def norm_ws(s):
    return re.sub(r"\s+", " ", str(s or "").lower()).strip()


def run_cli():
    data = load_data()
    while True:
        print("\n" + "=" * 72)
        print(f"  HUAWEI ICT COMPETITION NATIONAL STAGE — {data['title']}")
        print("=" * 72)
        print("  [0] 🌐 Open Interactive DataCamp-Style Web App (index.html) in Browser")
        for h in data["hours"]:
            print(f"  [{h['hour_number']}] ⏱️  Hour 0{h['hour_number']}: {h['title']} (4 Bite-Sized Sprints)")
        print(f"  [9] 🏆 Hour 09: {data['mock_exam']['title']} (60 Questions, 60 Mins)")
        print("  [q] Quit")
        choice = input("\nSelect an option (0-9 or q): ").strip().lower()
        if choice == "q":
            break
        elif choice == "0":
            webbrowser.open(os.path.join(HERE, "index.html"))
            print("Launched index.html in your default browser!")
        elif choice in [str(i) for i in range(1, 9)]:
            h = data["hours"][int(choice) - 1]
            study_hour(h)
        elif choice == "9":
            run_mock_exam(data["mock_exam"])


def study_hour(h):
    for s in h["sprints"]:
        lec = s["lecture"]
        ex = s["exercise"]
        print("\n" + "-" * 72)
        print(f"📖 LECTURE (Hour 0{h['hour_number']} • Sprint {s['sprint_number']}/4): {lec['title']}")
        print(f"   Ref: {lec['pdf_ref']} | Duration: {lec['duration_mins']} mins")
        print("-" * 72)
        print(lec["content_markdown"])
        print("\n🔑 Key Takeaways:")
        for k in lec.get("key_takeaways", []):
            print(f"  • {k}")
        print("\n⚠️ Exam Traps:")
        for t in lec.get("exam_traps", []):
            print(f"  ! {t}")
        input("\nPress Enter to start the immediate Hands-On Exercise...")

        print("\n" + "-" * 72)
        print(f"💻 HANDS-ON EXERCISE: {ex['title']}")
        print("-" * 72)
        print(f"Scenario: {ex['scenario']}\n")
        for idx, inst in enumerate(ex.get("instructions", []), 1):
            print(f"  Step {idx}: {inst}")
        print("\nStarter Workspace:")
        print(ex.get("starter_code", ""))
        ans = input("\nType your command/SQL/answer (or 's' to view solution): ").strip()
        if ans.lower() != "s" and ans:
            ans_norm = norm_ws(ans)
            checks = ex.get("validation_checks", [])
            for c_idx, chk in enumerate(checks, 1):
                reqs = chk.get("required_any", [])
                ok = (not reqs) or any(norm_ws(r) in ans_norm for r in reqs)
                print(f"  {'✅ PASS' if ok else '❌ CHECK'} Step {c_idx}: {chk['description']}")
        print("\nOfficial Solution:\n" + ex.get("solution_code", ""))
        print("\nSimulated Output:\n" + ex.get("simulated_output", ""))

        print("\n--- Quick Exam Verification Drill (3 Questions) ---")
        for q_idx, q in enumerate(ex.get("quiz_questions", []), 1):
            print(f"\nQ{q_idx} [{q['type'].upper()}]: {q['question']}")
            for opt in q.get("options", []):
                print(f"   {opt}")
            u_ans = input("Your Answer (e.g. A or ABD): ").strip().upper()
            target = "".join(sorted([c for c in q["answer"].upper() if c.isalpha()]))
            u_norm = "".join(sorted([c for c in u_ans if c.isalpha()]))
            if u_norm == target:
                print(f"✅ Correct ({target})! {q.get('explanation', '')}")
            else:
                print(f"❌ Official Answer: {target} | {q.get('explanation', '')}")
        cont = input("\nContinue to next sprint in this hour? (Y/n): ").strip().lower()
        if cont == "n":
            break


def run_mock_exam(mock):
    qs = mock.get("questions", [])
    print("\n" + "=" * 72)
    print(f"🏆 {mock['title']} ({len(qs)} Questions, {mock['total_points']} pts)")
    print("=" * 72)
    mode = input("Run in [1] Browser Timed GUI or [2] Terminal CLI mode? (1/2): ").strip()
    if mode == "1":
        webbrowser.open(os.path.join(HERE, mock["folder_name"], "Final-Mock-Exam.html"))
        return
    earned = 0
    total = 0
    for i, q in enumerate(qs, 1):
        pts = q.get("points", 15)
        total += pts
        print(f"\nQ{i}/{len(qs)} [{q['type'].upper()} • {pts} pts] ({q.get('chapter', '')})")
        print(q["question"])
        if q["type"] == "lab":
            if q.get("starter_code"):
                print(q["starter_code"])
            u = input("Your command/SQL/answer (or 'q' to finish early): ").strip()
            if u.lower() == "q":
                break
            kws = q.get("accepted_keywords", [q.get("solution", "")])
            u_norm = norm_ws(u)
            ok = bool(u) and all(norm_ws(k) in u_norm for k in kws)
            if ok:
                earned += pts
                print(f"✅ Correct (+{pts} pts)!")
            else:
                print(f"❌ Official Solution: {q.get('solution', q.get('answer', ''))}")
            print(f"   Explanation: {q.get('explanation', '')}")
        else:
            for opt in q.get("options", []):
                print(f"  {opt}")
            u = input("Your Answer (or 'q' to finish early): ").strip()
            if u.lower() == "q":
                break
            target = "".join(sorted([c for c in q["answer"].upper() if c.isalpha()]))
            u_norm = "".join(sorted([c for c in u.upper() if c.isalpha()]))
            if u_norm == target:
                earned += pts
                print(f"✅ Correct (+{pts} pts)!")
            else:
                print(f"❌ Official Answer: {target}")
            print(f"   Explanation: {q.get('explanation', '')}")
    print(f"\nFINAL SCORE: {earned} / {total} pts")


if __name__ == "__main__":
    run_cli()
