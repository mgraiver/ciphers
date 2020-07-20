import crypto_helpers as cr

def crypto_caesar(message,shift):
    '''
    Returns given message shifted by
    given number of characters along alphabet
    
    (str,int)-->str
    
    >>>crypto_caesar("klm",-10)
    'abc'
    >>> crypto_caesar("cats and dogs",4)
    'gexw erh hskw'
    >>> crypto_caesar("cow!!!",4)
    'gsa!!!'
    >>> crypto_caesar("help",5)
    'mjqu'
    >>>crypto_caesar("comp",0)
    'comp'
    >>>crypto_caesar("comp",-0)
    'comp'
    
    '''
    
    encrypt_caesar=""
    for i in range(len(message)):
        encrypt_caesar+=cr.shift_char(message[i],shift)
       
    return encrypt_caesar

def caesar(message,key,crypt):
    
    '''
    (str,int,int)--> str
    Returns encrypted/decrypted message, of given key. Returns error otherwise.
    
    >>> caesar("alphabet",7,1)
    'hswohila'
    >>> caesar("lmtts",82,-1)
    'hippo'
    >>> caesar("help",0,1)
    'help'
    caesar("0ctOpus",-5,1)
    '0xojkpn'
    
    '''
    # if encrypt, takes positive shift (key)
    # if decrypt, takes negative of shift (key)
    if crypt==1:
        new_message=crypto_caesar(message,key)
        
    elif crypt==-1:
        key=-key
        new_message=crypto_caesar(message,key)
    else:
        raise ValueError("mode not supported")
    return new_message

# takes the 'n' index of the key
def key_position(key,i):
    '''
    (str,int)-->int
    Returns position of given index by user of the key
    
    >>>key_position('alpha',0)
    0
    >>>key_position('alpha',3)
    7
    >>>key_position('',2)
    IndexError: list index out of range
    >>>key_position('cat and_Cow',3)
    ValueError: the input string must contain only characters from the English alphabet
    >>>key_position('apple',56)
    IndexError: list index out of range
    '''
    position=cr.get_keys(key)
    return (position[i])
  

def vigenere(message,key,crypt):
    
    '''
    (str,int,int)--> str
    Returns encrypted/decrypted message, of given key. Returns error otherwise.
    
    >>> vigenere("How are you?","good",1)
    'nck gfs eci?'
    >>> vigenere("nck gfs eci?","good",-1)
    'how are you?'
    >>>vigenere("rfavtoybkbs kg rqcx!", "comp",-1)
    "programming is cool!"
    >>>vigenere("programming", "computerprogramming",1)
    'rfavltqdxeu'
    >>> vigenere("The grass is green","green",1)
    'zyi txrww oj kekvr'
    >>> vigenere("The grass is green","",1)
    Traceback (most recent call last):
    ValueError: The string must contain at least one character
    >>> vigenere("The sky is blue", "aaa",-1)
    'the sky is blue'
    >>> vigenere("24 hours a day", "9to5",1)
    Traceback (most recent call last):
    ValueError: The input string must contain only characters from the English alphabet
    >>> vigenere("24 hours a day", "nine to five",1)
    Traceback (most recent call last):
    ValueError: The input string must contain only characters from the English alphabet
    >>>vigenere("coding is fun", "code",6)
    ValueError: mode not supported
    
    '''
    
    message_length=len(message)
#   variable returns index for all letters in given message
    keyword=cr.pad_keyword(key,message_length)
    
    i=0
    new_message=""
#   if encrypt, takes positive of each index (key_position())
#   if decrypt, takes negative of each index
    if crypt==1:
        
        for i in range (message_length):
            new_index=key_position(keyword,i)
            new_message+=cr.shift_char(message[i],new_index)
            i+=1

    elif crypt==-1:
        
        for i in range (message_length):
            new_index=-(key_position(keyword,i))
            new_message+=cr.shift_char(message[i],new_index)
            i+=1
        
    else:
        raise ValueError("mode not supported")
    
    return new_message


