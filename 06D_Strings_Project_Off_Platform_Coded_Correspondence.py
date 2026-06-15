'''
Learn Python 3
Off-Platform Project: Coded Correspondence
Overview
This project is slightly different than others you have encountered thus far on Codecademy. Instead of a step-by-step tutorial, this project contains a series of open-ended requirements which describe the project you’ll be building.

There are many possible ways to correctly fulfill all of these requirements, and you should expect to use the internet, Codecademy, and other resources when you encounter a problem that you cannot easily solve.

Project Goals
You and your pen pal, Vishal, have been exchanging letters for some time now. Recently, he has become interested in cryptography and the two of you have started sending encoded messages within your letters.

In this project, you will use your Python skills to decipher the messages you receive and to encode your own responses! Put your programming skills to the test with these fun cryptography puzzles.
'''
'''
Setup
We encourage you to complete this project on your own computer using Jupyter notebooks. To do so, continue following these instructions to get going.
'''
'''
task1
You just got a message from your pen pal Vishal!
Use your Python skills to decode Vishal’s message and print the result.
'''

'''
alphabet = [
  'a',
  'b',
  'c',
  'd',
  'e',
  'f',
  'g',
  'h',
  'i',
  'j',
  'k',
  'l',
  'm',
  'n',
  'o',
  'p',
  'q',
  'r',
  's',
  't',
  'u',
  'v',
  'w',
  'x',
  'y',
  'z'
]
'''
'''
message = \
'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
print('message: ')
print(message)

alphabet_interim = []

for i in range(0,len(alphabet)):
  #print(alphabet[i])
  alphabet_interim.append(alphabet[i-10])
print(alphabet_interim)
'''

'''
inspired by: https://habr.com/ru/articles/552212/
'''
'''
alphabet =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
shift = 0
shift = int(input("Encoding step: "))
message = input("Message for encoding: ").upper()
summary = ''

for i in message:
    place = alphabet.find(i)
    new_place = shift + place
    if i in alphabet:
        summary += alphabet[new_place]
    else:
        summary += i
print(summary)

'''
'''
alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
shift = 0
shift = int(input("Encoding step: "))
message = input("Message for encoding: ").upper()
summary = ''
lang = input("Choose your language: ").upper()

if lang == 'RU':
    for i in message:
       place = alphabet_RU.find(i)
       new_place = place + shift
       if i in alphabet_RU:
           summary += alphabet_RU[new_place]
       else:
           summary += i
else:
    for i in message:
        place = alphabet_EU.find(i)
        new_place = place + shift
        if i in alphabet_EU:
            summary += alphabet_EU[new_place]
        else:
            summary += i

print(summary)

alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
shift = 0
shift = int(input("Encoding step: "))
message_decode = input("Message for decoding: ").upper()
summary = ''
lang = input("Choose your language: ").upper()

if lang == 'RU':
    for i in message_decode:
        place = alphabet_RU.find(i)
        new_place = place - shift
        if i in alphabet_RU:
            summary += alphabet_RU[new_place]
        else:
            summary += i
else:
    for i in message_decode:
        place = alphabet_EU.find(i)
        new_place = place - shift
        if i in alphabet_EU:
            summary += alphabet_EU[new_place]
        else:
            summary += i
print((summary).lower())
'''
alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def f_caesar_encoding(shift,message):
    summary = ''
    if lang == 'RU':
        for i in message:
           place = alphabet_RU.find(i)
           new_place = place + shift
           if i in alphabet_RU:
               summary += alphabet_RU[new_place]
           else:
               summary += i
    else:
        for i in message:
            place = alphabet_EU.find(i)
            new_place = place + shift
            if i in alphabet_EU:
                summary += alphabet_EU[new_place]
            else:
                summary += i
    return summary

def f_caesar_decoding(shift,message_decode):
    summary = ''
    if lang == 'RU':
        for i in message_decode:
            place = alphabet_RU.find(i)
            new_place = place - shift
            if i in alphabet_RU:
                summary += alphabet_RU[new_place]
            else:
                summary += i
    else:
        for i in message_decode:
            place = alphabet_EU.find(i)
            new_place = place - shift
            if i in alphabet_EU:
                summary += alphabet_EU[new_place]
            else:
                summary += i
    return((summary).lower())

shift = int(input("Encoding step: "))
message = input("Message for encoding: ").upper()
lang = input("Choose your language: ").upper()
print(f_caesar_encoding(shift,message))
shift = int(input("Encoding step: "))
message_decode = input("Message for decoding: ").upper()
lang = input("Choose your language: ").upper()
print(f_caesar_decoding(shift,message_decode))

print("Now let's run the part when the shift is unknown")
'''
message for the part when the shift is unknown:
vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.
'''

#shift = int(input("Encoding step: "))
message_decode = input("Message for decoding: ").upper()
lang = input("Choose your language: ").upper()

if lang == 'RU':
    for counter_ru in range(0,len(alphabet_RU)):
        print(f_caesar_decoding(counter_ru,message_decode))
else:
    for counter_eu in range(0,len(alphabet_EU)):
        print(f_caesar_decoding(counter_eu,message_decode))