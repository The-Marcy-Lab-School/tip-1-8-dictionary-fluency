votes = ["pho", "tacos", "pho", "pizza", "pho"]


def count_votes_c(votes):
    vote_counts = {}
    for option in votes:
        vote_counts.get(option, 0) + 1
    return vote_counts


# Modify 1: count every vote → count_votes_c(votes) gives {'pho': 3, 'tacos': 1, 'pizza': 1}
print(count_votes_c(votes))

# Modify 2: blank votes don't count → count_votes_c(["pho", "", "tacos"]) gives {'pho': 1, 'tacos': 1}

# Modify 3: votes for one option → votes_for(votes, "pho") gives 3; votes_for(votes, "ramen") gives 0
