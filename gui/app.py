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
sys.path.append('../data_prep')
from database import *
from person import *
from college import *
from tkinter import *
from tkcalendar import Calendar
import datetime
import os 
from PIL import ImageTk, Image
#from tkinter.ttk import *

#helping
class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self)
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
class ScrollableFrame_min(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self)
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.config(width=100, height=100)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")



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
#clear all screen_friends
def clear_all():
    btn_search = None
    screen_friends.destroy()
    tab_friends()
    
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
    register_screen.geometry("600x700")
    register_screen.configure(bg='#206b71')
 
    Label(register_screen, text="Please enter details below", 
          bg="white", fg = "black", width=30, height=2, 
          font=("Times", 15, "bold")
          ).pack(pady=5)
   
    #frame for name and surname
    frame_name = Frame(register_screen, bg="#206b71")
    frame_name.pack(side=TOP, pady=5)
    Label(frame_name, text="Name:  *",
          bg="#206b71", width=10, height=2, 
          font=("Times", 13, "bold")
          ).pack(side = LEFT)
    global name
    name = StringVar()
    name_entry = Entry(frame_name, textvariable=name)
    name_entry.pack(side = LEFT)
    Label(frame_name, text="Surname:  *",
          bg="#206b71", width=10, height=2, 
          font=("Times", 13, "bold")
          ).pack(side = LEFT)
    global surname
    surname = StringVar()
    surname_entry = Entry(frame_name, textvariable=surname)
    surname_entry.pack(side = LEFT)
    #frame for gender
    frame_g = Frame(register_screen, bg="#206b71")
    frame_g.pack(side=TOP)
    Label(frame_g, text="Gender:  *",
          bg="#206b71", width=20, height=2, 
          font=("Times", 13, "bold")
          ).pack(side = LEFT)
    #frame for radiobtns
    frame_btn_g = Frame(frame_g, bg="#206b71")
    frame_btn_g.pack(side=RIGHT)
    global g
    g = StringVar()
    g.set("F")
    rbtn_f = Radiobutton(frame_btn_g,bg="#206b71", text="Female", variable=g, value="F")
    rbtn_m = Radiobutton(frame_btn_g, bg="#206b71",text="Male", variable=g, value="M")
    rbtn_f.pack(side=LEFT)
    rbtn_m.pack(side=RIGHT)
    #frame for birthday
    frame_bd = Frame(register_screen, bg="#206b71")
    frame_bd.pack(side=TOP)
    Label(frame_bd, text="Date:  *",
          bg="#206b71", width=20, height=2, 
          font=("Times", 13, "bold")
          ).pack(side = TOP)
    global cal
    cal = Calendar(frame_bd, selectmode = 'day',
                   year = 2000, month = 1, 
                   day = 1, date_pattern = 'y-mm-dd',
                   mindate= datetime.date(1980,1,1), maxdate=datetime.date(2000,1,1))
    cal.pack(side=TOP)
    #frame for college
    frame_coll = Frame(register_screen, bg="#206b71")
    frame_coll.pack(side=TOP)
    Label(frame_coll, text="College:  *",
          bg="#206b71", width=20, height=2, 
          font=("Times", 13, "bold")
          ).pack(side = TOP)
    #frame for radiobtns
    frame_btn_c = Frame(frame_coll, bg="#206b71")
    frame_btn_c.pack(side=TOP)
    global c
    c = StringVar()
    c.set("PMF")
    rbtn_1 = Radiobutton(frame_btn_c,bg="#206b71", text="PMF", variable=c, value="PMF")
    rbtn_2 = Radiobutton(frame_btn_c, bg="#206b71",text="FER", variable=c, value="FER")
    rbtn_3 = Radiobutton(frame_btn_c, bg="#206b71",text="TVZ", variable=c, value="TVZ")
    rbtn_4 = Radiobutton(frame_btn_c, bg="#206b71",text="FSB", variable=c, value="FSB")
    rbtn_5 = Radiobutton(frame_btn_c, bg="#206b71",text="PBF", variable=c, value="PBF")
    rbtn_6 = Radiobutton(frame_btn_c, bg="#206b71",text="FKIT", variable=c, value="FKIT")
    rbtn_7 = Radiobutton(frame_btn_c, bg="#206b71",text="FFZG", variable=c, value="FFZG")
    rbtn_8 = Radiobutton(frame_btn_c, bg="#206b71",text="FHS", variable=c, value="FHS")
    rbtn_9 = Radiobutton(frame_btn_c, bg="#206b71",text="Pravo", variable=c, value="pravo")
    rbtn_1.pack(side=LEFT)
    rbtn_2.pack(side=LEFT)
    rbtn_3.pack(side=LEFT)
    rbtn_4.pack(side=LEFT)
    rbtn_5.pack(side=LEFT)
    rbtn_6.pack(side=LEFT)
    rbtn_7.pack(side=LEFT)
    rbtn_8.pack(side=LEFT)
    rbtn_9.pack(side=LEFT)
    #frame for ey and gy 
    frame_ey_gy = Frame(register_screen, bg="#206b71")
    frame_ey_gy.pack(side=TOP)
    Label(frame_ey_gy, text="Enrollment year:  *",
          bg="#206b71", width=20, height=2, 
          font=("Times", 13, "bold")
          ).pack(side = LEFT)
    global ey
    ey = StringVar()    #must be string because of problems with IntVar and default zero in the end
    ey_entry = Entry(frame_ey_gy, textvariable=ey, width=10)
    ey_entry.pack(side = LEFT)
    global gy
    gy = StringVar()
    gy_entry = Entry(frame_ey_gy, textvariable=gy, width=10)
    gy_entry.pack(side = RIGHT)
    Label(frame_ey_gy, text="Graduate year:  *",
          bg="#206b71", width=20, height=2, 
          font=("Times", 13, "bold")
          ).pack(side = RIGHT)
    
    #frame for grade
    frame_grade = Frame(register_screen, bg="#206b71")
    frame_grade.pack(side=TOP)
    Label(frame_grade, text="Grade:  * (from 1.00 to 5.00 decimal number)",
          bg="#206b71", width=40, height=2, 
          font=("Times", 13, "bold")
          ).pack(side = LEFT)
    global grade
    grade = StringVar()
    grade_entry = Entry(frame_grade, textvariable=grade, width=10)
    grade_entry.pack(side = LEFT)
    global btn_add
    btn_add = Button(register_screen, bg="#547fa3", 
           text="Add skills and hobbies", width=20, height=2, 
           #TODO
           #command = lambda name=name.get(), surname=surname.get(), gender = g.get(),
           #                 date = cal.get_date(), college = c.get(), 
           #                 ey = ey.get(), gy = gy.get(), grade = grade.get(): 
           #                 add_skills_hobbies(name, surname, gender, date, college, ey, gy, grade)
           command = add_skills
           )
    btn_add.pack(side=BOTTOM,pady = 10)
    
    register_screen.mainloop()
    
    
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
           text="Friends \n recommendations",bg="#206b71", 
           height=2, width=20, 
           command=info_to_frec,
           font=("Times", 13)
           ).pack(side=LEFT)
    Button(navigation2, fg="white",
           text="Business \n recommendations",bg="#206b71", 
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
    
    Label(g_f, text=user.gender,
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
    global ey
    global gy
    global gr
    
    user_college, ey, gy, gr = user.get_attendance_info("../database/database.cfg")
    

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
           command=lambda screen=screen_information, key = "skills" : see_more_s_h(key, screen),
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
           command=lambda screen=screen_information, key = "hobbies" : see_more_s_h(key, screen),
           font=("Times", 12)
           ).pack(side=LEFT)
    #mozda dodat dio s statistikom prijatelja
    #TODO - mjenjanje podataka
    Button(info, fg="white",
           text="Change informations",bg="#547fa3", 
           height=1, width=20, 
           command=main_window,
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
           text="Friends \n recommendations",bg="#206b71", 
           height=2, width=20, 
           command=f_to_frec,
           font=("Times", 13)
           ).pack(side=LEFT)
    Button(navigation2, fg="white",
           text="Business \n recommendations",bg="#206b71", 
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
    radio_dict = {"All" : "all",
                   "Name" : "name",
                   "Surname" : "surname",
                   "Year of birth" : "year",
                   "College" : "college",
                   "Graduating year" : "gy",
                   "Enrollment year" : "ey"}
    style = ttk.Style(frame_radio)
    style.configure("TRadiobutton", background = "white",
                    font = ("arial", 10), width=20)
    
    radio_buttons = []
    for (text, value) in radio_dict.items():
        btn_r = ttk.Radiobutton(frame_radio, text = text, variable = keyword,
                        value = value, command=lambda l = radio_buttons: search_like(l))
        btn_r.pack(side = TOP, ipady = 5)
        radio_buttons.append(btn_r)
    
    Button(screen_friends,fg="white",
           text="Clear all",bg="#547fa3", 
           height=1, width=10, 
           command=clear_all,
           font=("Times", 13)
           ).pack(side=BOTTOM, pady=5)
    
# tab business recommendation
def tab_brec():
    global screen_brec
    screen_brec = Tk()
    screen_brec.geometry("900x800")
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
           text="Friends \n recommendations",bg="#206b71", 
           height=2, width=20, 
           command=brec_to_frec,
           font=("Times", 13)
           ).pack(side=LEFT)
    Button(navigation2, fg="white",
           text="Business \n recommendations",bg="#114d52", 
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
    
    global list_brec
    list_brec = user.get_business_recommendation(limit=9)
    
    if not list_brec:
        Label(screen_brec, text="No recommendations now. Try again later!", 
          bg='#acc4d7', fg="black",
          width=200,
          font=("Times", 25, "bold")
          ).pack(side=TOP, pady=15)
    else:
        nb = len(list_brec)
        index = 0
        button_list = []
        for i in range(3):
            row = Frame(screen_brec, bg="#acc4d7")
            row.pack(side=TOP, padx=10, pady = 15)
            if nb == 0:
                break;
            for j in range(3):
                if nb == 0:
                    break;
                person_card = Frame(row, bg="#d47474", borderwidth=1, relief=RAISED)
                person_card.pack(side=LEFT, padx=5, pady=10)
                #name
                Label(person_card, text=list_brec[index].name, 
                      bg="#d47474", fg="black",
                      width=20,
                      font=("Times", 15, "bold")
                      ).pack(side=TOP,pady=5)
                Label(person_card, text=list_brec[index].surname, 
                      bg="#d47474", fg="black",
                      width=20,
                      font=("Times", 15, "bold")
                      ).pack(side=TOP)
                f_buttons = Frame(person_card, bg="#d47474")
                f_buttons.pack(side=TOP,pady=10)
                Button(f_buttons, fg="white",
                       text="See more",bg="#547fa3", 
                       height=1, width=8, 
                       command=lambda person = list_brec[index], screen = screen_brec : person_info(person, screen),
                       font=("Times", 10)
                       ).pack(side=LEFT) 
                btn_add = Button(f_buttons, fg="white",
                       text="Add",bg="#547fa3", 
                       height=1, width=8, 
                       command=lambda person = list_brec[index], index=index, b_l= button_list, screen=screen_brec: add_friend(person, screen, index, b_l),
                       font=("Times", 10)
                       )
                btn_add.pack(side=RIGHT) 
                button_list.append(btn_add)
                nb -=1
                index +=1
                    
# tab friends recommendation
def tab_frec():
    global screen_frec
    screen_frec = Tk()
    screen_frec.geometry("900x800")
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
           text="Friends \n recommendations",bg="#114d52", 
           height=2, width=20, 
           state=DISABLED, command=main_window,
           font=("Times", 13)
           ).pack(side=LEFT)
    Button(navigation2, fg="white",
           text="Business \n recommendations",bg="#206b71", 
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
    
    global list_frec
    list_frec = user.get_personal_recommendation(limit=9)
    
    if not list_frec:
        Label(screen_frec, text="No recommendations now. Try again later!", 
              bg='#acc4d7', fg="black",
              width=200,
              font=("Times", 25, "bold")
              ).pack(side=TOP, pady=15)
    else:
        nb = len(list_frec)
        index = 0
        button_list = []
        for i in range(3):
            row = Frame(screen_frec, bg="#acc4d7")
            row.pack(side=TOP, padx=10, pady = 15)
            if nb == 0:
                break;
            for j in range(3):
                if nb == 0:
                    break;
                person_card = Frame(row, bg="#d47474", borderwidth=1, relief=RAISED)
                person_card.pack(side=LEFT, padx=5, pady=10)
                #name
                Label(person_card, text=list_frec[index].name, 
                      bg="#d47474", fg="black",
                      width=20,
                      font=("Times", 15, "bold")
                      ).pack(side=TOP,pady=5)
                Label(person_card, text=list_frec[index].surname, 
                      bg="#d47474", fg="black",
                      width=20,
                      font=("Times", 15, "bold")
                      ).pack(side=TOP)
                f_buttons = Frame(person_card, bg="#d47474")
                f_buttons.pack(side=TOP,pady=10)
                Button(f_buttons, fg="white",
                       text="See more",bg="#547fa3", 
                       height=1, width=8, 
                       command=lambda person = list_frec[index], screen = screen_frec : person_info(person, screen),
                       font=("Times", 10)
                       ).pack(side=LEFT) 
                btn_add = Button(f_buttons, fg="white",
                       text="Add",bg="#547fa3", 
                       height=1, width=8, 
                       command=lambda person = list_frec[index], index=index, b_l= button_list, screen=screen_frec: add_friend(person, screen, index, b_l),
                       font=("Times", 10))
                btn_add.pack(side=RIGHT) 
                button_list.append(btn_add)
                nb -=1
                index +=1
    
#--------------------------------------------------------------------

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
#-------------------------------------------------------------------------        
# TODO:dodat dio za unos podataka i provjerit je li vec u bazi
def add_hobbies(u_name, u_surname, u_birthday, u_gender, u_college, u_enrollment_year, u_graduate_year, u_grade):
    #print(u_name, u_surname, u_birthday, u_gender, u_college, u_enrollment_year, u_graduate_year, u_grade)
    skills = []
    index = choice_skills.curselection()
    for i in index:
        skills.append(choice_skills.get(i))
    if skills == []:
        pop_up("You need to choose skills!")
        return
    else:
        yscrollbar.destroy()
        frame_skills.destroy()
        b.destroy()
        
    #-----
    import configparser, json
    config = configparser.ConfigParser()
    config.read("../data_prep/data.cfg", encoding='utf-8')
    y = json.loads(config["data"]["hobbies"])
    #--------
    global frame_hobbies
    frame_hobbies = Frame (frame_last, bg="#206b71")
    frame_hobbies.pack(side=RIGHT, padx = 10)
    global yscrollbar1
    yscrollbar1 = Scrollbar(frame_hobbies)
    yscrollbar1.pack(side = RIGHT, fill = Y)
    global choice_hobbies
    choice_hobbies = Listbox(frame_hobbies, selectmode = "multiple", 
                            yscrollcommand = yscrollbar1.set)
  
    choice_hobbies.pack(padx = 10, pady = 10,
          expand = YES, fill = "both")
    
    
    for each_item in range(len(y)):
      
        choice_hobbies.insert(END, y[each_item])
  

    yscrollbar1.config(command = choice_hobbies.yview)
    global b2
    b2 = Button(frame_last, bg="#547fa3", 
           text="Register", width=10, height=2, 
           command = lambda a1 = u_name, a2 = u_surname, 
                            a3 = u_birthday, a4 = u_gender,
                            a5 = u_college, a6 = u_enrollment_year,
                            a7 = u_graduate_year, a8 = u_grade,
                            a9 = skills: 
                            register_user(a1, a2, a3, a4, a5, a6, a7, a8, a9)
           )
    b2.pack(side=RIGHT, pady = 10, padx=5)

#-------------------------------------------------------- 
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
#--------------------------------------------------------   

def see_more_s_h(key, screen):
    global see_more_screen
    see_more_screen = Toplevel(screen)
    see_more_screen.title("List of your " + key)
    see_more_screen.geometry("350x500")
    see_more_screen.configure(bg='#d47474')
    Label(see_more_screen, 
          text="Your " + key + " are: (resize window if needed)", 
          font=("Times", 12, "bold"),
          bg='#d47474').pack(pady=10)
    if key == "skills": 
        user_list =  user.skills
    else:
        user_list =  user.hobbies
    i = 1
    for item in user_list:
        Label(see_more_screen, 
              text=str(i) + ". " + item, 
              font=("Times", 10),
              bg='#d47474').pack(pady=10)
        i +=1
    Button(see_more_screen, text="Hide",
           bg="#547fa3", height=2, width=10,
           command=see_more_screen_delete).pack(pady=30)
    
def see_more_screen_delete():
    see_more_screen.destroy()  

#-----------------------------------------------------------------
    

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

#----------------------------------------------------------------------------
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
    #frame for enrollment_year
    e_f = Frame(college_screen, bg='#d47474')
    e_f.pack()
    Label(e_f, text="Enrollment year:",
          width=20,bg="#d47474",
          font=("Times", 13, "bold")
          ).pack()
    Label(e_f, 
          text=str(ey), 
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
          text=str(gy), 
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
          text=str(gr), 
          font=("Times", 13),
          bg='#d47474').pack()
    
    
    Button(college_screen, text="Hide",
           bg="#547fa3", height=3, width=10,
           command=college_screen_delete).pack(pady=30)
    
def college_screen_delete():
    college_screen.destroy()
#-------------------------------------------------------------------  
def search_like(radio_buttons): 
    #extra:
    for i in range(len(radio_buttons)):
        radio_buttons[i].configure(state = DISABLED)
    
    global search_entry_value
    search_entry_value = StringVar(screen_friends)
    if keyword.get() != "all":
        Label(left_frame, text="Keyword:",
              width=10,bg="#acc4d7",
              font=("Times", 12, "bold")
              ).pack(side=LEFT,pady=5)
        search_entry = Entry(left_frame, textvariable=search_entry_value)
        search_entry.pack(side=LEFT,pady=5,padx=5)
        
    global btn_search
    btn_search = Button(left_frame, text="Search",
           bg="#547fa3", height=2, width=5,
           command=lambda word = search_entry_value: search(word))
    btn_search.pack(side=RIGHT)
    
def search(word):    
    
    btn_search.configure(state = DISABLED)
    
    word = str(word.get())
    #frame for results
    right_frame = Frame(screen_friends, bg='#acc4d7')
    right_frame.pack(side=RIGHT,padx=10)
    if word == "" and keyword.get() != "all":
        Label(right_frame, text="Keyword is not valid.",
              width=20,bg="#acc4d7",
              font=("Times", 15, "bold")
              ).pack(side=LEFT, padx = 5)
        return
    elif keyword.get() == "all":
            friends = user.get_all_friends()
    elif keyword.get() == "name":
            friends = user.get_friends_by_sur_name(value = word, key = "name")
    elif keyword.get() == "surname":
            friends = user.get_friends_by_sur_name(value = word, key = "surname")
    elif keyword.get() == "year":
            friends = user.get_friends_by_birthyear(int(word))    
    elif keyword.get() == "college": #MORA UNIJETI KRAKTO IME
            friends = user.get_friends_by_college(word)
    elif keyword.get() == "gy":
            friends = user.get_friends_by_college_info(value = int(word), key = "graduate_year")
    else:
        friends = user.get_friends_by_college_info(value = int(word), key = "enrollment_year")
    
    if not friends:
        Label(right_frame, text="No matches found in database",
              width=20,bg="#acc4d7",
              font=("Times", 15, "bold")
              ).pack(side=LEFT, padx = 5)        
    else:
        frame = ScrollableFrame(right_frame)
        for f in friends:
            ff = Frame(frame.scrollable_frame, bg="#acc4d7")
            ff.pack(pady=15)
            Label(ff, text=f.name+" "+f.surname,
                  width=20,bg="#acc4d7",
                  font=("Times", 10)
                  ).pack(side=LEFT)
            Button(ff, text="See more",
                   bg="#547fa3", height=1, width=10,
                   command=lambda person=f, screen=screen_friends: person_info(person, screen)).pack(side=RIGHT)
            frame.pack(pady=10)

    
def add_friend(person, screen, index, b_l):
    if user.make_friendship(person) == True:
        b_l[index].configure(state=DISABLED)
        friendship_result(screen, "Friendship added. \n You and "+person.name+" "+person.surname+" are now friends!" )
    elif user.make_friendship(person) == False :
        friendship_result(screen, "You and " +person.name+" "+person.surname+" are already friends!")
    else:
        friendship_result(screen, "Error while creating")
        
# pop up window for friendships
def friendship_result(screen, message):
    global friendship_screen
    friendship_screen = Toplevel(screen)
    friendship_screen.title("Friendship")
    friendship_screen.geometry("450x100")
    friendship_screen.configure(bg='#f78383')
    Label(friendship_screen, 
          text=message, 
          font=("Times", 13, "bold"),
          bg='#f78383').pack(pady=10)
    Button(friendship_screen, text="OK",
           bg="#547fa3", 
           command=friendship_screen_delete).pack()
    
def friendship_screen_delete():
    friendship_screen.destroy() 

#----------------------------------------------------------------------------   
def person_info(person, screen):
    global person_screen
    person_screen = Toplevel(screen)
    person_screen.title("Person info")
    person_screen.geometry("650x600")
    person_screen.configure(bg='#d47474')
    Label(person_screen, 
          text="More information about person:  (resize window if needed)", 
          font=("Times", 15, "bold"),
          bg='#d47474').pack(pady=10)
    frame_g = Frame(person_screen, bg="#d47474")
    frame_g.pack(side=TOP)
    Label(frame_g, 
          text="Gender: ", 
          font=("Times", 13, "bold"),
          bg='#d47474').pack(side=LEFT)
    Label(frame_g, 
          text=person.gender, 
          font=("Times", 13),
          bg='#d47474').pack(side=RIGHT)
    frame_d = Frame(person_screen, bg="#d47474")
    frame_d.pack(side=TOP)
    Label(frame_d, 
          text="Date of birth: ", 
          font=("Times", 13, "bold"),
          bg='#d47474').pack(side=LEFT)
    Label(frame_d, 
          text=person.date_of_birth, 
          font=("Times", 13),
          bg='#d47474').pack(side=RIGHT)
    frame_c = Frame(person_screen, bg="#d47474")
    frame_c.pack(side=TOP)
    per_col, e_y, g_y, grade = person.get_attendance_info() 
    Label(frame_c, 
          text="College: ", 
          font=("Times", 13, "bold"),
          bg='#d47474').pack(side=LEFT)
    Label(frame_c, 
          text=per_col.short_name, 
          font=("Times", 13),
          bg='#d47474').pack(side=RIGHT)
    frame_bottom = Frame(person_screen, bg="#d47474")
    frame_bottom.pack(side=TOP, pady = 10)
    #college info part
    f_college_info = Frame(frame_bottom, bg="#d47474")
    f_college_info.pack(side=LEFT, padx = 15)
    Label(f_college_info, 
          text="More college info: ", 
          font=("Times", 12, "bold"),
          bg='#d47474').pack(side=TOP)
    Label(f_college_info, 
          text="Enrollment year: " + str(e_y), 
          font=("Times", 12),
          bg='#d47474').pack(side=TOP)
    Label(f_college_info, 
          text="Graduate year: " + str(g_y), 
          font=("Times", 12),
          bg='#d47474').pack(side=TOP)
    Label(f_college_info, 
          text="Grade: " + str(grade), 
          font=("Times", 12),
          bg='#d47474').pack(side=TOP)
    #skills part
    f_skills = Frame(frame_bottom, bg="#d47474")
    f_skills.pack(side=LEFT, padx = 15)
    Label(f_skills, 
              text="Skills: ", 
              font=("Times", 12, "bold"),
              bg='#d47474').pack(side=TOP)
    list_skills = person.skills
    for s in list_skills:
        Label(f_skills, 
              text=s, 
              font=("Times", 12),
              bg='#d47474').pack(side=TOP)
    #hobbies part
    f_hobbies = Frame(frame_bottom, bg="#d47474")
    f_hobbies.pack(side=LEFT, padx = 15)
    Label(f_hobbies, 
              text="Hobbies: ", 
              font=("Times", 12, "bold"),
              bg='#d47474').pack(side=TOP)
    list_hobbies = person.hobbies
    for h in list_hobbies:
        Label(f_hobbies, 
              text=h, 
              font=("Times", 12),
              bg='#d47474').pack(side=TOP)
        
    Button(person_screen, text="Hide",
           bg="#547fa3", height=1, width=10,
           command=person_screen_delete).pack(pady=30)    
def person_screen_delete():
    person_screen.destroy()    
#-------------------------------------------------------------    
def add_skills():
    
    global frame_last    
    u_name = name.get()
    if not u_name.isalpha():
        pop_up("Not valid name!")
        return
    u_surname = surname.get()
    if not u_surname.isalpha():
        pop_up("Not valid surname!")
        return
    
    check = Person.get_person_by_name_surname(u_name, u_surname)
    if check:
        pop_up("Person is in database, please log in instead!")
        return     
    u_gender = g.get()
    u_birthday = cal.get_date()    
    u_college = c.get()
    
    u_e_year = ey.get()
    if not u_e_year.isdigit():
        pop_up("Not valid enrollment year!")
        return
    u_enrollment_year = int(u_e_year)
    if int(u_birthday.split('-')[0])+18 > u_enrollment_year:
        pop_up("Not valid enrollment year! \n You need to be of legal age to start college!")
        return
    if u_enrollment_year > 2021:
        pop_up("Not valid enrollment year! \n You must be in college by now!")
        return
        
    u_g_year = gy.get()
    if not u_g_year.isdigit():
        pop_up("Not valid graduate year!")  
        return
    u_graduate_year = int(u_g_year)
    if u_graduate_year > u_enrollment_year + 10:
        pop_up("Not valid graduate year! \n You studied more than 10 years!")
        return
    if u_graduate_year < u_enrollment_year + 5:
        pop_up("Not valid graduate year! \n You studied less than 5 years!")
        return
    try:
       u_grade = float(grade.get())
       
    except ValueError:
        pop_up("Not valid format of grade! \n Make sure to write grade like x.yy!")
        return 
    
    if u_grade < 2.00 or u_grade > 5.00:
        pop_up("Not valid format of grade! \n Make sure to write grade like 2.00 <= x <= 5.00!")
        return 
    
    btn_add.destroy()
    
    #frame for skills and hobbies
    frame_last = Frame(register_screen, bg="#206b71")
    frame_last.pack(side=TOP)
    global frame_skills
    frame_skills = Frame (frame_last, bg="#206b71")
    frame_skills.pack(side=LEFT, padx = 10)
    global yscrollbar
    yscrollbar = Scrollbar(frame_last)
    yscrollbar.pack(side = LEFT, fill = Y)
    global choice_skills
    choice_skills = Listbox(frame_skills, selectmode = "multiple", 
                            yscrollcommand = yscrollbar.set)
  
    choice_skills.pack(padx = 10, pady = 10,
          expand = YES, fill = "both")
    x = College.get_all_skills_from_college(u_college)
    
    for each_item in range(len(x)):
      
        choice_skills.insert(END, x[each_item])
  

    yscrollbar.config(command = choice_skills.yview)
    global b
    b = Button(frame_last, bg="#547fa3", 
           text="Next", width=10, height=2, 
           command = lambda a1 = u_name, a2 = u_surname, 
                            a3 = u_birthday, a4 = u_gender,
                            a5 = u_college, a6 = u_enrollment_year,
                            a7 = u_graduate_year, a8 = u_grade : 
                            add_hobbies(a1, a2, a3, a4, a5, a6, a7, a8)
           )
    b.pack(side=RIGHT, pady = 10, padx=5)
    
    
def register_user(u_name, u_surname, u_birthday, u_gender, u_college, u_enrollment_year, u_graduate_year, u_grade, skills):
    #print(u_name, u_surname, u_birthday, u_gender, u_college, u_enrollment_year, u_graduate_year, u_grade, skills)
    hobbies = []
    index = choice_hobbies.curselection()
    for i in index:
        hobbies.append(choice_hobbies.get(i))
    if hobbies == []:
        pop_up("You need to choose hobbies!")
        return
    else:
        yscrollbar1.destroy()
        frame_hobbies.destroy()
        b2.destroy()
    
    #adding new person and relation is attending
    person = Person(u_name, u_surname, u_gender, datetime.date(int(u_birthday.split("-")[0]),int(u_birthday.split("-")[1]),int(u_birthday.split("-")[2])), skills, hobbies, Person.get_max_id()+1)
    person.add_person_to_db()
    person.add_to_college(u_college, u_enrollment_year, u_graduate_year, u_grade)
    pop_up("YOU ARE NOW REGISTERED. \n NOW LOGIN IN AT MAIN PAGE.")
    
# pop up window for friendships
def pop_up(message):
    global pop_screen
    pop_screen = Toplevel(register_screen)
    pop_screen.title("Error")
    pop_screen.geometry("450x100")
    pop_screen.configure(bg='#f78383')
    Label(pop_screen, 
          text=message, 
          font=("Times", 13, "bold"),
          bg='#f78383').pack(pady=10)
    Button(pop_screen, text="Try Again",
           bg="#547fa3", 
           command=pop_screen_delete).pack()
    
def pop_screen_delete():
    pop_screen.destroy() 

    
main_window()