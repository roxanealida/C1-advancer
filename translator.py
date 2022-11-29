from googletrans import Translator
# import pandas as pd  
import pandas as pd  


'''
1. Translate from Oxford 5000 C2 list
2. Each Language is in a different file
2. Array them into one dataframe

'''

# with open("Spanish_words.txt", "r", encoding="utf-8") as f:
#     with open("French_words.txt", "r", encoding="utf-8") as g:
#         with open("Portuguese_words.txt", "r", encoding= "utf-8") as h:
#             with open("English_words.txt", "r", encoding="utf-8") as i:
#                 data = {"English":[line[:-1] for line in i.readlines()], "French": [line[:-1] for line in g.readlines()],
#                 "Spanish": [line[:-1] for line in f.readlines()], "Portuguese": [line[:-1] for line in h.readlines()]}

# df = pd.DataFrame(data)
# print(df)

with open("Oxford_5000_C2.txt") as file:
    lines = file.readlines()
    words = [line[0: line.find(' ')] for line in lines]
 

with open("English_words.txt", "w", encoding="utf-8") as i:
    for j in words:
        i.write(j+"\n")

translator = Translator()


words_ar = [translator.translate(word, dest = "ar").text for word in words]


with open("Arabic_words.txt", "w", encoding= "utf-8") as f:
    for i in words_ar:
        f.write(i)
        f.write("\n")




# words_pt = [translator.translate(word, dest = "pt").text for word in words]

# with open("Portuguese_words.txt", "w", encoding= "utf-8") as f:
#     for i in words_pt:
#         f.write(i)
#         f.write("\n")

# for word in words:
#     translation_to_french = translator.translate(word, dest = "fr")
#     words_fr.append(translation_to_french.text)
# print(words_fr)

# print(len(words))
# words_es = []
# for word in words:
#     translation_to_spanish = translator.translate(word, dest = "es")
#     words_es.append(translation_to_french.text)
# print(words_es)
# print("Done")
