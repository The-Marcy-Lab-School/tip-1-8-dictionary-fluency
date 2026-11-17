reactions = {"👍": 4, "😂": 2, "❤️": 1}


def new_reactions_a(reactions, emoji):
    return reactions.get(emoji, 0) + 1


def new_reactions_b(reactions, emoji):
    return reactions.get(emoji) + 1


def new_reactions_c(reactions, emoji):
    return reactions[emoji] + 1


# A: Fill in the value and type of each expression, in the order Python works them out.
# reactions.get("🔥")             value:          type:
# reactions.get("🔥") + 1         value:          type:
# reactions.get("🔥", 0)          value:          type:
# reactions.get("🔥", 0) + 1      value:          type:

# B: Call all three functions with "🔥". Why does each one give what it gives?

# C: Run these in the REPL, one at a time.
# reactions = {"👍": 4, "😂": 2, "😮": 0}
# "👍" in reactions
# 4 in reactions
# "😮" in reactions
# "🔥" in reactions
# reactions.get("😮", 0)
# reactions.get("👍", 0) + 1
# reactions

# Rule:
