from  game import *
from .io import prompt_guess
from .words import choose_secret_words



def play(words: list[str], max_tries: int = 6) -> None:
    secret = choose_secret_word(words)
    state = init_state(secret)
    while not is_won() and not is_lost():
        ch = prompt_guess()
        while not validate_guess(ch):
            ch = prompt_guess()
        if not apply_guess(state, ch):
            state["wrong_guesses"] += 1
        



if __name__ == "__main__":
    play()