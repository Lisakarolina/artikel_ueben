import random


# counters for the ratio of success/failure

no_total = 0
no_correct = 0
no_sec_correct = 0
no_wrong = 0

vowels = ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü', 'ei', 'eu', 'au', 'ie']


def get_random_pair():

    # returns a random list containing two elements: article and substantive

    pair = random.choice(cresc)
    return pair
    


def benutzer_eingabe():

    print('Welcher Artikel gehört zu ' + subst + ': der, die oder das?')
    eingabe = input()
    return eingabe



def check_input(eingabe):

    # prompts the user to repeat input in case the input was not one of the three articles

    while eingabe not in ['der', 'die', 'das']:
        print('Eingabe ist nicht korrekt, bitte geben Sie der, die oder das an')
        eingabe = benutzer_eingabe()
        return eingabe       # Brauche ich dieses return in der while-Schleife?
    return eingabe



def bewerte1(eingabe):

    # evaluates the user's input. Repeating the question is conditioned upon the return value
    
    if eingabe == art:
        print('Richtig!')
        return 0

    else:
        print('Leider nicht richtig. Versuch es noch einmal!')

    return 1
    


def bewerte2(eingabe):

    # evaluates the second answer to the question and presents the solution if necessary
    
    if eingabe == art:
        print('Richtig!')
        return 0

    else:
        print('Das stimmt leider nicht. Die richtige Lösung ist: %s' % (art))
        return 1



def keep_playing():

    print('Willst du weiter üben: ja oder nein?')
    if not input().lower().startswith('j'):
        return 0
    return 1    



def get_cues():

    # helps user choose the right genus in case the first guess was wrong. 
    
    if art == 'das' and subst.startswith('Ge'):
        print('Hinweis: Kollektiva, die mit Ge- beginnen, sind meist neutrum.')
    elif art == 'der' and subst.endswith('ig'):
        print('Hinweis: Substantive auf -ig sind meist männlich.')
    elif art == 'der' and subst.endswith('ling'):
        print('Hinweis: Substantive auf -ling sind meist männlich.')
    elif art == 'der' and subst.endswith('s') and (subst[len(subst)-2] not in vowels):
        print('Hinweis: Substantive auf Konsonant + s sind meist männlich.')
    elif art == 'der' and subst.endswith('ant'):
        print('Hinweis: Fremdwörter auf -ant sind meist männlich')
    elif art == 'der' and subst.endswith('är'):
        print('Hinweis: Fremdwörter auf -är sind meist männlich')
    elif art == 'der' and subst.endswith('eur'):
        print('Hinweis: Fremdwörter auf -eur sind meist männlich')
    elif art == 'der' and subst.endswith('loge'):
        print('Hinweis: Fremdwörter auf -loge sind meist männlich')
    elif art == 'der' and subst.endswith('er'):
        print('Hinweis: Substantive auf -er sind meist männlich.')
      


    elif art == 'die' and subst.endswith('ei'):
        print('Hinweis: Substantive auf -ei sind meist weiblich.')
    elif art == 'die' and subst.endswith('heit'):
        print('Hinweis: Substantive auf -heit sind meist weiblich.')
    elif art == 'die' and subst.endswith('keit'):
        print('Hinweis: Substantive auf -keit sind meist weiblich.')
    elif art == 'die' and subst.endswith('schaft'):
        print('Hinweis: Substantive auf -schaft sind meist weiblich.')
    elif art == 'die' and subst.endswith('ung'):
        print('Hinweis: Substantive auf -ung sind meist weiblich.')
    elif art == 'die' and subst.endswith('e') and check_for_two_syllables(check_for_diphthongs(subst)):
        print('Hinweis: zweisilibige Substantive auf -e sind meist weiblich.')
    elif art == 'die' and subst.endswith('e'):
        print('Hinweis: viele Substantive auf -e sind weiblich.')
    elif art == 'die' and subst.endswith('age'):
        print('Hinweis: Fremdwörter auf -age sind meist weiblich.')
    elif art == 'die' and subst.endswith('ät'):
        print('Hinweis: Substantive auf -ät sind meist weiblich.')
    elif art == 'die' and subst.endswith('ie'):
        print('Hinweis: Fremdwörter auf -ie sind meist weiblich.')
    elif art == 'die' and subst.endswith('ion'):
        print('Hinweis: Substantive auf -ion sind meist weiblich.')


    
    elif art == 'das' and subst.endswith('ett'):
        print('Hinweis: Fremdwörter auf -ett sind meist neutrum.')
    elif art == 'das' and subst.endswith('ma'):
        print('Hinweis: Fremdwörter auf -ma sind meist neutrum.')
    elif art == 'das' and subst.endswith('um'):
        print('Hinweis: Fremdwörter auf -um sind meist neutrum.')
    elif art == 'das' and subst.endswith('nis'):
        print('Hinweis: Substantive auf -nis sind oft neutrum. Es gibt aber einige Ausnahmen')
    elif art == 'das' and subst.endswith('ment'):
        print('Hinweis: Substantive auf -ment sind meist neutrum.')


    
    
def h_filter_vowels(element):

    vowels = ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü', 'ei', 'eu', 'au', 'ie']
    if element in vowels:
        return True
    else:
        return False



def check_for_diphthongs(word):

    # checks for diphthongs that are supposed to be counted as one vowel (so that the syllable counting is still working)

    word = word.lower()
    diphthong_count = 0
    zähler = 0
    for letter in word:
        if letter == 'e' and word[zähler+1] in ['i', 'u'] or letter == 'a' and word[zähler+1] in ['u'] or letter == 'i' and word[zähler+1] in ['e']:  
            diphthong_count =+1                                                                                
        zähler =+ 1
    return diphthong_count



def check_for_two_syllables(diphthong_count):

    # combines number of diphthongs and number of single-letter vowels to correct number of syllables

    if check_for_single_vowels(subst) == 3 and diphthong_count == 2:                  # case 1: words like 'Kleie'
        return True
    if check_for_single_vowels(subst) == 3 and diphthong_count == 1:                  # case 2: words like 'Pleite'
        return True
    if check_for_single_vowels(subst) == 4 and diphthong_count == 2:                  # case 3: words like 'Blaukraut'
        return True
    if check_for_single_vowels(subst) == 2 and diphthong_count == 0:                  # case 4: words like 'Vase'
        return True

    else:
        return False
  
  

def check_for_single_vowels(word):

    # looks for vowels that are represented by only one letter

    word = word.lower()
    vowels_list = filter(h_filter_vowels, word)
    
    return len(list(vowels_list))
    



# read data into list of lists

myfile = open("newfile_nou.txt", "r")

cresc = []
for line in myfile:
    cresc.append(line.split())
    
myfile.close()

print('Hier kannst du üben, Substantiven den richtigen Artikel zuzuordnen. \n Du bekommst eine Frage gestellt und gibst als Antwort einen Artikel ein. Falls du falsch \
liegst, kannst du es noch einmal versuchen. Wenn es eine Regel gibt, die dir helfen könnte, bekommst du einen Hinweis. Am Ende des Spiels wird dir angezeigt, wie viele \
Aufgaben du richtig gelöst hast. \n Du kannst nach jeder Frage entscheiden, ob du weiter üben willst.')


# game-loop

while True:
    print()
    no_total += 1
    pair = get_random_pair()
    subst = pair[1]
    art = pair[0]
    eingabe = benutzer_eingabe()
    a = check_input(eingabe)
    if eingabe != a:          # assigns repeated user input to eingabe in case the input was incorrect
        eingabe = a
    if bewerte1(eingabe):
        get_cues()
        eingabe = benutzer_eingabe()   # second try
        if not bewerte2(eingabe):
            no_sec_correct += 1
        else:
            no_wrong += 1
            
    else:
        no_correct += 1        
            
    if not keep_playing():
        print('Du hast ' + str(no_correct) + ' von ' + str(no_total) + ' Fragen richtig beantwortet.')               # evaluation
        if no_sec_correct > 0:
            print('Du hast ' + str(no_sec_correct) + ' von ' + str(no_total) + ' Fragen beim zweiten Versuch richtig beantwortet.')
        if no_wrong > 0:
            print('Du hast ' + str(no_wrong) + ' von ' + str(no_total) + ' Fragen falsch beantwortet.')
        break

   
    


