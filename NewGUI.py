import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import NewGUI_support
dish=list()
chh=list()
cc=list()
def webp(cc):
    import pymysql.cursors
    import webbrowser
    # Connect to the database.
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='project',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    # print("connect successful!!")

    try:
        c=''.join(cc)
        with connection.cursor() as cursor:
            sqlll = "SELECT RECIPE_LINK FROM MASTER_CHEFF WHERE RECIPE_NAME=" + "'" + c + "'"
            # Execute query.
            cursor.execute(sqlll)

            print()

            for row in cursor:
                m = (row['RECIPE_LINK'])

            webbrowser.open(m)



    finally:
        # Close connection.
        connection.close()

def con2(chh):
    chh=chh[:3]
    import pymysql.cursors
    # Connect to the database.
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='project',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    # print("connect successful!!")

    try:

        with connection.cursor() as cursor:

            # SQL
            if (len(chh) == 1):
                sqll = "SELECT RECIPE_NAME,INGREDIENT1,INGREDIENT2,INGREDIENT3 from MASTER_CHEFF WHERE INGREDIENT1=" + "'" + \
                       chh[0] + "'" + " OR INGREDIENT2=" + "'" + chh[0] + "'" + " OR INGREDIENT3=" + "'" + chh[0] + "'"
            # print(sqll)
            elif (len(chh) == 2):
                sqll = "SELECT RECIPE_NAME,INGREDIENT1,INGREDIENT2,INGREDIENT3 from MASTER_CHEFF WHERE (INGREDIENT1=" + "'" + \
                       chh[0] + "'" + " OR INGREDIENT2=" + "'" + chh[0] + "'" + " OR INGREDIENT3=" + "'" + chh[
                           0] + "') AND (INGREDIENT1=" + "'" + chh[1] + "'" + " OR INGREDIENT2=" + "'" + chh[
                           1] + "'" + " OR INGREDIENT3=" + "'" + chh[1] + "')"
            elif (len(chh) == 3):
                sqll = "SELECT RECIPE_NAME,INGREDIENT1,INGREDIENT2,INGREDIENT3 from MASTER_CHEFF WHERE ((INGREDIENT1=" + "'" + \
                       chh[0] + "'" + " OR INGREDIENT2=" + "'" + chh[0] + "'" + " OR INGREDIENT3=" + "'" + chh[
                           0] + "') AND (INGREDIENT1=" + "'" + chh[1] + "'" + " OR INGREDIENT2=" + "'" + chh[
                           1] + "'" + " OR INGREDIENT3=" + "'" + chh[1] + "') AND (INGREDIENT1=" + "'" + chh[
                           2] + "'" + " OR INGREDIENT2=" + "'" + chh[2] + "'" + " OR INGREDIENT3=" + "'" + chh[
                           2] + "'))"
            # Execute query.
            if (cursor.execute(sqll) == 0):
                sqll = "SELECT RECIPE_NAME,INGREDIENT1,INGREDIENT2,INGREDIENT3 from MASTER_CHEFF WHERE INGREDIENT1=" + "'" + \
                       chh[0] + "'" + " OR INGREDIENT2=" + "'" + chh[0] + "'" + " OR INGREDIENT3=" + "'" + chh[0] + "'"
                cursor.execute(sqll)

            for row in cursor:
                print(row)
                dish.append(row['RECIPE_NAME'])
            print(dish)



            # print("cursor.description: ", cursor.description)
            # Execute query.
    finally:
        # Close connection.
        connection.close()



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    NewGUI_support.set_Tk_var()
    top = Toplevel1 (root)
    NewGUI_support.init(root, top)
    root.mainloop()

def con():
    import pymysql.cursors
    #import webbrowser
    # Connect to the database.
    l = list()
    k = list()
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='project',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    # print("connect successful!!")

    try:

        with connection.cursor() as cursor:

            # SQL
            sql = "SELECT INGREDIENT1,INGREDIENT2,INGREDIENT3 from MASTER_CHEFF"

            # Execute query.
            cursor.execute(sql)

            print()

            for row in cursor:
                # print(row)
                l.append(row["INGREDIENT1"])
                l.append(row["INGREDIENT2"])
                l.append(row["INGREDIENT3"])
            # print(l)
            for i in l:
                if (i not in k):
                    k.append(i) # k have the available material
            #print(k)
            #ch = input("Available Ingredients:  ")

            #sqll = "SELECT RECIPE_NAME,INGREDIENT1,INGREDIENT2,INGREDIENT3 from MASTER_CHEF1 WHERE INGREDIENT1=" + "'" + ch + "'" + " OR INGREDIENT2=" + "'" + ch + "'" + " OR INGREDIENT3=" + "'" + ch + "'"
            # print(sqll)

            # Execute query.
            #cursor.execute(sqll)

            # print("cursor.description: ", cursor.description)

            #print()
            return k
    finally:
        # Close connection.
        connection.close()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    NewGUI_support.set_Tk_var()
    top = Toplevel1 (w)
    NewGUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None




class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font11 = "-family {French Script MT} -size 28 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font16 = "-family Lemon -size 24 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        font17 = "-family Gabriola -size 28 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font21 = "-family MingLiU-ExtB -size 15 -weight bold -slant "  \
            "roman -underline 1 -overstrike 0"
        font23 = "-family {Comic Sans MS} -size 14 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Russo One} -size 14 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1168x950+375+0")
        top.title("MASTER CHEF")
        top.configure(background="#fffcb0")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.257, rely=0.189, relheight=0.574
                , relwidth=0.638)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#04091c")
        self.Frame1.configure(width=745)

        self.fra43_lab44 = tk.Label(self.Frame1)
        self.fra43_lab44.place(relx=0.027, rely=0.349, height=36, width=182)
        self.fra43_lab44.configure(background="#b5d8a4")
        self.fra43_lab44.configure(disabledforeground="#a3a3a3")
        self.fra43_lab44.configure(font=font9)
        self.fra43_lab44.configure(foreground="#000000")
        self.fra43_lab44.configure(text='''Ingredient 1''')
        self.fra43_lab44.configure(width=182)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.027, rely=0.532, height=36, width=182)
        self.Label1.configure(background="#ceefa7")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Ingredient 2''')
        self.Label1.configure(width=182)

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.027, rely=0.697, height=36, width=182)
        self.Label2.configure(background="#bfd8a2")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Ingredient 3''')
        self.Label2.configure(width=182)

        def callback():
            con2(z)
            button1()
        f=list()
        def returndish(event):
            f.append(self.TCombobox4.get())
            print(f)

        def button1():
            dish.append('select')
            k = tuple(dish)
            li = len(dish) - 1
            self.TCombobox4['values'] = k
            self.TCombobox4.current(li)
            self.TCombobox4.bind("<<ComboboxSelected>>", returndish)


        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.04, rely=0.862, height=53, width=386)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#ffffff")
        self.Button1.configure(background="#d81623")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font17)
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''|| Ingest Ingredients :) ||''')
        self.Button1.configure(width=386)
        self.Button1.config(command=callback)

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.04, rely=0.073, height=86, width=362)
        self.Label5.configure(background="#87ffeb")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font11)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(relief='raised')
        self.Label5.configure(text='''What do you have ??''')
        self.Label5.configure(width=362)
        z=list()
        def lcon(k):
            z.append(k)
            print(z)

        def callbackFunc(event):
            sel1=list()
            print("New Element Selected")
            #print(self.TCombobox1.get())
            sel1.append(self.TCombobox1.get())
            print(sel1)
            k=''.join(sel1)
            lcon(k)

        def callbackFunc2(event):
            sel2 = list()
            print("New Element Selected")
            # print(self.TCombobox1.get())
            sel2.append(self.TCombobox2.get())
            print(sel2)
            k=''.join(sel2)
            lcon(k)

        def callbackFunc3(event):
            sel3 = list()
            print("New Element Selected")
            # print(self.TCombobox1.get())
            sel3.append(self.TCombobox3.get())
            print(sel3)
            k=''.join(sel3)
            lcon(k)

        self.TCombobox1 = ttk.Combobox(self.Frame1)
        self.TCombobox1.place(relx=0.309, rely=0.349, relheight=0.066
                , relwidth=0.264)
        #self.TCombobox1.configure(textvariable=NewGUI_support.combobox)
        self.TCombobox1.configure(width=197)
        self.TCombobox1.configure(takefocus="")
        m1 = list()
        m1 = con()
        m1.append("select")
        ll1 = len(m1) - 1
        m1 = tuple(m1)
        self.TCombobox1['values'] = m1
        self.TCombobox1.current(ll1)
        self.TCombobox1.bind("<<ComboboxSelected>>", callbackFunc)


        self.TCombobox2 = ttk.Combobox(self.Frame1)
        self.TCombobox2.place(relx=0.309, rely=0.532, relheight=0.066
                , relwidth=0.264)
        #self.TCombobox2.configure(textvariable=NewGUI_support.combobox)
        self.TCombobox2.configure(width=197)
        self.TCombobox2.configure(takefocus="")
        m2 = list()
        m2 = con()
        m2.append("select")
        ll2 = len(m2) - 1
        m2 = tuple(m2)
        self.TCombobox2['values'] = m2
        self.TCombobox2.current(ll2)
        self.TCombobox2.bind("<<ComboboxSelected>>", callbackFunc2)

        self.TCombobox3 = ttk.Combobox(self.Frame1)
        self.TCombobox3.place(relx=0.309, rely=0.697, relheight=0.066
                , relwidth=0.264)
        #self.TCombobox3.configure(textvariable=NewGUI_support.combobox)
        self.TCombobox3.configure(width=197)
        self.TCombobox3.configure(takefocus="")
        m3 = list()
        m3 = con()
        m3.append("select")
        ll3 = len(m3) - 1
        m3 = tuple(m3)
        self.TCombobox3['values'] = m3
        self.TCombobox3.current(ll3)
        self.TCombobox3.bind("<<ComboboxSelected>>", callbackFunc3)
        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.644, rely=0.055, height=186, width=252)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self._img1 = tk.PhotoImage(file="C:/Users/Sumit Mehta/Desktop/CSE 3/PROJECT/Images_required/download (1).png")
        self.Label3.configure(image=self._img1)
        self.Label3.configure(text='''Label''')
        self.Label3.configure(width=252)

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.617, rely=0.477, height=176, width=272)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self._img2 = tk.PhotoImage(file="C:/Users/Sumit Mehta/Desktop/CSE 3/PROJECT/Images_required/rsz_1rsz_curry-05.png")
        self.Label4.configure(image=self._img2)
        self.Label4.configure(text='''Label''')
        self.Label4.configure(width=272)

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.223, rely=0.042, height=116, width=792)
        self.Label7.configure(background="#5e051a")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font16)
        self.Label7.configure(foreground="#ffffff")
        self.Label7.configure(text='''THE BELLY RULES THE MIND !! *_*''')
        self.Label7.configure(width=792)

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.026, rely=0.021, height=156, width=172)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self._img3 = tk.PhotoImage(file="C:/Users/Sumit Mehta/Desktop/CSE 3/PROJECT/Images_required/master-chef-stamp-clipart__k18629513.png")
        self.Label6.configure(image=self._img3)
        self.Label6.configure(text='''Label''')
        self.Label6.configure(width=172)

        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.009, rely=0.305, height=336, width=282)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self._img4 = tk.PhotoImage(file="C:/Users/Sumit Mehta/Desktop/CSE 3/PROJECT/Images_required/personagem-de-desenho-animado-sorridente_8250-10.png")
        self.Label8.configure(image=self._img4)
        self.Label8.configure(text='''Label''')
        self.Label8.configure(width=282)

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.257, rely=0.789, relheight=0.195
                , relwidth=0.634)
        self.Labelframe1.configure(relief='sunken')
        self.Labelframe1.configure(font=font21)
        self.Labelframe1.configure(foreground="#f0fff0")
        self.Labelframe1.configure(relief='sunken')
        self.Labelframe1.configure(text='''RECIPES FOUND''')
        self.Labelframe1.configure(background="#2b1121")
        self.Labelframe1.configure(highlightcolor="#0e1f63")
        self.Labelframe1.configure(width=740)

        self.TCombobox4 = ttk.Combobox(self.Labelframe1)
        self.TCombobox4.place(relx=0.027, rely=0.27, relheight=0.195
                , relwidth=0.834, bordermode='ignore')
        #self.TCombobox4.configure(textvariable=NewGUI_support.combobox)
        self.TCombobox4.configure(width=617)
        self.TCombobox4.configure(takefocus="")


        def webpage():
            webp(f)
        self.Button2 = tk.Button(self.Labelframe1)
        self.Button2.place(relx=0.176, rely=0.595, height=43, width=396
                , bordermode='ignore')
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#020811")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font23)
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''SHOW PROCEDURE''')
        self.Button2.configure(width=396)
        self.Button2.config(command=webpage)

if __name__ == '__main__':
    vp_start_gui()