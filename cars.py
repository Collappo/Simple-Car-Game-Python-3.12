#######################
wersja_pythona = 3.12 #
#######################

# Potrzebne biblioteki
import keyboard, time, os, random as r, pandas as pd

car_pos = 0
v = 1
km = 0
X = []
game_over = 0

class Menu():
    def __init__(self):
        self.df = None
        
    def leatherboard(self):
        try:
            f = open("data.csv", "x")
            f.close()
            pf = pd.DataFrame(columns=["PlayerName", "Kilimeters"])
            pf.to_csv("data.csv",index_label="ID")
        except FileExistsError:
            pass
                    
    def save(self, player_name: str, kilometers: float):
        self.df = self.df = pd.read_csv("data.csv", index_col="ID")
        self.df.loc[len(self.df.values)] = [player_name, kilometers]
        self.df.to_csv("data.csv", index_label="ID")
        
    
    def display(self):
        os.system("cls")
        Menu().leatherboard()
        if len(pd.read_csv("data.csv", index_col="ID").values) == 0:
            leatherboard = "[Nie grał nikt]"
        else:
            leatherboard = ""
            df = pd.read_csv("data.csv", index_col="ID")
            for i in range(len(df.values)):
                leatherboard += f"[{i}] {df.loc[i, "PlayerName"]}: {df.loc[i, "Kilimeters"]}\n"
        
        print(f"""
 ██████╗ █████╗ ██████╗ ███████╗
██╔════╝██╔══██╗██╔══██╗██╔════╝
██║     ███████║██████╔╝███████╗
██║     ██╔══██║██╔══██╗╚════██║
╚██████╗██║  ██║██║  ██║███████║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
 
[Enter] GRAJ

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

GRACZE:

{leatherboard}
        """)
            


class Console():
    def __init__(self):
        self.witdh = 43
        self.heigth = 20
        self.strips = [6, 12, 18, 24, 30, 36]
        self.space_for_X = [1]
        for i in self.strips: self.space_for_X.append(i + 2)
        self.X = []
        
    
    def display_para(self, v, km):
        match v:
            case 1:
                print(f"Predkosc: 1", end="")
            
            case 0.9:
                print(f"Predkosc: 2", end="")
                
            case 0.8:
                print(f"Predkosc: 3", end="")
            
            case 0.7:
                print(f"Predkosc: 4", end="")
                
            case 0.6:
                print(f"Predkosc: 5", end="")
                
            case 0.5:
                print(f"Predkosc: 6", end="")
                
            case 0.4:
                print(f"Predkosc: 7", end="")
                
            case 0.3:
                print(f"Predkosc: 8", end="")
        
        print(f";   Kilometry: {km}")
           
    def fill(self, car_pos, v, km, X: list):
        Console().display_para(v, km)
        Console().render_line(X)
        if Console().display_car("*[X]*", car_pos, X, 0) == True: return True
        if Console().display_car("*[_]*", car_pos, X, 1) == True: return True
        
    def render_line(self, tab: list):
        for _ in range(self.heigth):
            tab_X =[]
            for i in tab: tab_X.append(i[0]) if i[1] == _ else None
            continue_counter = 0
            
            line = ""
            for __ in range(self.witdh):
                if continue_counter > 0:
                    line += "X"
                    continue_counter -= 1
                else:
                    if __ == 0 or __ == self.witdh - 1:
                        line += "|"
                    elif __ in self.strips:
                        line += "|"
                    elif __ in tab_X:
                        line += "X"
                        continue_counter = 2
                        continue
                    else:
                        line += " "
            print(line, end="\n")
            
    def display_car(self, string: str, x: int, tab: list, one_or_2: int ):
        
        tab_X =[]
        for i in tab:
            if i[1] == 20 + one_or_2:
                tab_X.append(i[0])
                tab_X.append(i[0] + 1)
                tab_X.append(i[0] + 2)
        
        _counter = 0
        for _ in range(int(self.witdh / 2) - int(len(string) / 2) + x):
            if _ == 0:
                print("|", end="")
            elif _ in self.strips:
                print("|", end="")
            elif _ in tab_X:
                print("X", end="")
            else:
                print(" ", end="")
            _counter += 1
        
        for i in range (4):
            if _counter + i in tab_X:
                return True
            
        print(string, end="")
        _counter += 5
        
        for _ in range(self.witdh -_counter):
            _ += _counter
            if _ == self.witdh - 1:
                print("|", end="")
            elif _ in self.strips:
                print("|", end="")
            elif _ in tab_X:
                print("X", end="")
            else:
                print(" ", end="")
        print(end="\n")
        
        _counter = 0
        
    def random_X_pos(self, tab: list):
        if r.randint(0, 10) >= 6:
            tab.append([self.space_for_X[r.randint(0, len(self.space_for_X) - 1)], 0])
        return tab

    def update_X_pos(self, tab: list):
        for i in tab: i[1] += 1
        return tab

Menu().display()

input()

os.system("cls")
while True:
    if keyboard.is_pressed("a"):
        if car_pos >= -15:
            car_pos -= 3
    if keyboard.is_pressed("d"):
        if car_pos <= 15:
            car_pos += 3
            
    if keyboard.is_pressed("w"):
        if v > 0.3:
            v -= 0.1
    
    if keyboard.is_pressed("s"):
        if v < 1:
            v += 0.1
            
    v = round(v, 2)
    km = round(km + 0.1, 2)
    X = Console().random_X_pos(X)
    if Console().fill(car_pos, v, km, X) == True: break
    X = Console().update_X_pos(X)
    time.sleep(v)
    os.system("cls")

os.system("cls")
time.sleep(1)
os.system("cls")
print("""
 ______     ______     __    __     ______        ______     __   __   ______     ______    
/\  ___\   /\  __ \   /\ "-./  \   /\  ___\      /\  __ \   /\ \ / /  /\  ___\   /\  == \   
\ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\      \ \ \/\ \  \ \ \'/   \ \  __\   \ \  __<   
 \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\     \ \_____\  \ \__|    \ \_____\  \ \_\ \_\ 
  \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/      \/_____/   \/_/      \/_____/   \/_/ /_/                                                                                   
      """)

nick = input("[Podaj nick] ")
print(f"Gratujemy {nick}, pokonales {km}km!")
Menu().save(nick, km)
os.startfile("cars.py")