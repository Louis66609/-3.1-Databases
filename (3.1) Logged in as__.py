import customtkinter as ctk
import tkinter
import sqlite3
import os
import re

custom_font = ('Roboto', 20)
default_theme = "dark-blue"
default_appearance = "system"

def Create_Window(title):
    global window
    window = ctk.CTk()
    window.geometry("1400x800")
    window.resizable(width=False, height=False)
    Center_Window()
    frame = Create_Frame()
    window.wm_title(title)
    return window, frame 

def Center_Window():
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 1400
    window_height = 800
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

def Create_Frame():
    frame = ctk.CTkFrame(master=window, width=750, height=600)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    return frame

def Load_Page(Null, page_type):
    global window
    if window:
        window.destroy()
    else:
        Login_Page()

    if page_type == "admin_registration_page":
        Admin_Registration_Page()
    elif page_type == "employee_registration_page":
        Employee_Registration_Page()
    elif page_type == "settings":
        Settings_Page()
    elif page_type == "admin_main_page":
        Admin_Main_Page()
    elif page_type == "employee_main_page":
        Employee_Main_Page()
    elif page_type == "invalid_details_page":
        Invalid_Details_Page()
    elif page_type == "successful_registration_page":
        Successful_Registration_Page()
    else:
        Login_Page()

def Login_Page():
    LogPg_window, LogPg_frame = Create_Window("Login Page")

    LogPg_admin_txt = ctk.CTkLabel(master=LogPg_frame, text="Login as Admin:", font=('Roboto', 25))
    LogPg_admin_txt.place(x=85, y=50)

    LogPg_employee_txt = ctk.CTkLabel(master=LogPg_frame, text="Login as Employee:", font=('Roboto', 25))
    LogPg_employee_txt.place(x=450, y=50)

    LogPg_register_txt_1 = ctk.CTkLabel(master=LogPg_frame, font=('Roboto', 19), text="Don't have an account?   Register here as an")
    LogPg_register_txt_1.place(x=15, y=565)
    
    LogPg_register_txt_1 = ctk.CTkLabel(master=LogPg_frame, text="Or an", font=('Roboto', 18))
    LogPg_register_txt_1.place(x=535, y=565)

    LogPg_admin_underline = ctk.CTkButton(master=LogPg_frame, width=190, height=3, corner_radius=0, text="")
    LogPg_admin_underline.place(x=78, y=80)
 
    LogPg_employee_underline = ctk.CTkButton(master=LogPg_frame, width=230, height=3, corner_radius=0, text="")
    LogPg_employee_underline.place(x=442, y=80)

    LogPG_companyname_entry = ctk.CTkEntry(master=LogPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Company Name...')
    LogPG_companyname_entry.place(x=43, y=140)

    LogPG_admin_password_entry = ctk.CTkEntry(master=LogPg_frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Enter Password...')
    LogPG_admin_password_entry.place(x=43, y=260)

    LogPg_admin_lastname_entry = ctk.CTkEntry(master=LogPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Last Name...')
    LogPg_admin_lastname_entry.place(x=428, y=140)

    LogPg_employee_password_entry = ctk.CTkEntry(master=LogPg_frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Enter Password...')
    LogPg_employee_password_entry.place(x=428, y=260)
    
    LogPg_admin_login_button = ctk.CTkButton(master=LogPg_frame, width=200, text="Login", font=('Roboto', 15), corner_radius=20)
    LogPg_admin_login_button.configure(command=lambda: Login(LogPG_companyname_entry.get(), None, LogPG_admin_password_entry.get()))
    LogPg_admin_login_button.place(x=75, y=350)

    LogPg_employee_login_button = ctk.CTkButton(master=LogPg_frame, width=200, text="Login", font=('Roboto', 15), corner_radius=20)
    LogPg_employee_login_button.configure(command=lambda: Login(None, LogPg_admin_lastname_entry.get(), LogPg_employee_password_entry.get()))
    LogPg_employee_login_button.place(x=460, y=350)

    LogPg_settings_button = ctk.CTkButton(master=LogPg_frame, width=100, corner_radius=20, text="Settings", font=('Roboto', 15))
    LogPg_settings_button.configure(command=lambda:Load_Page(LogPg_window, "settings"))
    LogPg_settings_button.place(x=645, y=5)
    
    LogPg_refresh_button = ctk.CTkButton(master=LogPg_frame, width=100, corner_radius=20, text="Refresh Page", font=('Roboto', 15))
    LogPg_refresh_button.configure(command=lambda: Load_Page(LogPg_window, "login"))
    LogPg_refresh_button.place(x=5, y=5)
    
    LogPg_employee_register_button = ctk.CTkButton(master=LogPg_frame, width=115, text="Employee", corner_radius=20, font=('Roboto', 15))
    LogPg_employee_register_button.configure(command=lambda: Load_Page(LogPg_window, "employee_registration_page"))
    LogPg_employee_register_button.place(x=610, y=565)
    
    LogPg_admin_register_button = ctk.CTkButton(master=LogPg_frame, width=115, text="Admin", corner_radius=20, font=('Roboto', 15))
    LogPg_admin_register_button.configure(command=lambda: Load_Page(LogPg_window, "admin_registration_page"))
    LogPg_admin_register_button.place(x=400, y=565)

    LogPg_window.mainloop()

def Admin_Registration_Page():
    AdPg_window, AdPg_frame = Create_Window("Admin Registration")

    AdPg_txt = ctk.CTkLabel(master=AdPg_frame, text="Admin Registration:", font=('Roboto', 25))
    AdPg_txt.place(x=260, y=50)

    AdPg_underline = ctk.CTkButton(master=AdPg_frame, width=230, height=3, corner_radius=0, text="")
    AdPg_underline.place(x=250, y=80)

    AdPg_firstname_entry = ctk.CTkEntry(master=AdPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter First Name...')
    AdPg_firstname_entry.place(x=73, y=150)

    AdPg_lastname_entry = ctk.CTkEntry(master=AdPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Last Name...')
    AdPg_lastname_entry.place(x=408, y=150)

    AdPg_password_entry = ctk.CTkEntry(master=AdPg_frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Enter Password...')
    AdPg_password_entry.place(x=73, y=315)

    AdPg_confirmpassword_entry = ctk.CTkEntry(master=AdPg_frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Confirm Password...')
    AdPg_confirmpassword_entry.place(x=408, y=315)

    AdPg_companyname_entry = ctk.CTkEntry(master=AdPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Company Name...')
    AdPg_companyname_entry.place(x=73, y=430)

    AdPg_companyid_entry = ctk.CTkEntry(master=AdPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Create 8 Digit Company ID...')
    AdPg_companyid_entry.place(x=408, y=430)

    AdPg_register_button = ctk.CTkButton(master=AdPg_frame, width=200, text="Register for an account", font=('Roboto', 18), corner_radius=20)
    AdPg_register_button.configure(command=lambda: Get_Details(AdPg_firstname_entry, AdPg_lastname_entry, AdPg_password_entry, AdPg_confirmpassword_entry, AdPg_companyname_entry, None, AdPg_companyid_entry, "admin"))
    AdPg_register_button.place(x=260, y=525)
    
    AdPg_refresh_button = ctk.CTkButton(master=AdPg_frame, width=100, text="Refresh Page", font=('Roboto', 15), corner_radius=20)
    AdPg_refresh_button.configure(command=lambda: Load_Page(AdPg_window, "admin"))
    AdPg_refresh_button.place(x=5, y=5)
    
    AdPg_return_button = ctk.CTkButton(master=AdPg_frame, width=100, corner_radius=20, text="Return", font=('Roboto', 15))
    AdPg_return_button.configure(command=lambda: Load_Page(AdPg_window, "login"))
    AdPg_return_button.place(x=645, y=5)
    
    AdPg_window.mainloop()

def Employee_Registration_Page():
    EmpPg_window, EmpPg_frame = Create_Window("Employee Registration")

    EmpPg_txt = ctk.CTkLabel(master=EmpPg_frame, text="Employee Registration:", font=('Roboto', 25))
    EmpPg_txt.place(x=260, y=50)

    EmpPg_underline = ctk.CTkButton(master=EmpPg_frame, width=270, height=3, corner_radius=0, text="")
    EmpPg_underline.place(x=253, y=80)

    EmpPg_firstname_entry = ctk.CTkEntry(master=EmpPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter First Name...')
    EmpPg_firstname_entry.place(x=73, y=150)

    EmpPg_lastname_entry = ctk.CTkEntry(master=EmpPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Last Name...')
    EmpPg_lastname_entry.place(x=408, y=150)

    EmpPg_password_entry = ctk.CTkEntry(master=EmpPg_frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Enter Password...')
    EmpPg_password_entry.place(x=73, y=295)

    EmpPg_confirmpassword_entry = ctk.CTkEntry(master=EmpPg_frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Confirm Password...')
    EmpPg_confirmpassword_entry.place(x=408, y=295)

    EmpPg_companyname_entry = ctk.CTkEntry(master=EmpPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Company Name...')
    EmpPg_companyname_entry.place(x=73, y=430)

    EmpPg_companyid_entry = ctk.CTkEntry(master=EmpPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Valid Company ID...')
    EmpPg_companyid_entry.place(x=408, y=430)

    EmpPg_registration_button = ctk.CTkButton(master=EmpPg_frame, width=200, text="Register for an account", font=('Roboto', 18), corner_radius=20)
    EmpPg_registration_button.configure(command=lambda: Get_Details(EmpPg_firstname_entry, EmpPg_lastname_entry, EmpPg_password_entry, EmpPg_confirmpassword_entry, EmpPg_companyname_entry, EmpPg_companyid_entry, None, "employee"))
    EmpPg_registration_button.place(x=260, y=525)

    EmpPg_refresh_button = ctk.CTkButton(master=EmpPg_frame, width=100, text="Refresh Page", font=('Roboto', 15), corner_radius=20)
    EmpPg_refresh_button.configure(command=lambda: Load_Page(EmpPg_window, "employee"))
    EmpPg_refresh_button.place(x=5, y=5)
    
    EmpPg_return_button = ctk.CTkButton(master=EmpPg_frame, width=100, corner_radius=20, text="Return", font=('Roboto', 15))
    EmpPg_return_button.configure(command=lambda: Load_Page(EmpPg_window, "login"))
    EmpPg_return_button.place(x=645, y=5)
    
    EmpPg_window.mainloop()

def Settings_Page():
    SetPg_window, SetPg_frame = Create_Window("Settings")

    SetPg_txt = ctk.CTkLabel(master=SetPg_frame, text="Change colour scheme:", font=('Roboto', 30))
    SetPg_txt.place(x=220, y=75)

    SetPg_underline = ctk.CTkButton(master=SetPg_frame, width=330, height=3, corner_radius=0, text="")
    SetPg_underline.place(x=213, y=110)

    SetPg_theme_dropdownmenu = ctk.CTkComboBox(master=SetPg_frame,justify="center", values=["green", "dark-blue", "blue"], width=250, font=('Roboto', 20))
    SetPg_theme_dropdownmenu.set("Set Theme...")
    SetPg_theme_dropdownmenu.place(x=75, y=250)

    SetPg_appearance_dropdownmenu = ctk.CTkComboBox(master=SetPg_frame,justify="center", values=["light", "dark", "system"], width=250, font=('Roboto', 20))
    SetPg_appearance_dropdownmenu.set("Set Appearance Mode...")
    SetPg_appearance_dropdownmenu.place(x=425, y=250)

    SetPg_confirm_button = ctk.CTkButton(master=SetPg_frame, width=250, corner_radius=20, text="Confirm changes", font=('Roboto', 20))
    SetPg_confirm_button.configure(command=lambda: Confirm_Colour(SetPg_theme_dropdownmenu, SetPg_appearance_dropdownmenu,SetPg_window))
    SetPg_confirm_button.place(x=260, y=390)

    SetPg_return_button = ctk.CTkButton(master=SetPg_frame, width=100, corner_radius=20, text="Return", font=('Roboto', 15))
    SetPg_return_button.configure(command=lambda: Load_Page(SetPg_window, "login"))
    SetPg_return_button.place(x=645, y=5)

    SetPg_exit_button = ctk.CTkButton(master=SetPg_frame, width=250, corner_radius=20, text="Exit System", font=('Roboto', 20))
    SetPg_exit_button.configure(command=lambda: SetPg_window.destroy())
    SetPg_exit_button.place(x=260, y=505)

    SetPg_window.mainloop()

def Load_Saved_Colour_Changes(default_theme, default_appearance):
    saved_theme = default_theme
    saved_appearance = default_appearance
    
    if os.path.exists('saved_colour_changes.py'):
        with open('saved_colour_changes.py', 'r') as file:
            saved_colour_changes = file.read()
        try:
            saved_theme = re.search(r"Saved_Theme = '([^']*)'", saved_colour_changes).group(1)
            saved_appearance = re.search(r"Saved_Appearance = '([^']*)'", saved_colour_changes).group(1)
        except AttributeError:
            pass
    
    ctk.set_default_color_theme(saved_theme)
    ctk.set_appearance_mode(saved_appearance)

def Confirm_Colour(SetPg_theme_dropdownmenu, SetPg_appearance_dropdownmenu, SetPg_window):
    selected_theme = SetPg_theme_dropdownmenu.get()
    selected_appearance = SetPg_appearance_dropdownmenu.get()

    ctk.set_default_color_theme(selected_theme)
    ctk.set_appearance_mode(selected_appearance)

    with open('saved_colour_changes.py', 'w') as file:
        file.write(f"Saved_Theme = '{selected_theme}'\n")
        file.write(f"Saved_Appearance = '{selected_appearance}'\n")

    Load_Page(SetPg_window, "settings")

def Admin_Main_Page():
    AdMainPg_window, AdMainPg_frame = Create_Window("Admin Main Page")

    AdMainPg_tabview = ctk.CTkTabview(AdMainPg_frame, width=850, height=615, corner_radius=15)
    AdMainPg_tabview.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    AdMainPg_tab_names = ["Overview", "View Employee", "Settings", "Exit"]
    for tab_name in AdMainPg_tab_names:
        AdMainPg_tabview.add(tab_name)
        
    AdMainPg_tabview._segmented_button.configure(font=custom_font,height=40)

    AdMainPg_return_button = ctk.CTkButton(AdMainPg_tabview.tab("Exit"), width=250, corner_radius=20, text="Return To Login Page", font=('Roboto', 22))
    AdMainPg_return_button.configure(command=lambda: Load_Page(AdMainPg_window, "login"))
    AdMainPg_return_button.place(x=100, y=225)

    AdMainPg_LoggedInAs_Text = ctk.CTkLabel(AdMainPg_tabview, text="Logged In as: " + logged_in_as, font=('Roboto', 14))
    AdMainPg_LoggedInAs_Text.place(x=60, y=20)

    AdMainPg_exit_button = ctk.CTkButton(AdMainPg_tabview.tab("Exit"), width=250, corner_radius=20, text="Exit System", font=('Roboto', 22))
    AdMainPg_exit_button.configure(command=lambda: AdMainPg_window.destroy())
    AdMainPg_exit_button.place(x=475, y=225)

    AdMainPg_window.mainloop()

def Employee_Main_Page():
    EmpMainPg_window, EmpMainPg_frame = Create_Window("Employee Main Page")

    EmpMainPg_tabview = ctk.CTkTabview(EmpMainPg_frame, width=850, height=615, corner_radius=15)
    EmpMainPg_tabview.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    EmpMainPg_tab_names = ["Overview", "Live Feed", "Settings", "Exit"]
    for tab_name in EmpMainPg_tab_names:
        EmpMainPg_tabview.add(tab_name)

    EmpMainPg_tabview._segmented_button.configure(font=custom_font, height=40)

    EmpMainPg_return_button = ctk.CTkButton(EmpMainPg_tabview.tab("Exit"), width=250, corner_radius=20, text="Return To Login Page", font=('Roboto', 22))
    EmpMainPg_return_button.configure(command=lambda: Load_Page(EmpMainPg_window, "login"))
    EmpMainPg_return_button.place(x=100, y=225)

    EmpMainPg_LoggedInAs_Text = ctk.CTkLabel(EmpMainPg_tabview, text="Logged In as: " + logged_in_as, font=('Roboto', 14))
    EmpMainPg_LoggedInAs_Text.place(x=60, y=20)

    EmpMainPg_exit_button = ctk.CTkButton(EmpMainPg_tabview.tab("Exit"), width=250, corner_radius=20, text="Exit System", font=('Roboto', 22))
    EmpMainPg_exit_button.configure(command=lambda: EmpMainPg_window.destroy())
    EmpMainPg_exit_button.place(x=475, y=225)

    EmpMainPg_window.mainloop()

def Invalid_Details_Page():
    InvDePg_window, InvDePg_frame = Create_Window("Invalid Details")

    InvDePg_txt1 = ctk.CTkLabel(master=InvDePg_frame, text="Errenous Detials:", font=('Roboto', 30))
    InvDePg_txt1.place(x=250, y=75)

    InvDePg_underline = ctk.CTkButton(master=InvDePg_frame, width=225, height=3, corner_radius=0, text="")
    InvDePg_underline.place(x=250, y=110)

    InvDePg_txt2 = ctk.CTkLabel(master=InvDePg_frame, text="The details entered were invalid, please try again!", font=('Roboto', 20))
    InvDePg_txt2.place(x=150, y=250)

    InvDePg_return_button = ctk.CTkButton(master=InvDePg_frame, width=100, corner_radius=20, text="Return", font=('Roboto', 30))
    InvDePg_return_button.configure(command=lambda: Load_Page(InvDePg_window, "login"))
    InvDePg_return_button.place(x=300, y=400)

    InvDePg_window.mainloop()

def Successful_Registration_Page():
    SuccRegPg_window, SuccRegPg_frame = Create_Window("Invalid Details")

    SuccRegPg_txt1 = ctk.CTkLabel(master=SuccRegPg_frame, text="Succesful Registration!", font=('Roboto', 30))
    SuccRegPg_txt1.place(x=220, y=75)

    SuccRegPg_underline = ctk.CTkButton(master=SuccRegPg_frame, width=310, height=3, corner_radius=0, text="")
    SuccRegPg_underline.place(x=218, y=110)

    SuccRegPg_txt2 = ctk.CTkLabel(master=SuccRegPg_frame, text="Thank you for registering an account with us, welcome to the team!", font=('Roboto', 20))
    SuccRegPg_txt2.place(x=80, y=250)

    SuccRegPg_return_button = ctk.CTkButton(master=SuccRegPg_frame, width=100, corner_radius=20, text="Return to login page", font=('Roboto', 30))
    SuccRegPg_return_button.configure(command=lambda: Load_Page(SuccRegPg_window, "login"))
    SuccRegPg_return_button.place(x=230, y=400)

    SuccRegPg_window.mainloop()

def Get_Details(firstname_entry, lastname_entry, password_entry, confirmpassword_entry, companyname_entry, EmpPg_companyid_entry, AdPg_companyid_entry, user_type):
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    password = password_entry.get()
    confirmpassword = confirmpassword_entry.get()
    companyname = companyname_entry.get()
    
    if EmpPg_companyid_entry:
        emppgcompanyid = EmpPg_companyid_entry.get()
    else:
        emppgcompanyid = None

    if AdPg_companyid_entry:
        adpgcompanyid = AdPg_companyid_entry.get()
    else:
        adpgcompanyid = None

    if Verify_Details(firstname, lastname, password, confirmpassword, companyname, adpgcompanyid, emppgcompanyid):
        Write_User_Details_To_File(firstname, lastname, password, companyname, adpgcompanyid, emppgcompanyid, user_type)
        window.destroy()
        Load_Page(window, Successful_Registration_Page())
    else:
        window.destroy()
        Load_Page(window, Invalid_Details_Page())    

def Verify_Details(firstname, lastname, password, confirmpassword, companyname, adpgcompanyid, emppgcompanyid):
    
    if len(firstname) < 1 or len(lastname) < 1 or len(password) < 1 or len(confirmpassword) < 1 or len(companyname) < 1:
        return False
    
    if password != confirmpassword:
        return False
    
    if adpgcompanyid is not None and len(adpgcompanyid) != 8:
        return False
    if emppgcompanyid is not None and len(emppgcompanyid) != 8:
        return False
        
    for entry in [firstname, lastname, password, confirmpassword, companyname, str(adpgcompanyid), str(emppgcompanyid)]:
        if not entry.isalnum():
            return False
        
    with sqlite3.connect("EmployeeDetails.db") as connection:
        cursor = connection.cursor()
        # Check for existing details (excluding company ID)
        cursor.execute("SELECT * FROM Users WHERE FirstName = ? AND LastName = ? AND Password = ? AND CompanyName = ?", (firstname, lastname, password, companyname))
        match = cursor.fetchone()
        if match:
            return False  # Details already exist
    
        if emppgcompanyid is not None:
            cursor.execute("SELECT CompanyID FROM Users WHERE CompanyID = ?", (emppgcompanyid,))
            match = cursor.fetchone()
            if not match:
                return False  # Company ID does not exist
    
    return True
    
def Write_User_Details_To_File(firstname, lastname, password, companyname, adpgcompanyid, emppgcompanyid, user_type):
    if adpgcompanyid:
        uniquecompid = adpgcompanyid
    elif emppgcompanyid:
        uniquecompid = emppgcompanyid

    # Connect to DB (or create file if not exist)
    with sqlite3.connect("EmployeeDetails.db") as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Users (FirstName TEXT, LastName TEXT, Password TEXT, CompanyName TEXT, CompanyID INTEGER, UserType TEXT)")

        # Determine the user type based on the provided argument
        if user_type.lower() == 'admin':
            user_type = 'admin'
        else:
            user_type = 'employee'

        # Explicitly specify column names in the INSERT statement
        cursor.execute("INSERT INTO Users (FirstName, LastName, Password, CompanyName, CompanyID, UserType) VALUES (?, ?, ?, ?, ?, ?)",
                       (firstname, lastname, password, companyname, uniquecompid, user_type))
        connection.commit()

def Login(companyname, lastname, password):
    global logged_in_as
    with sqlite3.connect("EmployeeDetails.db") as connection:
        cursor = connection.cursor()

        if companyname:  # If companyname exists (admin login)
            # Check if admin credentials match
            cursor.execute("SELECT * FROM Users WHERE CompanyName = ? AND Password = ?", (companyname, password))
            match = cursor.fetchone()
            if match:
                user_type = match[-1]  # Get the UserType column value
                if user_type.lower() == 'admin':
                    logged_in_as = (companyname)
                    Load_Page(window, "admin_main_page")
                else:
                    Load_Page(window, "invalid_details_page")
            else:
                Load_Page(window, "invalid_details_page")

        else:  # If companyname doesn't exist (employee login)
            # Check if employee credentials match
            cursor.execute("SELECT * FROM Users WHERE LastName = ? AND Password = ?", (lastname, password))
            match = cursor.fetchone()
            if match:
                user_type = match[-1]  # Get the UserType column value
                if user_type.lower() == 'employee':
                    logged_in_as = (lastname)
                    Load_Page(window, "employee_main_page")
                else:
                    Load_Page(window, "invalid_details_page")
            else:
                Load_Page(window, "invalid_details_page")


if __name__ == "__main__":
    Load_Saved_Colour_Changes(default_theme, default_appearance)
    Login_Page()