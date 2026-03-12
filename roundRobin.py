import job
import makeGantt

def roundRobin(quantum, jobs):
    jobs.sort(key=lambda job:job.getArrival())
    gantt = []
    count = 0
    current_jobs =[]

    while jobs and jobs[0].getArrival() == 0 :
        temp = jobs.pop(0)
        temp.setStart(0)
        current_jobs.append(temp)

    while current_jobs or jobs:
        if not current_jobs: # CPU is idle
            start = count
            count = jobs[0].getArrival()
            gantt.append(makeGantt.makeGantt("idle", start, count))
            temp = jobs.pop(0)
            temp.setStart(count)
            current_jobs.append(temp)

        for job in current_jobs[:]:
            start = count
            time_slice = min(quantum, job.getBurst())
            job.setBurst(job.getBurst() - time_slice)
            count += time_slice
            gantt.append(makeGantt.makeGantt(job.getPid(),start,count))

            if job.getBurst() <= 0:
                current_jobs.remove(job)

            while jobs and jobs[0].getArrival() <= count:
                temp = jobs.pop(0)
                temp.setStart(count)
                current_jobs.append(temp)

    return gantt