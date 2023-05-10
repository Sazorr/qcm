from tkinter import *
from teacher import InitWindowTeacher
from students import InitWindowStudent




if __name__ == '__main__':
    home_window = Tk()
    students_window = Toplevel().wait_visibility()
    home_window.geometry("500x500")
    route_teach_btn = Button(home_window, text="Espace Formateur", width=20, height=5, command=InitWindowTeacher)
    route_student_btn = Button(home_window, text="Espace Etudiant", width=20, height=5, command=InitWindowStudent)
    route_teach_btn.pack(side=LEFT)
    route_student_btn.pack(side=RIGHT)
    home_window.mainloop()

