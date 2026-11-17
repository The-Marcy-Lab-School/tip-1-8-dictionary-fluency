picks = ["Ana:pho", "Bo:tacos", "Sam:pho", "Lee:pizza"]


def who_picked_a(picks):
    who_picked = {}
    for pick in picks:
        parts = pick.split(":")
        if parts[1] not in who_picked:
            who_picked[parts[1]] = []
        who_picked[parts[1]].append(parts[0])
    return who_picked


def who_picked_b(picks):
    who_picked = {}
    for pick in picks:
        parts = pick.split(":")
        who_picked[parts[1]] = [parts[0]]
    return who_picked


def who_picked_c(picks):
    who_picked = {}
    for pick in picks:
        parts = pick.split(":")
        who_picked.get(parts[1], []).append(parts[0])
    return who_picked


# A: In who_picked_a, fill in who_picked after each pass through the loop.
# after "Ana:pho":
# after "Bo:tacos":
# after "Sam:pho":
# after "Lee:pizza":

# B: Why does Ana disappear in who_picked_b, and why does who_picked_c end up empty?

# C: Run these in the REPL, one at a time.
# who_picked = {"pho": ["Ana", "Sam"], "tacos": ["Bo"]}
# for place in who_picked:
#     print(place)
# for place, names in who_picked.items():
#     print(place, len(names))
# who_picked.keys()
# who_picked.values()

# Rule:
