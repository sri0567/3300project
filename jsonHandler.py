from job import Job
from calculateMetrics import CalculateMetrics
from priority import PriorityScheduler
from roundRobin import roundRobin
from sjf import sjf
from fifo import FIFOScheduler


class JSONHandler:
    def __init__(self, data):
        self.data = data
        self.policy = data["policy"].strip().upper()
        self.quantum = data.get("quantum", None)

    def _build_jobs(self):
        jobs = []

        for item in self.data["jobs"]:
            jobs.append(
                Job(
                    pid=item["pid"],
                    arrival=item["arrival"],
                    burst=item["burst"],
                    priority=item["priority"],
                    actual_start=None,
                    actual_end=None
                )
            )

        # deterministic initial ordering
        jobs.sort(key=lambda j: (j.getArrival(), j.getPid()))
        return jobs

    def run(self):
        original_jobs = self._build_jobs()
        simulation_jobs = self._build_jobs()

        if self.policy == "RR":
            if self.quantum is None or self.quantum <= 0:
                raise ValueError("RR policy requires a positive quantum.")
            gantt = roundRobin(self.quantum, simulation_jobs)

        elif self.policy == "PRIORITY":
            gantt = PriorityScheduler.run(simulation_jobs)

        elif self.policy == "FIFO":
            gantt = FIFOScheduler.run(simulation_jobs)

        elif self.policy == "SJF":
            gantt = sjf(simulation_jobs)

        else:
            raise ValueError(f"Unsupported policy: {self.policy}")

        metrics = CalculateMetrics(original_jobs).calculate(gantt)

        return {
            "policy": self.policy,
            "gantt": gantt,
            "metrics": metrics
        }