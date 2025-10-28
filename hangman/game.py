def init_state(secret: str, max_tries = 6) -> dict:

    return {"secret":secret,
            "display": ["_"] * len(secret),
            "guessed": set(),
            "wrong_guesses":0,
            "max_tries":max_tries}

print(__name__)

def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    if len(ch) !=1:
          return False,'ch is not good'
    elif not ch.isalpha:
          return False,'ch none'
    elif ch in guessed:
          return False,'enter a letter else'
    else:
          return True,'your good man'
    
def apply_guess(state: dict, ch: str) -> bool:    
    ch=ch.lower()
    state["guessed"].add(ch)
    if ch not in state["secret"]:
        state["wrong_guesses"] += 1
        return False
    for i in range(len(state["secret"])):        
        if state["secret"][i]==ch:
             state["display"][i]=ch
    return True
    

def is_won(state: dict) -> bool:
    if "_" in state["display"]:   
        return False
    else:
        return True    

def  is_lost(state: dict) -> bool:
     if state["wrong_guesses"] >= state["max_tries"]:
        return True,"your lose ,game over!"
     else:
        return False

def  render_display(state: dict) -> str:
        return "".join(state["display"])


def render_summary(state: dict) -> str:
        return f"that the word you had to find :{state['secret']}. \nThese are the letters you entered:{state['display']}"

