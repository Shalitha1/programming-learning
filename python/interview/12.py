server_utilization = {
    "server-01": {"cpu": 32, "memory": 48},
    "server-02": {"cpu": 67, "memory": 72},
    "server-03": {"cpu": 21, "memory": 35},
    "server-04": {"cpu": 84, "memory": 81},
    "server-05": {"cpu": 56, "memory": 64},
    "server-06": {"cpu": 43, "memory": 52},
    "server-07": {"cpu": 91, "memory": 89},
    "server-08": {"cpu": 28, "memory": 41},
    "server-09": {"cpu": 73, "memory": 68},
    "server-10": {"cpu": 49, "memory": 57},
    "server-11": {"cpu": 62, "memory": 76},
    "server-12": {"cpu": 37, "memory": 44},
    "server-13": {"cpu": 88, "memory": 93},
    "server-14": {"cpu": 19, "memory": 31},
    "server-15": {"cpu": 54, "memory": 61}
}

print("CPU Usage")
for server in server_utilization:
    cpuUsage = server_utilization[server]["cpu"]
    if cpuUsage >= 80:
        print(server, ":", cpuUsage)

print("Memory Usage")
for server in server_utilization:
    memoryUsage = server_utilization[server]["memory"]
    if memoryUsage >= 80:
        print(server, ":", memoryUsage)

