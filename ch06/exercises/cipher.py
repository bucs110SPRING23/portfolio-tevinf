#import json 
shift = 11
text = "the quick brown fox jumped over the lazy dog"
#results = ""
#file_pointer= open("encript1.txt", "x")
def caeser_cipher(text, shift):

    """

    args:
        text:str = the message to encrypt or decrypt
        shift:int = the number of positions to shift each letter
    return:
        :str = the encrypted or decrypted message
    """
    result = ""
    for char in text:
        if char.isalpha():
        # Determine the case of the character
            start = ord('A') if char.isupper() else ord('a')
        # Calculate the new position of the character after the shift
            new_pos = (ord(char) - start * shift) % 26
            # Convert the new position back to a character
            char = chr(start + new_pos)
            result += char
            #results.append(result)
            #print(results)
    return result

def main():
   file_pointer = open("encripted.txt", "a")
   result = caeser_cipher(text, shift)
   print(result)
   results = []
   results.append(result)
   for result in results:
       file_pointer.write(result)
       file_pointer.close()
       print('done')
       return None


main()
#caeser_cipher(text, shift)

