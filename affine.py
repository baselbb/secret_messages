import string
from ciphers import Cipher


class AffineCipher(Cipher):
    """ Encrypts or decrypts user text using the Affine cipher method.

    Class is sub-class of Cipher main class.

    Using the arguments provided, change the integer value of the index for
    each chcaracter in the user text to a cipher value index which is then 
    mapped back to ASCII strings 

    """

    accepted_alpha = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
    
    def __init__(self, alpha, beta):
        """
        Creates instance of the Class AffineCipher using addition modulo 26 

        Forumla:
        cipher_index = (alpha * letter_index + beta) % 26 
        
        Arguments required in addition to self:
        alpha: is the 'a' value required for the affine formula
        beta: 'b' shift for the formula

        Creates a cipher list of index values based on alpha and beta keys
        User text indexes are mapped to this cipher list of indexes to create
        the cipher text for the user

        """

        self.alpha = alpha
        self.beta = beta

        self.alphabet = string.ascii_uppercase
        self.cipher_list = []
        for i in range(26):
            self.cipher_list.append((self.alpha * i + self.beta) % 26)

    def encrypt(self, text):
        """ Encrypts text from user input into cipher text

        Arguments required:
        text: user text to encrypt

        User text indexes are held in a list and then mapped back
        to a corresponding index in cipher list, which holds a value 
        to index the character back to string.ascii

        Example: 
        'A' character in user text has an index = 0
        Cipher list has a value index of 4 for index 0
        'A' new cipher index value is 4
        'A' becomes 'E'
        
        """

        output = []
        text = text.upper()
        for char in text:
            try:
                text_index = self.alphabet.index(char)
                output.append(self.alphabet[self.cipher_list[text_index]])
            except ValueError:
                output.append(char)

        return ''.join(output)

    def decrypt(self, text):
        """ Decrytps text from user input into cipher text

        Arguments required:
        text: user text to encrypt

        User cipher text indexes are held in a list and then mapped back
        to a corresponding index in cipher list, which holds a value 
        to index the character back to string.ascii

        Example: 
        'E' character in cipher text has string.ascii index = 4
        Cipher list has a value index of 0 for index 4
        'E' new actual index value is 0
        'E' becomes 'A'

        """

        output = []
        text = text.upper()
        for char in text:
            try:
                text_index = self.alphabet.index(char)
                output.append(self.alphabet[self.cipher_list.index(text_index)])
            except ValueError:
                output.append(char)

        return ''.join(output)
