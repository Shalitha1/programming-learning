

class LogAnalyser:
    def analyse_logs(self, logs):
        info_count = 0
        error_count = 0
        Warning_count = 0

        for key in logs:
            if logs[key].starswith("INFO"):
                info_count += 1

            elif logs[key].startswith("ERROR"):
                error_count += 1

            elif logs[key].startswith("WARNING"):
                Warning_count += 1


        print(info_count)
        print(error_count)
        print(Warning_count)

logs = {
    1: "INFO Server started",
    2: "ERROR Database connection failed",
    3: "WARNING High memory usage",
    4: "INFO User logged in",
    5: "ERROR API request failed",
    6: "ERROR Timeout occurred"
}

analyserObj = LogAnalyser()
analyserObj.analyse_logs(logs)