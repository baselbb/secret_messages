from ciphers import Cipher
import string

class KeywordCipher(Cipher):
  """ Encrypts or Decrypts user text using the Keyword cipher method.

  Class is sub-class of Cipher main class.

  Using the arguments provided, string.ascii alphabet is shifted by the keyword provided
  New alphabet for ciphering begins with the keyword letters provided bu the user
  Remaining alphabet letters are placed in order after keyword letters
  Each letter in the user text is mapped using its index to the new alphabet 

  """
  
  def __init__(self, keyword):
    """Creates instance of the Class KeywordCipher using addition modulo 26 

    Arguments required in addition to self:
    keyword: string keyword that contains unique non-duplicate letters

    Creates a new cipher alphabet starting with keyword letters
    """
    self.keyword = keyword
    self.alphabet = string.ascii_uppercase
    self.new_alphabet = ''.join([x for x in self.alphabet if x not in self.keyword])
    self.combined = self.keyword + self.new_alphabet 
  
  def encrypt(self, text):
    """ Encrypts text from user input into cipher text

    Arguments required:
    text: user text to encrypt

    User text indexes are held in a list and then mapped back
    to a corresponding index in cipher list, which holds a value 
    to index the character back to string.ascii

    """
    output = []
    text = text.upper()
    for char in text:
      try:
        text_index = self.alphabet.index(char)
        output.append(self.combined[text_index])
      except ValueError:
        output.append(char)

    return ''.join(output)

  def decrypt(self, text):
    """ Decrypts text from user input into text

    Arguments required:
    text: user text to encrypt

    User text indexes are held in a list and then mapped back
    to a corresponding index in cipher list, which holds a value 
    to index the character back to string.ascii

    """

    output = []
    text = text.upper()
    for char in text:
      try:
        text_index = self.combined.index(char)
        output.append(self.alphabet[text_index])
      except ValueError:
        output.append(char)

    return ''.join(output)
