def prompt_guess() -> str:
    a=input("enter a letter :")
    return a

def print_status(state: dict) -> None:
    print(state["display"])
    print(state["guessed"])
    print(state["wrong_guesses"])


def print_result(state: dict) -> None:
    if "_" in state["display"]:
        print("Looser!")
    else:
        print("your winner")
    








