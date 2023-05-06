  def cipher(self): 
        result = ("")
        for char in self.string:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                (ord(char) - start * len(self.string)) % 26
                result += char
        return result