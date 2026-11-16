
# class SystemMonitor:
#     def SystemMonitorFunc(self, server):
#         cpuUsage = server["cpu"]
#         memoryUsage = server["memory"]

#         if cpuUsage >= 80:
#             print("CPU usage is high")
#         elif cpuUsage <80:
#             print("CPU usage is normal")

#         if memoryUsage >= 80:
#             print("Memory usage is high")
#         elif memoryUsage < 80:
#             print("Memory usage is normal")

server = {
    "cpu": 85,
    "memory": 50
}

SystemMonitorObj = SystemMonitor()
SystemMonitorObj.SystemMonitorFunc(server)