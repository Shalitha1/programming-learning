class HTTPMonitor:
    def HTTPRequestMonitor(self, incomingRequests):
        successfulRequests = 0
        RedirectedRequests = 0
        failedRequests = 0

        for request in incomingRequests:
            if request >= 200 and request <= 299:
                successfulRequests += 1
            elif request >= 300 and request <= 399:
                RedirectedRequests += 1
            elif request >= 400 and request <= 599:
                failedRequests += 1

        print(successfulRequests)
        print(RedirectedRequests)
        print(failedRequests)

incomingRequests = [200,300,404]

HTTPMonitorObj = HTTPMonitor()
HTTPMonitorObj.HTTPRequestMonitor(incomingRequests)