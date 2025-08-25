# focusmate.py
import json, os
from datetime import date

DB_FILE = "tasks.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return {"tasks": [], "habits": {}}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_task(data):
    name = input("Task name: ").strip()
    due = input("Due date (YYYY-MM-DD or blank): ").strip()
    data["tasks"].append({"id": len(data["tasks"]) + 1, "name": name, "done": False, "due": due})
    save_data(data)
    print(f"Task '{name}' added.")

def list_tasks(data):
    today = date.today().isoformat()
    tasks = data["tasks"]
    if not tasks:
        print("No tasks.")
        return
    for t in tasks:
        due = t.get("due", "")
        overdue = (due and due < today and not t["done"])
        status = "OVERDUE" if overdue else ("✓" if t["done"] else "✗")
        print(f"{t['id']}. {t['name']} [{status}] due:{due}")

def mark_done(data):
    try:
        tid = int(input("Task id to mark done: "))
        for t in data["tasks"]:
            if t["id"] == tid:
                t["done"] = True
                print(f"Task '{t['name']}' marked done.")
        save_data(data)
    except ValueError:
        print("Invalid input.")

def log_habit(data):
    habit_name = input("Habit name: ").strip()
    habits = data.get("habits", {})
    habits.setdefault(habit_name, []).append(date.today().isoformat())
    data["habits"] = habits
    save_data(data)
    print(f"Habit '{habit_name}' logged for today.")

def show_stats(data):
    tasks = data["tasks"]
    total = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    print(f"Tasks completed: {done}/{total} ({done*100//total if total else 0}%)")

    habits = data.get("habits", {})
    if habits:
        print("Habit streaks:")
        for h, days in habits.items():
            print(f"{h}: {len(set(days))} day(s)")
    else:
        print("No habits logged yet.")

def main():
    data = load_data()
    while True:
        print("\n1. Add task\n2. List tasks\n3. Mark task done\n4. Log habit\n5. Show stats\n6. Quit")
        ch = input("Choose: ").str1ip()
        if ch == "1":
            add_task(data)
        elif ch == "2":
            list_tasks(data)
        elif ch == "3":
            mark_done(data)
        elif ch == "4":
            log_habit(data)
        elif ch == "5":
            show_stats(data)
        elif ch == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()