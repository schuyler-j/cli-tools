import re
import random
import time
import matplotlib.pyplot as plt
import os
import sys

#potentially auto run messagescraperloop.py




def parser():
    file = 'msgfull.txt'

    #if file doesn't exist
    try:
        msg = open(file, 'r').read()

    except Exception as e:
        print("NO FILE", e)
        sys.exit()

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

    msgtimes = []
    time_pattern = r'rm-received-ts'
    count = 0
    for chunk in chunks:
        x = re.findall(time_pattern, chunk)
        count += 1
        if x:
            times = chunks[count-1].split('=')[1]
            times_c = int(times)/1000
            msgtimes.append(times_c)


    #sort by most username occurences
    #print(sorted(userdict.items(), key=lambda x: x[1], reverse=True))

    #time conversion
    converted_times = []
    for t in msgtimes:
        converted_time = time.ctime(t)
        converted_times.append(converted_time)


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
            msgs.append(message[4: len(message)])


    return msgs, converted_times, msgtimes, userdict

def graph():
    #temp plot
    msgtimes = parser()[2]
    userdict = parser()[3]

    y = []
    x = msgtimes[:len(userdict)]
    for s in userdict:
        y.append(userdict[s])
    plt.plot(x, y)
    plt.show()

def printChats():
    msgs = parser()[0]
    converted_times = parser()[1]
    fmtdchats = []
    count = 0
    for m in msgs:
        t = ' '.join(m)[1:]
        t = t.split('","@')
        #TODO make the time optional 
        print(t[0], converted_times[count])
        fmtdchats.append(t[0])
        count += 1

def emoteCounter(f, d):
    msgs = parser()[0]
    ocount = 0
    tcount = 0
    pattern = input('Enter emote: ')
    counter = 0
    div = d
    length = len(msgs)
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

#test cases
'''
emoteCounter(r'GIGACHAD', 0, 10)
emoteCounter(r'GIGACHAD', 0, 10)
emoteCounter(r'LULW', 0, 10)
emoteCounter(r'Aware', 0, 10)
emoteCounter(r'Nerd', 0, 10)
'''      





args = sys.argv[1:]

if not args:
    print("No arguments given")
    sys.exit()

options = {'p': 'print scatter plot', '-c': 'print chat messages', '-e': 'print emote count', '-a': 'auto run scraper'}

commands = {
    '-a': lambda: os.system('python messagescraperloop.py'),
    '-h': lambda: print(f'Usage: python messageparser.py {options}'),
    '-c': lambda: printChats(),
    '-e': lambda: emoteCounter(0, 10),
    '-p': lambda: graph(), 
}

# Iterate over the arguments
for arg in args:
    # Check if the argument is a valid option
    if arg in commands:
        # Call the function associated with the option
        commands[arg]()