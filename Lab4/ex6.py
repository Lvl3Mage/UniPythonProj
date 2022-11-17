from test_module import test
from ex4 import ContentGC
from ex5 import MaxRepetitionsCAG

def Menu(menuTitle, menuItems, menuPrompt="Please select one of the options listed above: ", menuError="Option not valid"):
    print(menuTitle)
    menuOptions = []
    for menuItem in menuItems:
        menuOptions.append(menuItem[0])
        print("{0}) {1}".format(menuItem[0], menuItem[1]))

    userInput = None
    while(userInput not in menuOptions):
        userInput = input(menuPrompt)
        if(userInput not in menuOptions):
            print(menuError)
    return userInput

    
if __name__== '__main__':
    # this would be much easier with a dict
    actions = [('a',MaxRepetitionsCAG), ('b', ContentGC)]
    menuItems = [('a', 'Max repetitions of the "CAG" sequence'), ('b', 'Percentage content of the values G and C')]
    

    dnaString = input("Enter a dna string: ").upper()

    userInput = Menu("DNA operations", menuItems)
    for action in actions:
        if(action[0] == userInput):
            print("The result of the selected operation was '{0}'".format(action[1](dnaString)))
            #break
