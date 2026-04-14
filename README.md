# CPU Scheduling Simulator

A program that simulates OS scheduling algorithms with Python. There are four CPU scheduling algorithms implemented : 
- FIFO
- SJF (non-preemptive)
- Round Robin
- Priority (non-preemptive)

The main program takes in a JSON file that specifies the scheduling policy and jobs, and outputs the results as a JSON file containing the Gantt chart and performance metrics.

## Table of Contents
- [Features](#features)
- [Test Files](#test-files)
- [Demo Input and Output](#demo-input-and-output)
- [Usage](#usage)
- [Design Decisions](#design-decisions)
- [Tie-Breaking Policy](#tie-breaking-policy)
- [AI Usage Statement](#ai-usage-statement)

## Features

- Deterministic scheduling for consistent outputs
- Supports multiple CPU scheduling algorithms
- JSON-based input and output for easy testing
- Modular design for extensibility

## Test Files 
### FIFO
- input.json
- output.json
- fifo_in.json
- fifo_out.json
- idle_test.json
- idle_out.json
### Priority
- priority_out.json
- priority_test.json
### Round Robin
- rr_test.json
- rr_out.json
### Shortest Job First
- sjf_test.json
- sjf_out.json

## Demo Input and Output

<details>
<summary>Click to expand</summary>

Input (sjf_test.json) : 

~~~
{
  "policy": "SJF",
  "jobs": [
    { "pid": "A", "arrival": 0, "burst": 7, "priority": 3 },
    { "pid": "B", "arrival": 0, "burst": 4, "priority": 1 },
    { "pid": "C", "arrival": 0, "burst": 2, "priority": 2 }
  ]
}
~~~

Output (sjf_out.json) : 

~~~
{
  "policy": "SJF",
  "gantt": [
    { "pid": "C", "start": 0, "end": 2},
    { "pid": "B", "start": 2, "end": 6},
    {"pid": "A", "start": 6, "end": 13}
  ],
  "metrics": {
    "turnaround": {"A": 13, "B": 6, "C": 2},
    "waiting": {"A": 6, "B": 2, "C": 0},
    "avg_turnaround": 7.0,
    "avg_waiting": 2.67
  }
}
~~~

</details>

## Usage 

Run the program by opening the terminal and navigating to the folder containing the code, then run : 

~~~
python3 main.py input.json > output.json
~~~

Where input.json is the JSON file containing the input; and

output.json is the JSON file that will contain the results.

**(see Demo Input and Output for format of the input.json and what the output.json will look like)**

## Design decisions 
The design prioritizes modularity, determinism, and clarity. Each scheduling, calculating and formating algorithm is implemented independently to allow easy testing and comparison, while a central handler manages input parsing and output formatting.
The implementation also accounts for important edge cases such as simultaneous arrivals, CPU idle periods, and jobs completing within a single quantum to ensure correctness and deterministic behavior.

The program is structured as follows :

1. main.py takes in two parameters in the command line :
- input.json will contain the scheduling algorithm to use and the jobs it will work on
~~~
python3 main.py input.json > output.json
~~~

2. main.py converts and passes the information to jsonHandler.py
- The main program converts the input JSON file into python data types (dictionary that contains arrays, variables, etc.)
- The main program then calls jsonHandler
~~~
main.py(JSON data)
        | calls
        v
jsonHandler(dict data)
~~~

3. jsonHandler.py ls the appropriate scheduling algorithm
- jsonHandler parses the CPU scheduling algorithm, quantum and jobs from 'data'
- jsonHandler converts all jobs from 'data' into objects of type job
- jsonHandler ls the appropriate cpu algorithm and passes it the jobs (and quantum if it's RR)
~~~
jsonHandler(dict data)
        | calls
        v
cpuSchedulerAlgorithm(int quantum, dict jobs)
~~~
_cpuSchedulerAlgorithm means any of the 4 cpu scheduling algorithms of out design: fifo.py, sjf.py, roundRobin.py, priority.py_

4. the cpuSchedulerAlgorithm runs
- In any of the four cpu scheduling algorithms, they run their algorithm and create a gantt chart 
- The gantt chart is created with the help of makeGantt.py which creates a single gantt entry to be appended to the overall gantt chart
- Each of the algorithms return the overall gantt chart to the jsonHandler
- Note that the tiebreaking algorithm is based first on
  - Deterministic initial ordering, then
  - Lexicographily smallest PID, i.e. process 'A' takes precedence over process 'B'
~~~
# Very simple pseudocode
cpuSchedulerAlgorithm(int quantum, dict jobs)
    create a ganttchart
    for every job:
      run scheduling algorithm
      ganttchart.append(makeGantt.makeGantt(currentjob.getPid(), start, end))
~~~
~~~
cpuSchedulerAlgorithm(int quantum, dict jobs)
        | returns gantt chart
        v
jsonHandler(dict data)
~~~


5. jsonHandler.py calculates the metrics 
- jsonHandler takes the jobs an ls a method to calculate metrics
~~~
jsonHandler(dict data)
        | calls
        v
calculateMetrics(dict gantt)
~~~

6. calculateMetrics calculates important statistics
- calculateMetrics calculates:
   - Turnaround time: completion time - arrival time  
   - Waiting time : turnaround time - burst time
   
   for each individual job, as well as the
   
   - Average turnaround time
   - Average waiting time
   for all the jobs,
- then it returns this information to jsonHandler
~~~
calculateMetrics(dict gantt)
        | returns
        v
jsonHandler(dict data)
~~~

7. jsonHandler assembles all information and returns it in JSON format
- jsonHandler gets the policy, the gantt chart from the scheduler algorithm and the calculated metrics
- It returns all of it in JSON format
~~~
jsonHandler(dict data)
        | returns
        v
        {
            "policy": self.policy,
            "gantt": gantt,
            "metrics": metrics
        }
~~~

## Tie-breaking policy 
Tie-breaking is handled deterministically to ensure consistent outputs.

- Jobs are initially sorted by arrival time.
- If multiple jobs have the same arrival time, they are ordered by lexicographically smallest PID.
- During execution, the ready queue follows FIFO order.
- Newly arrived jobs are added to the queue before re-adding the currently executing job (for Round Robin).

This guarantees deterministic and reproducible scheduling behavior.

## AI usage statement
AI tools (such as ChatGPT) were used to assist with understanding concepts, refining code structure, and improving documentation. All code was conceptualized, writte, reviewed, understood, and adapted by the authors. No code was blindly copied, and full responsibility for correctness and design was maintained.

