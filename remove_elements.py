users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

print(users)

users.remove('Jordan')

print(users)

# pop function removes last element from list but also returns to command for use.
popped_users = users.pop()

print(popped_users)
print(users)

del users[0]

print(users)

# instructor notes
#working with list that you know the value -remove is perfect to use-searches entire collect_incoming_data(
#pop is if you want the very last element in the list 
#del or delete only use if you know the list and you are deleting
