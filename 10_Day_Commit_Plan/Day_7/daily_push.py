import datetime
import os
import time

# File to track the last push date
TRACK_FILE = "last_push.txt"

def get_last_push():
    if not os.path.exists(TRACK_FILE):
        return None
    with open(TRACK_FILE, "r") as f:
        return f.read().strip()

def save_push_date(date):
    with open(TRACK_FILE, "w") as f:
        f.write(date)

def daily_push():
    today = datetime.date.today().isoformat()
    last_push = get_last_push()

    if last_push == today:
        print("✅ Already pushed today.")
    else:
        print("🚀 Daily push completed!")
        save_push_date(today)

if __name__ == "__main__":
    while True:
        cmd = input("Enter 'push' to do daily push, 'quit' to exit: ").strip().lower()
        if cmd == "push":
            daily_push()
        elif cmd == "quit":
            print("Bye.")
            break
        else:
            print("Unknown command.")