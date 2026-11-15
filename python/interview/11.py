

class APIAnalyser:
    def findSlowEndPoints(self, requests):
        for i in requests:
            responseTime = requests[i]
            
            if responseTime > 500:
               print(i + ":" + str(responseTime) + "ms")
            

requests = {
    "login": 120,
    "users": 450,
    "payments": 1200,
    "products": 300,
    "orders": 900
}

analyserObj = APIAnalyser()
analyserObj.findSlowEndPoints(requests)