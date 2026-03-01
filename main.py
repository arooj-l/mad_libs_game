name = input("Enter the name: ")
place = input("Enter the place: ")
animal = input("Enter the animal: ")
adjective = input("Enter the adjective: ")

story = ("One day, NAME went to PLACE and saw a ANIMAL. "
         "It was very ADJECTIVE! "
         "Everyone was talking about the ANIMAL")

story = story.replace("NAME", name.upper())
story = story.replace("PLACE", place.title())
story = story.replace("ANIMAL", animal.lower())
story = story.replace("ADJECTIVE", adjective.lower())

print("\n**** Your Mad Lib Story ****")
print(story)