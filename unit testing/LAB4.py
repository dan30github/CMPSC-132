#Lab #4
#Due Date: 09/14/2018, 11:59PM
########################################
#                                      
# Name:
# Collaboration Statement:             
#
########################################

def encrypt(message, key):
    """
        Takes a string and an integer an returns the encrypted message using the Caesar cipher method 
        >>> encrypt("Hello world",12)
        'Tqxxa iadxp'
        >>> encrypt("We are Penn State!!!",6)
        'Ck gxk Vktt Yzgzk!!!'
        >>> encrypt("We are Penn State!!!",5)
        'Bj fwj Ujss Xyfyj!!!'
        >>> encrypt(5.6,3)
        'Invalid input'
        >>> encrypt('Hello',3.5)
        'Invalid input'
        >>> encrypt(5.6,3.15)
        'Invalid input'
    """
    # --- YOU CODE STARTS HERE
    if type(message) != str or type(key) != int:
        return 'Invalid input'
    alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    new_st = ''

    for x in message:
        if (alpha_lower.count(x) != 0) or (alpha_upper.count(x) != 0):
            if alpha_lower.count(x) != 0 and alpha_lower.index(x) + key < 26:
                new_st += alpha_lower[alpha_lower.index(x) + key]

            if alpha_upper.count(x) != 0 and alpha_upper.index(x) + key < 26:
                new_st += alpha_upper[alpha_upper.index(x) + key]

            if alpha_upper.count(x)!= 0 and alpha_upper.index(x) + key >= 26:
                new_st += alpha_upper[alpha_upper.index(x) + key - 26]

            if alpha_lower.count(x) != 0 and alpha_lower.index(x) + key >= 26:
                new_st += alpha_lower[alpha_lower.index(x) + key - 26]
        else:
            new_st += x

    return new_st

    # ---  CODE ENDS HERE

def decrypt(message, key):
    """
        Takes a string and an integer an returns the decrypted message using the Caesar cipher method 
        >>> decrypt("Tqxxa iadxp",12)
        'Hello world'
        >>> decrypt("Ck gxk Vktt Yzgzk!!!",6)
        'We are Penn State!!!'
        >>> decrypt("Bj fwj Ujss Xyfyj!!!",5)
        'We are Penn State!!!'
        >>> decrypt(5.6,3)
        'Invalid input'
        >>> decrypt('Hello',3.5)
        'Invalid input'
        >>> decrypt(5.6,3.15)
        'Invalid input'
    """

    # --- YOU CODE STARTS HERE
    if type(message) != str or type(key) != int:
        return 'Invalid input'
    new_st = ''
    alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for x in message:
        if (alpha_lower.count(x) != 0) or (alpha_upper.count(x) != 0):
            if alpha_lower.count(x) != 0:
                new_st += alpha_lower[alpha_lower.index(x) - key]
            if alpha_upper.count(x) != 0:
                new_st += alpha_upper[alpha_upper.index(x) - key]
        else:
            new_st += x

    return new_st


    # ---  CODE ENDS HERE




