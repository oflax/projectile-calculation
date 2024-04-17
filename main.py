"""

Başlık:       2023-2024 NİĞDE FEN LİSESİ FİZİK DERSİ PROJE ÖDEVİ
Teslim Eden:  Ahmed Kağan OFLAZ 11/A 22
Teslim Alan:  Ufuk Öz Fizik Öğretmeni

"""

import math
from colorama import Fore, Style

print(Style.BRIGHT)
print("""
(1): Aşağı Düşey Atış & Serbest Düşme
(2): Yatay Atış
(3): Eğik Atış & Yukarı Düşey Atış
      """)

reset = Style.RESET_ALL
bright = Style.BRIGHT + Fore.BLUE

tip = input(Fore.RED + 'Atış Tipi: ' + reset)

g = 9.8 # Yerçekimi İvmesi - m/s²

if tip == "1":
    print(Style.BRIGHT)
    print(Fore.RED)

    v0 = ""
    while v0 == "":
        v0 = input(bright + 'V0: ' + reset)
        h = input(bright + 'h: ' + reset)

        if h == "":
            t = input(bright + 't: ' + reset)

    if h == "":
        h = v0*t + g*t**2/2

    v0 = float(v0)
    h = float(h)

    v = math.sqrt(v0**2 + 2*g*h)
    t = (v-v0) / g

    t = round(t, 1)
    h = round(h, 1)
    v = round(v, 1)

    print(Fore.RESET)
    print(Style.BRIGHT)
    print(f"""
    {Fore.CYAN}ilk{Fore.RESET}
        _
       / \ {Fore.LIGHTGREEN_EX}⇣ V0 = {v0}m/s{Fore.RESET}
       \_/ {Fore.CYAN}⇣ G = {g}N{Fore.RESET}
        -
        |
        |
        |
        |  {Fore.LIGHTGREEN_EX}h = {h}m{Fore.RESET}
        |  {Fore.LIGHTGREEN_EX}t = {t}s{Fore.RESET}
        |
        |
    {Fore.CYAN}son{Fore.RESET} |
        _
       / \ {Fore.LIGHTGREEN_EX}⇣ V = {v}m/s{Fore.RESET}
   ____\_/____""")


if tip == "2":
    print(Style.BRIGHT)
    print(Fore.BLUE)

    h = ""
    while h == "":
        h = input(bright + 'h: ' + reset)
        v0 = input(bright + 'V: ' + reset)

        if v0 == "":
            x = input(bright + 'X: ' + reset)

    h = float(h)

    t = math.sqrt(h / (g/2))

    try:
        v0 = float(v0)
    except:
        v0 = x/t

    v = g*t
    vr = math.sqrt(v0**2 + v**2)
    a = math.degrees(math.atan(v/v0))

    x = v0*t

    h = round(h, 1)
    x = round(x, 1)
    vr = round(vr, 1)
    a = round(a, 1)


    print(Fore.RESET)
    print(Style.BRIGHT)
    print(f"""
        {Fore.LIGHTGREEN_EX}➜ V = {v0}m/s{Fore.RESET}
        _  {Fore.CYAN}⇣ G = {g}N{Fore.RESET}
{Fore.CYAN}ilk{Fore.RESET}    / \ ______
_______\_/       \_
        |          \_
        |            \_
        | h = {h}m    \ 
        |               \ _
        |            {Fore.CYAN}son{Fore.RESET} / \ {Fore.LIGHTGREEN_EX}↘ V = {vr}{Fore.RESET}
        _________________\_/ {Fore.LIGHTGREEN_EX}∠ α = {a}°{Fore.RESET}
            {Fore.LIGHTGREEN_EX}X = {x}m{Fore.RESET}""")

if tip == "3":
    print(Style.BRIGHT)
    print(Fore.BLUE)

    v0 = ""
    while v0 == "":
        v0 = input(bright + 'V0: ' + reset)
        a = input(bright + 'α°: ' + reset)

    if v0 == "":
        v0 = x/t

    v0 = float(v0)
    a = float(a)

    ar = math.radians(a)

    vx = v0*math.cos(ar)
    vy = v0*math.sin(ar)

    t = vy / g

    hmax = vy * (t/2) - ( ( g * ((t/2)**2) ) / 2)

    x = vx*t

    vr = math.sqrt((vx**2) + (vy**2))

    print(Fore.RESET)
    print(Style.BRIGHT)

    hmax = round(hmax, 1)
    x = round(x, 1)
    vr = round(vr, 1)


    print(f"""
{Fore.CYAN}⇣ G = {g}N{Fore.RESET}            _________________
                  __/        |        \__
                _/           |           \_
              _/             |             \_
            /                | {Fore.LIGHTGREEN_EX}h = {hmax}m{Fore.RESET}      \ 
       {Fore.CYAN}ilk{Fore.RESET} /                 |                 \ {Fore.CYAN}son{Fore.RESET}
        _ /                  |                  \ _
       / \                   |                   / \ 
_______\_/_______________________________________\_/ 
    {Fore.LIGHTGREEN_EX}↗ V = {v0}m/s{Fore.RESET}             {Fore.LIGHTGREEN_EX}⟷{Fore.RESET}               {Fore.LIGHTGREEN_EX}↘ V = {vr}m/s{Fore.RESET} 
    {Fore.LIGHTGREEN_EX}∠ α = {a}°{Fore.RESET}             {Fore.LIGHTGREEN_EX}X = {x}m{Fore.RESET}
""")

print()