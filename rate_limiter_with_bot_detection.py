# You're building a rate limiter for incoming API requests from Roblox game clients. You need to:

# Differentiate between human and bot behavior.
# Apply different rate limits:
# Humans: max 5 requests/second
# Bots: max 2 requests/second
# Bot Detection Logic (for now):
# If an IP address sends 10+ identical requests (same endpoint) in a row, consider it a bot.
# Inputs
requests = [
    {"timestamp": 1618500000, "ip": "192.168.1.1", "endpoint": "/jump"},
    {"timestamp": 1618500000, "ip": "192.168.1.1", "endpoint": "/jump"},
    {"timestamp": 1618500000, "ip": "192.168.1.1", "endpoint": "/jump"}
]

# Outut

[
    {"status": "allowed"},
    {"status": "allowed"},
    {"status": "blocked", "reason": "rate limit exceeded"},
    {"status": "blocked", "reason": "bot detected"}
]


from collections import defaultdict, deque


# lets assume a sliding window 
BOT_DETECTION_THRESHOLD = 10
def rate_limiter(requests):
    results = []
    # Track requests per IP per second (timestamp)
    request_counter = defaultdict(lambda: defaultdict(int)) # ip --> timestamp --> count

    # Track last N endpoint hits per each IP
    endpoint_history = defaultdict(deque) # ip --> deque of lastend points
   
    # set of known bot ips
    bot_ips = set()
   
    for req in requests:
        timestamp  = req["timestamp"]
        ip = req["ip"]
        endpoint = req["endpoint"]

        # --- BOT DETECTION ---
        endpoint_history[ip].append(endpoint)
        if len(endpoint_history[ip]) > BOT_DETECTION_THRESHOLD:
            endpoint_history[ip].popleft()

        if len(endpoint_history[ip]) == BOT_DETECTION_THRESHOLD and len(set(endpoint_history[ip])) == 1:
            bot_ips.add(ip)

        # --- RATE LIMITING ---
        request_counter[ip][timestamp] += 1
        limit = 2 if ip in bot_ips else 5

        if request_counter[ip][timestamp] > limit:
            results.append({
                "status": "blocked",
                "reason": "bot detected" if ip in bot_ips else "rate limit exceeded"
            })
        else:
            results.append({"status": "allowed"})

    return results

