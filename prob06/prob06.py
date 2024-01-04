"""
Eve is at it again and may have discovered a new way to intercept and read encrypted WiFi network traffic at her
local coffee shop.
She has determined the following mapping by performing a few tests:

PLAINTEXT ABCDEFGHIJKLMNOPQRSTUVWXYZ
CIPHERTEXT FGHIJKLMNOPQRSTUVWXYZABCDE

EXAMPLES:
    PLAINTEXT HELLO WORLD
    CIPHERTEXT MJQQT BTWQI

    PLAINTEXT CODE WARS RULES
    CIPHERTEXT HTIJ BFWX WZQJX

    PLAINTEXT SUPERCALIFRAGILISTICEXPIALIDOCIOUS
    CIPHERTEXT XZUJWHFQNKWFLNQNXYNHJCUNFQNITHNTZX
"""

file = open("input.txt", 'r')  # open file in read mode
cipertext = file.readlines()[1]  # get the ciphertext
plaintext = ""

for char in cipertext:
    if char == ' ':
        plaintext += char
        continue
    ascii_val = ord(char)
    if ascii_val - 5 < 65:
        ascii_val = ascii_val + 26
    plaintext += chr(ascii_val - 5)

print(plaintext)

file.close()
