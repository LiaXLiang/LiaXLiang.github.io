# Chapter2: Process Management

## 1. Process v.s. Program
- A *Program* is a set of static instructions and data, typically stored on disk.
- A *Process* is a **dynamic** concept, representing an active instance of a running program. The process executes sequentially, one instruction at a time. 

<br> &nbsp; Several processes can run the same program, but each is a distinct process with its own execution context and state, e.g., multiple instances of MicroSoft Word can run at the same time. <br> &nbsp; Metaphorically, multiple cooks (processes) can use the same recipe (program): while each cook follows the same instructions, each has their own ingredients and cooking tools (execution context), and their operations do not interfere with one another.

<br> &nbsp; A Process's Memory / Address Space is split into several sections:

<figure class="half" style="display: flex; justify-content: space-between;">
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap2/1.ProcessMemoryLayout.png?raw=true" style="width: 25%; margin-right: 15%;">
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap2/1a.example.png?raw=true" style="width: 60%; margin-left: 1%;">
</figure>

- *Kernel memory* is shared between all processes, accessible only in supervisor mode.
-  *Text Segment* is where the binary program is loaded in memory. It contains the actual binary instructions that will be executed by the CPU.
- *Data Segment* contains initialized global variables and static local variables, constant strings. <br> e.g., a global: ```static int idx = 0;``` <br> or a local: ```int count = 0;```
-  BSS (block starting symbol) contains static uninitialized variables. <br> e.g., a global: ```static int i;```
-  *Heap* contains dynamically allocated memory, grows towards higher addresses. <br> e.g., ```malloc(), brk/sbrk, mmap()```
-  *Stack* contains local variables, environment variable, calling context (stack frame)



## 2. Process Execution State
<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap2/2.Process_Execution_State.png?raw=true" alt="Process Execution State">
</figure>

- new/create: the OS is setting up the process state
- ready: ready to run, but waiting for the CPU 
- running: executing the instructions on the CPU
- waiting: waiting for an event to complete
- terminated: the OS is destroying this process
  
<br> As the program executes, it moves from state to state, as
a result of the program actions (e.g., system calls), OS
actions (scheduling), and external actions (interrupts).
<br>e.g.
<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap2/2a.Example.png?raw=true" alt="Process Execution State Example">
</figure>


## 3. How are processes represented in the OS? 
### I. Process Control Block (PCB / 进程控制块) 
&nbsp; PCB is an OS data structure in order for OS to keep track of all processes. 
<br> &nbsp; The OS allocates a new PCB on the creation of each process and places it
on a state queue; The PCB tracks the execution state and location of each process; The OS deallocates the PCB when the process terminates.

<br> &nbsp; The PCB contains the set of information required for the program to execute properly:

<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap2/3.PCB.png?raw=true" alt="PCB">
</figure>

- Process execution state (ready, running, etc.).
- Process creation time
- Program Counter (PC), indicating the next instruction.
- CPU Registers and their current values.
- CPU Scheduling information: Priorities, scheduling algorithms, and queue pointers for state queues, etc.
- Process environment, including the working directory.
- Consumed CPU time.
- Memory management information (Details about memory allocation for the process, including pointers to allocated memory areas.)
- OS resources in use by the process(e.g., open files).
- Process-, parent process-, and user-ID(who is the owner of the process)


### II. How are PCBs organized? 
The OS maintains the PCBs of all the processes in state queues.

<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap2/3a.StateQueue.png?raw=true" alt="State Queue">
</figure>

## 4. How does the OS change the currently running process?

Stopping one and starting another processes involves a **context switch**, which is a relatively expensive operation. 
<br> e.g., Context switching between the *running* process A and the *ready* process B happens in several steps:

<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap2/4.ContextSwitch.png?raw=true" alt="State Queue">
</figure>

- ① Change the state of the currently running process A to *ready*.
- ② Save the CPU registers (PC, SP, etc.) into process A's PCB
- ③ Load the hardware registers (PC, SP, etc.) from B’s PCB into the CPU registers
- ④ Change the state of B from ready to *running*

This switching of the CPU from one process to another ensures that multiple processes can share the CPU effectively, but it involves overhead due to saving and loading register states.


## How are processes created in the system?

##  How do processes communicate? Is this efficient?

### Heading 3 for Subsection

#### Heading 4 for Subsubsection

##### Heading 5

###### Heading 6