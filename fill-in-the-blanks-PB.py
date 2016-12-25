# STAGE 2 FINAL PROJECT: Fill-in-the-Blanks Game
# Dec 25, 2016

# Global inputs
levels = ["easy","medium","hard"]
intro = "\nPlease select a game difficulty by typing it in.\nPossible choices: easy, medium, and hard.\n"
paragraph_intro = "\nThe current paragraph reads as such:\n"
q_prompt = "\nEnter the correct word for blank "
space_holders = ["__1__","__2__","__3__","__4__"]
allowed_error_count = 3

# EASY level inputs
answers_easy = ["pwd","ls","cd","mkdir"]
paragraph_easy = "Important commands to remember include: the __1__ command, which prints the current working directory; the __2__ command, which prints the contents of the current working directory; the __3__ command, which changes the directory; and the __4__ command, which creates a new directory."

# MEDIUM level inputs
answers_med = ["function","arguments","none","list"]
paragraph_med = "A __1__ is created with the def keyword. You specify the inputs \na __1__ takes by adding __2__ separated by commas between the parentheses. \n__1__ by default return __3__ if you don't specify the value to return.\n__2__ can be standard data types such as string, number, dictionary, tuple, \nand __4__ or can be more complicated such as objects and lambda functions."

# HARD level inputs
answers_hard = ["find","replace","while","or"]
paragraph_hard = "Review of common Python methods! The __1__ method returns the starting index of the substring. The __2__ method replaces all instances of the old string with the new string. __3__ loops repeat an action until the expression is True. The __4__ operator evaluates whether the 1st expression is True, and does not evaluate the second expression if it is."

def word_answer(word,answers,index):
    """This function takes as inputs a word, an answer set, and an index and outputs either the word (if it equals the answer) or the space_holder (if the word is not equal to the answer)"""
    if word == answers[index-1]:
        return word
    else:
        return space_holders[index-1]

def word_in_spaceholder(word, space_holder):
    """This function takes as inputs a word and a specific "spaceholder" (e.g. "__1__" ) and returns as output either the word itself (if equal to the spaceholder) or nothing (if the word is not equal to the spaceholder)"""
    if word == space_holder:
            return word
    else:
        return None

def replace_words(paragraph,space_holder,user_answer):
    """This function takes in a paragraph, a space_holder and a user's answer, and replaces all instances of the spaceholder with the user's answer (when correct)."""
    replaced = []
    paragraph = paragraph.split()
    for word in paragraph:
        replacement = word_in_spaceholder(word, space_holder)
        if replacement != None:
            word = word.replace(replacement, user_answer)
            replaced.append(word)
        else:
            replaced.append(word)
    paragraph = " ".join(replaced)
    return paragraph

def fill_in_the_blanks(paragraph,space_holders,answers):
    """This function takes as inputs a paragraph, a set of placeholders, and an answer set. It integrates the above functions, and calls for user input based on the paragraph prompts"""
    print paragraph_intro
    print paragraph
    index = 0
    for i in space_holders:
        word = "na"
        index += 1
        count = 0
        while word != answers[index-1]:
            user_answer = raw_input(q_prompt + i + ": ")
            if word_answer(user_answer,answers,index) == answers[index-1]:
                print "\nCorrect! Well done."
                word = word.replace(word,user_answer)
                paragraph = replace_words(paragraph,space_holders[index-1],user_answer)
                print paragraph_intro
                print paragraph
            elif count == allowed_error_count:
                print "\nSorry, you've guessed incorrectly too many times in a row. Try again soon!"
                exit()
            else:
                print "\nNot quite right...try again!\n\nYou have " + str(allowed_error_count-count) + " chances left..."
            count += 1

def play_the_game():
    """This integrates all of the functions and inputs above into a game with 3 possible levels (easy, medium, and hard)."""
    print intro
    user_level = raw_input("Type in a level: ")
    print "You chose: " + user_level + ".\n"
    if user_level == "easy":
        fill_in_the_blanks(paragraph_easy,space_holders,answers_easy)
    if user_level == "medium":
        fill_in_the_blanks(paragraph_med,space_holders,answers_med)
    if user_level == "hard":
        fill_in_the_blanks(paragraph_hard,space_holders,answers_hard)
    print "\nCongratulations, you've won the game!!! \n\nSee you next time."
    exit()

print play_the_game()
