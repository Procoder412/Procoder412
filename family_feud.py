guess = input("please guess a word : ")
turn = 1
team1score = 0
team2score = 0
team1strikes = 0
team2strikes = 0
guessword = {"one": 1, 'two':2, 'three':3}


if guess in guessword:
    
    team1score += guessword[guess]
    print("team1 score: ")
    print(team1score)
else:
    team1strikes += 1
    print("theam1 has the following strikes : ")
    print(team1strikes)

turn = 2


guessword = {"one": 1, 'two':2, 'three':3}


if guess in guessword:
    print("team1 score : ")
    team1score += guessword[guess]
    print("team1 score: ")
    print(team1strikes)
