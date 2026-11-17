# Make 3: give back a list of the people on the team who aren't on this week's schedule at all.
def unscheduled(hours, team):
    pass


hours = {"Ana": 12, "Bo": 8, "Priya": 0}
print(unscheduled(hours, ["Ana", "Priya", "Sam"]))      # ['Sam']
print(unscheduled(hours, ["Bo", "Lee", "Jordan"]))      # ['Lee', 'Jordan']
print(unscheduled(hours, ["Ana", "Bo"]))                # []
