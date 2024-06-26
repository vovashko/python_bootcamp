print('''
           .::7777::-.
          /:'////' `::>/|/             ,.-----__
        .',  ||||   `/( e\          ,:::://///,:::-.
    -==~-'`-Xm````-mr' `-_\        /:''/////// ``:::`;/|/
                                  /'   ||||||     :://'`\
                     ,          .' ,   ||||||     `/(  e \
         \/               -===~__-'\__X_`````\_____/~`-._ `.
                   .,                 ~~        ~~       `~-'
                       _____               /`
       '\/          ,::////;::-.          \|      o
                   /:'///// ``::>/|/            \/
                 .',  ||||    `/( e\
             -==~-'`-Xm````-mm-' `-_\      \,     
    ''')

print("Welcome to the Armadillo World")
print("It's a world full of armadillos.")
first_question = input("Would you like to pet one of the armadillos? Y or N\n")
if first_question == "Y":
    print("You made a mistake. Armadillo bit off your finger and you died in pain.")
elif first_question == "N":
    print("Wise decision")
    second_question = input("One of the armadillos looking at you with curiosity. It says that you are the chose one. Do you accept your faith? Y or N\n")
    if second_question == "N":
        print("Too bad. Go home you sore loser. Coward!")
    elif second_question == "Y":
        print("Armadillo handed you a secret sword.")
        third_question = input("Armadillos noticed that one of them is the impostor. You should find him out and kill before it's too late. Which one is it? Left, right, center\n")
        if third_question == "left":
            print("You killed the wrong armadillo. Piglet took over the kingdom and destroyed armadillo world.")
        elif third_question == "center":
            print("You are indeed the chosen. The overseer of armadillos. Long live you!")
        elif third_question == "right":
            print("You tried to swing your sword, but you triped and fell on it yourself. Too bad. You dead.")