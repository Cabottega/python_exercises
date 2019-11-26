username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'


if username == 'jonsnow' and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')

# alternative method notes>>>
# if username == 'jonsnow': 
#   if password == 'thenorth':
#     print('Access permitted')
# else:
#   print('Not allowed')


if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')



logged_in = True
standard_user = False

if logged_in and not standard_user:
  print('you can log into the admin dashboard')
else:
  print('you can only access the standard dashboard')

#   #multiple conditions in one

# username = 'jonsnow'
# email = 'jon@email.com'  #variables in string value
# password = 'thenorth'

# # need all items true

# if username == 'jonsnow' and password == 'thenorth': #joining conditions-everythong on left and right have to be true
#    print('Access permitted')
# else:
#    print('you shall not pass')    
# #---------------------------------------------------------------------------
# # or looks at the full expression and goes through it and only needs one side matched up
# # or operator allows you to use either username and or password--as long as one side matches up

# if username == 'jonsnow' or password == 'thenorth': 
#    print('Access permitted')
# else:
#    print('you shall not pass')
# #-----------------------------------------------------------------------------

# #as long as one or the other passes it treats whole object to true
# if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
#       print('Access permitted')
# else:
#   print('Not allowed')   
# #----------------------------------------------------------------------------
# # and not condition-not true-combining two expressions where one is true and one is false

# logged_in = True
# stadard_user = True

# if logged_in and not stadard_user:  # if statement can only look at one item! and not though--right side is false
#     print('You can access the admin')
# else:
#     print('You can only access the standard dashboard')   

