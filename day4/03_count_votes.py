from collections import Counter

votes = ["pho", "tacos", "pho", "pizza", "pho"]


def count_votes_a(votes):
    vote_counts = {}
    for option in votes:
        vote_counts[option] = vote_counts.get(option, 0) + 1
    return vote_counts


# Modify 1: votes for one option, in one line → votes_for(votes, "ramen") gives 0; votes_for(votes, "pho") gives 3
print(count_votes_a(votes)["ramen"])

# Modify 2: more than half the votes → has_majority(votes, "pho") gives True; has_majority(votes, "tacos") gives False

# Modify 3: the option with the most votes → winner(votes) gives 'pho'
