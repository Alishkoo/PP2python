#in pep8 we write first letter with upper 

class Sstring:
    word = ""


    def getString(self, word):
        self.word = word


    def printString(self):
        print(self.word.upper())


a = Sstring()

a.getString(input("Enter the word: "))

a.printString()


