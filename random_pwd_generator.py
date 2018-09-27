# Write a password generator in Python. Be creative with how you generate passwords
# trong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time
# the user asks for a new password. Include your run-time code in a main method.
# Ask the user how strong they want their password to be. 
# For weak passwords, pick a word or two from a list.
import string
from string import punctuation
import random

def pwd_gen(userInput):
  list2 = list(string.ascii_lowercase)
  list1 = list(string.ascii_uppercase)
  list3 = list(range(0,10))
  list4 = list(set(punctuation))
  list5 = [random.choice(list1), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list3), random.choice(list4)]
  if userInput == 'strong':
    pwd = random.sample(list5, 8)
    return ''.join(map(str,pwd))

userInput = raw_input("How strong password you want: ")
result = pwd_gen(userInput)
print ("Generated random pwd is: {}".format(result))  
