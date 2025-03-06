class CaesarCipher:
    def __init__(self,symbols_to_move):
        self.symbols_to_move = symbols_to_move

    def encrypted(self, string):
        ords = [ord(char) + self.symbols_to_move for char in string]

        return ''.join(chr(ord_num) for ord_num in ords)

    def unencrypted(self, string):
        ords = [ord(char) - self.symbols_to_move for char in string]

        return ''.join(chr(ord_num) for ord_num in ords)


move_symbols = 3
sentence = input()


caesar_cipher = CaesarCipher(move_symbols)
print(caesar_cipher.encrypted(sentence))
