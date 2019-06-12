import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"

words = []

phrases = {
    "class %%%(%%%):": "Make a class named %%% that is-a %%%",
    "class %%%(object):\n \t def __init__(self, ***)": "Class %%% has an init method, with self and *** arguments.",
    "class %%%(object): \n\tdef ***(self, @@@)": "class %%% has-a function *** taking self and @@@",
    "*** = %%%()": "variable *** is an instance of class %%%",
    "***.***( @@@ )": "From ***, get the *** function, calling it with params @@@",
    "***.*** = '***'": "From ***, get the attribute *** and set it to ***"
}

if len(sys.argv) == 2 and sys.argv[1] == "english":
    phrase_first = True
else:
    phrase_first = False

for word in urlopen(WORD_URL).readlines():
    words.append(str(word.strip(), encoding = "utf-8"))

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(words, snippet.count("%%%"))]
    other_names = random.sample(words,snippet.count("***"))
    results = []
    param_names = []

    for sentence in snippet, phrase:
        result = sentence[:]

        for word in class_names:
            result = result.replace("%%%", word, 1)

        for word in other_names:
            result = result.replace("***", word, 1)

        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

try:
    while True:
        snippets = list(phrases.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = phrases[snippet]
            question, answer = convert(snippet, phrase)
            if phrase_first:
                question, answer = answer, question

            print(question)

            input(">")

            print(f"Answer: {answer}\n\n")
except EOFE:
    print("Bye.")
