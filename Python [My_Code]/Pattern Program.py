def function(n):
	for i in range(0, n):
		for j in range(0, i+1):
			print("* ",end="")
		print("\r")
n = int(input("ENTER A NUMBER: "))
function(n)
