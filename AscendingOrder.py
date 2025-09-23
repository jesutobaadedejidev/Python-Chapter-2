num1 = float(input("Enter the first floating point number: "))
num2 = float(input("Enter the second floating point number: "))
num3 = float(input("Enter the third floating point number: "))

if num1 > num2 and num1 > num3 and num2 > num3:
	print(num3, num2, num1)
elif num1 > num2 and num1 > num3 and num3 > num2:
	print(num2, num3, num1)
elif num2 > num1 and num2 > num3 and num1 > num3:
	print(num3, num1, num2)
elif num2 > num1 and num2 > num3 and num3 > num1:
	print(num1, num3, num2)
elif num3 > num1 and num3 > num2 and num2 > num1:
	print(num1, num2, num3)
else:
	print(num2, num1, num3)

