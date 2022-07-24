# This program asks the user to enter how many basketball points that they had in their last five games.
# This program displays a scale for each score and the average test score.
# This is regardless of position.
# The following functions are in the program:

# PPG — AKA Points Per Game. This function accepts five scores as arguments
# and return the average of the scores.

# determineGrade — This function accepts a points score as an argument
# and return a letter scale for the score based on the following grading scale:

#    Score          Letter Grade
#   Above 30        Excellent
#   20 - 29         Good
#   10 - 19         Average
#   5 - 9           Poor
#   Below 5         Very Poor

# Starting out with Python. Third Edition. Tony Gaddis

# Reference
# 5.15 (Part 1) Test Average and Grade - Python. (2017).
# Retrieved from https://www.youtube.com/watch?v=J_DlZ0iS2f8

# 5.15 (Part 2) Test Average and Grade - Python. (2017).
# Retrieved from https://www.youtube.com/watch?v=J_DlZ0iS2f8

print("Hello, this program will ask how much points you had throughout the last five basketball games.")
print("With that said, here it is")

print()

def determineGrade(userPoints):
    if (userPoints >= 0 and userPoints <= 5):
        return "Very Poor"
    elif (userPoints >= 6 and userPoints <= 9):
        return "Poor"
    elif (userPoints >= 10 and userPoints <= 19):
        return "Average"
    elif (userPoints >= 20 and userPoints <= 29):
        return "Good"
    elif (userPoints >= 30):
        return "Excellent"

def askForScores():
        points1 = int(input("Please enter how many points you had in game one: "))
        points2 = int(input("Please enter how many points you had in game two: "))
        points3 = int(input("Please enter how many points you had in game three: "))
        points4 = int(input("Please enter how many points you had in game four: "))
        points5 = int(input("Please enter how many points you had in game five: "))
        return points1, points2, points3, points4, points5


def printTableOfResults(points1, points2, points3, points4, points5):
    print("Score\tLetter Grade")
    print(str(points1) + "\t\t" + determineGrade(points1),
          str(points2) + "\t\t" + determineGrade(points2),
          str(points3) + "\t\t" + determineGrade(points3),
          str(points4) + "\t\t" + determineGrade(points4),
          str(points5) + "\t\t" + determineGrade(points5), sep="\n")
    average = (points1 + points2 + points3 + points4 + points5) / 5
    print()
    print("You averaged " + str(average) + " points a game in the last five games.")

def main():
    points1, points2, points3, points4, score5 = askForScores()
    print()
    printTableOfResults(points1, points2, points3, points4, score5)

main()
print()
input('Press ENTER to exit')

