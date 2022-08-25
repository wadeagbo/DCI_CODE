vowels = "aeiou"
Vowels= vowels.upper()
consonant = "bcdfghjklmnpqrstvwxyz"
Consonant = consonant.upper()
    
def func_Contcatene (word):
    length_w= len(word)
    if word[-1] in consonant or word[-1] in Consonant:
         print(f"{word}inator {length_w}000") 
    elif word[-1] in vowels or word[-1] in Vowels:
        print(f"{word}-inator {length_w}000")
       

func_Contcatene("Shrink")
func_Contcatene("Doom")
func_Contcatene("EvilClone")



### endswith method 
print()



vowels = "aeiou"
Vowels= vowels.upper()
consonant = "bcdfghjklmnpqrstvwxyz"
Consonant = consonant.upper()

def func_Contcatene2 (word):
    length_w= len(word)
    if word[-1] in consonant or word[-1] in Consonant:
        A_con = f"{word}inator {length_w}000"
        return A_con
    elif word[-1] in vowels or word[-1] in Vowels:
        A_vow = f"{word}-inator {length_w}000"
        return A_vow




print(func_Contcatene2("Shrink"))
print(func_Contcatene2("Doom"))
print(func_Contcatene2("EvilClone"))

