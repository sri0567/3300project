class Job:
    def _init_(self, pid, arrival, burst, priority, start, end):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.start = start
        self.end = end

    def getPid(self):
        return self.pid

    def getArrival(self):
        return self.arrival

    def getBurst(self):
        return self.burst

    def getPriority(self):
        return self.priority

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def setPid(self, pid):
        self.pid = pid

    def setArrival(self, arrival):
        self.arrival = arrival

    def setBurst(self, burst):
        self.burst = burst

    def setPriority(self, priority):
        self.priority = priority

    def setStart(self, start):
        self.start = start

    def setEnd(self, end):
        self.end = end
