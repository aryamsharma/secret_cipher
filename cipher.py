import time
import random

class CF:
    def __init__(self):
        self.chars = [i for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()\\*+,-./:;<=>?@[]^_`{|}~ "]
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


if __name__ == "__main__":
    text = input("Enter str: ").strip()
    # text = "test"
    cipher = CF()
    print(cipher.encrypt(text))
    
    print(f"seed     : {cipher.seed}")
    print(f"chars    : {''.join(cipher.chars)}")
    print(f"key      : {''.join(cipher.key)}")
    print(f"org      : {text}")
    print(f"encrypted: {cipher.encrypt(text)}")
    print(f"decrypted: {cipher.decrypt(cipher.encrypted)}")