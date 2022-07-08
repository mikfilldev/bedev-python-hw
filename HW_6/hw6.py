# from feeling import good_mood


user = {"username" : "Kolia",
		"level" : 0
		} 


message = {"user": user,
		   "word": "the"
		   }


sentences = [
	{"text": "When my time comes \n Forget the wrong that I’ve done.", 
	"level": 1},
	{"text": "In a hole in the ground there lived a hobbit.", 
	"level": 2},
	{"text": "The sky the port was the color of television, tuned to a dead channel.", 
	"level": 1},
	{"text": "I love the smell of napalm in the morning.", 
	"level": 0},
	{"text": "The man in black fled across the desert, and the gunslinger followed.", 
	"level": 0},
	{"text": "The Consul watched as Kassad raised the death wand.", 
	"level": 1},
	{"text": "If you want to make enemies, try to change something.", 
	"level": 2},	{"text": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore", 
	"level": 1},
	{"text":"I learned very early the difference between knowing the name of something and knowing something.", 
	"level": 2},
	{"text":"I learned very early the difference between knowing the name of something take knowing something.", 
	"level": 1}
	]


def is_valid_username(name: str) -> bool:
	""""Checking for correct username input.
	
	Return false if name have less then 2 letters.
	""" 

	return isinstance(name, str) and len(name) > 1


def is_valid_userlevel(level: int) -> bool:
	"""Checking for correct user level input.
	
	Return false if level not include number between 0-2.
	"""
	
	return isinstance(level, int) and 0 <= level <= 2


def is_valid_userword(word: str) -> bool:
	"""Checking for the correct user's input word.
	
	Return false if word have numbers in substring.
	"""
	
	if isinstance(word, str):
		if word.isalpha():
			return True
		return False
	return False


def get_list_dict_with_matched_userlevel(list_dicts: dict, level: int) -> list:
	
	if len(list_dicts) > 0:
		matched_dicts = [] # Initialize empty list for matched dicts
		for dict in list_dicts: 
			if dict.get("level") == level:
				matched_dicts.append(dict)

	return matched_dicts


def get_list_sentences_with_userword(matched_level_dict_list: list, word: str) -> list:
	
	matched_sentences = [] # Initialize empty list for matched sentences	
	for sentence in matched_level_dict_list:
		if word in sentence.get("text"):
			matched_sentences.append(sentence.get("text"))
	
	return matched_sentences
	

def make_message_for_matched_sentences(matched_sentences: list) -> str:
	
	result_msg = "" # Initialize empty string for rezult message

	if len(matched_sentences) == 0:
		result_msg = result_msg + "No matches"
	if len(matched_sentences) == 1:
		result_msg = result_msg + matched_sentences[0]
	if len(matched_sentences) > 1:
		for match_mess in matched_sentences:
			result_msg = result_msg + match_mess + "\n...\n" 

	return result_msg


# Код
if is_valid_username(user.get("username")):
	if is_valid_userlevel(user.get("level")):
		if is_valid_userword(message.get("word")):

			list_matched_level = get_list_dict_with_matched_userlevel(sentences, user.get("level"))
			list_matched_sentences = get_list_sentences_with_userword(list_matched_level, message.get("word"))
			result_msg = make_message_for_matched_sentences(list_matched_sentences)
			print(result_msg)

		else:
			print("Word incorrect")
	else:
		print("Userlevel invalid")
else: 
	print("Username invalid") 

