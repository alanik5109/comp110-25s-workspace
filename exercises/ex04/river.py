"""File to define River class."""

___author___ = "730547147"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear
#from fish import Fish
#from bear import Bear

class River:
    """The bears and fish in the river."""
    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Checking the ages of the fish and bears in the river to see who is alive."""
        surviving_fish = []
        surviving_bears = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)      
        self.fish = surviving_fish
        
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears

        return None
    
    def remove_fish(self, amount:int) -> None:
        """Removing fish from the river as they are eaten by the bears."""
        count: int = 0
        remaining_fish_list = []
        for fish in self.fish:
            if count < amount:
                count += 1
            else:
                remaining_fish_list.append(fish)
        self.fish = remaining_fish_list
        return None


    def bears_eating(self):
        """Increasing their hunger as the eat the available fish in the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat
        return None
    
    def check_hunger(self) -> None:
        """Keeping track of bears that are not hungry enough to die."""
        alive_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                alive_bears.append(bear)
        self.bears = alive_bears
        return None
            
        
    def repopulate_fish(self):
        """Modeling the reproduction of the fish population."""
        num_fish_spawn = (len(self.fish) // 2) *4
        idx: int = 0
        while idx < num_fish_spawn:
            self.fish.append(Fish())
            idx += 1   
        return None
    
    def repopulate_bears(self) -> None:
        """Modeling the reproduction of the bear population."""
        number_bear_cubs = len(self.bears) //2
        idx_2: int = 0
        while idx_2 < number_bear_cubs:
            self.bears.append(Bear())
            idx_2 += 1
        return None
    
    def view_river(self) -> None:
        """Viewing the status of the river on a given day.""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish Population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self) -> None:
        days = 7
        count = 0
        while count < days:
            self.one_river_day()
            count += 1


            
