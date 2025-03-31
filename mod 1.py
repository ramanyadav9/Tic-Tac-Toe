def sum(a,b,c):
    return a+b+c

def printBoard(xstate, zstate):
    zero = 'X' if xstate[0] else ('O' if zstate[0] else 0)
    one = 'X' if xstate[1] else ('O' if zstate[1] else 1)
    two = 'X' if xstate[2] else ('O' if zstate[2] else 2)
    three = 'X' if xstate[3] else ('O' if zstate[3] else 3)
    four = 'X' if xstate[4] else ('O' if zstate[4] else 4)
    five = 'X' if xstate[5] else ('O' if zstate[5] else 5)
    six = 'X' if xstate[6] else ('O' if zstate[6] else 6)
    seven = 'X' if xstate[7] else ('O' if zstate[7] else 7)
    eight= 'X' if xstate[8] else ('O' if zstate[8] else 8)

    print("*********")
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|--")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight} ")
    print("*********")

def checkwin(xstate, zstate):
    winning_combos = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]
    for win in winning_combos:
        if(sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3):
            print("\nX WON THE MATCH !")
            return 1
        if(sum(zstate[win[0]], zstate[win[1]], zstate[win[2]]) == 3):
            print("\nO WON THE MATCH !")
            return 0
    return -1    




if __name__=="__main__":
    while True:
        xstate =[0,0,0,0,0,0,0,0,0]
        zstate =[0,0,0,0,0,0,0,0,0]
        turn = 1 # 1 for X and 0 for O
        print("WELCOME to TIC TAC TOE ")
        while True:
            printBoard(xstate, zstate)
            print("ENTER THE NUMBER FROM THE BOARD ON YOUR CHANCE!\n")
            
            if turn == 1:
                print("X CHANCE")
            else:
                print("O CHANCE")
            
            try:
                val = int(input("Enter a Value: "))
                
                if 0 <= val <= 8 and xstate[val] == 0 and zstate[val] == 0:
                    if turn == 1:
                        xstate[val] = 1
                    else:
                        zstate[val] = 1
                else:
                    print("Invalid move. Try again.")
                    continue
                    
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            cwin = checkwin(xstate, zstate)

            if cwin != -1:
                print(f"\nHURRAYYYY...")
                break
            elif all(x != 0 for x in xstate) and all(z != 0 for z in zstate):
                print("It's a draw! Nobody wins.")
                break

            turn = 1 - turn
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break