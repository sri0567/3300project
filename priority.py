import makeGantt

class PriorityScheduler:
    @staticmethod
    def run(jobs):
        # deterministic order for arrivals
        jobs = sorted(jobs, key=lambda j: (j.getArrival(), j.getPid()))

        gantt = []
        ready = []
        time = 0
        i = 0
        n = len(jobs)

        while i < n or ready:
            # move all arrived jobs into ready queue
            while i < n and jobs[i].getArrival() <= time:
                ready.append(jobs[i])
                i += 1

            # if CPU idle, jump to next arrival
            if not ready:
                next_time = jobs[i].getArrival()
                if time < next_time:
                    gantt.append(makeGantt.makeGantt("idle", time, next_time))
                time = next_time
                continue

            # smaller priority value = higher priority
            # tie-breaker: lexicographically smallest PID
            ready.sort(key=lambda j: (j.getPriority(), j.getPid()))

            current = ready.pop(0)

            if current.getActualStart() is None:
                current.setActualStart(time)

            start = time
            end = time + current.getBurst()
            time = end

            current.setActualEnd(end)
            gantt.append(makeGantt.makeGantt(current.getPid(), start, end))

        return gantt