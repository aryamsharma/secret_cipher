import time
import random
import string


class CF:
    def __init__(self):
        self.chars = [i for i in string.printable[:-5]]
        del self.chars[-10]
        self.key = self.chars[:]
        self.seed = time.strftime("%Y%m%d")
        random.seed(self.seed)
        random.shuffle(self.key)

    def encrypt(self, text):
        self.encrypted = ""
        for k, v in enumerate(text):
            pos = self.chars.index(v)
            self.encrypted += self.key[pos]
        return self.encrypted

    def decrypt(self, text):
        self.decrypted = ""
        for k, v in enumerate(text):
            pos = self.key.index(v)
            self.decrypted += self.chars[pos]
        return self.decrypted

    def dignostic(self):
        text = "The 1 Quick Brown fox Jumped over The 2 lazy Dogs -_- !?// WOW"
        print(f"seed     : {self.seed}")
        print(f"chars    : {''.join(self.chars)}")
        print(f"key      : {''.join(self.key)}")
        print(f"org      : {text}")
        print(f"encrypted: {cipher.encrypt(text)}")
        print(f"decrypted: {cipher.decrypt(cipher.encrypted)}")


if __name__ == "__main__":
    to_do = input("(E)ncrypt / (D)ecrypt / (Di)gnostic\n").lower().strip()

    cipher = CF()

    if to_do == "di":
        cipher.dignostic()
        exit()

    text = input("Enter str: ").strip()

    if to_do == "e":
        print(f"encrypted: {cipher.encrypt(text)}")

    elif to_do == "d":
        print(f"decrypted: {cipher.decrypt(text)}")

    else:
        print("Wrong input please execute again")
