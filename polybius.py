import string
from ciphers import Cipher

class PolybiusCipher(Cipher):
  """ Encrypts or Decrypts user text using the Poylbius cipher method.

  Class is sub-class of Cipher main class.

  A 5x5 array is created and letters in user text are mapped
  to corresponsding x and y values of the array
  I and J letter have are given the same x,y value to fit in
  the 25 spaces of the array

  e.g. 'B' letter cipher is 12 

  """
  def __init__(self):
    """Creates instance of the Class KeywordCipher using addition modulo 26 

    Arguments required in addition to self:
    None

    List holding x,y values for 26 alphabet letters is created

    """
    self.alphabet = string.ascii_uppercase
    self.coordinates = []
    for x in range(6):
      for y in range(6):
        self.coordinates.append(str(x)+str(y))
        self.coordinates.insert(8, '24')
  
  def encrypt(self, text):
    """ Encrypts text from user input into cipher text

    Arguments required:
    text: user text to encrypt

    User text indexes are held in a list and then mapped back
    to a corresponding index in coordinates list

    Returns user ciphered text as xy coordinates for each letter

    """
    output = []
    text = text.upper()
    for char in text:
      try:
        text_index = self.alphabet.index(char)
        output.append(self.coordinates[text_index])
      except ValueError:
        output.append(char)

    return ''.join(output)

  def decrypt(self, text):
    """ Decrytps text from user input into cipher text
  
    Arguments required:
    text: user text to encrypt
  
    User text indexes are held in a list and then mapped back
    to a corresponding index in coordinates list
  
    Returns usertext as letters from ciphered xy coordinates for each letter
  
    """
  
    output = []
    text = (str(text)).replace(" ", "")
  
    for i in range(0, len(text), 2):
      try:
        combined_letter = text[i]+text[i+1]
        text_index = self.coordinates.index(combined_letter)
        output.append(self.alphabet[text_index])
      except ValueError:
        output.append(text[i])
  
    return ''.join(output)
