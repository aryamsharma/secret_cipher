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
        cipher.log(text, "di")

    def log(self, text, mode):
        to_write = [
            "#################################################\n",
            f"Mode     : {mode}\n",
            f"seed     : {self.seed}\n",
            f"chars    : {''.join(self.chars)}\n",
            f"key      : {''.join(self.key)}\n",
            f"org      : {text}\n",
            f"encrypted: {cipher.encrypt(text)}\n",
        ]
        if mode == "e":
            to_write.append(f"decrypted: {cipher.decrypt(cipher.encrypted)}\n")

        elif mode == "d":
            to_write.append(f"decrypted: {cipher.decrypt(text)}\n")

        elif mode == "di":
            to_write.append(f"decrypted: {cipher.decrypt(cipher.encrypted)}\n")
            to_write.append(f"decrypted: {cipher.decrypt(text)}\n")

        with open("Log.txt", "a") as f:
            f.writelines(to_write)


if __name__ == "__main__":
    to_do = input("(E)ncrypt / (D)ecrypt / (Di)gnostic\n").lower().strip()

    cipher = CF()

    if to_do == "e":
        text = input("Enter str: ").strip()
        print(f"encrypted: {cipher.encrypt(text)}")

    elif to_do == "d":
        text = input("Enter str: ").strip()
        print(f"decrypted: {cipher.decrypt(text)}")

    elif to_do == "di":
        cipher.dignostic()
        exit()

    else:
        print("Wrong input please execute again")
        exit()

    cipher.log(text, to_do)
