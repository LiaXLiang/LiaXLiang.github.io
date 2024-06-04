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

<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap1/01_OSLayers.png?raw=true" alt="OS Layers">
</figure>

## 2. Generic Computer Hardware Architecture

<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap1/02_Generic_Computer_Architecture.png?raw=true" alt="Generic Computer Architecture">
</figure>
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
| OS Service | Hardware Support |
|:------------ | -------------:|
| Protection | Kernel/user mode, protected instructions, base/limit registers |
| System Calls | Trap instructions and trap vectors |
| Interrupts | Interrupt vectors |
| manage I/O devices | Interrupts and memory mapping |
| Scheduling, error recovery, accounting | Timer |
| Synchronization | Atomic instructions |
| Virtual Memory | Translation look-aside buffers|


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

<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap1/03_Baselimit_Register.png?raw=true" alt="Base- Limit Registers">
</figure>


<br> *Register* is a dedicated name for **one word of memory** managed by CPU  
(one word: CPU一次能并行处理的二进制位数)

| General Purpose Registers/通用目的寄存器 | Special Purpose Registers/特殊目的寄存器 |
|:------------|:-------------:|
| General Purpose Registers are like the *workbench* of a computer, storing temporary data and intermediate results. | Special purpose registers are like a *specialized toolbox*, holding the tools needed to perform specific tasks. |
| Data Registers / 数据寄存器 <br> ① Store operands and results of calculations. (存储计算的操作数及结果) <br>② The size of data registers is often used to classify processors: 32- or 64-bit processors. | SP / Stack Pointer <br>存储堆栈指针 |
| Address Registers / 地址寄存器 <br> Store memory addresses of operands or instructions | FP / Frame Pointer |
| Status Register / 状态寄存器 <br> Store the state after an instruction (存储指令执行后的状态) | Program Counter / 程序计数器 <br>Store the address of the **next** instruction to be executed |
| Interrupt Control Register / 中断控制寄存器 | Instruction Register / 指令寄存器 <br> Store the instruction being processed |


#### Method(2): Kernel Mode v.s. User Mode

|   | Kernel Mode | User Mode |
|:------------ |:-------------| :-------------|
| **Components** | core OS components + many drivers | applications + some drivers |
| **Location** | Main Memory <br><br> The kernel encompasses nearly all operating system services. Since it requires direct access to core functionalities, it is essential for the kernel to always reside in main memory to ensure quick access. | - |
| **Shared vs. Single** | All code executed in kernel mode shares a single virtual address space. A kernel-mode driver does not isolate itself from other kernel mode drivers or the OS itself. | A user mode application is activated <br> → The OS creates a process for this application <br> → This process provides the application with a private virtual address space and a private handle table, ensuring that one application cannot modify the data of another, as each application operates independently. |


Accordingly, we can divide a set of assembly instructions which CPU support into two basic categories: *Regular Instructions*, which can be executed by anyone; and *Privileged Instructions*, which can only be executed by the kernel. The execution of these instructions depends on the type of code running on the processor.



### II. System Calls
#### Intuition 
&nbsp; System calls are the *interface* provided by the OS for user programs to access OS services. Any operation that a user process is not permitted to perform directly, because it is protected by the kernel, must be requested via these system calls. The kernel processes these requests, executes the necessary operations, and returns the result or data back to the user processes. 
<br> &nbsp; Typically, programmers do not issue system calls directly. Instead, we use APIs provided by high-level languages like C or C++. These APIs abstract the complexity of system calls, offering a simpler and more user-friendly interface. 

#### Formal
&nbsp; A system call is an OS procedure that executes privileged instructions, such as I/O operations, and serves as an API exported by the kernel. 

-  When a system call is made, it causes a trap (*Traps* are special conditions detected by the architecture).
- The hardware detects the trap and:
  - Saves the state of the process (Program Counter, stack, etc.).
  - Transfers control to the appropriate Trap Handler (an OS routine within the OS kernel).
- The trap handler performs the following steps:
  - Uses the system call parameters to direct execution to the appropriate service routine (e.g., I/O, Terminal handling).
  - Saves the caller's state, including the Program Counter, stack, and mode bit, ensuring control can be restored to the user process afterward.
- The CPU actions:
  - Indexes the memory-mapped trap vector using the trap number.
  - Jumps to the address given in the vector.
Begins execution at that address.
  - Upon completion of the trap handling, the OS:
    -  resumes execution of the interrupted process; 
    -  returns to user mode, ensuring the system architecture allows verification of the caller's parameters and restoration of the user process control.


<br> &nbsp; Passing parameters to the OS often requires more information. The exact type and amount of information vary according to the OS and the specific call. There are three general methods to pass parameters：
- **Passing parameters in registers**: The simplest method is passing parameters in registers, but this is limited by the number of available registers. 
- **Using a block or table in memory**: parameters can be stored in a block or table in memory, with the address of this block passed as a parameter in a register. This approach is used by Linux and Solaris. 
- **Placing parameters onto the stack**: The program places parameters onto the stack, which the OS then pops off. The block and stack methods do not limit the number or length of parameters being passed. 

### III. Scheduling, error recovery, accounting
Timer - Accounting and Billing: 
<br>Keeps track of the time an active process has been running on the CPU; Ensuring Fair CPU Scheduling

→ The timer issues an interrupt periodically.
<br>→ When the interrupt occurs, control is taken away from the executing process and transferred back to the OS.
<br>→ The OS can then select a new process to execute.

### IV. Virtual Memory
- Virtual memory allows users to run programs without loading the entire program into memory at once. Instead, parts of the program are loaded as needed. The OS must keep track of which parts of the program are in which parts of physical memory, and which parts are on the disk. 
- To ensure that parts of the program can be loaded without causing major disruptions, the hardware provides a Translation Lookaside Buffer (TLB) to speed up the lookup process.



## ⭐️ Definitions

- **Processor/处理器**: The hardware component, typically referring to the CPU (Central Processing Unit).
- **Core/核心**: An independent unit within a processor that can execute instructions and tasks independently. A processor may have one or multiple cores, enabling the CPU to handle multiple tasks simultaneously.
- **Kernel/内核**: The core component of an operating system, responsible for scheduling tasks to be executed on the various cores of the CPU.
 
## ⭐️ 4 main types of Kernels
|  | Monolithic Kernels <br>/ 宏内核 | Microkernel <br>/ 微内核 | Hybrid kernels <br>/ 混合内核 | Unikernels <br>/ 单一内核|
|:------------ |:-------------|:-------------|:-------------|:-------------|
| Characteristics| · A monolithic kernel provides, in kernel space, a large amount of core features, e.g., process and memory management, synchronization, file systems, etc., as well as device drivers. <br><br> · Defines a high level interface through system calls. <br><br> · All modules share the same address space and system resources in the kernel. | · A microkernel contains only the minimal set of features needed in kernel space: address-space management, basic scheduling and basic inter-process communication. <br><br> · All other services are pushed in user space as servers: file systems, device drivers, high level interfaces, etc. | · The hybrid kernel architecture sits between *monolithic kernels* and *microkernels*.  <br><br>· It is a monolithic kernel where some components have been moved out of kernel space as servers running in user space.  <br><br>· While the structure is similar microkernels, i.e., using user servers, hybrid kernels do not provide the same safety guarantees as most components still run in the kernel. | · A unikernel, or *library operating system*, embeds ALL the software in supervisor mode. <br><br>· The kernel as well as all user applications run in the same privileged mode. <br><br>· It is used to build single application operating systems, embedding only the necessary set of applications in a minimal image.|
|(+) | Good performance when kernel components communicate (regular function calls in kernel space) | · Small memory footprint, making it a good choice for embedded systems <br>  ·  Enhanced safety: when a user space server crashes, it does not crash the whole system <br> · Adaptability: servers can be replaced/updated easily, without rebooting | - | · High peformance: system calls become regular function calls and no copies between user and kernel spaces <br> · Security: attack surface is minimized, easier to harden.|
|(-) | Limited safety: Even separate programs within the kernel operate with the same privileges, increasing the risk of widespread system issues from a single fault. i.e., if one kernel component crashes, the whole system crashes | Limited performance: IPCs are costly and numerous in such an architecture | - | Usability: hard to build unikernels due to lack of features supported|
|Examples | Unix family: BSD, Solaris <br> Unix-like: Linux <br> DOS: MS-DOS <br>Critical embedded systems: Cisco IOS | Minix <br> L4 family: seL4, OKL4, sepOS <br> Mach <br> Zircon |  Windows NT <br> XNU (Mach + BSD)| Unikraft <br> clickOS <br> IncludeOS

<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap1/04_Kernel_Architectures.png?raw=true" alt="Kernel Architectures">
</figure>




