reactions = {"👍": 4, "😂": 2, "❤️": 1}
# Data types of these values:


def new_reactions_a(reactions, emoji):
    return reactions.get(emoji, 0) + 1


def new_reactions_b(reactions, emoji):
    return reactions.get(emoji) + 1


def new_reactions_c(reactions, emoji):
    return reactions[emoji] + 1


print(new_reactions_a(reactions, "😂"))
# Prediction:
# Actual:

print(new_reactions_a(reactions, "🔥"))
# Prediction:
# Actual:

print(new_reactions_c(reactions, "👍"))
# Prediction:
# Actual:

print(new_reactions_b(reactions, "🔥"))
# Prediction:
# Actual:
