from collections import Counter

votes = ["pho", "tacos", "pho", "pizza", "pho"]
# Data types of these values:


def count_votes_a(votes):
    vote_counts = {}
    for option in votes:
        vote_counts[option] = vote_counts.get(option, 0) + 1
    return vote_counts


def count_votes_b(votes):
    return Counter(votes)


print(count_votes_a(votes))
# Prediction:
# Actual:

print(count_votes_b(votes))
# Prediction:
# Actual:

print(count_votes_b(votes)["ramen"])
# Prediction:
# Actual:

print(count_votes_a(votes)["ramen"])
# Prediction:
# Actual:
