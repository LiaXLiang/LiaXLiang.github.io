## 1.  Scheduler
&nbsp; The scheduler is the OS component that allocates CPU resources to processes. It decides which process runs on **which CPU**, **when** and for **how long**.

### I. How the scheduling decisions are made?
&nbsp; The *scheduling algorithm* (or policy) used to take these decisions depends on three primary factors:
- ① The system itself
<br> This includes hardware resources such as the number of CPUs and the amount of memory available. 

- ② The workloads running on it
<br> This refers to the nature of the applications, such as interactive applications or long-running programs.
- ③ The goals to achieve
<br> These include objectives like responsiveness, energy efficiency, and overall performance.


<br> &nbsp; When the scheduling algorithm considers the system itself to make decisions about the scheduling policy, it is performing *long-term scheduling*. Long-term scheduling involves decisions about which processes to admit into the system based on its capacity. This ensures that the system maintains an optimal level of *multiprogramming* and does not become overloaded. 
<br> &nbsp; When the scheduling algorithm considers the workloads and the goals to achieve, it is making *short-term scheduling* decisions. Short-term scheduling involves selecting which of the *ready* processes or threads will be executed by the CPU next. It takes into account the current state of the processes, the specific requirements of the workloads (e.g., CPU-bound or I/O-bound), and the desired performance goals to optimize CPU utilization and ensure efficient execution.

<br> &nbsp; Two main classes of applications:
- CPU-bound (or compute-bound): long computations with a few IO waits <br>e.g., data processing applications
- IO-bound: short computations and frequent IO waits <br> e.g., web server forwarding requests to worker threads

<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap3/1.CPU&I:O_Bound.png?raw=true" alt="CPU and I/O Bound">
</figure>

### II. Different categories of scheduling algorithms and their performance metrics
<style>
table {
  width: 100%;
  border-collapse: collapse;
}

table, th, td {
  border: 1px solid black;
}

th, td {
  padding: 8px;
  text-align: left;
}
</style>


|       | Batch Scheduling <br>批处理调度 | Interactive Scheduling <br>交互式调度 | Real Time Scheduling <br>实时调度 | 
| ----------- | ----------- |----------- |----------- |
| **Usage**    | Business applications, with long running background tasks (compute-bound)  <br> 适用于具有长时间运行的后台任务（计算密集型）的业务应用   | Users are interacting with the system, or IO-bound applications      | Constrained environments, where deadlines must be met. <br>e.g., if a computer is controlling a device that produces data at a regular rate, failure to run the data-collection process on time may result in lost data.    |
| **e.g.**   | accounting, file conversion/encoding, training machine learning models etc.        | text editor, web server, etc.    | embedded systems    |
| **Characteristics**   | Usually NO preemption to minimize scheduling overhead        | Preemption is **necessary** for responsiveness      | May or may not have preemption, as these systems are usually fully controlled, with no arbitrary programs running |
| **Performance Metrics**   | **Throughput/吞吐量**: <br> ⭐️ The number of processes completed in a unit of time.  <br> ⭐️ Maximize throughput (two components):  <br> &nbsp; ① minimize overhead (OS overhead, context switching);  <br> &nbsp; ② efficient use of system resources (CPU, I/O devices) | **Response time/latency**: <br> ⭐️ The time between when the process is in *ready state* and gets the CPU for the first time . <br> ⭐️ Minimize **variance of & average** response time | **Meeting deadlines**: Finish jobs before the requested deadlines to avoid safety problems   |
| **Performance Metrics** | **Turnaround Time/周转时间**: <br> ⭐️ The length of time it takes to run a process from initialization to termination, including all the waiting time. ( = Waiting Time + I/O Time + Actual CPU Time) <br> ⭐️ Minimize waiting time, i.e., minimize the total amount of time that a process is in the *ready* queue. | User experience: The system should *feel* responsive to users | **Predictability**: Behave in a deterministic manner, easy to model and understand |


For ALL categories, there are 2 general metrics: 
- Fairness: Processes should get a similar amount of CPU resource allocated to them. **Fairness is not equality**, the amount of CPU allocation can be weighted, e.g, depending on priority
- Resource utilization: Hardware resources, e.g., CPU, devices, should be kept busy as much as possible


## 2. Scheduling Policies
- Non-preemptive schedulers choose a process to run and let it run until it *blocks*, *terminates* or voluntarily *yields* the CPU.
- Preemptive schedulers might stop a *running* process to execute another one after a given period of time. Preemption is only possible on systems with a hardware clock.
### Batch Scheduling

| Algorithms      | FCFS <br>First-Come, First Served | SJF <br> Shortest Job First | SRT <br> Shortest Remaining Time |
| --------------- | --------------------------------- | --------------------------- | -------------------------------- |
| **Runqueue**    | Processes are stored in a list sorted by order of *arrival*, with the *first* element being the *oldest*. | SJF assumes that a job’s run time is known in advance. Processes are stored in a list sorted by increasing *total CPU time* | Processes are stored in a list sorted by increasing *remaining duration* |
| **Election**    | Choose the head of the runqueue   | Choose the head of the runqueue | Choose the head of the runqueue |
| **Block**       | Remove the process from the runqueue and trigger an election | Remove the process from the runqueue and trigger an election | Remove the process from the runqueue and trigger an election |
| **Wake Up**     | Non-preemptive, add the process to the *end* of the runqueue, like a newly created process | Non-preemptive, add the process to the runqueue *at its sorted position* | **Preemptive**, if the newly arriving process has a lower remaining time than the running process, preempt it; otherwise add it to the runqueue at its sorted position |
| **(+)**         | Easy to implement | I/O bound jobs get priority over CPU bound jobs <br> → Optimal w.r.t. minimizing the average waiting time | Optimal w.r.t. minimizing the average waiting time |
| **(-)**         | ① Average wait time is highly variable as short jobs may wait behind long jobs. <br> ② With many processes, long latencies for IO-bound processes and high turnaround time for CPU-bound processes. <br> (Poor overlap of I/O and CPU operations since CPU-bound processes will force I/O bound processes to wait for the CPU, leaving the I/O devices idle.) | Long running CPU bound jobs can starve | Impossible to predict the amount of CPU time a job has left |



### Interactive Scheduling

| Algorithms      | Round-Robin | MLQ <br> / Multilevel Feedback Queues | Fair |
| --------------- | ----------- |---------------------------------------|------|
| **Intuition**   | Each process is assigned a time interval (Quantum) during which it is allowed to run. When the process uses up its quantum, it is **preempted** and put back to the end of the FIFO-queue. | Use *Round Robin* at each priority level, jobs are executed starting from the highest priority queue. Only when this queue is empty will jobs in the next highest priority queue be executed. | A fair scheduler tries to give the same amount of CPU time to all processes. Some may also enforce fairness between users (so-called *fair-share schedulers*). |
| **(+)**         | It's fair, each job gets an equal shot at the CPU. | MLQ policy is *adaptive* because it relies on past behavior to predict the future and assign job priorities, it overcomes the prediction problem in SJF. <br> CPU-bound jobs quickly drop in priority, while I/O-bound jobs remain at a high priority. | Fairness. |
| **(-)**         | Average waiting time can be bad. | Lower priority jobs might starve if higher priority queues continuously receive new jobs. | Increased overhead. |
| **Selecting Criterion** | **Selecting a time slice:** <br> - Too large: waiting time suffers, degenerates to FCFS if processes are never preempted. <br> - Too small: *Throughput* suffers because too much time is spent context switching. <br> → Balance these tradeoffs by selecting a time slice where context switching is roughly 1% of the time slice. | - **Starting priority:** Every newly arriving job begins in the highest priority queue. <br> - **Priority drop:** If a job uses up its entire time slice without completing, drop its priority one level down. <br> - **Priority boost:** If a job makes an I/O request before its time slice expires, it is moved up to a higher priority queue, promoting jobs that are I/O-bound and ensuring they receive more CPU time. | e.g., user A starts 9 processes, user B starts 1 process, they should still get 50% of the CPU each. |



### Real Time Scheduling
Real time schedulers must enforce that processes meet their deadlines. They can be separated in two classes:
- Hard real time / 硬实时系统: Deadlines must be met or the system breaks
<br> e.g., the brake system of a car must respond to the pedal being pressed very quickly to avoid accidents.
- Softreal time / 软实时系统: Deadlines can be missed from time to time without breaking the system
<br> e.g., a video player must decode 50 frames per second, but missing a frame from time to time is fine.

Real time applications may also be:
- Periodic: the task periodically runs for some (usually short) amount of time
<br> e.g., the frame decoder of the video player is started every 20 ms and must complete in less than 5 ms.
- Aperiodic: the task occurs in an unpredictable way
<br> e.g., the brake mechanism of a car is triggered when the pedal is pressed and must engage the brakes in less than 1 ms.

### multiprogramming v.s. multitasks