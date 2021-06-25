import glob
import json
import os
import sys
from os import system, name
from random import choice
from pyfiglet import Figlet
from colorama import init, Fore, Back, Style
from prettytable import PrettyTable

init()

t1, t2 = "Team 1", "Team 2"


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def main():
    global t1, t2
    poolfiles = []
    i = 1

    clear()
    l = Figlet('rectangles')
    txt = l.renderText('Map Veto by synth')
    print(Fore.RED + txt + Style.RESET_ALL)
    print('Available map pools:')
    for x in glob.glob(resource_path('pools/*.json')):
        file = open(x)
        poolfiles.append(x)
        print(str(i) + '. ' + json.load(file)['pool_name'])
        i += 1
    print()
    print(Style.RESET_ALL + Fore.LIGHTCYAN_EX + "Please, choose a map pool to use: " + Style.RESET_ALL, end="")
    pool = int(input())
    print(Style.RESET_ALL + Fore.LIGHTCYAN_EX + "Match type: Bo" + Style.RESET_ALL, end="")
    bo = int(input())
    print(Style.RESET_ALL + Fore.LIGHTCYAN_EX + "Team 1 Name: " + Style.RESET_ALL, end="")
    t1 = input()
    print(Style.RESET_ALL + Fore.LIGHTCYAN_EX + "Team 2 Name: " + Style.RESET_ALL, end="")
    t2 = input()

    while bo % 2 == 0:
        print(Fore.LIGHTRED_EX + "Number must be odd.")
        print(Style.RESET_ALL + Fore.LIGHTCYAN_EX + "Match type: Bo" + Style.RESET_ALL, end="")
        bo = int(input())

    try:
        poolfile = poolfiles[pool - 1]
        poolmaps = json.load(open(poolfile))['maps']
        return poolmaps, bo
    except IndexError:
        print('You might have chosen an invalid map file.')
        quit()
    except:
        print('There was an error.')
        quit()

    return False, False


def generate_table(ava, vet, pic):
    table = PrettyTable()

    # Lengths
    av_len = len(ava)
    ve_len = len(vet)
    pi_len = len(pic)

    top = max(av_len, ve_len, pi_len)

    while len(ava) < top:
        ava.append("")
    while len(vet) < top:
        vet.append("")
    while len(pic) < top:
        pic.append("")

    table.add_column(Fore.LIGHTCYAN_EX + "Available" + Style.RESET_ALL, ava)
    table.add_column(Fore.LIGHTRED_EX + "Vetoed" + Style.RESET_ALL, vet)
    table.add_column(Fore.LIGHTGREEN_EX + "Picked" + Style.RESET_ALL, pic)

    return table


def veto(maps, bo):
    # Execute veto
    if bo == 1:
        veto_bo1(maps)
    elif bo == 3:
        veto_bo3(maps)


def veto_bo1(maps):
    global t1, t2
    available = maps
    num_maps = len(maps)
    vetoed, picked = [], []
    i, p = 0, 0
    while i < num_maps-3:
        clear()
        print(generate_table(available, vetoed, picked))
        if p % 2 == 0:
            print(t1, Fore.LIGHTRED_EX + "VETO" + Style.RESET_ALL + ": ", end="")
        else:
            print(t2, Fore.LIGHTRED_EX + "VETO" + Style.RESET_ALL + ": ", end="")
        sel = input()
        try:
            index = available.index(sel)
            vetoed.append(available[index])
            available.pop(index)
            vetoed = list(filter(lambda x: x != "", vetoed))
            available = list(filter(lambda x: x != "", available))
            p += 1
            i += 1
        except ValueError:
            print(Fore.LIGHTRED_EX + "Invalid map." + Style.RESET_ALL)
    clear()
    auto = choice(available)
    picked.append(auto)
    available.pop(available.index(auto))
    available = list(filter(lambda x: x != "", available))
    picked = list(filter(lambda x: x != "", picked))
    print(generate_table(available, vetoed, picked))
    i = 1
    picked = list(filter(lambda x: x != "", picked))
    for x in picked:
        print(Fore.LIGHTCYAN_EX + "Map " + str(i) + ":", Style.RESET_ALL + x)
        i += 1
    return picked


def veto_bo3(maps):
    global t1, t2
    available = maps
    num_maps = len(maps)
    vetoed, picked = [], []
    i, p, v = 0, 0, True
    while i < num_maps-3 or len(list(filter(lambda x: x != "", picked))) < 2:
        clear()
        print(i)
        print(len(list(filter(lambda x: x != "", picked))))
        print(generate_table(available, vetoed, picked))
        if p % 2 == 0 and p == 0:
            print(t1, Fore.LIGHTRED_EX + "VETO" + Style.RESET_ALL + ": ", end="")
            v = True
            sel = input()
        elif p % 2 != 0 and p == 1:
            print(t2, Fore.LIGHTRED_EX + "VETO" + Style.RESET_ALL + ": ", end="")
            v = True
            sel = input()
        elif p % 2 == 0 and p == 2:
            print(t1, Fore.LIGHTGREEN_EX + "PICK" + Style.RESET_ALL + ": ", end="")
            v = False
            sel = input()
        elif p % 2 != 0 and p == 3:
            print(t2, Fore.LIGHTGREEN_EX + "PICK" + Style.RESET_ALL + ": ", end="")
            v = False
            sel = input()
        elif p % 2 == 0 and p > 3:
            print(t1, Fore.LIGHTRED_EX + "VETO" + Style.RESET_ALL + ": ", end="")
            v = True
            sel = input()
        else:
            print(t2, Fore.LIGHTRED_EX + "VETO" + Style.RESET_ALL + ": ", end="")
            v = True
            sel = input()
        if v:
            try:
                index = available.index(sel)
                vetoed.append(available[index])
                available.pop(index)
                vetoed = list(filter(lambda x: x != "", vetoed))
                available = list(filter(lambda x: x != "", available))
                p += 1
                i += 1
            except ValueError:
                print(Fore.LIGHTRED_EX + "Invalid map." + Style.RESET_ALL)
        else:
            try:
                index = available.index(sel)
                picked.append(available[index])
                available.pop(index)
                picked = list(filter(lambda x: x != "", picked))
                available = list(filter(lambda x: x != "", available))
                p += 1
                i += 1
            except ValueError:
                print(Fore.LIGHTRED_EX + "Invalid map." + Style.RESET_ALL)
    clear()
    auto = choice(available)
    picked.append(auto)
    available.pop(available.index(auto))
    available = list(filter(lambda x: x != "", available))
    picked = list(filter(lambda x: x != "", picked))
    print(generate_table(available, vetoed, picked))
    i = 1
    picked = list(filter(lambda x: x != "", picked))
    for x in picked:
        print(Fore.LIGHTCYAN_EX + "Map " + str(i) + ":", Style.RESET_ALL + x)
        i += 1
    return picked


data, best_of = main()
veto(data, best_of)
print(Fore.LIGHTCYAN_EX + "Good Luck, Have Fun." + Style.RESET_ALL)
input()
