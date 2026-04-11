import makeGantt


def sjf(jobs):
    time = 0
    ganttchart = []
    ready = []

    # deterministic ordering by arrival, then PID
    jobs = sorted(jobs, key=lambda j: (j.getArrival(), j.getPid()))

    while jobs or ready:
        # move arrived jobs to ready queue
        while jobs and jobs[0].getArrival() <= time:
            ready.append(jobs.pop(0))

        # if nothing is ready, CPU is idle until next arrival
        if not ready:
            next_arrival = jobs[0].getArrival()
            if time < next_arrival:
                ganttchart.append(makeGantt.makeGantt("idle", time, next_arrival))
            time = next_arrival
            continue

        # shortest burst first, tie-break by PID
        ready.sort(key=lambda j: (j.getBurst(), j.getPid()))

        current = ready.pop(0)

        start = time
        end = time + current.getBurst()

        current.setActualStart(start)
        current.setActualEnd(end)

        ganttchart.append(makeGantt.makeGantt(current.getPid(), start, end))

        time = end

    return ganttchart