from hw6 import is_valid_username, is_valid_userlevel
from hw6 import is_valid_userword, get_list_dict_with_matched_userlevel 


user_names_test_list = [["Mykola","Nataliia"],{"username":"Mykola"},"M","Mykola2303","M.V.",True,None,12345,"Mykola@","myk0l@"]

for count, username in enumerate(user_names_test_list):
	try:
		
		assert is_valid_username(username)==True
	except:
		print(f"Test #{count+1} failed username: ({username}) type ({type(username)}) not correct!")

print("\nTests for usernames DONE!\n")


user_levels_test_list = [0,1,[0,1,2],"2",-1,2,6,-2]

for count, level in enumerate(user_levels_test_list):
	try:
		assert is_valid_userlevel(level)==True
	except:
		print(f"Test #{count+1} failed level ({level}) type ({type(level)}) not correct!")

print("\nTests for userlevels DONE!\n")


user_words_test_list = ["w0rd","word",12345,("word1","word2"),["word3","word4"],"goodword"]

for count, word in enumerate(user_words_test_list):
	try:
		assert is_valid_userword(word)==True
	except:
		print(f"Test #{count+1} failed word ({word}) type ({type(word)}) not correct!")

print("\nTests for userwords DONE!\n")


# list_dicts_with_text_test = [
# 	{"text": "TEXT FOR LVL 1", 
# 	"level": 1},
# 	{"text": "TEXT FOR LVL 2", 
# 	"level": 2},
# 	{"text": "TEXT FOR LVL 1", 
# 	"level": 1},
# 	{"text": "TEXT FOR LVL 0", 
# 	"level": 0},
# 	{"text": "TEXT FOR LVL 0", 
# 	"level": 0},
# 	{"text": "TEXT FOR LVL 1", 
# 	"level": 1},
# 	{"text": "TEXT FOR LVL 2", 
# 	"level": 2},
#     ]

