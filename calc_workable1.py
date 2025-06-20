import winsound
from colorama import Back
from colorama import Style
import time
import keyboard
anim = False



def intro():
    for qw in range(0, 10):
        print('\rC', ' '*qw, 'A', ' '*qw,'L', ' '*qw,'C', ' '*qw,'U', ' '*qw,'L', ' '*qw, 'A', ' '*qw, 'T', ' '*qw, 'O', ' '*qw, 'R', end='')
        time.sleep(0.1)
        winsound.Beep(500, 50)
        winsound.Beep(800, 50)
    for ii in range(0, 5):
        i = 10-ii
        print('\rC', ' '*i, 'A', ' '*i,'L', ' '*i,'C', ' '*i,'U', ' '*i,'L', ' '*i, 'A', ' '*i, 'T', ' '*i, 'O', ' '*i, 'R', end='')
        time.sleep(0.1)
    print(Back.GREEN + "\r\033[30m{}".format('C        A        L        C        U        L        A        T        O        R'), end='')
    print(Style.RESET_ALL, end='')
    print('              ', end='')
    print(Style.RESET_ALL, end='')
    print(Back.RED + "\033[30m{}".format('1.0'), end='')
    print(Style.RESET_ALL)
    print('commands: #stop  #rerun  #anim')
intro()
while True:
    def outro():
        time.sleep(0.1)
        winsound.Beep(500, 50)
        print(Back.RED + "\r\033[30m{}".format(
            '.        .        .        .        .        .        .        .        .        .'), end='')
        time.sleep(0.1)
        winsound.Beep(500, 50)
        print(Back.RED + "\r\033[30m{}".format(
            '.       .       .       .       .       .       .       .       .       .'),
              end='')
        time.sleep(0.1)
        winsound.Beep(500, 50)
        print(Back.RED + "\r\033[30m{}".format('.      .      .      .      .      .      .      .      .      .'),
              end='')
        time.sleep(0.1)
        winsound.Beep(500, 50)
        print(Back.RED + "\r\033[30m{}".format('.     .     .     .     .     .     .     .     .     .'), end='')
        time.sleep(0.1)
        winsound.Beep(500, 50)
        print(Back.RED + "\r\033[30m{}".format('.   .   .   .   .   .   .   .   .  .'), end='')
        time.sleep(0.1)
        winsound.Beep(500, 50)
        print(Back.RED + "\r\033[30m{}".format('.  .  .  .  .  .  .  .  . .'), end='')
        time.sleep(0.1)
        winsound.Beep(500, 50)
        print(Back.RED + "\r\033[30m{}".format('. . . . . . . . . .'), end='')
        time.sleep(0.1)
        winsound.Beep(500, 50)
        print(Back.RED + "\r\033[30m{}".format('..........'), end='')
        time.sleep(0.1)
        winsound.Beep(500, 50)
        print(Back.RED + "\r\033[30m{}".format('......'), end='')
        time.sleep(0.1)
        winsound.Beep(500, 50)
        print(Back.RED + "\r\033[30m{}".format('....'), end='')
        time.sleep(0.1)
        winsound.Beep(500, 50)
        print(Back.RED + "\r\033[30m{}".format('..'), end='')
        time.sleep(0.1)
        print('\r', Style.RESET_ALL)
    skip = False
    err = False
    ops_cont = 0
    l = input('\n')
    if l == 'stop':
        outro()
        break
    elif l == 'rerun':
        outro()
        keyboard.press('shift')
        keyboard.press('f10')
        keyboard.release('shift')
        keyboard.release('f10')
    elif l == 'anim':
        if anim == False:
            anim = True
            print(Back.BLUE + "\r\033[30m{}".format('ON'), end='')
            print(Style.RESET_ALL)
        else:
            anim = False
            print(Back.RED + "\r\033[30m{}".format('OFF'), end='')
            print(Style.RESET_ALL)
        for iii in range(2):
            winsound.Beep(550, 150)
    elif ("(" or ')') in l:
        print('): Wait for the update to use brackets')
    else:
        def get():
            global anim, l, skip, err
            l.replace(' ', '')
            l.replace(':', '/')
            l.replace(',', '.')
            c = []
            tm = ''
            for i in l:
                if i in '0123456789.':
                    tm += i
                elif i in '+-*/^':
                    c.append(float(tm))
                    tm = ''
                    c.append(i)
                else:
                    if err == False:
                        err = True
                        if anim == True:
                            winsound.Beep(900, 100)
                            winsound.Beep(1500, 100)
                            for i in range(2):
                                print(Back.RED + "\r\033[30m{}".format(' INCORRECT INPUT '), end='')
                                time.sleep(0.25)
                                print(Back.BLUE + "\r\033[30m{}".format(' INCORRECT INPUT '), end='')
                                time.sleep(0.25)
                            print(Back.RED + "\r\033[30m{}".format(' INCORRECT INPUT '))
                            print(Back.RED + "\r\033[30m{}".format(' EXTRA CHARACTERS HAVE BEEN REMOVED'))
            c.append(float(tm))
            return c
        def ops(q):
            global anim, fl
            for j in '^*/+-':
                for i in range(q.count(j)):
                    ind = q.index(j)
                    if j == '^':
                        q[ind] = (q[ind - 1] ** q[ind + 1])
                    elif j == '*':
                        q[ind] = (q[ind - 1] * q[ind + 1])
                    elif j == '/':
                        q[ind] = (q[ind - 1] / q[ind + 1])
                    elif j == '+':
                        q[ind] = (q[ind - 1] + q[ind + 1])
                    else:
                        q[ind] = (q[ind - 1] - q[ind + 1])
                    q.remove(q[ind - 1])
                    q.remove(q[ind])
            if float(q[0]) == int(q[0]):
                return int(q[0])
            else:
                return float(q[0])
        def prt_answer():
            global anim
            if skip == False:
                answ = ops(get())
                if anim == True:
                    for i in range(3):
                        print(Back.BLUE + "\r\033[30m{}".format(f'ANSWER:  {answ}  '), end='')
                        time.sleep(0.25)
                        print(Back.GREEN + "\r\033[30m{}".format(f'ANSWER:  {answ}  '), end='')
                        time.sleep(0.25)
                    winsound.Beep(400, 70)
                    print(Back.GREEN + "\r\033[30m{}".format(f'ANSWER:  {answ}  '))
                    print(Style.RESET_ALL)
                else:
                    print(answ)
        prt_answer()


