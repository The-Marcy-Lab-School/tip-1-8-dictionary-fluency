votes = ["pho", "tacos", "pho", "pizza", "pho"]
# Data types of these values:


def count_votes_a(votes):
    vote_counts = {}
    for option in votes:
        vote_counts[option] = vote_counts.get(option, 0) + 1
    return vote_counts


def count_votes_b(votes):
    vote_counts = {}
    for option in votes:
        vote_counts[option] = 1
    return vote_counts


def count_votes_c(votes):
    vote_counts = {}
    for option in votes:
        vote_counts.get(option, 0) + 1
    return vote_counts


print(count_votes_a(votes))
# Prediction:
# Actual:

print(count_votes_b(votes))
# Prediction:
# Actual:

print(count_votes_c(votes))
# Prediction:
# Actual:
