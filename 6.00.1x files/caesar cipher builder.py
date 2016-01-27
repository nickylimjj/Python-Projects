import string

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    assert type(shift) == int and shift < 26 and shift >=0
    
    lettersL = string.ascii_lowercase
    lettersU = string.ascii_uppercase
    dic = {}
    dicU = {}
    
    for i in range(0,len(lettersL and lettersU)):
        dic[lettersL[i]] = lettersL[(i+shift)%26]
        dicU[lettersU[i]] = lettersU[(i+shift)%26]
        
        dic.update(dicU)
    return dic
    
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    res=''
    for i in text:
        if i in coder:
            i=coder[i]
        res+=i
        
    return res
    
def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ###This is a wrapper function - a function that is build upon functions
    
    #build coder
    coder=buildCoder(shift)
    #apply the coder on the text
    coded_text = applyCoder(text, coder)
    return coded_text


def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the aencoded text. King of the hill

    text: string
    returns: 0 <= int < 26
    """
    #1. Set the maximum number of real words found to 0.
    real_words = 0
    #2. Set the best shift to 0.
    best_shift = 0
    #3. For each possible shift from 0 to 26:
    for value in range(0,26): 
        valid_words = 0
        decrypted_text_wo_punct = ''
        #4. Shift the entire text by this shift.
        decrypted_text = applyShift(text,value)
        decrypted_text = decrypted_text.lower()
        #5. Split the text up into a list of the individual words.
        for i in decrypted_text:
            if i in (string.ascii_lowercase + ' '):
                decrypted_text_wo_punct += i
                decrypted_text_list = decrypted_text_wo_punct.split(' ')
        
        #6. Count the number of valid words in this list.
        for i in decrypted_text_list:
            if i in wordList:
                valid_words+=1
        #7. If this number of valid words is more than the largest number of 
        #    real words found, then:
        if valid_words > real_words:
        #8. Record the number of valid words.
            real_words = valid_words 
        #9. Set the best shift to the current shift.
            best_shift = value


    #10. Increment the current possible shift by 1. Repeat the loop
    #  starting at line 3.
    #11. Return the best shift.
    return best_shift