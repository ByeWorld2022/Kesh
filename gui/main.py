from tkinter import *
from tkinter import messagebox
<<<<<<< HEAD
from simple_facerec import SimpleFacerec
=======
>>>>>>> d188924607c97f67956a6006a796dd284e98247c
from mss import mss
import os
import shutil
import cv2


def validIPAddress(IP):
    def isIPv4(s):
        try: return str(int(s)) == s and 0 <= int(s) <= 255
        except: return False
    def isIPv6(s):
        if len(s) > 4:
            return False
        try : return int(s, 16) >= 0 and s[0] != '-'
        except:
            return False
    if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
        return "IPv4"
    if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
        return "IPv6"
    return None

def find(filename,search_path="./Admin/"):
    for root, dir, files in os.walk(search_path):
        if filename in files:
            return 1
    return 0

class MainWindow():

    def __init__(self,root, title, size):
        self.root = root
        self.title = title
        self.size = size
        self.root.title(self.title)
        self.root.geometry(self.size)
        self.root.resizable(False,False)

        self.bg = PhotoImage(file="./images/b1.png")
        Label(self.root,image=self.bg).pack(fill="both",expand="yes")

        self.frame = Frame(self.root,bg="misty rose",width='950',height=570).place(x=100,y=70)

        self.side_img2 = PhotoImage(file="./images/ip.png")
        Label(self.frame,image=self.side_img2,bg="misty rose").place(x=450,y=100)

        self.ip = Label(self.frame,text="IP Address :",bg="misty rose",font=("yu gothic ui", 18, "bold")).place(x=350,y=400)

        self.iptext = Entry(self.frame,relief = "flat",font=("yu gothic ui", 15))
        self.iptext.insert(0, "192.168.1.1")
        self.iptext.configure(state=DISABLED)
        self.iptext.place(x=550,y=400)
        self.on_click_id = self.iptext.bind('<Button-1>', self.on_click)

        self.enterButton = Button(self.frame,text = "Enter",font=("yu gothic ui", 18, "bold"),cursor = "hand2",command = self.enter).place(x=530,y=470)

    def on_click(self,event):
        self.iptext.configure(state=NORMAL)
        self.iptext.delete(0, END)
        self.iptext.unbind('<Button-1>', self.on_click_id)

    def enter(self):
        IP = self.iptext.get()
        self.iptext.delete(0,END)
        if not validIPAddress(IP):
            messagebox.showerror("Error", "Invalid IP Address")
        else:
            self.root.destroy()  
            loginWindow = Tk() 
            obj = LoginWindow(loginWindow,"Face Recognition", "1166x718",IP)   
            loginWindow.mainloop()


class LoginWindow():

    def __init__(self, root, title, size,IP):
        self.ip = IP
        self.root = root
        self.title = title
        self.size = size
        self.root.title(self.title)
        self.root.geometry(self.size)
        self.root.resizable(False,False)

        self.bg = PhotoImage(file="./images/b1.png")
        Label(self.root,image=self.bg).pack(fill="both",expand="yes")

        self.frame = Frame(self.root,bg="PeachPuff3",width='950',height=570).place(x=100,y=70)

        self.user = PhotoImage(file="./images/user.png")
        Label(self.frame,image=self.user,bg="PeachPuff3").place(x=430,y=130)

        self.loginButton = Button(self.frame,text = "Login",font=("yu gothic ui", 25, "bold"),cursor = "hand2",command = self.login).place(x=420,y=480)
        self.regButton = Button(self.frame,text = "Register",font=("yu gothic ui", 25, "bold"),cursor = "hand2",command = self.register).place(x=560,y=480)


    def login(self):
        #cap = cv2.VideoCapture('rtsp://{}/1'.format(self.ip))
        cap=cv2.VideoCapture(0)
        #take all pics from admins
        sfr=SimpleFacerec()
        sfr.load_encoding_images("./Admin")

        while True:
            ret,frame = cap.read()
            
            #detect face
            face_locations,face_names=sfr.detect_known_faces(frame)
            for loc,name in zip(face_locations,face_names):
                y1,x1,y2,x2=loc[0],loc[1],loc[2],loc[3]
                cv2.putText(frame,name,(x1,y1-10),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,200),2)

            cv2.imshow("Auth",frame)
            key=cv2.waitKey(1)


            if key==27:
                break
        cap.release()
        cv2.destroyAllWindows()

        for name in face_names:
            if name != "Unknown":
                messagebox.showinfo("INFO","Successfully logged in!")
                return
        messagebox.showwarning("Warning","Invalid User!")
        self.root.destroy() 
        mainWindow = Tk()
        mainFenster = MainWindow(mainWindow, "Face Recognition", "1166x718")
        mainWindow.mainloop()


    def register(self):
        self.root.destroy() 
        regWindow = Tk() 
        obj = RegWindow(regWindow,"Face Recognition", "1166x718",self.ip) 
        regWindow.mainloop()

class RegWindow():

    def __init__(self, root, title, size, IP):
        self.ip = IP
        self.root = root
        self.title = title
        self.size = size
        self.root.title(self.title)
        self.root.geometry(self.size)
        self.root.resizable(False,False)

        self.bg = PhotoImage(file="./images/b1.png")
        Label(self.root,image=self.bg).pack(fill="both",expand="yes")

        self.frame = Frame(self.root,bg="PeachPuff3",width='950',height=570).place(x=100,y=70)

        self.name = Label(self.frame,text="Username",bg="PeachPuff3",font=("yu gothic ui", 18, "bold")).place(x=350,y=200)

        self.nameEntry = Entry(self.frame,relief = "flat",font=("yu gothic ui", 18))
        self.nameEntry.place(x=550,y=200)

        self.preference = Label(self.frame,text="Preference",bg="PeachPuff3",font=("yu gothic ui", 18, "bold")).place(x=350,y=280)

        self.v = StringVar(self.frame)
        values = {"Right-handed" : "1","Left-handed" : "2"}
        
        i=0
        for (text, value) in values.items():
            Radiobutton(self.frame, text = text, variable = self.v,value = value,font=("yu gothic ui", 18)).place(x=550+i,y=280)
            i+=230

        self.click = 0
        self.img = Label(self.frame,text="Upload photo",bg="PeachPuff3",font=("yu gothic ui", 18, "bold")).place(x=350,y=360)
        Button(self.frame,text = "Take Screenshot",font=("yu gothic ui", 18,),cursor = "hand2",command = self.screenshot).place(x=550,y=360)

        self.regButton = Button(self.frame,text = "Register",font=("yu gothic ui", 18, "bold"),cursor = "hand2",command = self.register).place(x=530,y=470)

    def register(self):
        loop = 1
        name = self.nameEntry.get()
        prefer = self.v.get()
        if not name:
            messagebox.showerror("Error", "Enter user name!")
        elif find(name+".jpg"):
            messagebox.showerror("Error", "User name already exists!")
        elif not prefer:
            messagebox.showerror("Error", "Enter your preference!")
        elif not self.click:
            messagebox.showerror("Error", "Screenshot not taken!")
        else:
            src = "./{}.jpg".format(name)
            dest = "./Admin/{}.jpg".format(name)
            shutil.move(src, dest)

            messagebox.showinfo("Success", "Registered successfully!")
            self.root.destroy() 
            mainWindow = Tk()
            mainFenster = MainWindow(mainWindow, "Face Recognition", "1166x718")
            mainWindow.mainloop()
            loop = 0
        # If it's not in mainloop
        if loop:
            self.nameEntry.delete(0,END)
            self.v.set(None)
            self.click = 0
            if os.path.exists("./{}.jpg".format(name)):
                os.remove("./{}.jpg".format(name))

    def screenshot(self):
        cap=cv2.VideoCapture(0)
        while True:
            ret,frame=cap.read()
            cv2.putText(frame, 'Press escape button to capture your picture!',(5, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 255, 0),2,cv2.LINE_AA)
            cv2.imshow("Auth",frame)
            key=cv2.waitKey(1)

            if key==27:
                cap.release()
                cv2.destroyAllWindows()
                name = self.nameEntry.get()
                if name:
                    path = "./{}.jpg".format(name)
                    with mss() as sct:
                        filename = sct.shot(output=path)
                    messagebox.showinfo("Success", "Screenshot saved!")
                    self.click = 1
                else:
                    messagebox.showwarning("Warning", "Username not entered!")
                break


if __name__ == "__main__":
    mainWindow = Tk()
    mainFenster = MainWindow(mainWindow, "Face Recognition", "1166x718")
<<<<<<< HEAD
    mainWindow.mainloop()
=======
    mainWindow.mainloop()
    #cap.release()
    #cv2.destroyAllWindows()
>>>>>>> d188924607c97f67956a6006a796dd284e98247c
