# raise NotimplementedError if a sub class method is missing

""" Cipher parent class that raises NotimplementedError if a subclass method is missing """

class Cipher:
    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()
