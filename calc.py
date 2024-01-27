import sys


a = sys.argv[1]
b = sys.argv[3]
operation = sys.argv[2]
file = open("./tmp/result.txt", "w")
result = f"Not recognizable operator {operation}."
if operation == "+":
	result = f"{a} {operation} {b} = {int(a) + int(b)}"
elif operation == "-":
	result = f"{a} {operation} {b} = {int(a) - int(b)}"
elif operation == "/":
	result = f"{a} {operation} {b} = {int(a) / int(b)}"
elif operation == "*":
	result = f"{a} {operation} {b} = {int(a) * int(b)}"
file.write(result)
print(result)
