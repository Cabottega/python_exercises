post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# Removing elements from end
post = post[:-1]

# Removing elements from beginning
post = post[1:]

# Removing specific element (messy/not recommended)
post = list(post)
post.remove('published')
post = tuple(post)

print(post)

# Instructor notes:
# users = ["kristnine", 'Tiffany', 'Jordan', 'Leann']  #list of users-database query

# print(users)

# users.remove('Jordan') #remove function takes an arguement- the value we are removing

# print(users)

# popped_user = users.pop()  #pop returns the last item  of the list so you can use it!
#                            #and stores in the variable
# print(popped_user)
# print(users)

# del users[0]
# print(users)

# #working with list that you know the value -remove is perfect to use-searches entire collect_incoming_data(
# #pop is if you want the very last element in the list 
# #del or delete only use if you know the list and you are deleting
