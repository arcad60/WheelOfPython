import json
import random
import sys
import time
import os
#import pygame

#Initialize the pygame
#pygame.init()
# Create the screen
#screen = pygame.display.set_mode((800,600))
# Background
#background = pygame.image.load('22.8.wheeljpg.jpg')

os.system('cls')
#os.system('color fc') # sets the background to blue
COLORS = {\
"Black": "\u001b[30m",
"Red": "\u001b[31m",
"Green": "\u001b[32m",
"Yellow": "\u001b[33m",
"Blue": "\u001b[34m",
"Magenta": "\u001b[35m",
"Cyan": "\u001b[36m",
"White": "\u001b[37m",
"Bright Black": "\u001b[30;1m",
"Bright Red": "\u001b[31;1m",
"Bright Green": "\u001b[32;1m",
"Bright Yellow": "\u001b[33;1m",
"Bright Blue": "\u001b[34;1m",
"Bright Magenta": "\u001b[35;1m",
"Bright Cyan": "\u001b[36;1m",
"Bright White": "\u001b[37;1m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
"Reset": "\u001b[0m"
}
def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]",COLORS[color])
    return text

"""with open('22.8.phrases.json','r') as f:
    s = list(json.loads(f.read()).keys())
    print(len(s))
    for k in s:
        print(k)
    print(type(s)) # 30 keys in dictionary
screen.fill((0,0,0))
#Background Image
screen.blit(background,(0,0))"""
OnOff = True
with open('22.8.graphic.txt','r') as f:
    ascii = "".join(f.readlines()) #f.readlines() return a list of each lines in the files, then  join these lines into one and turn it into a string
    print(colorText(ascii))

print("\u001b[45;1mGame On!!!\u001b[0m") # Background
while OnOff:
    class WOFPlayer():
        prizeMoney = 0 # class attribute
        prizes = []
        def __init__(self, name):
            self.name = name
            self.prizeMoney = self.prizeMoney
            self.prizes = self.prizes[:]

        def addMoney(self,amt):
            self.prizeMoney += amt

        def goBankrupt(self):
            self.prizeMoney = 0

        def addPrize(self,prize):
            self.prizes.append(prize)

        def __str__(self):
            return "{} (${})".format(self.name,self.prizeMoney)

    class WOFHumanPlayer(WOFPlayer):
        def getMove(self,category,obscuredPhrase,guessed):
            prompt_move ="{} has ${}\n".format(self.name,self.prizeMoney) +\
    "{}\n".format(showBoard(category,obscuredPhrase,guessed)) +\
    "\nGuess a letter, phrase, or type 'exit'(only you) or 'pass': """
            move = input(prompt_move)
            return move
    """
    print("\n==================Testing getmove()=====================")
    wofh = WOFHumanPlayer("Steve")
    wofh.getMove(category,obscured_phrase,guessed)
    print("===================End of Testing=====================\n")
    """
    class WOFComputerPlayer(WOFPlayer):
        SORTED_FREQUENCIES = "ZQXJKVBPYGFWMUCLDRHSNIOATE" # class variable

        def __init__(self,name,difficulty_level):
            WOFPlayer.__init__(self,name)
            self.difficulty = difficulty_level

        def smartCoinFlip(self):
            rand_number = random.randint(1,10)
            #print('smart',rand_number)
            if rand_number > self.difficulty:
                return True
            else:
                return False

        def getPossibleLetters(self,guessed): #this method collect all possible remaining letters that can be chosen

            #print(sorted(guessed))
            #print('Above in getPossibleLetters')
            g_lst = []
            for c in LETTERS:
                if (c not in guessed) and (c not in VOWELS):
                    g_lst.append(c)
                elif (c not in guessed) and (c in VOWELS):
                    #print(self.prizeMoney)
                    if self.prizeMoney > VOWEL_COST:
                        g_lst.append(c)
            #print(g_lst)
            return g_lst

        def getMove(self,category,obscuredPhrase,guessed):
            gpl_list = self.getPossibleLetters(guessed)
            #print('gpl_list in getMove',gpl_list)
            frequent = gpl_list[0]
            #print('frequent 0',frequent)
            frequent_index = self.SORTED_FREQUENCIES.find(frequent)
            #print('frequent_index 0',frequent_index)
            smart = self.smartCoinFlip()
            for s in gpl_list:
                if (s in VOWELS) and (self.prizeMoney < VOWEL_COST):
                    pass
                else:
                    if smart:
                        if frequent_index < self.SORTED_FREQUENCIES.find(s):
                            #print('good')
                            frequent = s
                            frequent_index = self.SORTED_FREQUENCIES.find(s)
                            #print('new frequent_index',frequent_index)
                            #print(frequent_index)
                            #print(frequent)
                    else:
                        #print('bad')
                        frequent = random.choice(gpl_list)
            #step = input("See computer's step")
            return frequent


    VOWEL_COST = 250
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    VOWELS = 'AEIOU'

    # Repeatedly asks the user for a number between min & max(inclusive)
    def getNumberBetween(prompt,min,max):
        userinp = input(prompt) # ask the first time

        while True:
            try:
                n = int(userinp) # try casting to an integer
                if n < min:
                    errmessage = 'Must be at least {}'.format(min)
                elif n > max:
                    errmessage = 'Must be at most {}'.format(max)
                else:
                    return n
            except ValueError: # The user didn't enter a number
            #I preferred (except Exception to error_inst:) it handled all exception
                errmessage = '{} is not a number.'.format(userinp)

                # If we haven't gotten a number yet, add the error message
                # and ask again
            userinp = input("{}\n{}".format(errmessage,prompt))

    # Spins the wheel of fortune wheel to give a random prize
    # Examples:
    #    { "type": "cash", "text": "$950", "value": 950, "prize": "A trip to Ann Arbor!" },
    #    { "type": "bankrupt", "text": "Bankrupt", "prize": false },
    #    { "type": "loseturn", "text": "Lose a turn", "prize": false }

    def spinWheel():
        with open('22.8.wheel.json','r') as f:
            wheel = json.loads(f.read()) # this's a list
            print("\nBehold the Wheel of Python's Mark up ")
            j = 64
            for i in range(len(wheel)):
                if i == 12:
                    print("\u001b[48;5;{}m||__________".format(j) +wheel[i]['type'] + ': ' + wheel[i]['text'] + ('_'*10 + 'prize: {}'.format(wheel[i]['prize']),'_'*10 + 'No prize')[isinstance(wheel[i]['prize'],bool)] + "_"*24 + "||\u001b[0m")
                elif i == 11:
                    print("\u001b[48;5;{}m||__________".format(j) + wheel[i]['type'] + ': ' + wheel[i]['text'] + ('_'*10 + 'prize: {}'.format(wheel[i]['prize']),'_'*11 + 'No prize')[isinstance(wheel[i]['prize'],bool)] + "_"*24 + "||\u001b[0m")
                elif i==10:
                    print("\u001b[48;5;{}m||__________".format(j) + wheel[i]['type'] + ': ' + wheel[i]['text'] + ('_'*10 + 'prize: {}'.format(wheel[i]['prize']),'_'*10 + 'No prize')[isinstance(wheel[i]['prize'],bool)] + "_"*28 + "||\u001b[0m")
                elif i == 9:
                    print("\u001b[48;5;{}m||__________".format(j) + wheel[i]['type'] + ': ' + wheel[i]['text'] + ('_'*10 + 'prize: {}'.format(wheel[i]['prize']),'_'*10 + 'No prize')[isinstance(wheel[i]['prize'],bool)] + "_"*12 + "||\u001b[0m")
                elif i == 8:
                    print("\u001b[48;5;{}m||__________".format(j) + wheel[i]['type'] + ': ' + wheel[i]['text'] + ('_'*10 + 'prize: {}'.format(wheel[i]['prize']),'_'*10 + 'No prize')[isinstance(wheel[i]['prize'],bool)] + "_"*15 + "||\u001b[0m")
                elif i == 7:
                    print("\u001b[48;5;{}m||__________".format(j) + wheel[i]['type'] + ': ' + wheel[i]['text'] + ('_'*10 + 'prize: {}'.format(wheel[i]['prize']),'_'*10 + 'No prize')[isinstance(wheel[i]['prize'],bool)] + "_"*10 + "||\u001b[0m")
                elif i == 6:
                    print("\u001b[48;5;{}m||__________".format(j) + wheel[i]['type'] + ': ' + wheel[i]['text'] + ('_'*10 + 'prize: {}'.format(wheel[i]['prize']),'_'*10 + 'No prize')[isinstance(wheel[i]['prize'],bool)] + "_"*33 + "||\u001b[0m")
                elif i == 5:
                    print("\u001b[48;5;{}m||__________".format(j) + wheel[i]['type'] + ': ' + wheel[i]['text'] + ('_'*10 + 'prize: {}'.format(wheel[i]['prize']),'_'*10 + 'No prize')[isinstance(wheel[i]['prize'],bool)] + "_"*25 + "||\u001b[0m")
                elif (i == 0) or (i ==1):
                    print("\u001b[48;5;{}m||__________".format(j) + wheel[i]['type'] + ': ' + wheel[i]['text'] + ('_'*10 + 'prize: {}'.format(wheel[i]['prize']),'_'*10 + '_No prize')[isinstance(wheel[i]['prize'],bool)] + "_"*34 + "||\u001b[0m")
                else:
                    print("\u001b[48;5;{}m||__________".format(j) + wheel[i]['type'] + ': ' + wheel[i]['text'] + ('_'*10 + 'prize: {}'.format(wheel[i]['prize']),'_'*10 + 'No prize')[isinstance(wheel[i]['prize'],bool)] + "_"*34 + "||\u001b[0m")
                j -= 1
            return random.choice(wheel)

            #wheel = json.loads(f.read()) # turned a string into a list or dictionary
            #return random.choice(wheel) # random item from a list is returned

    # Returns a category & phrase (as a tuple) to guess
    ## Example:
    #     ("Artist & Song", "Whitney Houston's I Will Always Love You")
    def getRandomCategoryAndPhrase():
        with open('22.8.phrases.json','r') as f:
            phrases = json.loads(f.read()) #Read method reads the whole file as a single string while readlines segregates each of the line in the file
            category = random.choice(list(phrases.keys()))
            phrase = random.choice(phrases[category])
            return (category,phrase.upper())

    # Given a phrase and list of guessed letters, returns an obscured version
    # Example:
    #     guessed: ['L', 'B', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
    #     phrase:  "GLACIER NATIONAL PARK"
    #     returns> "_L___ER N____N_L P_RK"

    def obscurePhrase(phrase, guessed):
        rv = ''
        for s in phrase:
            if (s in LETTERS) and (s not in guessed):
                rv = rv+'_'
            else:
                rv = rv+s
        return rv

    # Returns a string representing the current state of the game
    def showBoard(category, obscuredPhrase, guessed):
        return """
    Category: {}
    Phrase:   {}
    Guessed:  {}""".format(category, obscuredPhrase, ', '.join(sorted(guessed)))

    # GAME LOGIC CODE
    print("="*15)
    print("WHEEL OF PYTHON")
    print("="*15)
    print('')

    num_humnan = getNumberBetween("How many human players, at most 10: ",0,10)

    # Create the human player instances
    #"\u001b[3{};1m" | Let's try 250 color extended color set
    human_players = [WOFHumanPlayer("\u001b[38;5;{ID}m".format(ID=random.randint(1,255)) + input("Enter the name for human player #{}: ".\
    format(i+1))  + "\u001b[0m") for i in range(num_humnan)] # list comprehension

    num_computer = getNumberBetween("How many computer players?: ",0,10)

    # If there are computer players, ask how difficult they should be
    if num_computer >= 1:
        difficulty = getNumberBetween("What difficulty for the computers? (1-10): ",1,10)

    # Create the computer player instances
    computer_players = [WOFComputerPlayer("\u001b[48;5;{ID}".format(ID=8) +"mComputer {}\u001b[0m".\
    format(i+1),difficulty) for i in range(num_computer)]

    players = human_players + computer_players

    # No players, no game :(
    if len(players) == 0:
        print("We need players to play!")
        raise Exception('Not enough players') # forcing a specified exception to occur

    # category and phrase are strings.
    category, phrase = getRandomCategoryAndPhrase()
    # guessed is a list of the letters that have been guessed
    guessed = []

    # playerIndex keeps track of the index (0 to len(players)-1) of the player whose turn it is
    playerIndex = 0

    # will be set to the player instance when/if someone wins
    winner = False

    def requestPlayerMove(player,category,guessed):
        while True: # we're going to keep asking the player for a move until they give a valid one
            time.sleep(0.1) # added so that any feedback is printed out before the next prompt

            move = player.getMove(category,obscurePhrase(phrase,guessed),guessed)
            move = move.upper() # convert whatever the palyer entered to UPPERCASE
            if move == 'EXIT' or move == 'PASS':
                return move
            elif len(move) == 1: # they guessed a character
                if move not in LETTERS: # the user entered an invalid letter (suas as @, #, or $)
                    print('Guesses should be letters. Try again.')
                    continue
                elif move in guessed: # this letter has already been guessed
                    print('{} has already been guessed. Try again.'.format(move))
                    continue
                elif move in VOWELS and player.prizeMoney < VOWEL_COST: # if it's a vowel, we need to be  sure the player has enough
                    print('Need ${} to guess a vowel. Try again.'.format(VOWEL_COST))
                    continue
                else:
                    return move
            else: # they guessed the phrase
                return move

    while True:
        """if len(players) == len(num_computer):
            watch_step = input("Would you like to watch computers play?(y/n): ")
            comp_l = True
            if watch_step.upper() == 'Y':
                step = input()"""

        player = players[playerIndex]
        wheelPrize = spinWheel()

        print('')
        print('-'*15)
        print(showBoard(category,obscurePhrase(phrase,guessed),guessed))
        print('')
        print('{} spins...'.format(player.name))
        time.sleep(2) # pause for dramatic effect!
        print('{}!'.format(wheelPrize['text']))
        time.sleep(1) # pause again for more dramatic effect!

        if wheelPrize['type'] == 'bankrupt':
            player.goBankrupt()
        elif wheelPrize['type'] == 'loseturn':
            pass # do nothing; just move on to the next player
        elif wheelPrize['type'] == 'cash':
            move = requestPlayerMove(player, category, guessed)
            if move == 'EXIT': # leave the game
                players.remove(player)
                if len(players) == 0:
                    print('Until next time!')
                    break
                else:
                    playerIndex = (playerIndex) % len(players)
                    print("{} human players and {} computer players in the game".\
                    format(len(players) - num_computer,num_computer))
                    continue
            elif move == 'PASS': # will just move on to next player
                print('{} passes'.format(player.name))
            elif len(move) == 1: # they guessed a letter
                guessed.append(move)

                print('{} guesses "{}"'.format(player.name, move))
                #step_confirm
                #step = input("Watch next step(y/n): ")
                if move in VOWELS:
                    player.prizeMoney -= VOWEL_COST

                count = phrase.count(move) # returns an integer with how many times this letter appears
                if count > 0:
                    if count == 1:
                        print("There is one {}".format(move))
                    else:
                        print("There are {} {}'s".format(count, move))

                    # Give them the money and the prizes
                    player.addMoney(count * wheelPrize['value'])
                    if wheelPrize['prize']:
                        player.addPrize(wheelPrize['prize'])

                    # all of the letters have been guessed
                    if obscurePhrase(phrase, guessed) == phrase:
                        winner = player
                        break

                    continue # this player gets to go again

                elif count == 0:
                    print("There is no {}".format(move))
            else: # they guessed the whole phrase
                if move == phrase: # they guessed the full phrase correctly
                    winner = player

                    # Give them the money and the prizes
                    player.addMoney(wheelPrize['value'])
                    if wheelPrize['prize']:
                        player.addPrize(wheelPrize['prize'])

                    break
                else:
                    print('{} was not the phrase'.format(move))

        # Move on to the next player (or go back to player[0] if we reached the end)
        playerIndex = (playerIndex + 1) % len(players)

    if winner:
        # In your head, you should hear this as being announced by a game show host
        print('{} wins! The phrase was {}'.format(winner.name, phrase))
        print('{} won ${}'.format(winner.name, winner.prizeMoney))
        if len(winner.prizes) > 0:
            print('{} also won:'.format(winner.name))
            for prize in winner.prizes:
                print('    - {}'.format(prize))
    else:
        print('Nobody won. The phrase was {}'.format(phrase))
        time.sleep(2)
    definitive = input("\nWould you like to play again?(y/n): ")
    if definitive.upper() == 'Y':
        OnOff = True
    else:
        print("\u001b[45;1mGame off!!!\u001b[0m") #background
        OnOff = False
