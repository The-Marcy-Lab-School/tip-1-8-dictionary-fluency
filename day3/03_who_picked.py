picks = ["Ana:pho", "Bo:tacos", "Sam:pho", "Lee:pizza"]


def who_picked_b(picks):
    who_picked = {}
    for pick in picks:
        parts = pick.split(":")
        who_picked[parts[1]] = [parts[0]]
    return who_picked


# Modify 1: everyone who picked a place stays on its list → who_picked_b(picks)["pho"] gives ['Ana', 'Sam']
print(who_picked_b(picks)["pho"])

# Modify 2: the place the most people picked → top_pick(picks) gives 'pho'

# Modify 3: every place more than one person picked → picked_by_more_than_one(picks) gives ['pho']
