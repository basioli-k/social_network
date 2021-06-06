"""
tab_...  = function to call screen...
screen_... = tkinter window 

tab_information = user info
tab_friends = info about friends
tab_rec = recommendation page
"""
import sys
sys.path.append('../database')
sys.path.append('../entities')
from database import *
from person import *
from college import *
from tkinter import *
import os 
from PIL import ImageTk, Image
#from tkinter.ttk import *



#CONTROLLERS-----
def login_ok():
    #delete login and main screen
    login_screen.destroy()
    main_screen.destroy()
    tab_information()
# from information to friends tab
def info_to_f():
    screen_information.destroy()
    tab_friends()
# from information to friends recommendation tab
def info_to_frec():
    screen_information.destroy()
    tab_frec()
# from information to business recommendation tab
def info_to_brec():
    screen_information.destroy()
    tab_brec()
# from info to logout
def info_to_lg():
    screen_information.destroy()
    main_window()
#from friends to friends recommendation tab
def f_to_frec():
    screen_friends.destroy()
    tab_frec()
    #from friends to friends recommendation tab
def f_to_brec():
    screen_friends.destroy()
    tab_brec()
# from friends to information tab
def f_to_info():
    screen_friends.destroy()
    tab_information()
# from info to logout
def f_to_lg():
    screen_friends.destroy()
    main_window()
# from friends recommendation to information tab
def frec_to_info():
    screen_frec.destroy()
    tab_information()
# from friends recommendation to friends tab
def frec_to_f():
    screen_frec.destroy()
    tab_friends()
# from friends recommendation to business recommendation
def frec_to_brec():
    screen_frec.destroy()
    tab_brec()
# from friends recommendation to logout
def frec_to_lg():
    screen_frec.destroy()
    main_window()
# from business recommendation to information tab
def brec_to_info():
    screen_brec.destroy()
    tab_information()
# from business recommendation to friends tab
def brec_to_f():
    screen_brec.destroy()
    tab_friends()
# from business recommendation to friends recommendation tab
def brec_to_frec():
    screen_brec.destroy()
    tab_frec()
# from business recommendation to logout
def brec_to_lg():
    screen_brec.destroy()
    main_window()
    
#---------------------------------
# TABS----------------------------

# window for login
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("500x400")
    login_screen.configure(bg='#acc4d7')
    Label(login_screen, text="Please enter details below", 
          bg="#acc4d7", width="30", height="2", 
          font=("Times", 15, "bold")
          ).pack(pady=(20,0))
    
   
    global name_verify
    global surname_verify
 
    name_verify = StringVar()
    surname_verify = StringVar()
 
    global name_login_entry
    global surname_login_entry
 
    Label(login_screen, text="Name  *",
          bg="white", width=17, height=2, 
          font=("Times", 13)
          ).pack()
    # frame for entry
    frame = Frame(login_screen, bg="white",bd=18)
    frame.pack()
    # entry username
    name_login_entry = Entry(frame, textvariable=name_verify)
    name_login_entry.pack()
    # label for password
    Label(login_screen, text="Surname  *",
          bg="white", width=17, height=2, 
          font=("Times", 13)
          ).pack()
    # frame for entry
    frame2 = Frame(login_screen, bg="white",bd=18)
    frame2.pack()
    # entry password
    surname_login_entry = Entry(frame2, textvariable=surname_verify)
    surname_login_entry.pack()
    
    Button(login_screen, bg="#547fa3", 
           text="Login", width=10, height=2, 
           command = login_verify
           ).pack(side=TOP)
    
# window for registration - TODO
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("500x400")
    register_screen.configure(bg='#acc4d7')
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", 
          bg="#acc4d7", width="30", height="2", 
          font=("Times", 15, "bold")
          ).pack(pady=(20,0))
    
    Label(register_screen, text="Username  *",
          bg="white", width=17, height=2, 
          font=("Times", 13)
          ).pack()
    # frame for entry
    frame = Frame(register_screen, bg="white",bd=18)
    frame.pack()
    # entry username
    username_entry = Entry(frame, textvariable=username)
    username_entry.pack()
    # label for password
    Label(register_screen, text="Password  *",
          bg="white", width=17, height=2, 
          font=("Times", 13)
          ).pack()
    # frame for entry
    frame2 = Frame(register_screen, bg="white",bd=18)
    frame2.pack()
    # entry password
    password_entry = Entry(frame2, textvariable=password, show= '*')
    password_entry.pack()
    
    Button(register_screen, bg="#547fa3", 
           text="Register", width=10, height=2, 
           command = register_user
           ).pack(side=TOP)
    
# main window with login or register selection    
def main_window():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x250")
    main_screen.title("Account Login")
    main_screen.configure(bg='#acc4d7')
    Label(text="Select Your Choice", 
          bg="white", width="30", height="2", 
          font=("Times", 15, "bold")
          ).pack(pady=(40,0))
    
    Button(text="Log in", bg="#547fa3", 
           height="2", width="20", command = login
           ).pack(side=LEFT,padx=(100,0))
    
    Button(text="Register",bg="#547fa3", 
           height="2", width="20", command=register
           ).pack(side=RIGHT,padx=(0,100))
 
    main_screen.mainloop()
    
#tab informations - "main" tab
def tab_information():
    global screen_information
    screen_information = Tk()
    screen_information.geometry("900x700")
    screen_information.title("Project - social network")
    screen_information.configure(bg='#acc4d7')
    
    navigation = Frame(screen_information, 
                       bg="#206b71")
    navigation.pack(side=TOP)
    #profile icon
    image = Image.open("profile.png")
    photo = ImageTk.PhotoImage(image.resize((150, 150), Image.ANTIALIAS))
    label = Label(navigation, image=photo, bg='#206b71')
    label.image = photo
    label.pack(side=TOP)
    Label(navigation, text=user.name + " " + user.surname, 
          bg='#206b71', fg="white",
          width=200,
          font=("Times", 20, "bold")
          ).pack(side=TOP)
    
    navigation2 = Frame(navigation, 
                        bg="#206b71")
    navigation2.pack()
    
    #butons for navigation    
    Button(navigation2, fg="white",
           text="About you",bg="#114d52", 
           height=2, width=20, 
           state=DISABLED, command=main_window,
           font=("Times", 13)
           ).pack(side=LEFT)  
    Button(navigation2, fg="white",
           text="Friends",bg="#206b71", 
           height=2, width=20, 
           command=info_to_f,
           font=("Times", 13)
           ).pack(side=LEFT)
    Button(navigation2, fg="white",
           text="Friends recommendations",bg="#206b71", 
           height=2, width=20, 
           command=info_to_frec,
           font=("Times", 13)
           ).pack(side=LEFT)
    Button(navigation2, fg="white",
           text="Business recommendations",bg="#206b71", 
           height=2, width=20, 
           command=info_to_brec,
           font=("Times", 13)
           ).pack(side=LEFT)
    Button(navigation2, fg="white",
           text="Log out",bg="#547fa3", 
           height=2, width=20, 
           command=info_to_lg,
           font=("Times", 13)
           ).pack(side=LEFT)
    
    #informations
    info = Frame(screen_information, 
                 bg="#acc4d7")
    info.pack(pady=30)
    #name frame
    n_f = Frame(info, 
                 bg="#acc4d7")
    n_f.pack(side=TOP)
    Label(n_f, text="Name:",
          width=20,bg="#acc4d7",
          font=("Times", 15, "bold")
          ).pack(side=LEFT)
    Label(n_f, text=user.name,
          bg="#547fa3",
          fg="white", width=20,
          font=("Times", 13)
          ).pack(side=RIGHT)
    #surname frame
    sur_f = Frame(info, 
                bg="#acc4d7")
    sur_f.pack(side=TOP)
    Label(sur_f, text="Surname:",
          width=20,bg="#acc4d7",
          font=("Times", 15, "bold")
          ).pack(side=LEFT)
    #TODO - pozvat funkciju za prezime
    Label(sur_f, text=user.surname,
          bg="#547fa3",
          fg="white", width=20,
          font=("Times", 13)
          ).pack(side=RIGHT)
    #gender frame - male blue female red
    g_f = Frame(info, 
                bg="#acc4d7")
    g_f.pack(side=TOP)
    Label(g_f, text="Gender:",
          width=20,bg="#acc4d7",
          font=("Times", 15, "bold")
          ).pack(side=LEFT)
    if user.gender == "F":
        color = '#d47474'
    else:
        color = "#547fa3"
    
    Label(g_f, text="F",
          bg=color,
          fg="white", width=20,
          font=("Times", 13)
          ).pack(side=RIGHT)
    #birth frame
    b_f = Frame(info, 
                bg="#acc4d7")
    b_f.pack(side=TOP)
    Label(b_f, text="Date of birth:",
          width=20,bg="#acc4d7",
          font=("Times", 15, "bold")
          ).pack(side=LEFT)
    Label(b_f, text=user.date_of_birth,
          bg="#547fa3",
          fg="white", width=20,
          font=("Times", 13)
          ).pack(side=RIGHT)
    #college frame
    c_f = Frame(info, 
                bg="#acc4d7")
    c_f.pack(side=TOP)
    Label(c_f, text="College:",
          width=20,bg="#acc4d7",
          font=("Times", 15, "bold")
          ).pack(side=LEFT)
    global user_college
    user_college = user.get_college()
    Button(c_f, fg="white",
           text=user_college.short_name,bg="#547fa3", 
           height=1, width=20, 
           command=see_college,
           font=("Times", 12)
           ).pack(side=LEFT)
    #skills frame
    s_f = Frame(info, 
                bg="#acc4d7")
    s_f.pack(side=TOP)
    Label(s_f, text="Skills:",
          width=20,bg="#acc4d7",
          font=("Times", 15, "bold")
          ).pack(side=LEFT)
    Button(s_f, fg="white",
           text="See More",bg="#547fa3", 
           height=1, width=20, 
           command=see_skills,
           font=("Times", 12)
           ).pack(side=LEFT)
    #hobbies frame
    h_f = Frame(info, 
                bg="#acc4d7")
    h_f.pack(side=TOP)
    Label(h_f, text="Hobbies:",
          width=20,bg="#acc4d7",
          font=("Times", 15, "bold")
          ).pack(side=LEFT)
    Button(h_f, fg="white",
           text="See More",bg="#547fa3", 
           height=1, width=20, 
           command=see_hobbies,
           font=("Times", 12)
           ).pack(side=LEFT)
    #mozda dodat dio s statistikom prijatelja
    #TODO - mjenjanje podataka
    Button(info, fg="white",
           text="Change informations",bg="#547fa3", 
           height=1, width=20, 
           command=see_skills,
           font=("Times", 15)
           ).pack(pady = 50)  
    
# tab friends
def tab_friends():
    global screen_friends
    screen_friends = Tk()
    screen_friends.geometry("900x700")
    screen_friends.title("Project - social network")
    screen_friends.configure(bg='#acc4d7')
    
    navigation = Frame(screen_friends, 
                       bg="#206b71")
    navigation.pack(side=TOP)
    #profile icon
    image = Image.open("profile.png")
    photo = ImageTk.PhotoImage(image.resize((150, 150), Image.ANTIALIAS))
    label = Label(navigation, image=photo, bg='#206b71')
    label.image = photo
    label.pack(side=TOP)
    #label for name TODO - iz baze ocitaj
    Label(navigation, text=user.name + " " + user.surname, 
          bg='#206b71', fg="white",
          width=200,
          font=("Times", 20, "bold")
          ).pack(side=TOP)
    
    navigation2 = Frame(navigation, 
                        bg="#206b71")
    navigation2.pack()
    
    #butons for navigation    
    Button(navigation2, fg="white",
           text="About you",bg="#206b71", 
           height=2, width=20, 
           command=f_to_info,
           font=("Times", 13)
           ).pack(side=LEFT)  
    Button(navigation2, fg="white",
           text="Friends",bg="#114d52", 
           height=2, width=20, 
           state=DISABLED, command=main_window,
           font=("Times", 13)
           ).pack(side=LEFT)
    Button(navigation2, fg="white",
           text="Friends recommendations",bg="#206b71", 
           height=2, width=20, 
           command=f_to_frec,
           font=("Times", 13)
           ).pack(side=LEFT)
    Button(navigation2, fg="white",
           text="Business recommendations",bg="#206b71", 
           height=2, width=20, 
           command=f_to_brec,
           font=("Times", 13)
           ).pack(side=LEFT)
    Button(navigation2, fg="white",
           text="Log out",bg="#547fa3", 
           height=2, width=20, 
           command=f_to_lg,
           font=("Times", 13)
           ).pack(side=LEFT)
    global left_frame
    #frame floating left
    left_frame = Frame(screen_friends, bg='#acc4d7')
    left_frame.pack(side=LEFT)
    Label(left_frame, text="Find friends by:",
          width=20,bg="#acc4d7",
          font=("Times", 15, "bold")
          ).pack(side=TOP)
    #frame for radio button and entry
    frame_radio = Frame(left_frame, bg='#acc4d7')
    frame_radio.pack(side=TOP)
    
    global keyword
    global value
    
    # variable for input
    keyword = StringVar(screen_friends, "all")
    # variable for radio button value
    value = StringVar(screen_friends, "all")
    radio_dict = {"all" : "all",
                   "name" : "name",
                   "surname" : "surname",
                   "year of birth" : "year",
                   "college" : "college",
                   "year graduating" : "yg",
                   "enrollment year" : "ey"}
    style = ttk.Style(frame_radio)
    style.configure("TRadiobutton", background = "white",
                    font = ("arial", 10), width=20)
    for (text, value) in radio_dict.items():
        ttk.Radiobutton(frame_radio, text = text, variable = keyword,
                        value = value, command=search_like).pack(side = TOP, ipady = 5)
    #ERROR NE SALJU SE DOBRO ARGUMENTI
    
# tab business recommendation
def tab_brec():
    global screen_brec
    screen_brec = Tk()
    screen_brec.geometry("900x700")
    screen_brec.title("Project - social network")
    screen_brec.configure(bg='#acc4d7')
    
    navigation = Frame(screen_brec, 
                       bg="#206b71")
    navigation.pack(side=TOP)
    #profile icon
    image = Image.open("profile.png")
    photo = ImageTk.PhotoImage(image.resize((150, 150), Image.ANTIALIAS))
    label = Label(navigation, image=photo, bg='#206b71')
    label.image = photo
    label.pack(side=TOP)
    #label for name TODO - iz baze ocitaj
    Label(navigation, text=user.name + " " + user.surname, 
          bg='#206b71', fg="white",
          width=200,
          font=("Times", 20, "bold")
          ).pack(side=TOP)
    
    navigation2 = Frame(navigation, 
                        bg="#206b71")
    navigation2.pack()
    
    #butons for navigation    
    Button(navigation2, fg="white",
           text="About you",bg="#206b71", 
           height=2, width=20, 
           command=brec_to_info,
           font=("Times", 13)
           ).pack(side=LEFT)  
    Button(navigation2, fg="white",
           text="Friends",bg="#206b71", 
           height=2, width=20, 
           command=brec_to_f,
           font=("Times", 13)
           ).pack(side=LEFT)
    Button(navigation2, fg="white",
           text="Friends recommendations",bg="#206b71", 
           height=2, width=20, 
           command=brec_to_frec,
           font=("Times", 13)
           ).pack(side=LEFT)
    Button(navigation2, fg="white",
           text="Business recommendations",bg="#114d52", 
           height=2, width=20, 
           state=DISABLED, command=main_window,
           font=("Times", 13)
           ).pack(side=LEFT)
    Button(navigation2, fg="white",
           text="Log out",bg="#547fa3", 
           height=2, width=20, 
           command=brec_to_lg,
           font=("Times", 13)
           ).pack(side=LEFT)  
    #TODO - dohvacanje
    preporuke = [["name", "surname", ["a","b","c"], ["a","b","c"]],
                 ["name2", "surname2", ["a","b","c"], ["a","c"]],
                 ["name3", "surname2", ["a","b","c"], ["a","c"]],
                 ["name4", "surname2", ["a","b","c"], ["a","c"]],
                 ["name5", "surname2", ["a","b","c"], ["a","c"]],
                 ["name6", "surname2", ["a","b","c"], ["a","c"]]
                 ]
    
    #preporuke = []
    if not preporuke:
        Label(screen_brec, text="No recommendations now. Try again later!", 
          bg='#acc4d7', fg="black",
          width=200,
          font=("Times", 25, "bold")
          ).pack(side=TOP, pady=15)
    #dodat nesto ako ih nije 6
    #DODAT CU IH SVE RUCNO STO NIJE LIJEPO ALI ...
    else:
        brojac = 0
        for i in range(2):
            row = Frame(screen_brec, bg="#acc4d7")
            row.pack(side=TOP, padx=10, pady = 15)
            for j in range(3):
                person_card = Frame(row, bg="#d47474", borderwidth=1, relief=RAISED)
                person_card.pack(side=LEFT, padx=5, pady=10)
                #name
                Label(person_card, text=preporuke[brojac][0], 
                      bg="#d47474", fg="black",
                      width=20,
                      font=("Times", 15, "bold")
                      ).pack(side=TOP,pady=5)
                Label(person_card, text=preporuke[brojac][1], 
                      bg="#d47474", fg="black",
                      width=20,
                      font=("Times", 15, "bold")
                      ).pack(side=TOP)
                f_buttons = Frame(person_card, bg="#d47474")
                f_buttons.pack(side=TOP,pady=10)
                Button(f_buttons, fg="white",
                       text="See more",bg="#547fa3", 
                       height=1, width=8, 
                       command=person_info,
                       font=("Times", 10)
                       ).pack(side=LEFT) 
                Button(f_buttons, fg="white",
                       text="Add",bg="#547fa3", 
                       height=1, width=8, 
                       command=add_friend,
                       font=("Times", 10)
                       ).pack(side=RIGHT) 
                brojac +=1
                    
# tab friends recommendation
def tab_frec():
    global screen_frec
    screen_frec = Tk()
    screen_frec.geometry("900x700")
    screen_frec.title("Project - social network")
    screen_frec.configure(bg='#acc4d7')
    
    navigation = Frame(screen_frec, 
                       bg="#206b71")
    navigation.pack(side=TOP)
    #profile icon
    image = Image.open("profile.png")
    photo = ImageTk.PhotoImage(image.resize((150, 150), Image.ANTIALIAS))
    label = Label(navigation, image=photo, bg='#206b71')
    label.image = photo
    label.pack(side=TOP)
    #label for name TODO - iz baze ocitaj
    Label(navigation, text=user.name+" "+user.surname, 
          bg='#206b71', fg="white",
          width=200,
          font=("Times", 20, "bold")
          ).pack(side=TOP)
    
    navigation2 = Frame(navigation, 
                        bg="#206b71")
    navigation2.pack()
    
    #butons for navigation    
    Button(navigation2, fg="white",
           text="About you",bg="#206b71", 
           height=2, width=20, 
           command=frec_to_info,
           font=("Times", 13)
           ).pack(side=LEFT)  
    Button(navigation2, fg="white",
           text="Friends",bg="#206b71", 
           height=2, width=20, 
           command=frec_to_f,
           font=("Times", 13)
           ).pack(side=LEFT)
    Button(navigation2, fg="white",
           text="Friends recommendations",bg="#114d52", 
           height=2, width=20, 
           state=DISABLED, command=main_window,
           font=("Times", 13)
           ).pack(side=LEFT)
    Button(navigation2, fg="white",
           text="Business recommendations",bg="#206b71", 
           height=2, width=20, 
           command=frec_to_brec,
           font=("Times", 13)
           ).pack(side=LEFT)
    Button(navigation2, fg="white",
           text="Log out",bg="#547fa3", 
           height=2, width=20, 
           command=frec_to_lg,
           font=("Times", 13)
           ).pack(side=LEFT)  
    #TODO - dohvacanje
    preporuke = [["name", "surname", ["a","b","c"], ["a","b","c"]],
                 ["name2", "surname2", ["a","b","c"], ["a","c"]],
                 ["name3", "surname2", ["a","b","c"], ["a","c"]],
                 ["name4", "surname2", ["a","b","c"], ["a","c"]],
                 ["name5", "surname2", ["a","b","c"], ["a","c"]],
                 ["name6", "surname2", ["a","b","c"], ["a","c"]]
                 ]
    
    #preporuke = []
    if not preporuke:
        Label(screen_frec, text="No recommendations now. Try again later!", 
          bg='#acc4d7', fg="black",
          width=200,
          font=("Times", 25, "bold")
          ).pack(side=TOP, pady=15)
    #dodat nesto ako ih nije 6
    #DODAT CU IH SVE RUCNO STO NIJE LIJEPO ALI ...
    else:
        brojac = 0
        for i in range(2):
            row = Frame(screen_frec, bg="#acc4d7")
            row.pack(side=TOP, padx=10, pady = 15)
            for j in range(3):
                person_card = Frame(row, bg="#d47474", borderwidth=1, relief=RAISED)
                person_card.pack(side=LEFT, padx=5, pady=10)
                #name
                Label(person_card, text=preporuke[brojac][0], 
                      bg="#d47474", fg="black",
                      width=20,
                      font=("Times", 15, "bold")
                      ).pack(side=TOP,pady=5)
                Label(person_card, text=preporuke[brojac][1], 
                      bg="#d47474", fg="black",
                      width=20,
                      font=("Times", 15, "bold")
                      ).pack(side=TOP)
                f_buttons = Frame(person_card, bg="#d47474")
                f_buttons.pack(side=TOP,pady=10)
                Button(f_buttons, fg="white",
                       text="See more",bg="#547fa3", 
                       height=1, width=8, 
                       command=person_info,
                       font=("Times", 10)
                       ).pack(side=LEFT) 
                Button(f_buttons, fg="white",
                       text="Add",bg="#547fa3", 
                       height=1, width=8, 
                       command=add_friend,
                       font=("Times", 10)
                       ).pack(side=RIGHT) 
                brojac +=1
                    
    
#-----------------------
#pomocna
def pomocna():
    print("uspio")
    
# TODO: spojit ovo s bazom
def login_verify():
    user_name = name_verify.get()
    user_surname = surname_verify.get()
    name_login_entry.delete(0, END)
    surname_login_entry.delete(0, END)
    
    #creating instance of person
    global user
    user = Person.get_person_by_name_surname(user_name, user_surname)
    if not user:
        login_error("User with given name and surname is not in database")
    else:
        login_ok()
        
# TODO:dodat dio za unos podataka i provjerit je li vec u bazi
def register_user():
 
    username_info = username.get()
    password_info = password.get()
    
    # if empty
    if username_info == "" or password_info == "":
        username_entry.delete(0, END)
        password_entry.delete(0, END)
 
        Label(register_screen, 
              text="All fields are required!", 
              fg="#f78383", font=("calibri", 11)
              ).pack(pady = 10)
    else:
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
 
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        
        Label(register_screen, bg="#acc4d7",
              text="Registration Successfull. Close this window and log in.", 
              fg="#206b71", font=("calibri", 11, "bold")
              ).pack(pady = 10)
 
    

 
# pop up window for user not found while logging in 
def login_error(message):
    global login_error_screen
    login_error_screen = Toplevel(login_screen)
    login_error_screen.title("Failed")
    login_error_screen.geometry("450x100")
    login_error_screen.configure(bg='#f78383')
    Label(login_error_screen, 
          text=message, 
          font=("Times", 13, "bold"),
          bg='#f78383').pack(pady=10)
    Button(login_error_screen, text="Try again.",
           bg="#547fa3", 
           command=login_error_screen_delete).pack()
    
def login_error_screen_delete():
    login_error_screen.destroy()   
    



    
#TODO - iz baze izvuc    
def see_skills():
    global skills_screen
    skills_screen = Toplevel(screen_information)
    skills_screen.title("Skills set")
    skills_screen.geometry("350x300")
    skills_screen.configure(bg='#d47474')
    Label(skills_screen, 
          text="Your skills are: (resize window if needed)", 
          font=("Times", 12, "bold"),
          bg='#d47474').pack(pady=10)
    i = 1
    for skill in user.skills:
        Label(skills_screen, 
              text=str(i)+". "+skill, 
              font=("Times", 10),
              bg='#d47474').pack(pady=10)
        i +=1
    Button(skills_screen, text="Hide",
           bg="#547fa3", height=2, width=10,
           command=skills_screen_delete).pack(pady=30)
def skills_screen_delete():
    skills_screen.destroy()   
#TODO - iz baze izvuc    
def see_hobbies():
    global hobbies_screen
    hobbies_screen = Toplevel(screen_information)
    hobbies_screen.title("Hobbies set")
    hobbies_screen.geometry("550x300")
    hobbies_screen.configure(bg='#d47474')
    
    Label(hobbies_screen, 
          text="Your hobbies are: (resize window if needed)", 
          font=("Times", 15, "bold"),
          bg='#d47474').pack(pady=10)
    i = 1
    for hobby in user.hobbies:
        Label(hobbies_screen, 
              text=str(i)+". "+hobby, 
              font=("Times", 10),
              bg='#d47474').pack(pady=10)
        i +=1
    
    Button(hobbies_screen, text="Hide",
           bg="#547fa3", height=3, width=10,
           command=hobbies_screen_delete).pack(pady=30)
    
def hobbies_screen_delete():
    hobbies_screen.destroy()

def see_college():
    global college_screen
    college_screen = Toplevel(screen_information)
    college_screen.title("College")
    college_screen.geometry("450x400")
    college_screen.configure(bg='#d47474')
    Label(college_screen, 
          text="More details about education at " + user_college.short_name +":", 
          font=("Times", 15, "bold"),
          bg='#d47474').pack(pady=10)
    
    #frame for full name 
    f_n_f = Frame(college_screen, bg='#d47474')
    f_n_f.pack()
    Label(f_n_f, text="Full name:",
          width=20,bg="#d47474",
          font=("Times", 13, "bold")
          ).pack()
    Label(f_n_f, 
          text=user_college.name, 
          font=("Times", 13),
          bg='#d47474').pack()
    #frame for area 
    a_f = Frame(college_screen, bg='#d47474')
    a_f.pack()
    Label(a_f, text="Area:",
          width=20,bg="#d47474",
          font=("Times", 13, "bold")
          ).pack()
    Label(a_f, 
          text=user_college.area, 
          font=("Times", 13),
          bg='#d47474').pack()
    #from database get
    enrollment_y = user.get_college_enroll() 
    graduate_y = user.get_college_graduate() 
    grade = user.get_college_grade() 
    
    #frame for enrollment_year
    e_f = Frame(college_screen, bg='#d47474')
    e_f.pack()
    Label(e_f, text="Enrollment year:",
          width=20,bg="#d47474",
          font=("Times", 13, "bold")
          ).pack()
    Label(e_f, 
          text=enrollment_y, 
          font=("Times", 13),
          bg='#d47474').pack()
    #frame for graduate_year
    gy_f = Frame(college_screen, bg='#d47474')
    gy_f.pack()
    Label(gy_f, text="Graduate year:",
          width=20,bg="#d47474",
          font=("Times", 13, "bold")
          ).pack()
    Label(gy_f, 
          text=graduate_y, 
          font=("Times", 13),
          bg='#d47474').pack()
    #frame for graduate_year
    grade_f = Frame(college_screen, bg='#d47474')
    grade_f.pack()
    Label(grade_f, text="Grade:",
          width=20,bg="#d47474",
          font=("Times", 13, "bold")
          ).pack()
    Label(grade_f, 
          text=grade, 
          font=("Times", 13),
          bg='#d47474').pack()
    
    
    Button(college_screen, text="Hide",
           bg="#547fa3", height=3, width=10,
           command=college_screen_delete).pack(pady=30)
    
def college_screen_delete():
    college_screen.destroy()


def search_like():
    print(keyword.get())

    
def search_like():
    global search_entry_value
    search_entry_value = StringVar(screen_friends)
    if keyword.get() != "all":
        Label(left_frame, text="Keyword:",
              width=10,bg="#acc4d7",
              font=("Times", 12, "bold")
              ).pack(side=LEFT,pady=5)
        search_entry = Entry(left_frame, textvariable=search_entry_value)
        search_entry.pack(side=LEFT,pady=5,padx=5)
        #TODO - pozvati nesto s tim vrijednostima
    
    Button(left_frame, text="Search",
           bg="#547fa3", height=2, width=10,
           command=search).pack(side=RIGHT)
    
def search():    
    #TODO iz baze ucitaj
    friends = [("ja", "sam"), ("ja","sam")]
    #POMOCNO - promjenit cu im smjer na lijevo i ovo desno
    right_frame = Frame(screen_friends, bg='#acc4d7')
    right_frame.pack(side=RIGHT,padx=10)
    for (name, surname) in friends:
        #frame for friends
        ff = Frame(right_frame, bg="#acc4d7")
        ff.pack(pady=15)
        Label(ff, text=name+" "+surname,
              width=20,bg="#acc4d7",
              font=("Times", 15)
              ).pack(side=LEFT)
        Button(ff, text="Add",
               bg="#547fa3", height=1, width=5,
               command=add_friend).pack(side=RIGHT)
    
def add_friend_frec():
    #tu dodat da se gumb disablea s config kada se doda
    #u listi je pa se makne (vidi web)
    print("a")    
def add_friend_brec():
    #tu dodat da se gumb disablea s config kada se doda
    #u listi je pa se makne (vidi web)
    print("a")     

#TODO   
def person_info():
    global person_screen
    person_screen = Toplevel(screen_frec)
    person_screen.title("Person info")
    person_screen.geometry("350x300")
    person_screen.configure(bg='#d47474')
    Label(person_screen, 
          text="More information about person:", 
          font=("Times", 15, "bold"),
          bg='#d47474').pack(pady=10)
    Label(person_screen, 
          text="1. ....", 
          font=("Times", 13),
          bg='#d47474').pack()
    Label(person_screen, 
          text="2. .....", 
          font=("Times", 13),
          bg='#d47474').pack()
    Label(person_screen, 
          text="3. .....", 
          font=("Times", 13),
          bg='#d47474').pack()
    Button(person_screen, text="Hide",
           bg="#547fa3", height=2, width=10,
           command=person_screen_delete).pack(pady=30)
def person_screen_delete():
    person_screen.destroy()    
    

#TODO - mjenjanje podataka

    
main_window()