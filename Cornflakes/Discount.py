def my_discount(discount,price):
	discount_amount = price - (price * discount/100 )
	return discount_amount
amount1 = int(input("Enter the discount: "))
amount2 = int(input("Enter the price: "))

result = my_discount(amount1, amount2)
print (result)
	