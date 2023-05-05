class StringUtility: 
    
    def __init__(self, string):
        #instance variable
        self.string = string 

    def __str__(self): 
        #internal string 
        return self.string 
    
    def vowels(self):
        count = 0 
        for letter in self.string: 
            if letter in 'aeiou':
                count += 1
            else: 
                pass
        if count >= 5: 
            return("many") 
        else: 
            return(str(count))
        
    def bothEnds(self): 
        if len(self.string) <= 2: 
            return ("")
        else: 
            return (self.string[0:2] + self.string[-2:]) #blank to index from second to end to the end 
            
    def fixStart(self): 
        if len(self.string) >= 1: 
            replaced_str = self.string[0] + str(self.string[1:]).replace(self.string[0], "*")
            return replaced_str
        else:
            return self.string
    
    def asciiSum(self):
        ascii_sum = 0 
        for char in self.string:
            ascii_sum += ord(char)
        return ascii_sum
        
    def cipher(self): 
        result = ("")
        for char in self.string:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                (ord(char) - start * len(self.string)) % 26
                result += char
        return result