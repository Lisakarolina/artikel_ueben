"""
This game presents the player with a randomly chosen substantive and prompts then to determine its grammatical genus

If the first guess was not correct, the player gets a second chance and is prompted to give it another try. For some groups of substantives
there are rules, so in case the current substantive belongs to one of these groups the rule is given as a cue. 
The evaluation at the end of a session takes into account that the second guess is much more likely to give the correct solution (50 % 
probability, and in some cases even a hint to the right article): It shows the number of correct guesses that were right at the first
try separately.
 
"""




import random
import sys




class Scores():

    """contains counters for the record of sucess/failure and methods to manipulate them"""

    def __init__(self):
        self.no_total = 0
        self.no_correct_first_try = 0
        self.no_correct_sec_try = 0
        self.no_wrong = 0

    def increment_total(self):
        self.no_total += 1

    def increment_first_try(self):
        self.no_correct_first_try += 1

    def increment_sec_try(self):
        self.no_correct_sec_try += 1

    def increment_wrong(self):
        self.no_wrong += 1



VOWELS = ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü', 'ei', 'eu', 'au', 'ie']


FILE_NAME = "/home/lisaac/newfile_nou.txt"




def check_input(user_input):

    """prompt the user to repeat input in case the input was not one of the three articles"""

    while user_input not in ['der', 'die', 'das']:
        print('Eingabe ist nicht korrekt, bitte geben Sie der, die oder das an')
        user_input = request_user_input()
        
    return user_input



def evaluate1(user_input):

    """evaluate the user's input. Repeating the question is conditioned upon the return value"""
    
    if user_input == art:
        return True

    else:
        return False
    


def evaluate2(user_input):

    """evaluates the second answer to the question and presents the solution if necessary"""
    
    if user_input == art:
        return True

    else:
        return False



#---------------------------CLI-Stuff---------------------------------------------------------------------------------------------------------------------------


def printout_evaluation1(result):
    if result == True:
        print('Richtig!')
    else:
        print('Leider nicht richtig. Versuch es noch einmal!')



def printout_evaluation2(result):
    if result == True:
        print('Richtig!')
    else:
         print('Das stimmt leider nicht. Die richtige Lösung ist: ' + art)


def printout_total_record(no_correct_first_try, no_correct_sec_try, no_wrong, no_total):
    print('Du hast ' + str(no_correct_first_try) + ' von ' + str(no_total) + ' Fragen richtig beantwortet.')               # evaluation
    if no_correct_sec_try > 0:
        print('Du hast ' + str(no_correct_sec_try) + ' von ' + str(no_total) + ' Fragen beim zweiten Versuch richtig beantwortet.')
    if no_wrong > 0:
        print('Du hast ' + str(no_wrong) + ' von ' + str(no_total) + ' Fragen falsch beantwortet.')


def request_user_input():

    """request user_input and return it"""

    print('Welcher Artikel gehört zu ' + subst + ': der, die oder das?')
    user_input = input()
    return user_input


def keep_playing():

    print('Willst du weiter üben: ja oder nein?')
    return input().lower().startswith('j')
        

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------


def get_cues():

    """help user choose the right genus in case the first guess was wrong.""" 
    
    if art == 'der':
        if subst.endswith('ig'):
            print('Hinweis: Substantive auf -ig sind meist männlich.')
        elif subst.endswith('ling'):
            print('Hinweis: Substantive auf -ling sind meist männlich.')
        elif subst.endswith('s') and (subst[len(subst)-2] not in vowels):
            print('Hinweis: Substantive auf Konsonant + s sind meist männlich.')
        elif subst.endswith('ant'):
            print('Hinweis: Fremdwörter auf -ant sind meist männlich')
        elif subst.endswith('är'):
            print('Hinweis: Fremdwörter auf -är sind meist männlich')
        elif subst.endswith('eur'):
            print('Hinweis: Fremdwörter auf -eur sind meist männlich')
        elif subst.endswith('loge'):
            print('Hinweis: Fremdwörter auf -loge sind meist männlich')
        elif subst.endswith('er'):
            print('Hinweis: Substantive auf -er sind meist männlich.')
            
  
    elif art == 'die':
        if subst.endswith('ei'):
            print('Hinweis: Substantive auf -ei sind meist weiblich.')
        elif subst.endswith('heit'):
            print('Hinweis: Substantive auf -heit sind meist weiblich.')
        elif subst.endswith('keit'):
            print('Hinweis: Substantive auf -keit sind meist weiblich.')
        elif subst.endswith('schaft'):
            print('Hinweis: Substantive auf -schaft sind meist weiblich.')
        elif subst.endswith('ung'):
            print('Hinweis: Substantive auf -ung sind meist weiblich.')
        elif subst.endswith('e') and check_for_two_syllables(check_for_diphthongs(subst), subst):
            print('Hinweis: zweisilibige Substantive auf -e sind meist weiblich.')
        elif subst.endswith('e'):
            print('Hinweis: viele Substantive auf -e sind weiblich.')
        elif subst.endswith('age'):
            print('Hinweis: Fremdwörter auf -age sind meist weiblich.')
        elif subst.endswith('ät'):
            print('Hinweis: Substantive auf -ät sind meist weiblich.')
        elif subst.endswith('ie'):
            print('Hinweis: Fremdwörter auf -ie sind meist weiblich.')
        elif subst.endswith('ion'):
            print('Hinweis: Substantive auf -ion sind meist weiblich.')

      
    elif art == 'das':
        if subst.endswith('ett'):
            print('Hinweis: Fremdwörter auf -ett sind meist neutrum.')
        elif subst.endswith('ma'):
            print('Hinweis: Fremdwörter auf -ma sind meist neutrum.')
        elif subst.endswith('um'):
            print('Hinweis: Fremdwörter auf -um sind meist neutrum.')
        elif subst.endswith('nis'):
            print('Hinweis: Substantive auf -nis sind oft neutrum. Es gibt aber einige Ausnahmen')
        elif subst.endswith('ment'):
            print('Hinweis: Substantive auf -ment sind meist neutrum.')
        elif subst.startswith('Ge'):
            print('Hinweis: Kollektiva, die mit Ge- beginnen, sind meist neutrum.')
    
    
def filter_vowels(element):

    if element in vowels:
        return True
    else:
        return False



def check_for_diphthongs(word):

    """checks for diphthongs that are supposed to be counted as one vowel (so that the syllable counting is still working)"""

    word = word.lower()
    diphthong_count = 0
    zähler = 0
    for letter in range(0, len(word) - 1):         # make sure an index error is avoided by only checking vowels that are not the last letter
        letter = word[zähler] 
        if (letter == 'e' and word[zähler+1] in ['i', 'u'] or
        letter == 'a' and word[zähler+1] in ['u'] or
        letter == 'i' and word[zähler+1] in ['e']):  
            diphthong_count += 1                                                                                
        zähler += 1
    return diphthong_count

  
  

def check_for_two_syllables(diphthongs, substantive):
 
    """combines number of diphthongs and number of single-letter vowels to correct number of syllables"""

    vowels = check_for_single_vowels(substantive)

    return (vowels == 3 and diphthongs == 2 or             # case 1: words like 'Kleie'
            vowels == 3 and diphthongs == 1 or             # case 2: words like 'Pleite'
            vowels == 4 and diphthongs == 2 or             # case 3: words like 'Blaukraut'
            vowels == 2 and diphthongs == 0)               # case 4: words like 'Vase'




def check_for_single_vowels(word):

    """look for vowels that are represented by only one letter"""

    return len([letter for letter in word.lower() if letter in VOWELS])
    




def read_in_file(FILE_NAME):                      # read the content of the file containing the substantives and articles into the variable content_of_file

    myfile = open(FILE_NAME, "r")
    content_of_file = []
    for line in myfile:                            
        content_of_file.append(line.split())
    myfile.close()
    return content_of_file





print('Hier kannst du üben, Substantiven den richtigen Artikel zuzuordnen. \n Du bekommst eine Frage gestellt und gibst als Antwort einen Artikel ein. Falls du falsch \
liegst, kannst du es noch einmal versuchen. Wenn es eine Regel gibt, die dir helfen könnte, bekommst du einen Hinweis. Am Ende des Spiels wird dir angezeigt, wie viele \
Aufgaben du richtig gelöst hast. \n Du kannst nach jeder Frage entscheiden, ob du weiter üben willst.')


content_of_file = read_in_file(FILE_NAME)

counters = Scores()

# game-loop

while True:
    print()
    counters.increment_total()
    pair = random.choice(content_of_file)           # randomly choose an element of the list
    subst = pair[1]
    art = pair[0]

    if not evaluate1(check_input(request_user_input())):
        printout_evaluation1(False)
        get_cues()
        # if input() == 'q':  # Frage: gibt man dem Nutzer so die Möglichkeit, das Spiel jederzeit abbrechen zu können ? und warum funktioniert's nicht?
        #    sys.exit
        user_input = request_user_input()   # second try
        if evaluate2(user_input):
            printout_evaluation2(True)
            counters.increment_sec_try()
            
        else:
            printout_evaluation2(False)
            counters.increment_wrong()
                  
    else:
        printout_evaluation1(True)
        counters.increment_first_try()
               
            
    if not keep_playing():

        printout_total_record(counters.no_correct_first_try, counters.no_correct_sec_try, counters.no_wrong, counters.no_total)

        break

   
    


