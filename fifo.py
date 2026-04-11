import makeGantt


class FIFOScheduler:
    @staticmethod
    def run(jobs):
        # Deterministic ordering:
        # first by arrival, then lexicographically by PID
        jobs = sorted(jobs, key=lambda j: (j.getArrival(), j.getPid()))

        gantt = []
        time = 0

        for current in jobs:
            # If CPU is idle before this job arrives, record idle time
            if time < current.getArrival():
                gantt.append(makeGantt.makeGantt("idle", time, current.getArrival()))
                time = current.getArrival()

            if current.getActualStart() is None:
                current.setActualStart(time)

            start = time
            end = time + current.getBurst()

            current.setActualEnd(end)
            gantt.append(makeGantt.makeGantt(current.getPid(), start, end))

            time = end

        return gantt