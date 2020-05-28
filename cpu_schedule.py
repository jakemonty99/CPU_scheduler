import os
import time
import sys
import math

taskList = []
QUANTUM = 10

#Extra Credit Shortest First is located at the bottom!

def run(task, timeSlice):
	print("Running task = [", task["name"], "], [", task["priority"], "] [", task["burst"], "] for ", timeSlice, " units.")
	

def add(name, priority, burst):
    # Provide definition for add function here
	Dict = {"name": name,"priority": priority,"burst": burst}
	taskList.append(Dict)
# Implement your CPU schedule algorithms here

def FCFS():#Print all the task in the order they were entered in
	n = 0
	while n < len(taskList):
		taskList[n]
		run(taskList[n], taskList[n]["burst"])
		n += 1


	
		

def Priority():#Compare all the task and have the ones with the highest priority go first
	p = 0	
	n = 0
	print("Run task with the hieghest priority first!")
	while len(taskList) != 0:
		if taskList[p]["priority"] >= taskList[n]["priority"]:
			
			if n == len(taskList) - 1:
				run(taskList[p],taskList[p]["burst"]) 
				taskList.remove(taskList[p])#Remove from list once done
				p = 0
				n = 0	
			else:
				n += 1								
		else:
			if p == len(taskList) - 1:
				p = 0
			else:
				p += 1
			

	
			
		
				
		
	


def RR():#Run each task in the order they came in but they only have 10 millieseconds to finissh before being swapped out
	print("Run task in order by increments of 10 milliseconds!")
	n = 0
	while len(taskList) != 0:
		if taskList[n]["burst"] <= 10:
			run(taskList[n], taskList[n]["burst"])			
			taskList.remove(taskList[n]) #Remove from list once done
			
			
		else:
			
			run(taskList[n], 10)
			taskList[n]["burst"] = (taskList[n]["burst"] - 10)
			if n == len(taskList) - 1:
				n = 0
			else:
				n += 1
	



def PriorityRR():
#Run each task with the hieghest priority going first, if they tie then execute those using round robin until finished
	Q10 = []
	Q9 = []
	Q8 = []
	Q7 = []
	Q6 = []
	Q5 = []
	Q4 = []
	Q3 = []
	Q2 = []
	Q1 = []
	n = 0
#Move each task with the given priority into its own queue and then run each individual queue
	while n <= len(taskList) - 1:
		if taskList[n]["priority"] == 10:
			Q10.append(taskList[n])
			n += 1

		elif taskList[n]["priority"] == 9:
			Q9.append(taskList[n])
			n += 1

		elif taskList[n]["priority"] == 8:
			Q8.append(taskList[n])
			n += 1

		elif taskList[n]["priority"] == 7:
			Q7.append(taskList[n])
			n += 1

		elif taskList[n]["priority"] == 6:
			Q6.append(taskList[n])
			n += 1

		elif taskList[n]["priority"] == 5:
			Q5.append(taskList[n])
			n += 1

		elif taskList[n]["priority"] == 4:
			Q4.append(taskList[n])
			n += 1

		elif taskList[n]["priority"] == 3:
			Q3.append(taskList[n])
			n += 1

		elif taskList[n]["priority"] == 2:
			Q2.append(taskList[n])
			n += 1

		elif taskList[n]["priority"] == 1:
			Q1.append(taskList[n])	
			n += 1
	T = True
	while T == True: #Run each queue, if multiple use round robin to execute	
		if len(Q10) == 1:
			run(Q10[0],Q10[0]["burst"])
			Q10.remove(Q10[0])
		elif len(Q10) > 1:
			print("Run task in order by increments of 10 milliseconds!")
			n = 0
			while len(Q10) != 0:
				if Q10[n]["burst"] <= 10:
					run(Q10[n], Q10[n]["burst"])			
					Q10.remove(Q10[n])
			
				else:
					
					run(Q10[n], 10)
					Q10[n]["burst"] = (Q10[n]["burst"] - 10)
					if n == len(Q10) - 1:
						n = 0
					else:
						n += 1
	
		elif len(Q9) == 1:
			run(Q9[0],Q9[0]["burst"])
			Q9.remove(Q9[0])
		elif len(Q9) > 1:
			print("Run task in order by increments of 10 milliseconds!")
			n = 0
			while len(Q9) != 0:
				if Q9[n]["burst"] <= 10:
					run(Q9[n], Q9[n]["burst"])			
					Q9.remove(Q9[n])
			
				else:
					
					run(Q9[n], 10)
					Q9[n]["burst"] = (Q9[n]["burst"] - 10)
					if n == len(Q9) - 1:
						n = 0
					else:
						n += 1
		
		elif len(Q8) == 1:
			run(Q8[0],Q8[0]["burst"])
			Q8.remove(Q8[0])
		elif len(Q8) > 1:
			print("Run task in order by increments of 10 milliseconds!")
			n = 0
			while len(Q8) != 0:# change to end when list is empty
				if Q8[n]["burst"] <= 10:
					run(Q8[n], Q8[n]["burst"])			
					Q8.remove(Q8[n])
			
				else:
					
					run(Q8[n], 10)
					Q8[n]["burst"] = (Q8[n]["burst"] - 10)
					if n == len(Q8) - 1:
						n = 0
					else:
						n += 1
	
		elif len(Q7) == 1:
			run(Q7[0],Q7[0]["burst"])
			Q7.remove(Q7[0])
		elif len(Q7) > 1:
			print("Run task in order by increments of 10 milliseconds!")
			n = 0
			while len(Q7) != 0:# change to end when list is empty
				if Q7[n]["burst"] <= 10:
					run(Q7[n], Q7[n]["burst"])			
					Q7.remove(Q7[n])
			
				else:
					
					run(Q7[n], 10)
					Q7[n]["burst"] = (Q7[n]["burst"] - 10)
					if n == len(Q7) - 1:
						n = 0
					else:
						n += 1
	
		elif len(Q6) == 1:
			run(Q6[0],Q6[0]["burst"])
			Q6.remove(Q6[0])
		elif len(Q6) > 1:
			print("Run task in order by increments of 10 milliseconds!")
			n = 0
			while len(Q6) != 0:# change to end when list is empty
				if Q6[n]["burst"] <= 10:
					run(Q6[n], Q6[n]["burst"])			
					Q6.remove(Q6[n])
			
				else:
					
					run(Q6[n], 10)
					Q6[n]["burst"] = (Q6[n]["burst"] - 10)
					if n == len(Q6) - 1:
						n = 0
					else:
						n += 1
	
		elif len(Q5) == 1:
			run(Q5[0],Q5[0]["burst"])
			Q5.remove(Q5[0])
		elif len(Q5) > 1:
			print("Run task in order by increments of 10 milliseconds!")
			n = 0
			while len(Q5) != 0:# change to end when list is empty
				if Q5[n]["burst"] <= 10:
					run(Q5[n], Q5[n]["burst"])			
					Q5.remove(Q5[n])
			
				else:
					
					run(Q5[n], 10)
					Q5[n]["burst"] = (Q5[n]["burst"] - 10)
					if n == len(Q5) - 1:
						n = 0
					else:
						n += 1

		elif len(Q4) == 1:
			run(Q4[0],Q4[0]["burst"])
			Q4.remove(Q4[0])
		elif len(Q4) > 1:
			print("Run task in order by increments of 10 milliseconds!")
			n = 0
			while len(Q4) != 0:# change to end when list is empty
				if Q4[n]["burst"] <= 10:
					run(Q4[n], Q4[n]["burst"])			
					Q4.remove(Q4[n])
			
				else:
					
					run(Q4[n], 10)
					Q4[n]["burst"] = (Q4[n]["burst"] - 10)
					if n == len(Q4) - 1:
						n = 0
					else:
						n += 1

		elif len(Q3) == 1:
			run(Q3[0],Q3[0]["burst"])
			Q3.remove(Q3[0])
		elif len(Q3) > 1:
			print("Run task in order by increments of 10 milliseconds!")
			n = 0
			while len(Q3) != 0:# change to end when list is empty
				if Q3[n]["burst"] <= 10:
					run(Q3[n], Q3[n]["burst"])			
					Q3.remove(Q3[n])
			
				else:
					
					run(Q3[n], 10)
					Q3[n]["burst"] = (Q3[n]["burst"] - 10)
					if n == len(Q3) - 1:
						n = 0
					else:
						n += 1

		elif len(Q2) == 1:
			run(Q2[0],Q2[0]["burst"])
			Q2.remove(Q2[0])
		elif len(Q2) > 1:
			print("Run task in order by increments of 10 milliseconds!")
			n = 0
			while len(Q2) != 0:# change to end when list is empty
				if Q2[n]["burst"] <= 10:
					run(Q2[n], Q2[n]["burst"])			
					Q2.remove(Q2[n])
			
				else:
					
					run(Q2[n], 10)
					Q2[n]["burst"] = (Q2[n]["burst"] - 10)
					if n == len(Q2) - 1:
						n = 0
					else:
						n += 1

		elif len(Q1) == 1:
			run(Q1[0],Q1[0]["burst"])
			Q1.remove(Q1[0])
		elif len(Q1) > 1:
			print("Run task in order by increments of 10 milliseconds!")
			n = 0
			while len(Q1) != 0:# change to end when list is empty
				if Q1[n]["burst"] <= 10:
					run(Q1[n], Q1[n]["burst"])			
					Q1.remove(Q1[n])
			
				else:
					
					run(Q1[n], 10)
					Q5[n]["burst"] = (Q1[n]["burst"] - 10)
					if n == len(Q1) - 1:
						n = 0
					else:
						n += 1
		else:
			T = False

def shortest():#Compare all the task and have the ones with the shortest burst go first
	p = 0	
	n = 0
	print("Run task with the shortest burst first!")
	while len(taskList) != 0:
		if taskList[p]["burst"] <= taskList[n]["burst"]:
			
			if n == len(taskList) - 1:
				run(taskList[p],taskList[p]["burst"]) 
				taskList.remove(taskList[p])#Remove from list once done
				p = 0
				n = 0	
			else:
				n += 1								
		else:
			if p == len(taskList) - 1:
				p = 0
			else:
				p += 1
	
			
	
	



	







    

