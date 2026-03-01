name = input("Enter the name: ")
place = input("Enter the place: ")
animal = input("Enter the animal: ")
adjective = input("Enter the adjective: ")

story = "One day, NAME went to PLACE and saw a ANIMAL. It was very ADJECTIVE!"

story = story.replace("NAME", name)
story = story.replace("PLACE", place)
story = story.replace("ANIMAL", animal)
story = story.replace("ADJECTIVE", adjective)

print(story)