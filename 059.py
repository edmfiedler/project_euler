"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII
 (American Standard Code for Information Interchange).
  For example, uppercase A = 65, asterisk (*) = 42,
   and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
 then XOR each byte with a given value, taken from a secret key.
  The advantage with the XOR function is that using the same encryption key on the cipher text,
   restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message,
 and the key is made up of random bytes. The user would keep the encrypted message
  and the encryption key in different locations, and without both "halves",
   it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
 If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
  The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters.
 Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes,
  and the knowledge that the plain text must contain common English words,
   decrypt the message and find the sum of the ASCII values in the original text.
"""

with open('txt_files/p059_cipher.txt') as f:
    lines = f.readlines()

letters = lines[0].split(",")

for k, l in enumerate(letters):
    letters[k] = format(int(l),'08b')

# The 3 letter password is repeated over the course of the letters
key_1_letters = letters[0::3]
key_2_letters = letters[1::3]
key_3_letters = letters[2::3]

# XOR converter
def xor(a,b):
    l = ''
    for k, x in enumerate(a):
        if x != b[k]:
            l += '1'
        else:
            l += '0'
    return chr(int(l,2))

# 3 Letter password combination
for p1 in range(97,123):
    for p2 in range(97, 123):
        for p3 in range(97, 123):
            decryp_1 = []
            p1_b = format(int(p1),'08b')
            for l in key_1_letters:
                decryp_1.append(xor(l,p1_b))

            decryp_2 = []
            p2_b = format(int(p2),'08b')
            for l in key_2_letters:
                decryp_2.append(xor(l,p2_b))

            decryp_3 = []
            p3_b = format(int(p3),'08b')
            for l in key_3_letters:
                decryp_3.append(xor(l,p3_b))

            letters[0::3] = decryp_1
            letters[1::3] = decryp_2
            letters[2::3] = decryp_3

            text = ''.join(letters)
            # Identify a common word in english
            if ' the ' in text:
                print(text)
                sum_lets = sum([ord(x) for x in letters])
                print(sum_lets)
                quit()