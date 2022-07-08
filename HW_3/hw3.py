user = {
  'id' : 1,
  'first_name': 'someName',
  'last_name': 'someLastName',
  'level': 4
  }

msg_from_user = 'Input from user with SomeWord and same text'
word_from_user = 'SomeWord'
user_level = user.get("level")

sentences_list = [
  f'Example #1 for lvl {user_level} with {word_from_user}', 
  f'Example #2 for lvl {user_level} with {word_from_user}', 
  f'Example #3 for lvl {user_level} with {word_from_user}',
  f'Example #4 for lvl {user_level} with {word_from_user}',
  f'Example #5 for lvl {user_level} with {word_from_user}'
  ]

sentence_output = {
  'level' : user_level,
  'text' : sentences_list[user_level - 1]
  }

print(sentence_output)

