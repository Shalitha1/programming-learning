class LogAnalyser:
    def analyseLogs(self, filename):
        infoCount = 0
        errorCount = 0
        warningCount = 0

        file = open(filename, "r")

        for line in file:
            if line.startswith("INFO"):
                infoCount += 1

            elif line.startswith("ERROR"):
                errorCount += 1
            elif line.startswith("WARNING"):
                warningCount += 1

        file.close()

        print(infoCount)
        print(errorCount)
        print(warningCount)

analyser = LogAnalyser()
analyser.analyseLogs("apps.log")