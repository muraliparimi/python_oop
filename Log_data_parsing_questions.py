# Problem: Log Parsing for Game Events
# You're given unsorted log entries from a Roblox game server. Each log entry is a string containing:
# 
# Timestamp (ISO 8601 format or Unix timestamp)
# User ID (alphanumeric)
# Event Type (e.g., jump, attack, heal)
# Requirements:
# ✅ Parse the log entries into a structured format.
# ✅ Sort the entries by timestamp.
# ✅ Detect suspicious activity where a user performs 3 identical actions within 10 seconds.
# ✅ Return both the sorted logs and the list of suspicious users.

## Input

logs = [
    "2025-03-20 14:25:45, user_123, jump",
    "2025-03-20 14:26:01, user_456, attack",
    "2025-03-20 14:24:40, user_123, jump",
    "2025-03-20 14:25:05, user_789, heal",
    "2025-03-20 14:25:07, user_123, jump",
    "2025-03-20 14:25:10, user_123, jump"
]

# Expected output 

sorted_logs = [
    {"timestamp": "2025-03-20 14:24:40", "user_id": "user_123", "event": "jump"},
    {"timestamp": "2025-03-20 14:25:05", "user_id": "user_789", "event": "heal"},
    {"timestamp": "2025-03-20 14:25:07", "user_id": "user_123", "event": "jump"},
    {"timestamp": "2025-03-20 14:25:10", "user_id": "user_123", "event": "jump"},
    {"timestamp": "2025-03-20 14:25:45", "user_id": "user_123", "event": "jump"},
    {"timestamp": "2025-03-20 14:26:01", "user_id": "user_456", "event": "attack"}
]
suspicious_users = ["user_123"]

from datetime import datetime

def format_datetime(list_element):
    return datetime.strptime(list_element, "%Y-%m-%d %H:%M:%S")

def sort_and_find_bad_users(logs):
    # Sort based on timestamp and create a list of dictionary and identify bad logs
    sort_logs_op = sorted(logs, key=lambda x: format_datetime(x.split(",")[0]))
    sorted_logs_op = []
    bad_users= set()
    bad_users_activity = {}
    for log in sort_logs_op:
        try:
            ts, uid, action = map(str.strip, log.split(','))
            ts = format_datetime(ts.strip())
        except (ValueError, IndexError):
            print(f"Skipping malformed log: {log}")
            continue
        key = f"{uid}-{action}"
        sorted_logs_op.append({"timestamp": ts, "user_id": uid, "action": action})
        if key not in bad_users_activity:
            bad_users_activity[key] = [ts]
        else:
            difference_in_seconds = (ts - bad_users_activity[key][-1]).total_seconds()
            if difference_in_seconds <10:
                bad_users.add(uid)
            bad_users_activity[key] = [ts]
    return bad_users, sorted_logs_op


if __name__ == '__main__':
    bad_users , sorted_data = sort_and_find_bad_users(logs)
    if sorted(list(bad_users)) != sorted(suspicious_users):
        print(f"outputs not matching Expected: {suspicious_users} but got {bad_users}")
    else:
        print("outputs matched")