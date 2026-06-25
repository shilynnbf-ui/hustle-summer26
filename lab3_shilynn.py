
# Shilynn Ba-Farlough |lab 3| Intro to Python

# Ticket 1
username = "shypie"

print(len(username))

# PREDICT: 6
# EXPLAIN: yes len() counted the letters

# Ticket 2

print(username[0])
print(username[len(username)-1])

# PREDICT: S and E
# EXPLAIN The last inden len(username) is minus 1 because pyhton starts counting at zero

# Ticket 3

print("Welcome to Loop, @" + username + "!")
print(f"Welcome to Loop, @" + username + "!")

# PREDICT yes both lines look identical
# EXPLAIN the first method felt easier to me because it was a direct concept

# Ticket 4 

#username[0] = "X" # TypeError: 'str' object does not support item assignment

username = "shypie"
print(username.upper())

# PERDICT: and error and the progam will crash
# EXPLAIN: immutable strings cannot be changed after it is created you need a new string

# Ticket 5

feed = [" I like to listen to music" , "lifes a dream" , "Green is the best color"]
print(len(feed))
print(feed[0])

# PERDICT: the print number is gunna 3, and the first caption is "I like to listne to music"
# EXPLAIN: for the first post I used 0 for it's index because python starts with 0

# Ticket 6

feed.append("I have a cat named sumo")
print(feed)

# PERDICT the new foruth will be at index 3
# EXPLAIN the fourth post is at index 3 because python starts with 0

# Ticket 7

feed.pop(0)
feed.sort()
print(feed)

# PERDICT: " I liek to listen to music" gets removed and everything else is in alphabaical order
# EXPLAIN .pop() removed a post .sor() sorted everything in alphabical order

# Ticket 8

profile = {
    "username": "shypie",
    "followers": 100000,
    "verified": True
}

print(profile["followers"])

#profile[0] #KeyError: 0

# PREDICT: the follower count is print and profile [0] will cause an error
# EXPLAIN: they use keys like followers to find valuse instead of number indexes

# Ticket 9

profile["followers"] = profile[ "followers"] + 50
profile["bio"] = "wow this is great"

print(profile)
print(profile.get("age"))

# PREDICT: it will print none
# EXPLAIN: Square brackets will crash the whole program with a KeyError if the key does not exist

# Ticket 10

print(f"@{profile['username']} has {profile['followers']} followers and {len(feed)} posts. Top post: {feed[0]}")

# PREDICT shypie has 100050, followers and 3 posts. Top post: green is the best color
# EXPLAIN I used dictionarys, lists, and feeds
