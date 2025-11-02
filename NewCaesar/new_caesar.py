import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

def decode(encflag):
    dec = ""
    for i in range(0, len(encflag), 2):
        first = ALPHABET.index(encflag[i])
        second = ALPHABET.index(encflag[i + 1])
        binary = f"{first:04b}{second:04b}"
        dec += chr(int(binary, 2))
    return dec

encflag = "lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"
dec = ""

for key in ALPHABET:
    plain = ""
    for c in encflag:
        plain += shift(c, key)
    b16 = decode(plain)
    print (key, ": ", b16)
