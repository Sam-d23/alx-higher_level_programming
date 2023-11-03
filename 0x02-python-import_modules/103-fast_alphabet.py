def print_alphabet(char):
    if ord(char) <= ord('Z'):
        __import__('sys').stdout.write(char)
        print_alphabet(chr(ord(char) + 1))

print_alphabet('A')
