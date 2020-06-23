import time
import math
import random

def random_seed_value():
    return time.strftime("%Y%m%d")

def key_randomize(chars):
    key = chars[:]
    random.shuffle(key)
    return key

def encrypting(text, key, chars):
    new_text = ""
    for k, v in enumerate(text):
        pos = chars.index(v)
        new_text += key[pos]
    return new_text


def decrypting(text, key, chars):
    new_text = ""
    for k, v in enumerate(text):
        pos = key.index(v)
        new_text += chars[pos]
    return new_text


if __name__ == "__main__":
    seed = random_seed_value()
    random.seed(seed)
    chars = [i for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()\\*+,-./:;<=>?@[]^_`{|}~ "]
    key = key_randomize(chars)
    text = input("Enter str: ").strip()
    encrypted_text = encrypting(text, key, chars)
    decrypted_text = decrypting(encrypted_text, key, chars)
    
    print(f"seed     : {seed}")
    print(f"chars    : {''.join(chars)}")
    print(f"key      : {''.join(key)}")
    print(f"org      : {text}")
    print(f"encrypted: {encrypted_text}")
    print(f"decrypted: {decrypted_text}")