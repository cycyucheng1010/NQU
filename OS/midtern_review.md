# CH1_introduction 

## Operation system goals:
1. Execute user programs and make solving user problems easier
2. Make the computer system conventient to use 
3. Use the computer hardware in an efficient manner

## Computer Ststem Structure
* Hard ware
  * CPU
  * memory
  * I/O devices
* OS
  * control and coordinates use of hardware among various applications and users
* APP 
  * word processors 
  * compilers
  * web browsers
  * database system
  * video game
* user 
  * people
  * machine
  * other computers

## What OS Do
* ease of use
* good performance
* resouce utilization

## OS Definition
* OS No universally accepted definition
* OS is a resource allocator 
 * Manages all resources
 * Decides between conflicting requests for efficient and fair resource use
* OS is a control program
 * Controls execution of programs to prevent errors and improper use of the computer 
## Computer Startup
* boostrap program is loaded at power-up or  reboot
  * stored in ROM or EPROM as firmware
  * Initializes all aspects of system ex: CPU, memory 
  * Load operating system kernel and starts execution
## Computer ststem Organization
![image](https://user-images.githubusercontent.com/62127656/140488980-1f2153f4-14cc-419e-a049-99adee09d698.png)
>透過通用匯流排存取記憶體
## Computer-System Operation
* I/O devices and the CPU can execute concurrently 
* Each device controller is in charge of a particular device type and it has a local buffer
* CPU moves data form/to main memory to/from local buffers
* I/O is form the device to local buffer of controller
* Device controller informs CPU that it has finished its operation by causing an interrupt
## Common Function of Interrupts
* Interrupt transfers control to the interrupte sevice routine generally, though the interrupt vector, which contains the addresses of all the service routines
* Interrupt architecture must save the address of the interruptrd instruction
* An operating system is interrupt driven
## Interrput Handing
* The operating system preserves the state of the CPU by storing register and the program counter
* Determines which type of interrupt has occurred:
  * polling
  * vectored interrupt system
* separate segments of code determine what action should be taken for each type of interrupt 
## Interrupt Timeline
![image](https://user-images.githubusercontent.com/62127656/140497727-a152591f-550e-4b71-89f4-82a2b3d66682.png)
>處理完後回復原本狀態

## Storage Structure
* The CPU can only access the most data from main memory 
  * the main memory also called RAM 
  * the main memory is made up of DRAM(dynamic random-access memory)
  * random access 
  * Typically volatile 
* Secondary storage -extension of main memory
  * provides large nonvolatile storage capacity
  * Disk surface is logically divided into tracks, which are subdivided into sectors
  * SSD faster than hard disks, nonvolatile and becoming more popular
* 3 important things : speed , cost volatility
* Caching 
  * copying information into faster storage system
  * main memory can be viewed as a cache for secondary storage
* Device Driver
  * for each device controller to manage I/O provides uniform interface between controller and kernel
![image](https://user-images.githubusercontent.com/62127656/140500291-2be9d319-8b0b-4d4d-9fda-72cb02c070c1.png)
> 儲存裝置的階層

## How a Modern Computer Works
![image](https://user-images.githubusercontent.com/62127656/140501357-0a9adeb9-bfdd-4f93-b2bf-5c8d034baf64.png)
>逢紐曼架構

## Computer-System Architecture
* Most system have special-purpose processors as well Multiprocessors systems growing in use and importance also known as parallel systems, tightly-coupled systems
* Advantages:
  * Increased throughput
  * Economy of scale
  * Increased reliability: graceful degradation and fault tolerrant
* two types: 
  * asymmertric miltiprocessing: each processor is assigned a special task
  * symmertric multiprocessing : each processor performs all tasks
![image](https://user-images.githubusercontent.com/62127656/140502840-1c147a4b-9bfc-49f0-890f-794389c248dc.png)
> 對稱式多元處理器架構
## A Dual-Core Design 
* Multi-chip and multicore
* Systems containing all chips 
* Chassis containing multiple separate systems
* fast than multi-single chip 
![image](https://user-images.githubusercontent.com/62127656/140503436-93024461-fff6-4d5e-8318-4db4340d6f38.png)
>雙核心晶片示意圖

## Clustered Systems
* Like multiprocessor systems, but multiple system working together
* sharing storage via a SAN(storage-area network)
* Provides a high-availability service 
  * Asymmertric clustering gas one machine in hot-standby mode
  * Symmertric clustering has multiple nodes runnung applications,monitoring each other
* Some clusters are for high-performance computing(HPC)
  * Applications must be written to use parallelization
* Some have distributed lock manager to avoid conflicting operations
![image](https://user-images.githubusercontent.com/62127656/140504532-b4d2dc93-3644-4e82-a546-78400d2f04f4.png)
>叢集式系統的一般架構

## Operating System Structure
* Multiprogramming needed for efficiency
  * aingle user cannot keep CPU and I/O devices busy at all times 
  * CPU always has one to execute
  * A subset of toatal jobs in system is kept in memory
  * one job selected and run via job scheduling
* Timesharing is logical extension in which CPU switches jobs so frequently that user can interacrt with each job while running creating interactive computing
