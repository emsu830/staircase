# Author: Emily Su
# Last Revised: May 2021

'''
prompts user to provide the number of steps to create
'''
def getUserInput():
    return input("How many steps do you want to move?\n")


'''
parameter: number of steps
return: string containing steps determined by parameter
'''
def createSteps(stepCount):
    '''handling edge cases: non-integer input, negative input, input of 0, or input greater than 499'''
    try:
        s = int(stepCount)
    except ValueError:
        return "Invalid staircase size provided."
        
    if s < 0:
        return "Invalid staircase size provided."
        
    if s == 0:
        return "Your staircase has no steps."

    if s >= 500:
        return "I can't build a staircase that tall."
            
    '''creating steps for valid input'''
    stairs = ""
    for i in reversed(range(s)):
        if i == s-1: #top of highest step
            stairs += "  " * i + "+-+\n"
        else:
            stairs += "  " * i + "+-+-+\n"
                                
        stairs += "  " * i + "| |\n" #middle of step
            
        if i == 0: #bottom of lowest step
            stairs += "+-+"

    return stairs

    

if __name__ == "__main__":
    print(createSteps(getUserInput()))
