score1 = int(input("Enter the first score: "))
score2 = int(input("Enter the second score: "))
score3 = int(input("Enter the third score: "))

if score1 > score2 and score1 > score3:
	print(score1)
elif score2 > score1 and score2 > score3:
	print(score2)
else:
	print(score3)