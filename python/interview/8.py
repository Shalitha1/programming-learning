class HTTPMonitor:
    def HTTPMonitorFunction(self, status_codes):
        successRequests = 0
        redirectRequests = 0
        failedRequests = 0

        for req in status_codes:
            if status_codes >= 200 and status_codes <= 299:
                successRequests += 1
            if status_codes >= 300 and status_codes <= 399:
                redirectRequests += 1
            if status_codes >= 400 and status_codes <= 599:
                failedRequests += 1

        print(successRequests)
        print(redirectRequests)
        print(failedRequests)


status_codes = [201,301,401]
HTTPMonitorObj = HTTPMonitor()
HTTPMonitorObj.HTTPMonitorFunction(status_codes)