from collections import Counter

votes = ["pho", "tacos", "pho", "pizza", "pho"]

# A: Fill in the value and type of each expression.
# Counter(votes)                  value:          type:
# Counter(votes)["pho"]           value:          type:
# Counter(votes)["ramen"]         value:          type:
# "ramen" in Counter(votes)       value:          type:

# B: Both functions in 01 count the same votes. Why does only one of them crash on "ramen"?

# C: Run these in the REPL, one at a time.
# from collections import Counter
# Counter(["ok", "ok", "see"])
# Counter("ok ok see")
# Counter("ok ok see".split())
# Counter(["pho", "pho"]) == {"pho": 2}

# Rule:
