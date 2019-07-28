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
        print("Player Name:", player.replace(",", " Score: ").strip("\n"))
    golf_file.close

main()