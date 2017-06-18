import string

class UserInput():

    def affine_input():
        accepted_alpha = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
        while True:
            try:
                alpha = int(input("""Please enter alpha key, should be an odd integer from 3-25, except 13 > """))
                if alpha in accepted_alpha:
                    break
                else:
                    print ("Invalid alpha key")
            except ValueError:
                print ("Invalid alpha value")
        
        beta = int(input("""Please enter beta key, any integer 1-100 > """))
        
        return alpha, beta
    
    def keyword_input():
        while True:
            try:
                keyword = (input("Please enter a KEYWORD with unqiue letters > ")).upper()
                if len(keyword) == len(set(keyword)) and keyword.isalpha():
                    break
                else:
                    print ("Keyword has duplicate letters or contains characters other than letters")
            except ValueError: 
                print ("Invalid keyword")    
        
        return keyword
    
    def padinput():
        accepted_keys = string.ascii_uppercase
        while True:
            try:
                padkey = (input("Please enter your One-Time Pad KEY > ")).upper()
                key_comp = padkey.replace(" ","")
                if (set(key_comp)).issubset(set(accepted_keys)):
                  break
                else:
                  print ("Pad key has special characters or integers that are not acceptable values")

            except ValueError:
                print ("Invalid Pad key")
        
        return padkey		
