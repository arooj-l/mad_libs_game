name = input("Enter the name: ")
place = input("Enter the place: ")
animal = input("Enter the animal: ")
adjective = input("Enter the adjective: ")

story = (
    f"One day, {name.upper()} went to {place.title()} and saw a {animal.lower()}."
    f"The {animal.lower()} was very {adjective.lower()}!"
    f"Everyone was talking about that {animal.lower()}"
)

print("\n**** Your Mad Lib Story ****")
print(story)