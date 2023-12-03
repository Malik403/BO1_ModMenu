import Tkinter_Class
from game_connecting import game
import threading
import tkinter
import bg_fg

# Offsets
offsets = {
    "BO1_Name": 0x0385892C,
    "BO1_Ammo1": 0x01C08F00,
    "BO1_Ammo2": 0x01C08E88,
    "BO1_Ammo3": 0x01C08E98, 
    "BO1_Points": 0x01C0A6C8, 
    "BO1_Grenades": 0x01C08F08, 
    "BO1_Noclip": 0x01C0A74C, 
    "BO1_Kills": 0x01C0A6CC, 
    "BO1_Headshots": 0x01C0A6EC, 
    "BO1_Health": 0x01A7987C, 
}

# Mods
#Modification Functions
#Test function
def test():
    """ This is a test function for new options. """
    print("Hello")

#Points
def points():
    """ This function is the unlimated points option. """
    game.write_int(offsets["BO1_Points"], 99999999)

#Unlimited Ammo
def unlimated_ammo():
    """ This function is for the unlimited ammo mod. """
    game.write_int(offsets["BO1_Ammo1"], 999)
    game.write_int(offsets["BO1_Ammo2"], 999)
    game.write_int(offsets["BO1_Ammo3"], 999)

    unlimammothread = threading.Thread(target=unlimated_ammo, daemon=True)
    unlimammothread.start()
#Grenades
def grenades():
    """ This function is used to modify the grenades. """
    game.write_int(offsets["BO1_Grenades"], 999)

#Noclip
def noclipon():
    """ This function is for the noclip mod (On). """
    game.write_bool(offsets["BO1_Noclip"], True)

def noclipoff():
    """ This function is for the noclip mod (Off). """
    game.write_bool(offsets["BO1_Noclip"], False)

#GodMode
def godmode():
    """ This function is for the godmode mod. """
    game.write_int(offsets["BO1_Health"], 9999)

    godthread = threading.Thread(target=godmode, daemon=True)
    godthread.start()

#Name
def name():
    """ This function is the edit name mod. """
    reading_name = name_entry.get()

    #This long Enter is because some string is still exposed if you dont get ALL of it!
    game.write_string(offsets["BO1_Name"], "                                                                ")
    game.write_string(offsets["BO1_Name"], reading_name)

#Headshot Score
def headshot_score():
    """ This function is for changing the Headshot Score. """
    reading_headshot = int(headshot_entry.get())

    game.write_int(offsets["BO1_Headshots"], reading_headshot)

def kill_score():
    """ This function is for changing the Kill Score. """
    reading_kills = int(kill_entry.get())

    game.write_int(offsets["BO1_Kills"], reading_kills)

#Function to close mod menu (Closes Tkinter)
def norun():
    """ This function is to close the mod menu """
    Tkinter_Class.root.destroy()

#Exits the whole program
def destroy():
    """ This function is used for the safe way to exit the program! """
    Tkinter_Class.root.quit()
    exit()

#Main Menu

""" This function is the Main Menu. """
main = Tkinter_Class.TkinterGUI() #Instance of Tkinter Class

#Check Buttons For Mod Menu
#Main Mods Buttons
main.Button("", points, 80, 10, 30) #Points
main.Button("", unlimated_ammo, 80, 10, 70) #Ammo
main.Button("", grenades, 80, 10, 110) #Grenades
main.Button("", godmode, 80, 10, 150) #God Mode
main.Button("", noclipon, 30, 240, 190)
main.Button("", noclipoff, 30, 240, 230)
main.Button("", destroy, 100, 100, 530) #Destroy Tkinter + End Program
main.Button("", name, 40, 160, 298) #Change Name Button
main.Button("", headshot_score, 40, 160, 347) #Change Headshot Button
main.Button("", kill_score, 40, 160, 398) #Change Kill Button

#Custmization Buttons - BackGround
main.Button("White", bg_fg.white_bg, 11, 500, 75)
main.Button("Black", bg_fg.black_bg, 11, 500, 100)
main.Button("Red", bg_fg.red_bg, 11, 500, 125)
main.Button("Green", bg_fg.green_bg, 11, 500, 150)
main.Button("Blue", bg_fg.blue_bg, 11, 500, 175)
main.Button("Cyan", bg_fg.cyan_bg, 11, 500, 200)
main.Button("Yellow", bg_fg.yellow_bg, 11, 500, 225)
main.Button("Magenta", bg_fg.magenta_bg, 11, 500, 250)

#Customization Buttons - ForeGround
main.Button("White", bg_fg.white_fg, 11, 650, 75)
main.Button("Black", bg_fg.black_fg, 11, 650, 100)
main.Button("Red", bg_fg.red_fg, 11, 650, 125)
main.Button("Green", bg_fg.green_fg, 11, 650, 150)
main.Button("Blue", bg_fg.blue_fg, 11, 650, 175)
main.Button("Cyan", bg_fg.cyan_fg, 11, 650, 200)
main.Button("Yellow", bg_fg.yellow_fg, 11, 650, 225)
main.Button("Magenta", bg_fg.magenta_fg, 11, 650, 250)

name_entry = tkinter.IntVar()
headshot_entry = tkinter.IntVar()
kill_entry = tkinter.IntVar()


#Labels (Spaced out so it can be in the middle of the GUI - Might change to the ACTUAL function.)
#Try-Except for changing color(This saves their customization!)
try:
    with open("bg-label.txt", "r") as myFile1:
        with open("fg-label.txt", "r") as myFile2:
            reading_background = myFile1.read()
            reading_foreground = myFile2.read()
            
            Tkinter_Class.root.configure(background=reading_background)

            #Text Labels
            main.Label("                                                                                                                       BO1 GUI MENU!", 140, 0, 0, reading_background, reading_foreground)
            main.Label("Change Color", 13, 575, 15, reading_background, reading_foreground)
            main.Label("BackGround", 11, 500, 50, reading_background, reading_foreground)
            main.Label("ForeGround", 11, 650, 50, reading_background, reading_foreground)

            #Check Button Labels
            main.Label("Change Name", 13, 240, 300, reading_background, reading_foreground)
            main.Label("Change Headshot Score", 22, 220, 350, reading_background, reading_foreground)
            main.Label("Change Kill Score", 16, 230, 400, reading_background, reading_foreground)
            main.Label("Exit Program!", 12, 350, 533, reading_background, reading_foreground)

            #Main Mods Labels
            main.Label("Points", 6, 230, 33, reading_background, reading_foreground)
            main.Label("Ammo", 6.5, 230, 72, reading_background, reading_foreground)
            main.Label("Grenades", 8.5, 230, 113, reading_background, reading_foreground)
            main.Label("Juggernaut", 10, 230, 153, reading_background, reading_foreground)
            main.Label("Noclip", 6, 120, 210, reading_background, reading_foreground)
            main.Label("On", 3, 325, 193, reading_background, reading_foreground)
            main.Label("Off", 3, 325, 233, reading_background, reading_foreground)

            name_entry = tkinter.Entry(Tkinter_Class.root, bd=5)
            name_entry.place(x=10, y=300)

            #Headshot Score
            headshot_entry = tkinter.Entry(Tkinter_Class.root, bd=5)
            headshot_entry.place(x=10, y=350)

            #Kill Score
            kill_entry = tkinter.Entry(Tkinter_Class.root, bd=5)
            kill_entry.place(x=10, y=400)
            
except FileNotFoundError:
    #Text Labels
    main.Label("                                                                                                                       BO1 GUI MENU!", 140, 0, 0, "black", "white")
    main.Label("Change Label Color", 18, 560, 15, "black", "white")
    main.Label("BackGround", 11, 500, 50, "black", "white")
    main.Label("ForeGround", 11, 650, 50, "black", "white")
    
    #Check Button Labels
    main.Label("Change Name", 13, 240, 300)
    main.Label("Change Headshot Score", 22, 220, 350)
    main.Label("Change Kill Score", 16, 230, 400)
    main.Label("Exit Program!", 12, 350, 533)

    #Main Mods Labels
    main.Label("Points", 6, 230, 33)
    main.Label("Ammo", 6.5, 230, 72)
    main.Label("Grenades", 8.5, 230, 113)
    main.Label("Juggernaut", 10, 230, 153)
    main.Label("Noclip", 8, 120, 210)
    main.Label("On", 3, 325, 193)
    main.Label("Off", 3, 325, 233)

    

    name_entry = tkinter.Entry(Tkinter_Class.root, bd=5)
    name_entry.place(x=10, y=300)

    #Headshot Score
    headshot_entry = tkinter.Entry(Tkinter_Class.root, bd=5)
    headshot_entry.place(x=10, y=350)

    #Kill Score
    kill_entry = tkinter.Entry(Tkinter_Class.root, bd=5)
    kill_entry.place(x=10, y=400)

Tkinter_Class.root.mainloop()