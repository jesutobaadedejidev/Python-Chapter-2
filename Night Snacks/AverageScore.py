#Prompt the user to enter the first score and store it in a container.
#Prompt the user to enter the second score and store it in a container.
#Prompt the user to enter the third score and store it in a container.
#Get the average score by calculating the sum of the scores divided by the number of the scores.
#Check if the average score is between 90 and 100, then display A when true.
#Check if the average score is between 80 and 90, then display B when true.
#Check if the average score is between 70 and 80, then display C when true.
#Check if the average score is between 60 and 70, then display D when true.
#Check if the average score is between 0 and 60, then display F when true.






score1 = int(input("Enter the first score: "))
score2 = int(input("Enter the second score: "))
score3 = int(input("Enter the third score: "))

average_score = (score1 + score2 + score3)/3

if average_score >= 90 and average_score <= 100 :
	print("A")
elif average_score >= 80 and average_score < 90 :
	print("B")
elif average_score >= 70 and average_score < 80 :
	print("C")
elif average_score >= 60 and average_score < 70 :
	print("D")
else:
	print("F")