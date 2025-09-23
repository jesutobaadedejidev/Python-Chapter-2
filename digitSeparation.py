num1 = int(input("Enter a five digit number: "))
num2 = (num1 // 10000)
num3 = ((num1 % 10000) // 1000)
num4 = (((num1 % 10000) %  1000) // 100 )
num5 = ((((num1 % 10000) % 1000) % 100) // 10)
num6 = ((((num1 % 10000) % 1000) % 100) % 10)

print(num2,"   ",num3,"   ",num4,"   ",num5,"   ",num6)
