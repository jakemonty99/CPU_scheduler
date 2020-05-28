import os
import time
import sys
import math
import cpu_schedule

#Extra Credit Shortest First is located at the bottom!

def main():
	if len(sys.argv) != 3:
		print("Usage: driver.py inputFile algorithm");
		sys.exit(1)

	inputFile = sys.argv[1]
	fin = open(inputFile, 'r')

	for line in fin:
		task = line.strip().split(',')
		name = task[0]
		priority = int(task[1])
		burst = int(task[2])

		cpu_schedule.add(name, priority, burst)

        # Add the task to the scheduler's list of tasks
    

	fin.close()

	print(cpu_schedule.taskList)

	algorithm = sys.argv[2]

    # Invoke the appropriate scheduler
	
		
	if algorithm == ("FCFS"):
		print("Using first come first serve!")
		cpu_schedule.FCFS()
	elif algorithm == ("Priority"):
		print("Using priority")
		cpu_schedule.Priority()
	elif algorithm == ("RR"):
		print("Using round robin!")
		cpu_schedule.RR()
	elif algorithm == ("PriorityRR"):
		print("Using priority with round robin!")
		cpu_schedule.PriorityRR()
	elif algorithm == ("shortest"):#Extra Credit Bottom of CPU_Schedule!
		print("The shortest programs go first")
		cpu_schedule.shortest()
		

main()
