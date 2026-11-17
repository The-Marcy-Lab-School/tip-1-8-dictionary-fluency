reactions = {"👍": 4, "😂": 2, "❤️": 1}


def new_reactions_b(reactions, emoji):
    return reactions.get(emoji) + 1


# Modify 1: a new emoji starts from 0 → new_reactions_b(reactions, "🔥") gives 1
print(new_reactions_b(reactions, "🔥"))

# Modify 2: someone takes their reaction back → fewer_reactions(reactions, "😂") gives 1

# Modify 3: an emoji nobody used can't go below 0 → fewer_reactions(reactions, "🔥") gives 0
