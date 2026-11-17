# Dictionaries Practice

## Every day

- **Predict first.** Write your prediction in the file before you run anything.
- **Extra files.** Modify 2–3 and Make `05`–`06` are extra practice. Do them if you finish early.
- **Stuck rule.** After 5 minutes or two different tries, ask for help. Bring the line, your prediction, what actually happened, and what you tried.
- **Rule slot.** At the end of `02`, write the day's rule in your own words under `# Rule:`.
- **Check-ins.** ✅ after `02` and ✅ after `04`: show an instructor before moving on.

## Day 1

Look up a count in a dictionary and get a sensible answer every time.

```py
open_hours = {
    "Monday": "9am-5pm",
    "Tuesday": "9am-5pm",
    "Wednesday": "9am-5pm",
    "Thursday": "9am-5pm",
    "Friday": "9am-5pm",
    "Saturday": "10am-6pm"
}
print(open_hours.get("Monday")) # "9am-5pm"
print(open_hours.get("Saturday", "closed")) # "10am-6pm"
print(open_hours.get("Sunday", "closed")) # "closed"
```

## Day 2

Turn a list into a count for each item.

```py
letters = ['a', 'b', 'c', 'b', 'c', 'b']

counts = {}
for letter in letters:
    counts[letter] = counts.get(letter, 0) + 1

print(counts)
# {'a': 1, 'b': 3, 'c': 2}
```

## Day 3

Group names under a key, then find the biggest group.

```py
letters = ['a', 'b', 'c', 'b', 'c', 'b']

counts = {}
for letter in letters:
    counts[letter] = counts.get(letter, 0) + 1

max_letter = ''
max_count = 0
for letter, count in counts.items():
    if count > max_count:
        max_letter = letter
        max_count = count

print(max_letter, max_count)
# b 3
```

## Day 4

Count in one line, and know exactly what that line gives back.

```py
from collections import Counter
letters = ['a', 'b', 'c', 'b', 'c', 'b']
counts = Counter(letters)
print(counts)
# Counter({'b': 3, 'c': 2, 'a': 1})
print(counts['b'])
# 3
print(counts.get('b'))
# 3
```
