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


def next_question(question, correct_answer, score, total):
    '''Function to display next question'''
    guess = input(question + " ")

    if guess.lower() == correct_answer.lower():
        score += 1
        print(f"Correct! Current score: {score}/{total}")
        return score
    else:
        print(f"Incorrect! The answer is: {correct_answer}.")
        print(f"Current score: {score}/{total}")
        return score


def start_message():
    '''Function to display game message'''
    message = '''
    Welcome to the Flashcards game!
    Today you will be tested on capitals.
    GOOD LUCK!!
    '''
    print(message)


def end_message(score, total):
    '''End game message function'''
    if score / total < 3/5:
        print("You need more practice, try again! :)")
    elif score / total <= 4/5:
        print("Great work!")
    else:
        print("Amazing!")



def main():
    '''Main game function'''
    file_path = 'me-capitals.json'
    data = read_json(file_path)
    total_questions = len(data["cards"])
    score = 0

    start_message()

    for card in data["cards"]:
        question = card["q"]
        answer = card["a"]
        score = next_question(question, answer, score, total_questions)

    end_message(score, total_questions)

if __name__ == "__main__":
    main()

#TODO: try adding different card decks