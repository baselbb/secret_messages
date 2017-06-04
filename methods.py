""" Import required built in python modules, 
cipher subclasses for different ciphering methods and 
subclass for asking and checking user input """

import os
from affine import AffineCipher
from keywords import KeywordCipher
from polybius import PolybiusCipher
from onetimepad import PadCipher
from required import UserInput

# clear screen function when user quits or wants to rerun encryption program
def clear_screen():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

# create a menu for Cipher method and return user choice
def menu():
  """ User menu function for different cipher methods. Main function which calls different and output cipher 			methods.

  This is the main function which asks a user for 
  1. Encrypt or decrypt a message
  2. Text to encrypt or decrypt
  3. If a additional cipher input is needed, return values from required.py
  4. Pass user text, encryption method and required parameters to selected encryption functions
  5. Return encrypted or decrypted text to the user

  'paramters' calls and holds additional user input instance from required.py for required cipher parameters
  'formula' creates cipher class instance using required arguments held in paramters
  'formula.encrypt/decrypt' calls encrypt or decrypt method from the class instance set by the user

  Encryption Process:
  User Text > One Time Pad > Chosen Cipher > Ciphered Text Output

  Decrypt Process:
  Cipher Text > Cipher Method > One Time Pad > Text Output

  """

  encrypt_choice = input('Welcome. Please type E to Encrypt or D to Decrypt a message >').upper()

  options = {1: 'Affine', 2: 'Keyword', 3: 'Polybius'}

  print("""From the menu below choose the NUMBER for the Cipher method.""")

  for key, items in options.items():
    print("{}: {}".format(key, items))

  # check is the user chose a method between 1-3.
  chosen = int(input("Please input method NUMBER here > "))
  if not 1 <= chosen <= 3:
    print("Your selection is not valid. Please choose a method between 1-3")
    input("Press enter to continue...")
    clear_screen()
    menu()

  user_text = input ("Please enter TEXT to encrypt or decrypt > ")

  # run main program depedning on users choices for cipher method
  if chosen == 1:
    parameters = UserInput.affine_input()
    formula = AffineCipher(parameters[0], parameters[1])
    if encrypt_choice == 'E':
      padded_text = onetimepad(user_text, encrypt_choice)
      print("Your encryption is {}".format(formula.encrypt(padded_text)))
    else:
      cipher_text = formula.decrypt(user_text)
      padded_text = onetimepad(cipher_text, encrypt_choice)
      print("Your decrypted text is {}".format(padded_text))

  elif chosen == 2:
    parameters = UserInput.keyword_input()
    formula = KeywordCipher(parameters)
    if encrypt_choice == 'E':
      padded_text = onetimepad(user_text, encrypt_choice)
      print("Your encryption is {}".format(formula.encrypt(padded_text)))
    else:
      cipher_text = formula.decrypt(user_text)
      padded_text = onetimepad(cipher_text, encrypt_choice)
      print("Your decrypted text is {}".format(formula.decrypt(padded_text)))

  elif chosen == 3:
    formula = PolybiusCipher()
    if encrypt_choice == 'E':
      padded_text = onetimepad(user_text, encrypt_choice)      
      print("Your encryption is {}".format(formula.encrypt(padded_text)))
    else:
      cipher_text = formula.decrypt(user_text)
      padded_text = onetimepad(cipher_text, encrypt_choice)
      print("Your decrypted text is {}".format(formula.decrypt(padded_text)))

def onetimepad(text, choice):
  """ Checks if user text is less than user provided key.

  Arguments required:
  text: user text input to encrypt or decrypt.
  choice: user selected choice to encrypt or decypt a message

  Returns ciphered user text to main program to perform additional method encrypting or decrytping

  """
  while True:
    try:
      parameters = UserInput.padinput()
      if len(parameters) >= len(text):
        if choice == 'E':
          formula = PadCipher(parameters)
          output = formula.encrypt(text)
          break
        else:
          formula = PadCipher(parameters)
          output = formula.decrypt(text)
          break
      else:
        print ("Keyword length is less than text to encrypt or decrypt.")
  
    except ValueError:
      print ("Invalid keyword entry")

  return output

if __name__ == "__main__":
  clear_screen()
  menu()