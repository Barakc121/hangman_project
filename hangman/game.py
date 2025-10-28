import random
from .words import choose_secret_word,words

def init_state(secret: str, max_tries = 6) -> dict:

    return {"secret":secret,
            "display": "_"*len(secret),
            "guessed":set[str],
            "wrong_guesses":0,
            "max_tries":max_tries}

print(init_state(words[random.randint(0, len(words) -1)],10))
def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    if ch !=1:
          return False,'ch is not good'
    elif not ch.isalpha:
          return False,'ch none'
    elif ch in guessed:
          return False,'enter a letter else'
    else:
          return True,'your good man'
def apply_guess(state: dict, ch: str) -> bool:
    ch=ch.lower()
    if ch not in state["secret"]:
        return False
    for i in range(len(state["secret"])):        
        if state["secret"][i]==ch:
             


             state["display"][i]==ch
    return True
    

def is_won(state: dict) -> bool:
    if  "_" in state["display"]:   
        return False
    else:
        return True    

def  is_lost(state: dict) -> bool:
     if "wrong_guesses" >= "max_tries":
        return True,"your lose ,game over!"

def  render_display(state: dict) -> str:
        return "bla bla:{display}"


def render_summary(state: dict) -> str:
        return "that the word you had to find :{secret}." \
        "These are the letters you entered:{display}"
