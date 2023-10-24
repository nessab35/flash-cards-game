'''Importing json'''
#Starting flashcard game
# flashcards.py
import json

def read_json(file_path):
    '''Function that reads json file and returns content'''
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, PermissionError):
        print(f"Error: Unable to access file '{file_path}'")
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}', does not contain JSON")
    return None


def next_question(question, correct_answer, score, total): # function bascially checks to see if user answer is correct and adds score
    '''Display next question'''
    guess = input(question + " ") # asks for input for whatever question is being asked

    if guess.lower() == correct_answer.lower(): # if guess is correct answer
        score += 1 # score goes up by 1
        print(f"Correct! Current score: {score}/{total}") # message is bring with score adn total
        return score # score is returned
    else:
        print(f"Incorrect! The answer is: {correct_answer}.") # if wrong, they are given correct answer
        print(f"Current score: {score}/{total}") # score and total is shown
        return score # score is returned


def start_message(): # start game message
    '''Function to display game message'''
    message = '''
    Welcome to the Flashcards game!
    Today you will be tested on capitals.
    GOOD LUCK!!
    '''
    print(message)


def end_message(score, total): # end message based of score and total
    '''End game message function'''
    if score / total < 3/5:
        print("You need more practice, try again! :)")
    elif score / total <= 4/5:
        print("Great work!")
    else:
        print("Amazing!")



def main():
    '''Main game function'''
    file_path = 'me-capitals.json' # saying which file you would like for it to read
    data = read_json(file_path)
    total_questions = len(data["cards"]) # assigning total questions to length of deck
    score = 0 # assigining score to 0

    start_message() # printing start message

    for card in data["cards"]:
        question = card["q"] # question is assigned to "q" in json file
        answer = card["a"] # answer is assigned to "a" in json file
        score = next_question(question, answer, score, total_questions) # score is assigned to next_question file

    end_message(score, total_questions) # end message is printed

if __name__ == "__main__":
    main()

#TODO: try adding different card decks