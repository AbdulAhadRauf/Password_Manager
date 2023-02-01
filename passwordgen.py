letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

import random
class PasswordGen:
    def __init__(self):
        self.generator

        
    def generator(self):
        password = [random.choice(letters) for n in range(random.randint(8,10))]
        password += [random.choice(symbols) for n in range(random.randint(2,4))]
        password += [random.choice(numbers) for n in range(random.randint(2,4))]
        random.shuffle(password)
        password = "".join(password)
        return password
