###___ExerciseOne___###
 
bot_name = 'Oliver'
bot_id = 1
date_time_now = '13.05.2022' 
bot_greetings = f'Hello my name BOT_{bot_name} {date_time_now} today i help you to learn English!'
print(bot_greetings)

user_name = 'Mykola'
user_id = 1
user_age = 25
user_language_proficiency = 20 # USER level English knowledge in % 0-100 
user_request_word = 'Hello'

# Some magic(logic) for make response from BOT
number_of_examples = 5 # Not more 10!
bot_response = f'Some of {number_of_examples} examples string generated .....'
bot_response_string = f'BOT_[{bot_name}]: Number of example #{{number_of_example}} for word `{user_request_word}`:\n{bot_response}'
print(bot_response_string)

print("\n")###___ExerciseTwo___###

# Data about USER
user_id = 1
user_name = 'Filippenko Mykola Viktorovich' 
billing_period_month = 'May' 
room_area = 62.3 # m^2
house_number = 27
room_number = 81
room_address_string = f'Slava-Ukraine {house_number}/{room_number}'
user_gas_used = 40.5 # m^3

# Rezulted string
msg = f'Dear: {user_name}\nLiving at: {room_address_string}\nAmount of gas used per {billing_period_month}: {user_gas_used} cubic meters'
print(msg)


