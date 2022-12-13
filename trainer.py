import random

#While True to continue the option of training.

while True:
    language_today = input("Which language do you want to train today? ")
    if language_today == "end":
        break
    train_mode = input("Do you want to repeat past wrong words or learn new ones? (repeat/new) ")
    while True:
        try: 
            goal = int(input("How many words do you want to train? "))
            break
        except:
            print("The goal must be an integer.")
            

    #repeat_or_new = input("Do you want to repeat past wrong words or learn new ones? ")
    #the positions are in lists because in the dataframe there are 5 languages and in the repetition mode there is just En and the language in the file


    if language_today in ["German", "Ger", "G", "German "]:
        positions = [1,1]
        language_today = "German"
    elif language_today in ["French", "Fr", "french", "French "]:
        positions = [2,1]
        language_today = "French"
    elif language_today in ["Spanish", "Es", "spanish", "Spanish "]:
        positions = [3,1]
        language_today = "Spanish"
    elif language_today in ["Portuguese", "P", "Port", "portuguese", "Portuguese "]:
        positions = [4,1]
        language_today  = "Portuguese"


    #function for the trainer that takes mode as an argument; either new words or repetition


    def learn_language_new(mode): 

        # open the dataframe if new words should be learned

        if mode == "new":
            with open("Df_translations.csv", "r", encoding= "utf-8") as f:
                lines = f.read().splitlines()
            position_of_language = positions[0]

        # open the textfile containing wrong words if the mode is to repeat

        elif mode == "repeat":
            with open(f"Wrong_words_{language_today}.txt", "r", encoding= "utf-8") as g:
                lines = g.read().splitlines()
            position_of_language = positions[1]


        score = 0

        for n in range(0,goal):


            rando = random.randint(0,(len(lines)-1)) #dynamic: length of lines of the text file/csv file

            word_line = lines[rando].split(",")

            word = word_line[position_of_language]
            if word[-1:] == "\n":
                word = word[:-1]

            print(f"What is the {language_today} word for {word_line[0]}?")

            input1 = input()

            if input1 == word:
                print("Good job!\n")
                score += 1
                
            else:
                with open(f"Wrong_words_{language_today}.txt", "r+", encoding = ":utf-8") as file:
                    if f"{word_line[0]},{word}" not in file.read().splitlines():
                        file.read()
                        file.write(f"{word_line[0]},{word}\n")

                input2 = input("Want a tip? " )
                if input2 in ["yes", "ys", "y", "ye", "ja", "j"]:
                    print(f"The word starts with {word[:2]}")
                    input3 = input("Next try: ")
                    if input3 == word:
                        print("Good job!\n")
                    else: print(f"The word was {word}\n")
                elif input2 != "yes":
                    print(f"The word was {word}\n")
        print(f"Your task is completed for today, great effort! Your score is {score}/{goal}.")

    learn_language_new(train_mode)
    