import random

class Process:
    def __init__(self, process_id, num_tickets):
        self.process_id = process_id
        self.num_tickets = num_tickets

class Scheduler:
    def __init__(self):
        self.processes = []
        self.total_tickets = 0

    def add_process(self, process):
        self.processes.append(process)
        self.total_tickets += process.num_tickets

    def allocate_tickets(self):
        for process in self.processes:
            process.lottery_tickets = random.sample(range(1, self.total_tickets + 1), process.num_tickets)

    def select_winner(self):
        winning_ticket = random.randint(1, self.total_tickets)
        for process in self.processes:
            if winning_ticket in process.lottery_tickets:
                return process

if __name__ == "__main__":
    # Sample usage
    scheduler = Scheduler()

    process1 = Process(1, 5)
    process2 = Process(2, 3)
    process3 = Process(3, 2)

    scheduler.add_process(process1)
    scheduler.add_process(process2)
    scheduler.add_process(process3)

    scheduler.allocate_tickets()

    winner = scheduler.select_winner()
    print(f"Process {winner.process_id} wins the lottery!")
