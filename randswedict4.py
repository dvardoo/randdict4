import random
import string

#Function for getting a random passphrase
#Choses 4 random words from wordlist and concatenates as passphrase.
def passwd():
    with open('/usr/share/dict/swedish', 'r', encoding='iso-8859-1') as allWords:
        wordList = allWords.read()
        wordList = wordList.split()

    #Collects 4 random words and joins these to get the passphrase.
    for word in  wordList:	    
        randWord1 = random.choice(wordList)
        randWord2 = random.choice(wordList)
        randWord3 = random.choice(wordList)
        randWord4 = random.choice(wordList)
        randPasswd = '{0}{1}{2}{3}'.format(randWord1,randWord2,randWord3,randWord4)    
    
    #Checks if password is longer then 20 characters, if not it runs again.
    if len(randPasswd) > 20:
        print('*' * len(randPasswd) + '*****','\n',
        'Random words are:\n', randWord1.capitalize(), randWord2.capitalize(), randWord3.capitalize(), randWord4.capitalize())
        print('*' * len(randPasswd) + '*****','\n',
        'Random passphrase is:\n',randPasswd, '\n Passphrase length:', len(randPasswd), 'characters')
        print('*' * len(randPasswd) + '*****')
    else:
        print('*** \t Short random passphrase, running again \t***')
        passwd()
        
passwd()
