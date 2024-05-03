# input
student_score = 80

# Process: Your Solution Code Here
inputScore = input("Enter your score : ")
studentScore = int(inputScore)

if studentScore >= 80 :
    print("Nilai A")

elif studentScore <= 79 and studentScore >= 65 :
    print("Nilai B+")

elif studentScore <= 64 and studentScore >= 50 :
    print("Nilai B")

elif studentScore <=49 and studentScore >= 35 :
    print("Nilai C")

else :
    print("Nilai D")

# Output "Nilai A"