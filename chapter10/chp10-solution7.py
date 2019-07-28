'''
Victor Montoya
Chapter 10 Solution 7
Best Golf Scores
Reads Data From File
19 July 2019
'''

FIRST_ELEMENT = 0
SECOND_ELEMENT = 1

top_scorer = None
score = 0

def main():
    open_file()

def open_file():
    golf_file = open("golf.dat", "r")
    for player in golf_file:
        print("Player Name:", player.replace(",", " Score: ").strip("\n"))
        check_high_score(player)
    golf_file.close
    print("\nThe player with the best score is ", top_scorer)
    golf_file.close

def check_high_score(data):
    global score
    global top_scorer
    if int(data.split(',')[SECOND_ELEMENT]) > score:
        score = int(data.split(',')[SECOND_ELEMENT])
        top_scorer = data.split(',')[FIRST_ELEMENT]

main()