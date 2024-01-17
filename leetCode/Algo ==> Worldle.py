import random

def make_initial_guess(word_length, vocabulary):
    # Choose a random word from the vocabulary with the specified length
    possible_words = [word for word in vocabulary if len(word) == word_length]
    return random.choice(possible_words)

def provide_feedback(hidden_word, guess):
    correct_positions = sum(1 for i, (hw, gw) in enumerate(zip(hidden_word, guess)) if hw == gw)
    correct_letters = sum(min(hidden_word.count(letter), guess.count(letter)) for letter in set(guess)) - correct_positions
    return correct_positions, correct_letters

def update_word_list(word_list, guess, feedback):
    return [word for word in word_list if provide_feedback(word, guess) == feedback]

def solve_wordle(hidden_word, vocabulary, max_attempts=10):
    word_length = len(hidden_word)
    word_list = [word for word in vocabulary if len(word) == word_length]
    
    for attempt in range(1, max_attempts + 1):
        guess = make_initial_guess(word_length, word_list)
        feedback = provide_feedback(hidden_word, guess)

        print(f"Attempt {attempt}: Guessing {guess}, Feedback {feedback}")

        if feedback[0] == word_length:
            print(f"Congratulations! Guessed the word '{hidden_word}' in {attempt} attempts.")
            break

        word_list = update_word_list(word_list, guess, feedback)

    print(f"Out of attempts. The hidden word was '{hidden_word}'.")

# Example usage:
hidden_word = "apple"
vocabulary = ["table", "apple", "orange", "grape", "water", "melon", "peach", "lemon"]

solve_wordle(hidden_word, vocabulary, max_attempts=10)
