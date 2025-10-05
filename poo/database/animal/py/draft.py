class Animal:
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"
    
    def ageBy(self, increment: int) -> None:
        if self.age == 4:
            print(f"warning: {self.species} morreu")
            return
        self.age+=increment
        if self.age >= 4:
            self.age = 4
            print(f"warning: {self.species} morreu")

    def makeSound(self) -> str:
        if self.age == 0:
            return "---"
        elif self.age >= 4:
            return "RIP"
        else:
            return self.sound
    
def main():
        animal: Animal = Animal("","")

        while True:
            line: str = input()
            print("$"+line)
            args: list[str] = line.split(" ")

            if args[0] == "end":
                break
            elif args[0] == "init":
                if len(args)<2:
                    print("grow requer increment")
                    continue
                
                species: str = args[1]
                sound: str = args[2]
                animal= Animal(species, sound)
            elif args[0] == "grow":
                if len(args)<2:
                    print("grow requer increment")
                    continue

                increment: int= int(args[1])
                animal.ageBy(increment)
            elif args[0] == "noise":
                print(animal.makeSound())
            elif args[0] == "show":
                print(animal)

main()
        