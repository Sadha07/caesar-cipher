
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def carsar(direction,text,shift):
    enr_word=""
    if(direction=="decode"):
        shift*=-1
    for i in text:
        if(i.isalpha()):
            loc = alphabet.index(i)
            enr_word+=(alphabet[loc+shift])
        else:
            enr_word+=i
    print(f"\n{direction}d text:{enr_word}")

print(art.logo)
while True:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = (shift % 26) if shift>26 else shift
    carsar(direction,text,shift)
    print("\nWant to run again?")
    ext = input("Enter 'yes' to redo or 'no' to exit\n").lower()
    if(ext=='no'):
        break


