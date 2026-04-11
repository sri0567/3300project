import makeGantt


def roundRobin(quantum, jobs):
    # Deterministic initial ordering
    jobs.sort(key=lambda job: (job.getArrival(), job.getPid()))

    gantt = []
    time = 0
    ready = []

    # Add all jobs that arrive at time 0
    while jobs and jobs[0].getArrival() <= time:
        ready.append(jobs.pop(0))

    while ready or jobs:
        # If no job is ready, CPU is idle until next arrival
        if not ready:
            next_arrival = jobs[0].getArrival()
            if time < next_arrival:
                gantt.append(makeGantt.makeGantt("idle", time, next_arrival))
                time = next_arrival

            while jobs and jobs[0].getArrival() <= time:
                ready.append(jobs.pop(0))

        # Take the first job in the ready queue
        current = ready.pop(0)

        if current.getActualStart() is None:
            current.setActualStart(time)

        start = time
        time_slice = min(quantum, current.getBurst())
        current.setBurst(current.getBurst() - time_slice)
        time += time_slice

        gantt.append(makeGantt.makeGantt(current.getPid(), start, time))

        # Add all newly arrived jobs before re-queueing current job
        while jobs and jobs[0].getArrival() <= time:
            ready.append(jobs.pop(0))

        # If current job still has remaining burst, put it back
        if current.getBurst() > 0:
            ready.append(current)
        else:
            current.setActualEnd(time)

    return gantt