"""File to define River class."""



from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear
from fish import Fish
from bear import Bear

class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
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
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat
        return None
    
    def check_hunger(self) -> None:
        alive_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                alive_bears.append(bear)
        self.bears = alive_bears
        return None
            
        
    def repopulate_fish(self):
        fish_spawn = []
        num_fish_spawn = (len(self.fish) // 2) *4
        while len(fish_spawn) < num_fish_spawn:
            fish_spawn.append(Fish())
        self.fish = fish_spawn    
        return None
    
    def repopulate_bears(self) -> None:
        bear_cubs = []
        number_bear_cubs = len(self.bears) //2
        while len(bear_cubs) < number_bear_cubs:
            bear_cubs.append(Bear())
        self.bears = bear_cubs
        return None




        
        return None
    
    def view_river(self) -> None:
        print(f"~~~ {self.day}: ~~~")
        print(f"Fish Population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
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


            
