from logo import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print(logo)


def caesar(text, shift, direction):
    code = ""
    for i in text:
        if i in alphabet:
            pos = alphabet.index(i)
            if direction == 'encode':
                pos += shift
            elif direction == "decode":
                pos -= shift
            code += alphabet[pos % 26]
        else:
            code += i
    print(f"The {direction}d is {code}")


ch = 'yes'
while ch == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    ch = input("Type 'yes' if you want to go again, else type 'no'.\n")
print("Goodbye 👋")
