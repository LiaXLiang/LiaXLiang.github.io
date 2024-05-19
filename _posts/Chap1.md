# Chap1: &nbsp; Basic OS Functionality

## 1. The role of an operating system
### Intuition
&nbsp; Computer systems are complex machines with a large number of components. Application programmers cannot be expected to know how to program ALL kinds of devices, and even if they do, they would rewrite the exact same code for every application, for example, the code to read inputs from the keyboard. Furthermore, resources can be shared by multiple programs: expecting programs to collaborate and not mess with each other is not possible, e.g., the printer can only print one coherent job at a time. 

&nbsp; Intuitively, we can think of 
- OS as Government: Protects users from each other while allocating resources efficiently and fairly, ensuring secure and safe communication; 
- OS as Juggler: It provides the illusion of a dedicated machine with infinite memory and CPU; 
- OS as Complex System: Emphasizes that simplicity in OS design and implementation is crucial; 
- OS as History Teacher: Uses past experiences to predict future design trade-offs as technology evolves.

### Formally
&nbsp; The operating system is the **software layer** (the glue) that lies between applications and hardware. &nbsp; It can be split into two parts:

- User interface programs: libraries, shell, graphical interfaces (GUI), etc.
<br>They offer a high level of abstractions, and are usually used by user applications to manipulate the underlying system.
- Kernel: executes critical operations with a high level of privilege (*supervisor mode*) and directly interacts with hardware. 
<br>User interface programs go through the kernel to manipulate the state of the underlying hardware.  

![avatar](/Users/xxuan/Desktop/RWTH/Github_Blogs/Operating_Systems/Markdown_Images/Chap1/01_OSLayers.png)

## 2. Generic Computer Hardware Architecture
![avatar](/Users/xxuan/Desktop/RWTH/Github_Blogs/Operating_Systems/Markdown_Images/Chap1/02_Generic_Computer_Architecture.png)
#### CPU / Central Processing Unit
- CPU is the processor that performs the actual computation. How? It operates by fetching instructions from the main memory and temporarily storing them in its cache, once the required instructions and data are loaded into the cache, the CPU performs the computation tasks as dictated by the instructions. 
- There are multiple “cores” common in today’s processors

#### Main Memory
- Memory is a passive device that stores data and programs that the CPU and devices uses during operation.

#### I/O devices
- e.g., terminal, disks, video board, printer, etc. Note that Network card is a key component, but also an I/O device

#### System Bus
- The system bus is a communication medium that connects the CPU, memory, and peripherals. It consists of a *data bus*, *address bus*, and *control bus*, which together enable data transfer, address communication, and control signals to flow between the components. 

## 3. Architectural Features Motivated by OS Services
OS Service| Hardware Support
------------ | -------------
Protection | Kernel/user mode, protected instructions, base/limit registers
System Calls | Trap instructions and trap vectors
Interrupts | Interrupt vectors
I/O | Interrupts and memory mapping
Scheduling, error recovery, accounting | Timer
Synchronization | Atomic instructions
Virtual Memory | Translation look-aside buffers

### I. Protection
#### Intuition
The need for isolation is crucial. Certain operations, if performed incorrectly, can compromise the entire system:
- Modify the state of a device. 
<br>e.g., modify the state of the microphone LED to make it look muted when it is not; make a USB drive from read-only to writable 
- Access restricted memory areas.
<br> e.g., modify a variable from another program; read private data like passwords from other programs. 

&nbsp; We cannot trust all application software to do these critical operations. Furthermore, there could be malicious programmers that want to attack a system, so the  operating system needs to isolate these operations to make the system safe and secure. 
<br>&nbsp; In order to provide the necessary isolation, operating systems provide different protection domains or modes.
<br>&nbsp; These domains give different capabilities to the code executing on the machine. Usually, two protection domains are provided: **Supervisor mode** and **User mode**. They have different privilege levels, allowing or restricting a set of operations.

#### Method(1): Simplest Technique:  Base & Limit registers
Base and limit registers are loaded by the OS before starting a program. 
<br> The CPU checks each user reference (instruction and data addresses), ensuring it falls between the base and limit register values.

![avatar](/Users/xxuan/Desktop/RWTH/Github_Blogs/Operating_Systems/Markdown_Images/Chap1/03_Baselimit_Register.png)

<br> *Register* is a dedicated name for one word of memory managed by CPU  (one word: CPU一次能并行处理的二进制位数)
General Purpose Registers/通用目的寄存器 | Special Purpose Registers/特殊目的寄存器
------------ | -------------
General Purpose Registers are like the *workbench* of a computer, storing temporary data and intermediate results. | Special purpose registers are like a *specialized toolbox*, holding the tools needed to perform specific tasks.
Data Registers / 数据寄存器<br> ① Store operands and results of calculations. (存储计算的操作数及结果) <br>② The size of data registers is often used to classify processors: 32- or 64-bit processors. | SP / Stack Pointer<br>存储堆栈指针
Address Registers / 地址寄存器 <br> Store memory addresses of operands or instructions | FP / Frame Pointer
Status Register / 状态寄存器 <br> Store the state after an instruction (存储指令执行后的状态)| Program Counter / 程序计数器 <br>Store the address of the **next** instruction to be executed
Interrupt Control Register / 中断控制寄存器  | Instructrion Register / 指令寄存器 <br> Store the instruction being processed

#### Method(2): Kernel Mode v.s. User Mode
|   | Kernel Mode | User Mode |
------------ | ------------- | -------------
Components | core OS components + many drivers| applications + some drivers
Location| Main Memory <br><br> The kernel encompasses nearly all operating system services. Since it requires direct access to core functionalities, it is essential for the kernel to always reside in main memory to ensure quick access.
| Shared v.s. Single | All code executed in kernel mode shares a single virtual address space. A kernel-mode driver does not isolate itself from other kernel mode drivers or the OS itself. |  A user mode application is activated <br> $\rightarrow$ The OS creates a process for this application <br> $\rightarrow$ This process provides the application with a private virtual address space and a private handle table, ensuring that one application cannot modify the data of another, as each application operates independently.

Accordingly, we can divide a set of assembly instructions which CPU support into two basic categories: *Regular Instructions*, which can be executed by anyone; and *Privileged Instructions*, which can only be executed by the kernel. The execution of these instructions depends on the type of code running on the processor.



### II. System Calls
&nbsp; A system call is an OS procedure that executes privileged instructions, such as I/O operations, and serves as an API exported by the kernel. 

-  When a system call is made, it causes a trap (*Traps* are special conditions detected by the architecture).
- The hardware detects the trap and:
  - Saves the state of the process (Program Counter, stack, etc.).
  - Transfers control to the appropriate Trap Handler (an OS routine within the OS kernel).
- The trap handler performs the following steps:
  - Uses the system call parameters to direct execution to the appropriate service routine (e.g., I/O, Terminal).
  - Saves the caller's state, including the Program Counter, stack, and mode bit, ensuring control can be restored to the user process afterward.
- The CPU actions:
  - Indexes the memory-mapped trap vector using the trap number.
  - Jumps to the address given in the vector.
Begins execution at that address.
  - Upon completion of the trap handling, the OS:
    -  resumes execution of the interrupted process; 
    -  returns to user mode, ensuring the system architecture allows verification of the caller's parameters and restoration of the user process control.


<br>&nbsp;The system architecture must allow the OS to verify the caller's parameters and provide a mechanism to return to user mode upon completion of the system call.

### III. Scheduling, error recovery, accounting
Timer - Accounting and Billing: 
<br>Keeps track of the time an active process has been running on the CPU; Ensuring Fair CPU Scheduling

→ The timer issues an interrupt periodically.
<br>→ When the interrupt occurs, control is taken away from the executing process and transferred back to the OS.
<br>→ The OS can then select a new process to execute.

### IV. Virtual Memory
- Virtual memory allows users to run programs without loading the entire program into memory at once. Instead, parts of the program are loaded as needed. The OS must keep track of which parts of the program are in which parts of physical memory, and which parts are on the disk. 
- To ensure that parts of the program can be loaded without causing major disruptions, the hardware provides a translation lookaside buffer (TLB) to speed up the lookup process.



## ⭐️ Definitions

- **Processor/处理器**: The hardware component, typically referring to the CPU (Central Processing Unit).
- **Core/核心**: An independent unit within a processor that can execute instructions and tasks independently. A processor may have one or multiple cores, enabling the CPU to handle multiple tasks simultaneously.
- **Kernel/内核**: The core component of an operating system, responsible for scheduling tasks to be executed on the various cores of the CPU.
 





#### Heading 4 for Subsubsection

##### Heading 5

###### Heading 6


# Heading 1 for Chapter title

## Heading 2 for Section

### Heading 3 for Subsection

#### Heading 4 for Subsubsection

##### Heading 5

###### Heading 6