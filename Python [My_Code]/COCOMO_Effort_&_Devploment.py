# Function to calculate parameters of Basic COCOMO
def calculate(table, n ,mode ,size):
	effort = 0
	time = 0
	staff = 0
	model = 0
	
	# Check the mode according to size
	if(size >= 2 and size <= 50):
		model = 0
	elif(size > 50 and size <= 300):
		model = 1
	elif(size > 300):
		model = 2
	
	print("The mode is ", mode[model])
	
	# Calculate Effort
	effort = table[model][0]*pow(size, table[model][1])
	
	# Calculate Time
	time = table[model][2]*pow(effort, table[model][3])
	
	#Calculate Persons Required
	staff = effort/time;
	
	# Output the values calculated
	print("Effort = {} Person-Month".format(round(effort)))
	print("Development Time = {} Months".format(round(time)))
	print("Average Staff Required = {} Persons".format(round(staff)))

table = [[2.4,1.05,2.5,0.38],[3.0,1.12,2.5,0.35],[3.6,1.20,2.5,0.32]]
mode = ["Organic","Semi-Detached","Embedded"]
size = 4
calculate(table, 3, mode, size)