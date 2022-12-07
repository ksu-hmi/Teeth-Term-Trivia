## TTT GAME SETTINGS ##

## Questions: The player can choose to play from one of the four sets of terminology
## Each set will have ten questions each

    ## SET 1 QUESTIONS ##
question1 = ("True or False: Palate is the hard and soft tissues forming the roof of the mouth that separates the oral and nasal cavities.\n")
question2 = ("True or False: Periapical is the  area on top of tongue.\n")
question3 = ("True or False: Plaque build up does not affect tooth  health.\n"")
question4 = ("True or False: Periradicular is a small rod, cemented or driven into dentin to aid in retention of a restoration.\n")
question5 = ("True or False: Prophylaxis is the removal of plaque, calculus and stains from the tooth structures. It is intended to control local irritational factors\n")
question6 = ("What surgical procedure is done to create an opening in the trachea (windpipe) to aid in breathing.\n"
question7 = ("What is it called where there is restricted ability to open the mouth, usually due to inflammation or fibrosis of the muscles of mastication?\n")
question8 = ("Having the properties of dysplasia, invasion, and metastasis is called?.\n")
question9 = ("What is a positive reproduction of a body part formed on a cast from a negative impression?\n")
question10 = ("True or False: Occlusal pertains to the biting surfaces of the premolar and molar teeth or contacting surfaces of opposing teeth or opposing occlusion rims.\n")

## Answers correspond with the questions in the coressponding set
    ## SET 1 ANSWERS ##
    answers=
    ["True",
    "False", ## The area surrounding the end of the tooth root ##
    "False", ## Plaque is a  soft sticky substance that accumulates on teeth composed largely of bacteria and bacterial derivatives.##
    "False", 
    "True",
    "Tracheotomy", 
    "Trismus",
    "Malignant",
    "Moulage",
    "True"],

             
    ## SET 2 QUESTIONS ##   
question1 = ("True or False: Normally applied externally to teeth; bleaching be used internally for endodontically treated teeth.\n")
question2 = ("True or False: Calculus can adhere to crowns and/or roots of teeth or prosthetic devices.\n")
question3 = ("True or False: Crowns are solely made of metal.\n"") 
question4 = ("True or False: Decay is a term describing carious lesions in a tooth.\n")
question5 = ("True or False: Dentin in the mature state is not mineralized.\n")
question6 = ("True or False: Enamel is a soft calcified tissue covering dentin of the crown of tooth.\n")
question7 = ("True or False: Removing a tooth or tooth parts describes the term extraction.\n")
question8 = ("True or False: Fluoride is not necessary to maintain healthy teeth throughout your life.\n")
question9 = ("True or False: Gingivitis is inflammation of gingival tissue without loss of connective tissue.\n")
question10 = ("True or False: Halitosis is the dental term for bad breath.\n") 
    
    ## SET 2 ANSWERS ##  
answers =
    ["true",
    "true",
    "false", # It can be made of metal, ceramic or polymer materials or a combination of such materials.
    "true",
    "false", # Dentin is mineralized in its mature state
    "false", # Enamel is a HARD calcified tissue covering dentin of the crown of tooth
    "true",
    "false", # Fluoride is necessary to maintain healthy teeth.
    "true"],
    
     
    ## SET 3 QUESTIONS ##
question1 = ("True or False: Alloy is a compound combining two or more elements having properties not existing in any of the single constituent elements.\n”)
question2 = ("True or False: Parenteral is any technique of administration in which the agent is absorbed through the gastrointestinal (GI) tract or oral mucosa.\n”)
question3 = ("True or False: Transdermal is a technique of administration in which the drug is administered by patch or iontophoresis through skin.\n”)
question4 = ("True or False: Inhalation is a technique of administration in which a gaseous or volatile agent is introduced into the lungs and whose primary effect is due to absorption through the gas/blood interface.
question5 = ("True or False: Enteral is any technique of administration in which the drug bypasses the gastrointestinal tract
question6 = ("True or False: Intravenous is a technique of administration in which the anesthetic agent is not introduced directly into the patient’s venous system.
question7 = ("True or False: Transmucosal is muscle fibers covered by a mucous membrane that attaches the cheek, lips and or tongue to associated dental mucosa.\n”)
question8 = ("True or False: Palliative is an action that relieves pain but is not curative.\n”)
question9 = ("True or False: Pin is a small rod, cemented or driven into dentin to aid in retention of a restoration.\n”)
question10 = ("True or False: Rebase is the process of refitting a denture by replacing the base material.\n”)
    
    ## SET 3 ANSWERS ##
answers =
 ["true",
  "false," # Enteral #
  "true",
  "true",
  "false.", # Parenteral # 
  "false.", # Non-Intravenous #
  "false.", # Frenum #
  "true",
  "true",
  "true",
  "true"],
  
              
    ## SET 4 QUESTIONS ##
question1 = ("True or False: Brushing too hard can damage your tooth enamel.\n")
question2 = ("True or False: There is no right way to floss.\n")
question3 = ("True or False: Anyone can get a cavity.\n"")
question4 = ("True or False: Cavitys are only caused by sweets.\n")
question5 = ("True or False: Oral health affects your overall health\n")
question6 = ("True or False: Bleeding Gums is a bad sign.\n")
question7 = ("True or False: Brushing your teeth twice a day is enough to maintain good oral hygiene.\n")
question8 = ("True or False: You should only use a toothbrush with “hard” bristles for effective cleaning.\n")
question9 = ("True or False: When flossing, you only need to move the floss up and down between your teeth.\n")
question10 = ("True or False: You do not need to brush your gums, only your teeth.\n")
             
    ## SET 4 ANSWERS ##

answers =
    ["true",
    "false",
    "true",
    "false",
    "true",
    "true", 
    "false",
    "false",
    "false",
    "false"],
    
points = 0
name = None
yes = ['Yes', 'yes', 'YES']
no = ['No', 'no', 'NO']
category = 0

## RESET ZONE ##

def game_reset():
    '''
    Reset all variables of the whole game for a new play
    '''

    global points
    global name

    points = 0
    name = None
# end-function #

## GAME INTRO ZONE ##

def game_intro():
    '''
    Welcome the player and ask him for his name as long as he thinks is correct.
    '''

    print("\n       ***  Welcome to Teeth Term Trivia :D  **** \n")
    
    global name
    global category

    while name == None:
        name = input("What's your name? ")
        print("Welcome, "+name+", to Teeth Term Trivia!")
        correct = input("Are you ready to learn? ")
        if yes.count(correct) == True: ##"Yes" or ok == "yes" or ok == "YES":
            print("Awesome, let's do this!\n")
        else:
            print("Aww come on, let play anyways!")
            name = None

        list_categories() 
        start_system()

# end-function #
            
## GAME PLAY ZONE ##

def print_play_status(x):
    '''
    just print out the current score and the current challenge number.
    '''

    global points
    print("Right now your total score is", points)
    print("Challenge", x+1, "\n")

# end-function #

def start_system() : 
    
    system = int(input("Pick a category by typing a number (0 to exit) : 1-12\n"))
    if system == 0 : 
        game_end()
    else :
        print(greetings[system - 1])
        start_category(system)
   
def start_category(cat) : 
    global category
    category = cat
    
    game_play()
    
def list_categories() : 
    
  # loop through categories array and print categories #
  for c in categories : 
      print(categories.index(c) + 1 , " : " , c)

def play_quest(x):
    '''int -> int
    this functions asks the player question X, checks if player's answer is right and eventually changes the variable points.
    no examples needed
    '''
    global points
    global questions
    global answers
    answerPlayer = input(questions[category - 1][x])
    if answerPlayer.lower() == answers[category - 1][x]:
        print("Well done,", name + ", 10 points gained! Let's move to the next question.\n")
        points +=10
    else:
        print("Wrong! 0 points gained, the correct answer was:", answers[category - 1][x], ". Next question...\n")
    last_cat = len(questions[category - 1])
    if x == last_cat -1 : 
        global categories
        
        global greetings
        
        categories.pop(category - 1)
        greetings.pop(category - 1)
        questions.pop(category - 1)
        answers.pop(category - 1)
        if len(categories) == 0 : 
            game_end()
        else:
            list_categories() 
            start_system()

# end-function #

def game_play():
    '''
    first : tell the player his current score and the current challenge number
    second: tell the play_quest-function how many and which questions it must asks the player.
    '''
   
    for x in range(len(questions[category - 1])):
        print_play_status(x)
        play_quest(x)

# end-function #

## GAME END ZONE ##

def game_end():
    '''
    first : tell the player his finish score.
    second: ask the player if wants to play again and fullfil his wish.
    '''

    print("\nYou finished the game with a total of", points, "points! \n")

    again = None
    
    while again == None:
        again = input("Play again? ")
        if yes.count(again) == True:
            print("\nEnjoy :)\n")
            game_control()
        elif no.count(again) == True:
            print("        Congratulations!  You've completed the game."      )
            print("            https://github.com/ksu-hmi/Teeth-Term-Trivia"       )
            print("  Questions were created from terms gathered from the American Dental Association   ")
            print("  at the following address:  https://www.ada.org/publications/cdt/glossary-of-dental-clinical-terms  ")
            print("                                                         ")
            print("                   Thanks for playing!"                    )
            print("                ------ !! B Y E !! ------                  ")
            
        else:
            print("oh, just yes or no!")
            again = None

# end-function #
    
## GAME CONTROL ZONE ##

def game_control():
    '''
    Control the whole game with these single steps.
    '''
    game_reset()
    game_intro()
    
    #start_system()
   
    #game_play()
    #game_end()
# end-function #

## FIRST GAME START ZONE ##

game_control()
