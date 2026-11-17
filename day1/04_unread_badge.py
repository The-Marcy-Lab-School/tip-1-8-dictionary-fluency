# Make 1: give back the unread count a chat shows; a chat that isn't in the dictionary shows 0.
def unread_badge(unread, chat):
    pass


unread = {"family": 3, "roommates": 12, "work": 0}
print(unread_badge(unread, "roommates"))  # 12
print(unread_badge(unread, "work"))       # 0
print(unread_badge(unread, "gym"))        # 0
