def uppercase(input_str):
    for char in input_str:
        upper_code = ord(char) - 32 if 97 <= ord(char) <= 122 else ord(char)
        print(chr(upper_code), end='')
    print("")
