import json
from difflib import get_close_matches

while True:
    data = json.load(open("data.json", 'r'))


    def getKey(word):
        while True:
            word_l = word.lower()
            if word_l in data:
                return data[word_l]
            elif word_l.title() in data:
                return data[word_l.title()]
            elif word_l.upper() in data:
                return data[word_l.upper()]
            elif len(get_close_matches(word_l, data.keys())) > 0:
                choice = (input("Did you mean %s instead? \n Do you want to search another word? \n press Y to "
                                "continue \n press any key to end" % get_close_matches(word_l, data.keys())[0]))
                choice = choice.upper()
                if choice == "Y":
                    return data[get_close_matches(word_l, data.keys())[0]]

                elif choice == "N":
                    return "word not found"
                else:
                    return "word doesnt have any match "
                return "Word does not exist."


    word = input("Search word : ")
    results = getKey(word)
    if type(results) == list:
        for item in results:
            print(item)
    else:
        print(results)
    loop = input("Do you want to search another word? \n press Y to continue \n press any key to end")

    if loop.upper() == 'Y':
        continue
    else:
        print("---end----")
        break
