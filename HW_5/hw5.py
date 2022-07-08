########################### Вводные данные ###########################

user = {"username": "Kolia",
		"level": 0
		} 

message = {"user": user,
		   "text": "the"
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
	"level": 2},
	{"text": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore", 
	"level": 1},
	{"text":"I learned very early the difference between knowing the name of something and knowing something.", 
	"level": 2},
	{"text":"I learned very early the difference between knowing the name of something take knowing something.", 
	"level": 1}
	]

# Необходимые функции:
# 1. Проверка на корректность ввода имени юзера str -> True
# 2. Проверка на корректность ввода уровня юзера int -> True
# 3. Проверка на корректность ввода слова юзера
	# 3.1  не пустое 
	# 3.2  имеет только символы 
# 4. Проверка списка словарей на вхождение уровня юзера return list[{1:text},{2:text}]   
# 5. Проверка словарей подходящих по уровню на вхождение слова юзера 
	# 5.1 одно совпадение 
	# 5.2 несколько совпадений 
	# 5.3 ни одного совпадения 
# 6. Сформировать сообщение для вывода результата

def is_valid_username(name):
	 
	# some check 
	return isinstance(name, str) and len(name) > 0
	
def is_valid_userlevel(level):
	
	#some check
	return isinstance(level, int) and 0 <= level <= 2

def is_valid_userword(word):
	if isinstance(word, str):
		if word.isalpha():
			return True
		return False
	return False

def get_dict_with_userlevel(list_dicts, level):
	if len(list_dicts) > 0:
		matched_dicts_with_level = []
		for dict in list_dicts: 
			if dict.get("level") == level:
				matched_dicts_with_level.append(dict)

	return matched_dicts_with_level

def find_userword_in_sentences_list(matched_level_dict_list, word):
	matched_sentences = []	
	for sentence in matched_level_dict_list:
		if word in sentence.get("text"):
			matched_sentences.append(sentence.get("text"))
	
	return matched_sentences
	

def get_message_with_matched_sentences(matched_sentences):
	result_msg = ""

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
		if is_valid_userword(message.get("text")):
			list_dict_with_userlevel = get_dict_with_userlevel(sentences, user.get("level"))
			list_matched_sentences = find_userword_in_sentences_list(list_dict_with_userlevel, message.get("text"))
			result_msg = get_message_with_matched_sentences(list_matched_sentences)
			print(result_msg)
		else:
			print("Word incorrect")
	else:
		print("Userlevel invalid")
else: 
	print("Username invalid") 

