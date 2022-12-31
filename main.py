import keyboard

def funcion():
    keyboard.wait("F3")
    while True:
        if keyboard.is_pressed("a") or keyboard.is_pressed("b") or keyboard.is_pressed("c") or keyboard.is_pressed("d")or keyboard.is_pressed("e") or keyboard.is_pressed("f") \
                            or keyboard.is_pressed("g") or keyboard.is_pressed("h") or keyboard.is_pressed("i") or keyboard.is_pressed("j") or keyboard.is_pressed("k") or keyboard.is_pressed("l") or keyboard.is_pressed("m") \
                                or keyboard.is_pressed("n") or keyboard.is_pressed("o") or keyboard.is_pressed("p") or keyboard.is_pressed("q") or keyboard.is_pressed("r") or keyboard.is_pressed("s") or keyboard.is_pressed("t")\
                                    or keyboard.is_pressed("u") or keyboard.is_pressed("v") or keyboard.is_pressed("w") or keyboard.is_pressed("x") or keyboard.is_pressed("y") or keyboard.is_pressed("z"):
                keyboard.write("≋")
        if keyboard.is_pressed("F2"):
            funcion()
print(" _   _       _                       _     _____ _           _    ______                           ")
print("| | | |     | |                     | |   /  __ \ |         | |   | ___ \                          ")
print("| | | | __ _| | ___  _ __ __ _ _ __ | |_  | /  \/ |__   __ _| |_  | |_/ /_   _ _ __   __ _ ___ ___ ")
print("| | | |/ _` | |/ _ \| '__/ _` | '_ \| __| | |   | '_ \ / _` | __| | ___ \ | | | '_ \ / _` / __/ __|")
print("\ \_/ / (_| | | (_) | | | (_| | | | | |_  | \__/\ | | | (_| | |_  | |_/ / |_| | |_) | (_| \__ \__ \ ")
print(" \___/ \__,_|_|\___/|_|  \__,_|_| |_|\__|  \____/_| |_|\__,_|\__| \____/ \__, | .__/ \__,_|___/___/")
print("                                                                          __/ | |                  ")
print("                                                                         |___/|_|                  ")
print("\n                                       Made By Jalo#2296                                           ")
print("\nPress (F3) for activating it, press (F2) for deactivating it")
print("Suggestion: Only activate it when you open the chat, since if you try to move while having it active it wont let you move")

funcion()