# Make 2: give back how many spots are left in a gym class; a class nobody has booked yet is fully open, and a class the gym doesn't offer has 0 spots.
def spots_left(capacity, booked, gym_class):
    pass


capacity = {"spin": 20, "yoga": 15, "boxing": 12}
booked = {"spin": 20, "yoga": 9}
print(spots_left(capacity, booked, "yoga"))     # 6
print(spots_left(capacity, booked, "spin"))     # 0
print(spots_left(capacity, booked, "boxing"))   # 12
print(spots_left(capacity, booked, "pilates"))  # 0
