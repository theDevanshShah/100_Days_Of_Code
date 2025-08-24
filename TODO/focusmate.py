# focusmate.py
import json, os

DB_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DB_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add task\n2. List tasks\n3. Mark done\n4. Quit")
        ch = input("Choose: ").strip()
        if ch == "1":
            name = input("Task: ").strip()
            tasks.append({"id": len(tasks)+1, "name": name, "done": False})
            save_tasks(tasks)
        elif ch == "2":
            for t in tasks:
                status = "✓" if t["done"] else "✗"
                print(f"{t['id']}. {t['name']} [{status}]")
        elif ch == "3":
            tid = int(input("Task id: "))
            for t in tasks:
                if t["id"] == tid:
                    t["done"] = True
            save_tasks(tasks)
        elif ch == "4":
            break

if __name__ == "__main__":
    main()