from datetime import datetime
from collections import defaultdict

events = [
    {"user_id": "u1", "timestamp": "2025-01-01 10:00", "action": "login"},
    {"user_id": "u2", "timestamp": "2025/01/01 10:05", "action": "login"},
    {"user_id": "u1", "timestamp": "01-01-2025 10:07", "action": "purchase", "amount": "120"},
    {"user_id": "u1", "timestamp": "2025-01-01 10:07", "action": "purchase", "amount": "120"},
    {"user_id": None, "timestamp": "2025-01-01 10:10", "action": "logout"},
    {"user_id": "u3", "timestamp": "invalid-date", "action": "login"},
]
INPUT_FORMATS = [       # the formats of date
    "%Y-%m-%d %H:%M",
    "%Y/%m/%d %H:%M",
    "%d-%m-%Y %H:%M",]
FINAL_FORMAT = "%Y-%m-%d %H:%M"

def normalizeTimestamp(value):
    for fmt in INPUT_FORMATS:
        try:
         return datetime.strptime(value, fmt).strftime(FINAL_FORMAT)
        except ValueError:
         continue
    return None
cleaned_events = []
seen = set()  # i use set to avoid duplicate enteries
for event in events:
    user_id = event.get("user_id")
    timestamp = normalizeTimestamp(event.get("timestamp", ""))
    if not user_id or not timestamp: # ignore the invalid arguments
        continue
    cleaned_event = {
        "user_id": user_id,
        "timestamp": timestamp,
        "action": event.get("action"),
        "amount": int(event["amount"]) if event.get("action") == "purchase" else 0}
    event_key = tuple(cleaned_event.items())
    if event_key not in seen:
        seen.add(event_key)
        cleaned_events.append(cleaned_event)
print("Cleaned Events:")# Print cleaned events
for e in cleaned_events:
    print(e)
actionCount = defaultdict(int)# Analyze the events and count actions and purchases store in dictionary
totalPurchase = defaultdict(int)

for event in cleaned_events:
    actionCount[event["user_id"]] += 1
    totalPurchase[event["user_id"]] += event["amount"]

print("Actions:", dict(actionCount))
print("Total purchase:", dict(totalPurchase))
