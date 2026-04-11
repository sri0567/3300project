import makeGantt
from job import Job

def sjf(jobs):
    time=0
    ganttchart = []
    ready=[]

     # sort jobs by arrival time
    jobs = sorted(jobs, key=lambda j: j.getArrival())

    while jobs or ready:

        # move arrived jobs to ready queue
        while jobs and jobs[0].getArrival() <= time:
            ready.append(jobs.pop(0))

        
        if not ready:
            time = jobs[0].getArrival()
            continue

        # sort ready queue by burst time
        ready.sort(key=lambda j: j.getBurst())

        # get shortest job
        job = ready.pop(0)

        start = time
        end = time + job.getBurst()

        # store start and end times in the object
        job.setActualStart(start)
        job.setActualEnd(end)

        # create gantt entry
        ganttchart.append(makeGantt.makeGantt(job.getPid(), start, end))

        # update current time
        time = end

    return ganttchart

