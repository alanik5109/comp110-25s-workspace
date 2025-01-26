"""Program to help plan a cozy tea party in terms of supplies!"""


__author__: str = "730547147"


def main_planner(guests: int) -> None:
    """entrypoint of tea party planning functions."""
    print ("A Cozy Tea Party for " + (str(guests)) + " People!")
    print ("Tea " + "Bags" + ": " + str(tea_bags(people=guests)))
    print ("Treats" + ": " + str(treats(people=guests)))
    print ("Cost" + ": " + "$" + str(cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))))
    return None


def tea_bags(people: int) -> int:
    """This is to help determine how many tea bags per person."""
    return 2 * people



def treats(people: int) -> int:
    """Function that determines that for how many drinks a person consumes, how many treats they will want."""
    return int(tea_bags(people=people) * 1.5)



def cost(tea_count: int, treat_count: int) -> float:
    """Function used to determine the cost of the tea and the treats for the party depending on the number of people."""
    return (0.50 * tea_count) + (0.75 * treat_count)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))