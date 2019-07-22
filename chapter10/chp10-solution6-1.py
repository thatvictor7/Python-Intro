'''
Victor Montoya
Chapter 10 Solution 6-1
Golf Scores
Save Data to File
19 July 2019
'''

def main():
    iterate()

def request_player_info():
    player_name = str(input("Enter a player's name: "))
    player_score = str(input("Enter the player's score "))
    player_data = player_name + ", " + player_score + "\n"
    write_file(player_data)
    

def iterate():
    user_input = "y"
    while user_input == "y":
        request_player_info()
        user_input = str(input("Do you want to enter another record? \n" +
                            "Enter y for yes or anything else for no: "))

def write_file(data):
    golf_file = open("golf.dat", "a")
    golf_file.write(data)
    golf_file.close

main()