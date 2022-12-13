# '1. The objective is to build a dataframe that contains the Oxford 5000 C1 words 
# and their translations into French, Spanish, Portuguese and Arabic.
# 2. Each language's translation gets written into a separate file
# 2. From these files all pendants are arrayed into a dataframe'


from googletrans import Translator
import pandas as pd
import arabic_reshaper
from bidi.algorithm import get_display
import csv
import random

#First, the C1 Oxford words are written into the "English_words.txt" file.
#By doing this, the POS information is excluded.

with open("Oxford_5000_C2.txt", encoding="utf-8") as file:
    lines = file.readlines()
    words = [line[0: line.find(' ')] for line in lines]

with open("English_words.txt", "w", encoding="utf-8") as i:
    for j in words:
        i.write(j+"\n")

#The next step is to translate all English C1 words into the below languages.

translator = Translator()
words_fr = [translator.translate(word, dest = "fr").text for word in words]
words_es = [translator.translate(word, dest = "es").text for word in words]
words_pt = [translator.translate(word, dest = "pt").text for word in words]
words_ar = [translator.translate(word, dest = "ar").text for word in words]

#These words are now written into separate files.

with open("French_words.txt", "w", encoding= "utf-8") as f:
    for i in words_fr:
        f.write(i)
        f.write("\n")

with open("Spanish_words.txt", "w", encoding= "utf-8") as g:
    for i in words_es:
        g.write(i)
        g.write("\n")

with open("Portuguese_words.txt", "w", encoding= "utf-8") as h:
    for i in words_pt:
        h.write(i)
        h.write("\n")

with open("Arabic_words.txt", "w", encoding= "utf-8") as j:
    for i in words_ar:
        j.write(i)
        j.write("\n")


#and finally, all translations are arrayed into a dataframe.


with open("Spanish_words.txt", "r", encoding="utf-8") as f:
    with open("French_words.txt", "r", encoding="utf-8") as g:
        with open("Portuguese_words.txt", "r", encoding= "utf-8") as h:
            with open("English_words.txt", "r", encoding="utf-8") as i:
                with open("Arabic_words.txt", "r", encoding = "UTF-8") as j:
                    with open("German_words.txt", encoding = "utf-8") as k:
                        	data = {"English":[line[:-1] for line in i.readlines()],
                            "German":[line[:-1] for line in k.readlines()],
                            "French": [line[:-1] for line in g.readlines()],
                            "Spanish": [line[:-1] for line in f.readlines()],
                            "Portuguese": [line[:-1] for line in h.readlines()],
                            "Arabic": [get_display(arabic_reshaper.reshape(line[:-1])) for line in j.readlines()]}

df = pd.DataFrame(data)
df.to_csv('Df_translations.csv', index=False)



