votes = ["pho", "tacos", "pho", "pizza", "pho"]


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


# A: In count_votes_a, fill in vote_counts after each pass through the loop.
# after "pho":
# after "tacos":
# after "pho":
# after "pizza":
# after "pho":

# B: All three loops run five times. Why does each one end with the dictionary it ends with?

# C: Run these in the REPL, one at a time.
# vote_counts = {}
# vote_counts["pho"] = 1
# vote_counts["pho"] = 1
# vote_counts
# vote_counts["pho"] = vote_counts["pho"] + 1
# vote_counts
# vote_counts["tacos"] += 1

# Rule:
