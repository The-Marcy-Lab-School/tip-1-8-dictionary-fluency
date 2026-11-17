picks = ["Ana:pho", "Bo:tacos", "Sam:pho", "Lee:pizza"]
# Data types of these values:


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


print(who_picked_a(picks))
# Prediction:
# Actual:

print(who_picked_b(picks))
# Prediction:
# Actual:

print(who_picked_c(picks))
# Prediction:
# Actual:
