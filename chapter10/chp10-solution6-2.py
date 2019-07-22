'''
Victor Montoya
Chapter 10 Solution 6-1
Golf Scores
Reads Data From File
19 July 2019
'''

def main():
    open_file()

def open_file():
    golf_file = open("golf.dat", "r")
    for player in golf_file:
        player.replace("\n", "")
        print("Player Name:", player.replace(",", " Score: "))
    golf_file.close

main()