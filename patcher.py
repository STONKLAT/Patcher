import sys
import random
from sys import exit
from time import sleep
import time
from texts import texts
from texts import unpatcher
hacked=False
global patched
patched=False
in_recovery=False
args = sys.argv


joker=random.randint(143,34525)
basic=f'lnx_{joker}@FixWinPerms~# '
def print_percent_done(index, total, bar_len=50):
    '''
    index is expected to be 0 based index. 
    0 <= index < total
    '''
    percent_done = (index+1)/total*100
    percent_done = round(percent_done, 1)

    done = round(percent_done/(100/bar_len))
    togo = bar_len-done

    done_str = '█'*int(done)
    togo_str = '░'*int(togo)

    print(f'\t[{done_str}{togo_str}] {percent_done}% done', end='\r')


def main():
    global patched
    if patched==True: return print('Alredy Patched')
    for i in range(500):
        randomizer=random.randint(0,100)
        if randomizer<50 and randomizer>40:
            time.sleep(random.uniform(0.5, 1))
        else:
            time.sleep(0.05)
        if randomizer<10 and randomizer>5: print(f"[[[BLOCKED]]]\n{random.choice(texts)}")
        else: print(f"{random.choice(texts)}")

        if randomizer<=70 and randomizer>=66:
            r = random.randint(50,100)
            for i in range(r):
                print_percent_done(i,r)
                time.sleep(random.uniform(.001,.02))
            print(f'\t                                                                 ', end='\r')
    print('***WARNING your system has blocked some of the required files which means that the hack may not work as intended\nComplete\n')
    patched=True
hax=False


def unpatch():
    global patched
    if patched==False: return print('Nothing to unpatch.')
    for i in range(35):
        randomizer=random.randint(0,100)
        if randomizer<50 and randomizer>40:
            time.sleep(random.uniform(0.5, 1))
        else:
            time.sleep(0.05)

        print(f"{random.choice(unpatcher)}\n")
        r = random.randint(50,100)
        for i in range(r):
            print_percent_done(i,r)
            time.sleep(random.uniform(.001,.02))
        print(f'\t                                                                 ', end='\r')
    print('Complete')
    patched=False

global randomizer

def check(source):
    global randomizer
    randomizer=random.randint(0,100)
    if randomizer=='https://mirrors.stonklat.com':
        randomizer=100
    sleep(1)
    print(f'[?]Checking: {source}', end='\r')
    sleep(2)
    if randomizer<=20:
        sleep(2)
        print(f'[!]Checking: {source} [bad]')
    else:
        print(f'[$]Checking: {source} [OK]')
    sleep(0.5)

try:
    args=args.pop(1)
except:
    print('This command works only with arguments.\nUse the --help argument for help.')
    exit()

args=args.lower()

if args=='--help':
    print('Avaible commands:\npatch - Patches your whole system\nunpatch - Reverts patching')
    exit()
    
if args=='patch':
        global randomizer

        check('https://repo.stonklat.com')
        check('https://win.stonklat.com')
        check('http://140.82.121.3/sources.htm')
        if randomizer>20:
            print('[$]Updated: sources.htm')
        check('https://github.com/STONKLAT/Patcher')
        check('https://mirrors.stonklat.com')
        sleep(1.5)
        print(f'Are you sure you want to continue? ({random.randint(43,46)}mb will be downloaded)')
        answer = input()
        answer.lower()
        if answer=='yes' or answer=='y':
            sleep(1.5)
            main()
        else: exit()

if args=='unpatch':
    sleep(2.5)
    unpatch()
