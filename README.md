# CS540-Assignment-2
This Python script implements a basic lottery scheduling algorithm, simulating a system where processes are assigned lottery tickets, and the scheduler randomly selects a ticket to determine the next process to run.

Implementation Details:
Process Class:
The Process class represents a process with the following attributes:

process_id: Unique identifier for the process.
num_tickets: Number of lottery tickets assigned to the process.
Scheduler Class:
The Scheduler class manages the lottery scheduling algorithm with the following methods:

1. add_process(process): Adds a process to the scheduler and updates the total_tickets counter.

2. allocate_tickets(): Allocates lottery tickets to each process based on their specified number of tickets, using random.sample to ensure uniqueness.

3. select_winner(): Randomly selects a winning process based on lottery ticket selection and returns the winning process or None if no winning process is found.