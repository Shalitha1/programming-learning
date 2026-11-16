logs = [
    "2026-11-16T10:00:01Z GET /api/users 200 120ms",
    "2026-11-16T10:00:02Z GET /api/orders 500 340ms",
    "2026-11-16T10:00:03Z POST /api/orders 502 410ms",
    "2026-11-16T10:00:04Z GET /api/users 200 98ms",
    "2026-11-16T10:00:05Z GET /api/orders 500 305ms",
    "2026-11-16T10:00:06Z GET /health 200 5ms",
]

errorCount = {}

for log in logs:
    parts = log.split(" ")
    endpoint = parts[2]
    statusCode = int(parts[3])

    if statusCode >= 500 and statusCode <= 599:
        if endpoint in errorCount:
            errorCount[endpoint] = errorCount[endpoint] + 1
        else:
            errorCount[endpoint] =1

print(errorCount)




