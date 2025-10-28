from  hangman.game import *
from hangman.io import prompt_guess
from hangman.words import choose_secret_word, words



def play(words: list[str]) -> None:
    secret = choose_secret_word(words)
    state = init_state(secret)
    while not is_won(state) and not is_lost(state):
        print(render_display(state))
        print(state["guessed"] if len(state["guessed"]) else "")
        ch = prompt_guess()
        validate, msg = validate_guess(ch, state["guessed"])
        while not validate:
            print(msg)
            ch = prompt_guess()
            validate, msg = validate_guess(ch, state["guessed"])
        _ = apply_guess(state, ch)
    print("congratulation" if is_won(state) else "Mybe Next Time")
    print(render_summary(state))
        

if __name__ == "__main__":
    play(words)