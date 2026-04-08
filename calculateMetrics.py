class CalculateMetrics:
    def __init__(self, original_jobs):
        self.job_info = {}

        for job in original_jobs:
            self.job_info[job.getPid()] = {
                "arrival": job.getArrival(),
                "burst": job.getBurst()
            }

    def calculate(self, gantt):
        completion_time = {}

        for block in gantt:
            pid = block["pid"]
            if pid == "idle":
                continue
            completion_time[pid] = block["end"]  # last segment wins

        turnaround = {}
        waiting = {}

        for pid in sorted(self.job_info.keys()):
            arrival = self.job_info[pid]["arrival"]
            burst = self.job_info[pid]["burst"]
            completion = completion_time[pid]

            ta = completion - arrival
            wt = ta - burst

            turnaround[pid] = ta
            waiting[pid] = wt

        avg_turnaround = round(sum(turnaround.values()) / len(turnaround), 2)
        avg_waiting = round(sum(waiting.values()) / len(waiting), 2)

        return {
            "turnaround": turnaround,
            "waiting": waiting,
            "avg_turnaround": avg_turnaround,
            "avg_waiting": avg_waiting
        }