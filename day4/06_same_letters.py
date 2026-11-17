# Make 3: say whether two group-chat nicknames use exactly the same letters, ignoring capital letters and spaces.
from collections import Counter


def same_letters(name1, name2):
    pass


print(same_letters("Dormy", "My Dor"))  # True
print(same_letters("Listen", "Silent"))  # True
print(same_letters("Ana", "Anna"))       # False
