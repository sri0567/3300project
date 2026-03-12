class Job:
    def _init_(self, pid, arrival, burst, priority):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.priority = priority

    def getPid(self):
        return self.pid

    def getArrival(self):
        return self.arrival

    def getBurst(self):
        return self.burst

    def getPriority(self):
        return self.priority

    def setPid(self, pid):
        self.pid = pid

    def setArrival(self, arrival):
        self.arrival = arrival

    def setBurst(self, burst):
        self.burst = burst

    def setPriority(self, priority):
        self.priority = priority
