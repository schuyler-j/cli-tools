import re
import random
import time

msg = open('msgfull.txt', 'r').read()

chunks = msg.split(';')

pattern = r'^display-name='
count = 0

usernames = []

for chunk in chunks:
    x = re.findall(pattern, chunk)
    count += 1
    if x:
        username = chunks[count-1].split('=')[1]
        usernames.append(username)



ncount = 0

unique = []

for name in usernames:
    tempname = name
    for n in usernames:
        if n == tempname:
            unique.append(n)
            ncount += 1
            break
    ncount = 0


userdict = {}
for name in usernames:
    tempname = name

    for n in usernames:
        if n == tempname:
            ncount += 1
            userdict.update({tempname: ncount})
    ncount = 0

#sort by most occurences
#print(sorted(userdict.items(), key=lambda x: x[1], reverse=True))

pattern = r'^user-type='

place = 0
msgs = []
for chunk in chunks:
    x = re.findall(pattern, chunk)
    place += 1
    if x:
       """  message = chunks[count-1].split('=')[1] """
       message = chunks[place-1].split(' ')
       s = message[4: len(message)-1]
       if s == []:
        pass
       else:
        msgs.append(message[4: len(message)-1])

def emoteCounter(p, f, d):
    ocount = 0
    tcount = 0
    pattern = p
    counter = 0
    div = d
    length = len(msgs)
    f = 0


    #print(max((msgs), key = msgs.count))

    for m in msgs:
        if f:
            print(' '.join(m)[1:])
        counter += 1
        for word in m:
            x = re.findall(pattern, word)
            if x:
                ocount += 1
                tcount += 1

            if counter % div == 0:
                ocount = 0
        prb = (tcount / len(msgs)) * 100
    print(f'{pattern} was said {tcount} times in the last {length} messages, which is {prb}% of the messages')

emoteCounter(r'GIGACHAD', 0, 10)
emoteCounter(r'LULW', 0, 10)
emoteCounter(r'AWARE', 0, 10)
emoteCounter(r'Nerd', 0, 10)
        

