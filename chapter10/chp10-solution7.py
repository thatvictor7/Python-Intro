'''
Victor Montoya
Chapter 10 Solution 7
Best Golf Scores
Reads Data From File
19 July 2019
'''

top_scorer = None
score = 0

def main():
    open_file()

def open_file():
    golf_file = open("golf.dat", "r")
    for player in golf_file:
        # player.replace("\n", "")
        player.strip("\n")
        print("Player Name:", player.replace(",", " Score: "))
        check_high_score(player)
    golf_file.close
    print("The player with the best score is ", top_scorer)
    golf_file.close

def check_high_score(data):
    global score
    global top_scorer
    if int(data.split(',')[1]) > score:
        score = int(data.split(',')[1])
        top_scorer = data.split(',')[0]

main()