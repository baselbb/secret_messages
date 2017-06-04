from ciphers import Cipher
import random
import string

class PadCipher(Cipher):
  """ One-Time Pad cipher class that encrypts or decrypts text into groups of five

  class is a subclass of Cipher parent class

  """
  def __init__(self, keyword):
    """ Creates instance of the Class PadCipher using addition modulo 26

    Forumla:
    cipher text index = (user_text_index + keyword_index) % 26 

    Arguments required in addition to self:
    keyword: is keyword text from the user
    
    Creates a cipher list of index values based on keys
    User text indexes are mapped to this cipher list of indexes to create
    the cipher text for the user
    Text is grouped into multiples of 5 and additional random letters are added if required

    """

    # get user keyword and remove any spaces.  
    self.keyword = (keyword.replace(" ","")).upper()      
    self.special = string.ascii_uppercase

    # create a list of keyord letters indexes
    self.key_index = []
    for item in self.keyword:
      item_index = self.special.index(item)
      self.key_index.append(item_index)
  
  def encrypt(self,text):
    """ Encrypts text from user input into cipher text

    Arguments required:
    text: user text to encrypt

    User text indexes are held in a list and then mapped back
    to a corresponding index in cipher list, which holds a value 
    to index the character back to string.ascii

    """

    output = []
    text = text.upper().replace(" ","")

    # get indexes for user text and place them in a list
    char_index = []
    for char in text:
      text_index = self.special.index(char)
      char_index.append(text_index)

    # add index from user text and keyword using mod 26 to indexes for encrypted letters 
    # & place letters in a list
    encrypt_letters = []
    index_total = [(x + y) % 26 for x, y in zip(char_index, self.key_index)]
    for indexes in index_total:
      encrypt_letters.append(self.special[indexes])   

    # add additional random letter padding to encrypted letters to reach a multiple of 5
    if len(encrypt_letters) % 5 != 0:
      add_chars = 5 - (len(encrypt_letters) % 5)

      for letters in range(add_chars):
        encrypt_letters.append(random.choice(self.special))

    # group items from encrypted letters into groups of five letters
    for i in range(0, len(encrypt_letters), 5):
      output.append(''.join(encrypt_letters[i:i+5]))

    # return encrypted output as text and special characters into groups of five letters 
    # with additional random padding included
    return ' '.join(output)      

  def decrypt(self,text):
    """ Decrypts text from user input into cipher text

    Arguments required:
    text: user text to encrypt

    User text indexes are held in a list and then mapped back
    to a corresponding index in cipher list, which holds a value 
    to index the character back to string.ascii

    """
    output = []
    text = text.upper().replace(" ","")

    # get indexes for user text and place them in a list
    char_index = []
    for char in text:
      text_index = self.special.index(char)
      char_index.append(text_index)

    # subtraction of keyword index from user cipher text index using mod 26 
    index_subtract = [(x - y) for x, y in zip(char_index, self.key_index)]

    # if subtraction is a negative add 26 to it
    index_adjusted = []
    for value in index_subtract:
      if value >= 0:
        index_adjusted.append(value)
      else:
        index_adjusted.append(value + 26)

    # for the adjusted subtraction run mod 26 to get the final indexes for deciphered text
    decrypt_letters = []
    index_final = [x % 26 for x in index_adjusted]
    for indexes in index_final:
      decrypt_letters.append(self.special[indexes])   

    # group items from decrypted letters into groups of five letters
    for i in range(0, len(decrypt_letters), 5):
      output.append(''.join(decrypt_letters[i:i+5]))
  
    # return decrypted output
    return ' '.join(output)    
