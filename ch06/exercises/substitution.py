import json 

def main(): 
    text = open('news.txt', 'r').read()
    sub_fptr = open('subs.json', 'r') #don't need r, reading is default 
    subs = json.load(sub_fptr)
    print(subs, type(subs))

    #use one list to modify another list 
    #which list should you loop through?
    for k, v in subs.items():
        text = text.replace(k, v)
    fptr = open("betternews.txt", "w")
    fptr.write(text)
    fptr.close()

main()
        

