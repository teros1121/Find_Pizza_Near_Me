#Import python library
from pizzapi import *

#Assign a customer
customer = Customer('Donald', 'Trump', 'donald@whitehouse.gov', '2024561111')

#Assign location
address = Address('700 Pennsylvania Avenue NW', 'Washington', 'DC', '20408')

store = address.closest_store()

print(store.get_details())
