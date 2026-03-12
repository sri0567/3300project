class Job:
    def _init_(self, pid, arrival, burst, priority, actual_start, actual_end):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.actual_start = actual_start
        self.actual_end = actual_end

    def getPid(self):
        return self.pid

    def getArrival(self):
        return self.arrival

    def getBurst(self):
        return self.burst

    def getPriority(self):
        return self.priority

    def getActualStart(self):
        return self.actual_start

    def getActualEnd(self):
        return self.end

    def setPid(self, pid):
        self.pid = pid

    def setArrival(self, arrival):
        self.arrival = arrival

    def setBurst(self, burst):
        self.burst = burst

    def setPriority(self, priority):
        self.priority = priority

    def setActualStart(self, start):
        self.actual_start = start

    def setActualEnd(self, end):
        self.end = end
