"""Making a functional wordle program!"""
__author__: str = "730547147"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    player_turns: int = 1
    while player_turns <= 6:
        player_guess = input_guess(N = len(secret))
        print(f"=== Turn {player_turns}/6 ===")
        print(emojified(player_guess, secret))
        if player_guess == secret and player_turns <= 6:
            print(f"You won in {player_turns}/6 turns!")
            return None
        else:
            player_turns = player_turns + 1
    print("x/6 - Sorry, try again tomorrow!")
    return None


def contains_char(search_string: str, single_char: str) -> bool:
    """This function is to return true or false depending on an inputted string and character."""
    assert len(single_char) == 1, f"len('{single_char}') is not 1"
    idx: int = 0
    while idx < len(search_string):
        if search_string[idx] == single_char:
            return True
        else:
            idx = idx + 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def emojified(guess: str, secret: str) -> str: 
  """Emojifying the results of the above function in a Wordle-type fashion"""
  assert len(guess) == len(secret), "Guess must be same length as secret"  
  idx_two: int = 0
  output: str = ""
  while idx_two < len(guess):
     if guess[idx_two] == secret[idx_two]:
        output += GREEN_BOX
     elif contains_char(secret, guess[idx_two]) == True:
        output += YELLOW_BOX
     else:
        output += WHITE_BOX
     idx_two = idx_two +1
  return output



def input_guess(N: int) -> str:
    """This is where the player will be prompted to enter a guess that is the same length as the secret"""
    guess = input(f"Enter a {N} character word:")
    if len(guess) == N:
        return guess
    else:
        while len(guess) != N:
            print(f"That wasn't {N} chars! Try again:")
            guess = input(f"Enter a {N} character word:")
        return guess        


if __name__ == "__main__":
    main(secret="codes")




 

    
