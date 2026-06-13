Name =input("hello! what's your name? :")
mood =input("what's your mood today? :")
emotion =float(input("Enter today's mood using our scale : "))
if emotion > 5:
    print("you are happy! keep up the good attitude to improve your mood : ")
if emotion > 8:
    print("you are very happy! continue to stay well and positive :")
else:
    print("your mood is low,please seek help or partake in enjoyable activities to improve your mood:")
if emotion > 6:
    print("mood:above 5, satisfactory mood : ")
elif emotion > 6:
    print("mood: average, attempt to improve it:")
elif emotion > 6:
    print("mood:not the best, improve mood:")
else:
    print("mood:you are very sad, please talk to someone or do something to make you happy :")