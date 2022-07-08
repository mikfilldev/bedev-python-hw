sentences_dict = {
    "level1": [
        "In England the cuckoo is the herald of spring.",
        "His ancestors had come to England as refugees."
        ],
    "level2": [
        "some string with Ukraine",
        "ANOTHER STRING help me"
        # "The shares were underwritten by the Bank of England.",
        # "England saw off Luxembourg 5-0."
        ],
    "level3": [
        "The national emblem of England is a rose.",
        "Brighton is in southern England.",
        "hii",
        "Ukraine",
        "England"
        ],
    "level4": [
        "The winter sports bring the jet set from England.",
        "In the Middle Ages England waged war on France."
        ],
    "level5": [
        "England is the birthplace of the modern novel.",
        "In today's match England play their old enemy, Scotland."
        ]
    }

user = {
    "id": 1,
    "first_name": "nik",
    "last_name": "fil",
    }

user["level"] = 3
# user["word"] = "England"
user["word"] = "England"

is_level_find = False
is_word_find = False

for level in sentences_dict:
    # Ищем по ключу "уровень" в словаре с примерами
    if "level" + str(user.get("level")) == level:       
        is_level_find = True
        # Идём циклом по списку с примерами 
        for index, sentence in enumerate(sentences_dict[level]):
            # Проверяем в каждом из примеров наличие слова юзера 
            # Если находим соотвествие печатаем
            if user.get("word") in sentence:
                is_word_find = True
                print(f"Example sentence #{index + 1}\n{sentence}")    

    # Если мы нашли слово выходим из цикла 
    elif is_word_find:
        break

# Нет такого уровня в примерах
if not is_level_find:    
    print("Level error")    
else:
    # Не было слова в примерах "с учётом регистра"
    if not is_word_find:
        print("Word " + user.get("word") + " not find")
    
