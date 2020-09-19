# Python program to play Tic Tac Toe Game

#class containing input and output functions
class ioFunctions():
# Class containing methods to receive and validate inputs
    
    def take_input():
        isValid = False
        k=input("Enter an number between 0 and 2: ")
        while k.isdigit() == False:
            k=input("Enter an number between 0 and 2: ")
            if k.isdigit == True:
                if int(k) in range(0,3):
                    print(f"You entered {k}")
                else:
                    k=input("Enter an number between 0 and 2: ")
                
#class managDict:
# Class containing methods to manage the game dictionary



def main():
    print("Let's play Tic Tac Toe")
    ioFunctions.take_input()
        
    
if __name__ == "__main__":
    main()

