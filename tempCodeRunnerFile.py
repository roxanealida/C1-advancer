        # score = 0

        # for n in range(0,goal):

        #     rando = random.randint(1,len(lines)) #dynamic: length of lines of the text file/csv file
        #     word_line = lines[rando].split(",")

        #     print(f"What is the {language_today} word for {word_line[0]}?")

        #     input1 = input()

        #     if input1 == word_line[position_of_language]:
        #         print("Good job!\n")
        #         score += 1
                
        #     else:
        #         with open(f"Wrong_words_{language_today}", "a+", encoding = ":utf-8") as file:
        #             if word_line not in file.read().splitlines():
        #                 file.write(f"{word_line[0]},{word_line[position_of_language]}\n")
        #         input2 = input("Want a tip? " )
        #         if input2 in ["yes", "ys", "y"]:
        #             print(f"The word starts with {word_line[position_of_language][:2]}")
        #             input3 = input("Next try: ")
        #             if input3 == word_line[position_of_language]:
        #                 print("Good job!\n")
        #             else: print(f"The word was {word_line[position_of_language]}\n")
        #         elif input2 != "yes":
        #             print(f"The word was {word_line[position_of_language]}\n")
        # print(f"Your task is completed for today, great effort! Your score is {score}/{goal}.")