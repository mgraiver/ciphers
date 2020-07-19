ALPHABET='abcdefghijklmnopqrstuvwxyz'

def in_engl_alpha(char):
    '''
    (str)--> Bool
    Returns True if char is a non-empty string w/ only letters
    from the alphabet, False otherwise
     
    >>>in_engl_alpha('f')
    True
    >>>in_engl_alpha('H')
    True
    >>>in_engl_alpha('AppLe')
    True
    >>>in_engl_alpha('')
    False
    >>>in_engl_alpha('@pple')
    False
    >>>in_engl_alpha('apples and pears')
    False
    >>>in_engl_alpha('0range')
    False
    '''
    if len(char)==0:
        return False
    
    i=0
    char=char.lower()
    
    for i in range(len(char)):
        if (char[i]) in ALPHABET:
            i+=1
        else:
            return False
    return True

def retrieve_index(letter):
    '''
    (str)--> int
    Returns index of given letter in the alphabet
    
    >>>retrieve_index(F)
    6
    >>>retrieve_index(a)
    0
    >>>retrieve_index(Z)
    24
    >>>retrieve_index('')
    -1
    >>>retrieve_index(6)
    -1
    >>>retrieve_index(cow)
    -1
    '''
    
    letter=letter.lower()
    
    return(ALPHABET.find(letter))

def new_index(letter,number):
    '''
    Returns new letter indicated by shift given by user
    
    >>>new_index('p',5)
    u
    >>>shift_char('l',0)
    'l'
    >>> new_index('a',-1)
    'z'
    >>> new_index('d',-9)
    'u'
    >>> new_index('j',56)
    'n'
    
    '''
    new_index=(retrieve_index(letter)+number)%26
    return ALPHABET[new_index]

def shift_char(char,number):
    '''
    (str,int)-->str
    Returns letter shifted by given no. of characters in the alphabet by user.
    Returns character otherwise.

    >>>shift_char('aft',1)
    Traceback (most recent call last):
    ValueError: the input string should contain a single character
    >>>shift_char(f,4)
    k
    >>>shift_char('l',0)
    'l'
    >>> shift_char("!",0)
    '!'
    >>> shift_char("£",-4)
    '£'
    >>> shift_char("T",-63)
    'i'
    >>> shift_char("a",-1)
    'z'
    >>> shift_char("w",9)
    'f'
    
    '''
    if len(char)<1:
       raise ValueError("The input string should contain a single character")
    
    elif retrieve_index(char)==-1:
       return (char)
    else:
      return new_index(char,number)

def get_keys(word):
    '''
    (str)--> list
    Returns index of each letter in given str
    
    >>> get_keys('animal')
    [0, 13, 8, 12, 0, 11]
    >>> get_keys('')
    []
    >>> get_keys("CaPiTal")
    [2, 0, 15, 8, 19, 0, 11]
    >>> get_keys("h E l P")
    Traceback (most recent call last):
        ValueError: the input string should contain a single character
    ValueError: the input string must contain only characters from the English alphabet
    >>> get_keys("0rder")
    Traceback (most recent call last):
        ValueError: the input string should contain a single character
    ValueError: the input string must contain only characters from the English alphabet
    >>> get_keys("g_reen")
    Traceback (most recent call last):
        ValueError: the input string should contain a single character
    ValueError: the input string must contain only characters from the English alphabet
    
    '''
    if len(word)>0 and in_engl_alpha(word)== False:
        raise ValueError('The input string must contain only characters from the English alphabet')
    else:
        
        word_to_num=[]
        i=0
        index=0
        
        for i in range(len(word)):
#           variable returns index moving along string  
            index=retrieve_index(word[i])
            word_to_num.append(index)
            i+=1
    return word_to_num       

def pad_keyword(string,length):
    '''
    (str,int)-->str
    Returns given string with 'n' number of characters
    
    >>>pad_keyword("Apple",2)
    "Ap"
    >>>pad_keyword("Apple",0)
    ""
    >>>pad_keyword("Cat and Cow", 4)
    "Cat "
    >>>pad_keyword("Cr0zY!£",9)
    "Cr0zY!£Cr"
    >>> pad_keyword(" ",6)
    '      '
    >>> pad_keyword("",4)
    Traceback (most recent call last):
    ValueError: The string must contain at least one character
    >>>pad_keyword("",0)
    ValueError: The string must contain at least one character
    >>> pad_keyword("444",9)
    '444444444'
    
    '''
    if len(string)==0:
        raise ValueError('The string must contain at least one character')
    i=0
    string_var=""
    
    for e in range(length):
        string_var+=string[i]
        i+=1
#       returns back to first letter if length>=characters in string
        if (i)>=len(string):
            i=0
    return string_var

