import time
import math
import random

def random_seed_value():
    return time.strftime("%Y%m%d")

def encrypting(text, seed):
    new_text = ""
    for k, v in enumerate(text):
        html_code = ord(v)
        new_text += chr(int(math.sqrt(html_code + k)))
    
    return new_text


# def decrypting(text):
#     sectioned_text = section(text)

if __name__ == "__main__":
    random.seed(random_seed_value())
    # sentence = input("Enter str: ").strip()
    sentence = "test"
    print(encrypting(sentence))