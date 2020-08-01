import random



class Question():
    def __init__(self):

        self.vowels = ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü', 'ei', 'eu', 'au', 'ie']
        self.filename = "/home/lisaac/newfile_nou.txt"

        self.content_of_file = self.read_in_file(self.filename)

        self.pair = random.choice(self.content_of_file)           # randomly choose an element of the list
        self.subst = self.pair[1]
        self.art = self.pair[0]

   


    def der_das(self):    # der-button was pressed, but 'das' is the right answer
        if self.subst.endswith('ett'):
            return 'Hinweis: Fremdwörter auf -ett sind meist neutrum.'
        elif self.subst.endswith('ma'):
            return 'Hinweis: Fremdwörter auf -ma sind meist neutrum.'
        elif self.subst.endswith('um'):
            return 'Hinweis: Fremdwörter auf -um sind meist neutrum.'
        elif self.subst.endswith('nis'):
            return 'Hinweis: Substantive auf -nis sind oft neutrum. Es gibt aber einige Ausnahmen'
        elif self.subst.endswith('ment'):
            return 'Hinweis: Substantive auf -ment sind meist neutrum.'
        elif self.subst.startswith('Ge'):
            return 'Hinweis: Kollektiva, die mit Ge- beginnen, sind meist neutrum.'


    def der_die(self):    # der-button was pressed, but 'die' is the right answer
        if self.subst.endswith('ei'):
            return 'Hinweis: Substantive auf -ei sind meist weiblich.'
        elif self.subst.endswith('heit'):
            return 'Hinweis: Substantive auf -heit sind meist weiblich.'
        elif self.subst.endswith('keit'):
            return 'Hinweis: Substantive auf -keit sind meist weiblich.'
        elif self.subst.endswith('schaft'):
            return 'Hinweis: Substantive auf -schaft sind meist weiblich.'
        elif self.subst.endswith('ung'):
            return 'Hinweis: Substantive auf -ung sind meist weiblich.'
        elif self.subst.endswith('e') and self.check_for_two_syllables(self.check_for_diphthongs()):
            return 'Hinweis: zweisilibige Substantive auf -e sind meist weiblich.'
        elif self.subst.endswith('e'):
            return 'Hinweis: viele Substantive auf -e sind weiblich.'
        elif self.subst.endswith('age'):
            return 'Hinweis: Fremdwörter auf -age sind meist weiblich.'
        elif self.subst.endswith('ät'):
            return 'Hinweis: Substantive auf -ät sind meist weiblich.'
        elif self.subst.endswith('ie'):
            return 'Hinweis: Fremdwörter auf -ie sind meist weiblich.'
        elif self.subst.endswith('ion'):
            return 'Hinweis: Substantive auf -ion sind meist weiblich.'
        
            

    def die_der(self):    # die-button was pressed, but 'der' is the right answer
        if self.subst.endswith('ig'):
            return 'Hinweis: Substantive auf -ig sind meist männlich.'
        elif self.subst.endswith('ling'):
            return 'Hinweis: Substantive auf -ling sind meist männlich.'
        elif self.subst.endswith('s') and (self.subst[len(self.subst)-2] not in self.vowels):
            return 'Hinweis: Substantive auf Konsonant + s sind meist männlich.'
        elif self.subst.endswith('ant'):
            return 'Hinweis: Fremdwörter auf -ant sind meist männlich'
        elif self.subst.endswith('är'):
            return 'Hinweis: Fremdwörter auf -är sind meist männlich'
        elif self.subst.endswith('eur'):
            return 'Hinweis: Fremdwörter auf -eur sind meist männlich'
        elif self.subst.endswith('loge'):
            return 'Hinweis: Fremdwörter auf -loge sind meist männlich'
        elif self.subst.endswith('er'):
            return 'Hinweis: Substantive auf -er sind meist männlich.'


    def die_das(self):    # die-button was pressed, but 'das' is the right answer
        if self.subst.endswith('ett'):
            return 'Hinweis: Fremdwörter auf -ett sind meist neutrum.'
        elif self.subst.endswith('ma'):
            return 'Hinweis: Fremdwörter auf -ma sind meist neutrum.'
        elif self.subst.endswith('um'):
            return 'Hinweis: Fremdwörter auf -um sind meist neutrum.'
        elif self.subst.endswith('nis'):
            return 'Hinweis: Substantive auf -nis sind oft neutrum. Es gibt aber einige Ausnahmen'
        elif self.subst.endswith('ment'):
            return 'Hinweis: Substantive auf -ment sind meist neutrum.'
        elif self.subst.startswith('Ge'):
            return 'Hinweis: Kollektiva, die mit Ge- beginnen, sind meist neutrum.'
                
            

    def das_der(self):    # das-button was pressed, but 'der' is the right answer
        if self.subst.endswith('ig'):
            return 'Hinweis: Substantive auf -ig sind meist männlich.'
        elif self.subst.endswith('ling'):
            return 'Hinweis: Substantive auf -ling sind meist männlich.'
        elif self.subst.endswith('s') and (self.subst[len(self.subst)-2] not in self.vowels):
            return 'Hinweis: Substantive auf Konsonant + s sind meist männlich.'
        elif self.subst.endswith('ant'):
            return 'Hinweis: Fremdwörter auf -ant sind meist männlich'
        elif self.subst.endswith('är'):
            return 'Hinweis: Fremdwörter auf -är sind meist männlich'
        elif self.subst.endswith('eur'):
            return 'Hinweis: Fremdwörter auf -eur sind meist männlich'
        elif self.subst.endswith('loge'):
            return 'Hinweis: Fremdwörter auf -loge sind meist männlich'
        elif self.subst.endswith('er'):
            return 'Hinweis: Substantive auf -er sind meist männlich.'



    def das_die(self):    # das-button was pressed, but 'die' is the right answer
        if self.subst.endswith('ei'):
            return 'Hinweis: Substantive auf -ei sind meist weiblich.'
        elif self.subst.endswith('heit'):
            return 'Hinweis: Substantive auf -heit sind meist weiblich.'
        elif self.subst.endswith('keit'):
            return 'Hinweis: Substantive auf -keit sind meist weiblich.'
        elif self.subst.endswith('schaft'):
            return 'Hinweis: Substantive auf -schaft sind meist weiblich.'
        elif self.subst.endswith('ung'):
            return 'Hinweis: Substantive auf -ung sind meist weiblich.'
        elif self.subst.endswith('e') and self.check_for_two_syllables(self.check_for_diphthongs()):
            return 'Hinweis: zweisilibige Substantive auf -e sind meist weiblich.'
        elif self.subst.endswith('e'):
            return 'Hinweis: viele Substantive auf -e sind weiblich.'
        elif self.subst.endswith('age'):
            return 'Hinweis: Fremdwörter auf -age sind meist weiblich.'
        elif self.subst.endswith('ät'):
            return 'Hinweis: Substantive auf -ät sind meist weiblich.'
        elif self.subst.endswith('ie'):
            return 'Hinweis: Fremdwörter auf -ie sind meist weiblich.'
        elif self.subst.endswith('ion'):
            return 'Hinweis: Substantive auf -ion sind meist weiblich.'



    def check_for_diphthongs(self): 

        """checks for diphthongs that are supposed to be counted as one vowel (so that the syllable counting is still working)"""

        subst = self.subst.lower()
        diphthong_count = 0
        zähler = 0
        for letter in range(0, len(subst) - 1):         # make sure an index error is avoided by only checking vowels that are not the last letter
            letter = subst[zähler] 
            if (letter == 'e' and subst[zähler+1] in ['i', 'u'] or
            letter == 'a' and subst[zähler+1] in ['u'] or
            letter == 'i' and subst[zähler+1] in ['e']):  
                diphthong_count += 1                                                                                
            zähler += 1
        return diphthong_count

  
  

    def check_for_two_syllables(self, diphthongs):
 
        """combines number of diphthongs and number of single-letter vowels to correct number of syllables"""

        vowels = self.check_for_single_vowels()

        return (vowels == 3 and diphthongs == 2 or             # case 1: words like 'Kleie'
                vowels == 3 and diphthongs == 1 or             # case 2: words like 'Pleite'
                vowels == 4 and diphthongs == 2 or             # case 3: words like 'Blaukraut'
                vowels == 2 and diphthongs == 0)               # case 4: words like 'Vase'




    def check_for_single_vowels(self):

        """look for vowels that are represented by only one letter"""

        return len([letter for letter in self.subst.lower() if letter in self.vowels])




    def read_in_file(self, filename):       # read the content of the file containing the substantives and articles into the variable content_of_file

        myfile = open(filename, "r")
        content_of_file = []
        for line in myfile:                            
            content_of_file.append(line.split())
        myfile.close()
        return content_of_file





