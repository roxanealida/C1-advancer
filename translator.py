'''
1. The objective is to build a dataframe that contains the Oxford 5000 C1 words 
and their translations into French, Spanish, Portuguese and Arabic.
2. Each language's translation gets written into a separate file
2. From these files all pendants are arrayed into a dataframe
'''

from googletrans import Translator
import pandas as pd
import arabic_reshaper
from bidi.algorithm import get_display
import csv
import random

#First, the C1 Oxford words are written into the "English_words.txt" file.
#By doing this, the POS information is excluded.

# with open("Oxford_5000_C2.txt", encoding="utf-8") as file:
#     lines = file.readlines()
#     words = [line[0: line.find(' ')] for line in lines]

# with open("English_words.txt", "w", encoding="utf-8") as i:
#     for j in words:
#         i.write(j+"\n")

# #The next step is to translate all English C1 words into the below languages.

# translator = Translator()
# words_fr = [translator.translate(word, dest = "fr").text for word in words]
# words_es = [translator.translate(word, dest = "es").text for word in words]
# words_pt = [translator.translate(word, dest = "pt").text for word in words]
# words_ar = [translator.translate(word, dest = "ar").text for word in words]

# #These words are now written into separate files.

# with open("French_words.txt", "w", encoding= "utf-8") as f:
#     for i in words_fr:
#         f.write(i)
#         f.write("\n")

# with open("Spanish_words.txt", "w", encoding= "utf-8") as g:
#     for i in words_es:
#         g.write(i)
#         g.write("\n")

# with open("Portuguese_words.txt", "w", encoding= "utf-8") as h:
#     for i in words_pt:
#         h.write(i)
#         h.write("\n")

# with open("Arabic_words.txt", "w", encoding= "utf-8") as j:
#     for i in words_ar:
#         j.write(i)
#         j.write("\n")


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
                            "Arabic": [line[:-1] for line in j.readlines()]}

df = pd.DataFrame(data)

df.to_csv('Df_translations.csv', index=False)

#2. Algorithm for training
#3. Algorithm for translating


with open("Df_translations.csv", "r", encoding= "utf-8") as f:
    line = f.readline()        
    lines = f.readlines()

#1. Practicing
language_today = input("Which language do you want to train today? ")
#repeat_or_new = input("Do you want to repeat past wrong words or learn new ones? ")
goal = int(input("How many words do you want to train today? "))

'read input, repeating no: means learning with main csv file. but if repeptition French wrong words file'

if language_today == "German":
    position_of_language = 1
elif language_today == "French":
    position_of_language = 2
elif language_today== "Spanish":
    position_of_language = 3
elif language_today == "Portuguese":
    position_of_language = 4
elif language_today == "Arabic":
    position_of_language = 5

def learn_language(): #repeat_boolean

    score = 0

    for n in range(0,goal):

        rando = random.randint(1,1312) #dynamic: length of lines of he text file/csv file
        word_line = lines[rando].split(",")
        print(f"What is the {language_today} word for {word_line[0]}?")
        input1 = input()
        if input1 == word_line[position_of_language]:
            print("Good job!")
            score += 1
        else:
            input2 = input("Want a tip? " )
            if input2 == "yes":
                print(f"The word starts with {word_line[position_of_language][:1]}")
                input3 = input("Next try: ")
                if input3 == word_line[position_of_language]:
                    print("Good job!")
                else: print(f"The word was {word_line[position_of_language]}")
            elif input2 == "no":
                print(f"The word was {word_line[position_of_language]}")
    print(f"Your task is completed for today, good job! Your score is {score}/{goal}.")

learn_language()
