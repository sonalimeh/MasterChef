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

import secGUI_support

l1=list()
l2=list()
l3=list()
l4=list()
l5=list()
l6=list()
l7=list()
l8=list()
l9=list()
l10=list()

def weather():
    import datetime
    import json
    import urllib.request

    def time_converter(time):
        converted_time = datetime.datetime.fromtimestamp(
            int(time)
        ).strftime('%I:%M %p')
        return converted_time

    def url_builder(city_id):
        user_api = 'ee2ab3d5072901ba8e27fa048b3f51f6'  # Obtain yours form: http://openweathermap.org/
        unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
        api = 'http://api.openweathermap.org/data/2.5/weather?id=1273294'  # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz

        full_api_url = 'http://api.openweathermap.org/data/2.5/weather?id=1273294&appid=ee2ab3d5072901ba8e27fa048b3f51f6'
        return full_api_url

    def data_fetch(full_api_url):
        url = urllib.request.urlopen(full_api_url)
        output = url.read().decode('utf-8')
        raw_api_dict = json.loads(output)
        url.close()
        return raw_api_dict

    def data_organizer(raw_api_dict):
        data = dict(
            city=raw_api_dict.get('name'),
            country=raw_api_dict.get('sys').get('country'),
            temp=raw_api_dict.get('main').get('temp'),
            temp_max=raw_api_dict.get('main').get('temp_max'),
            temp_min=raw_api_dict.get('main').get('temp_min'),
            humidity=raw_api_dict.get('main').get('humidity'),
            pressure=raw_api_dict.get('main').get('pressure'),
            sky=raw_api_dict['weather'][0]['main'],
            sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
            sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
            wind=raw_api_dict.get('wind').get('speed'),
            wind_deg=raw_api_dict.get('deg'),
            dt=time_converter(raw_api_dict.get('dt')),
            cloudiness=raw_api_dict.get('clouds').get('all')
        )
        return data

    def data_output(data):
        m_symbol = '\xb0' + 'C'
        f = data['temp']
        f = f - 273
        l1.append('---------------------------------------')
        l2.append('Current weather in: {}, {}:'.format(data['city'], data['country']))
        l3.append(str(f) + ' ' + m_symbol + ' ' + data['sky'])
        # l4.append('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
        l4.append('')
        # print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
        l5.append('Humidity: {}'.format(data['humidity']))
        l6.append('Cloud: {}'.format(data['cloudiness']))
        l7.append('Pressure: {}'.format(data['pressure']))
        # print('Sunrise at: {}'.format(data['sunrise']))
        # print('Sunset at: {}'.format(data['sunset']))
        l8.append('')
        l9.append('Last update from the server: {}'.format(data['dt']))
        l10.append('---------------------------------------')

    if __name__ == '__main__':
        data_output(data_organizer(data_fetch(url_builder(2172797))))

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

def ranselect():
    import pymysql.cursors
    import webbrowser
    # Connect to the database.
    import random
    l1 = list()
    l2 = list()
    l3 = list()
    l4 = list()
    l5 = list()
    l6 = list()
    l7 = list()
    l8 = list()
    l9 = list()
    l10 = list()
    hum = list()

    def weather():
        import datetime
        import json
        import urllib.request

        def time_converter(time):
            converted_time = datetime.datetime.fromtimestamp(
                int(time)
            ).strftime('%I:%M %p')
            return converted_time

        def url_builder(city_id):
            user_api = 'ee2ab3d5072901ba8e27fa048b3f51f6'  # Obtain yours form: http://openweathermap.org/
            unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
            api = 'http://api.openweathermap.org/data/2.5/weather?id=1273294'  # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz

            full_api_url = 'http://api.openweathermap.org/data/2.5/weather?id=1273294&appid=ee2ab3d5072901ba8e27fa048b3f51f6'
            return full_api_url

        def data_fetch(full_api_url):
            url = urllib.request.urlopen(full_api_url)
            output = url.read().decode('utf-8')
            raw_api_dict = json.loads(output)
            url.close()
            return raw_api_dict

        def data_organizer(raw_api_dict):
            data = dict(
                city=raw_api_dict.get('name'),
                country=raw_api_dict.get('sys').get('country'),
                temp=raw_api_dict.get('main').get('temp'),
                temp_max=raw_api_dict.get('main').get('temp_max'),
                temp_min=raw_api_dict.get('main').get('temp_min'),
                humidity=raw_api_dict.get('main').get('humidity'),
                pressure=raw_api_dict.get('main').get('pressure'),
                sky=raw_api_dict['weather'][0]['main'],
                sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
                sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
                wind=raw_api_dict.get('wind').get('speed'),
                wind_deg=raw_api_dict.get('deg'),
                dt=time_converter(raw_api_dict.get('dt')),
                cloudiness=raw_api_dict.get('clouds').get('all')
            )
            return data

        def data_output(data):
            m_symbol = '\xb0' + 'C'
            f = data['temp']
            hum.append(data['humidity'])
            f = f - 273
            l1.append('---------------------------------------')
            l2.append('Current weather in: {}, {}:'.format(data['city'], data['country']))
            l3.append(str(f) + ' ' + m_symbol + ' ' + data['sky'])
            # l4.append('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
            l4.append('')
            # print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
            l5.append('Humidity: {}'.format(data['humidity']))
            l6.append('Cloud: {}'.format(data['cloudiness']))
            l7.append('Pressure: {}'.format(data['pressure']))
            # print('Sunrise at: {}'.format(data['sunrise']))
            # print('Sunset at: {}'.format(data['sunset']))
            l8.append('')
            l9.append('Last update from the server: {}'.format(data['dt']))
            l10.append('---------------------------------------')
            return f

        if __name__ == '__main__':
            z = data_output(data_organizer(data_fetch(url_builder(2172797))))
            return z

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
            sql = "SELECT RECIPE_NAME,CLIMATE from MASTER_CHEFF"
            # Execute query.
            cursor.execute(sql)
            r = list()
            c = list()
            for row in cursor:
                r.append(row["RECIPE_NAME"])
                c.append(row["CLIMATE"])
            cool = list()
            hot = list()
            rainy = list()
            for i in range(0, len(r)):
                if (c[i] == "COOL"):
                    cool.append(r[i])
                elif (c[i] == "HOT"):
                    hot.append(r[i])
                elif (c[i] == "RAINY"):
                    rainy.append(r[i])
            ch = ''
            f = weather()
            ran=list()
            if (hum[0] > 90):
                ch = "RAINY"
            elif (f > 26):
                ch = "HOT"
            elif (f <= 26):
                ch = "COOL"
            if (ch == "HOT"):
                ran.append(random.choice(hot))
                ran.append(random.choice(hot))
            elif (ch == "COOL"):
                ran.append(random.choice(cool))
                ran.append(random.choice(cool))
            elif (ch == "RAINY"):
                ran.append(random.choice(rainy))
                ran.append(random.choice(rainy))
            print(ran)







    finally:
        # Close connection.
        connection.close()
    return ran


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    secGUI_support.set_Tk_var()
    top = Toplevel1 (root)
    secGUI_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    secGUI_support.set_Tk_var()
    top = Toplevel1 (w)
    secGUI_support.init(w, top, *args, **kwargs)
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
        font10 = "-family Constantia -size 22 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family Arial -size 14 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        font14 = "-family {Comic Sans MS} -size 17 -weight bold -slant"  \
            " italic -underline 0 -overstrike 0"
        font15 = "-family Arial -size 11 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        font16 = "-family {Franklin Gothic Medium} -size 13 -weight "  \
            "bold -slant roman -underline 0 -overstrike 0"
        font23 = "-family Impact -size 24 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("949x794+528+98")
        top.title("MASTERCHEF's Food for Weather")
        top.configure(background="#dbfeff")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.021, rely=0.239, relheight=0.435, relwidth=0.69)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#070707")
        self.Frame1.configure(width=655)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.015, rely=0.029, height=36, width=362)
        self.Label1.configure(background="#0f0103")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#f7eca5")
        self.Label1.configure(text='''Weather Near You :''')
        self.Label1.configure(width=362)

        self.Listbox1 = tk.Listbox(self.Frame1)
        self.Listbox1.place(relx=0.031, rely=0.203, relheight=0.719
                , relwidth=0.51)
        self.Listbox1.configure(background="#ffffd6")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font=font11)
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(width=334)
        weather()
        self.Listbox1.insert(1,''.join(l1))
        self.Listbox1.insert(2, ''.join(l2))
        self.Listbox1.insert(3, ''.join(l3))
        self.Listbox1.insert(4, ''.join(l4))
        self.Listbox1.insert(5, ''.join(l5))
        self.Listbox1.insert(6, ''.join(l6))
        self.Listbox1.insert(7, ''.join(l7))
        self.Listbox1.insert(8, ''.join(l8))
        self.Listbox1.insert(9, ''.join(l9))
        self.Listbox1.insert(10, ''.join(l10))

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.565, rely=0.174, height=186, width=262)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self._img1 = tk.PhotoImage(file="C:/Users/Sumit Mehta/Desktop/CSE 3/PROJECT/Images_required/download (2).png")
        self.Label2.configure(image=self._img1)
        self.Label2.configure(text='''Label''')
        self.Label2.configure(width=262)

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.011, rely=0.693, relheight=0.283
                , relwidth=0.701)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(background="#0c0c0c")
        self.Frame2.configure(width=665)

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.03, rely=0.089, height=46, width=612)
        self.Label3.configure(background="#0c0c0c")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font14)
        self.Label3.configure(foreground="#ffc4f9")
        self.Label3.configure(text='''HOT OR COLD - Here's what we suggest :''')
        self.Label3.configure(width=612)
        f=list()
        def callbackFunc(event):
            f.append(self.TCombobox1.get())
            print(f)


        self.TCombobox1 = ttk.Combobox(self.Frame2)
        self.TCombobox1.place(relx=0.06, rely=0.4, relheight=0.16
                , relwidth=0.838)
        self.TCombobox1.configure(font=font15)
        self.TCombobox1.configure(textvariable=secGUI_support.combobox)
        self.TCombobox1.configure(width=557)
        self.TCombobox1.configure(takefocus="")
        rann=list()
        rann=ranselect()
        rann.append("Select")
        le=len(rann)-1
        rann=tuple(rann)
        self.TCombobox1['values']=rann
        self.TCombobox1.current(le)
        self.TCombobox1.bind("<<ComboboxSelected>>", callbackFunc)

        def webpage():
            webp(f)
        self.Button1 = tk.Button(self.Frame2)
        self.Button1.place(relx=0.256, rely=0.711, height=43, width=326)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d82906")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font16)
        self.Button1.configure(foreground="#ccffd4")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''SHOW ME HOW TO MAKE IT''')
        self.Button1.configure(width=326)
        self.Button1.config(command=webpage)

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.042, rely=0.013, height=166, width=162)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self._img2 = tk.PhotoImage(file="C:/Users/Sumit Mehta/Desktop/CSE 3/PROJECT/Images_required/master-chef-stamp-clipart__k18629513.png")
        self.Label4.configure(image=self._img2)
        self.Label4.configure(text='''Label''')
        self.Label4.configure(width=162)

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.221, rely=0.076, height=86, width=702)
        self.Label5.configure(background="#dbfdff")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font23)
        self.Label5.configure(foreground="#0038d1")
        self.Label5.configure(text='''ALL SEASONS ARE FOODIES LIKE US !! ^_^''')
        self.Label5.configure(width=702)

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.738, rely=0.315, height=211, width=212)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self._img3 = tk.PhotoImage(file="C:/Users/Sumit Mehta/Desktop/CSE 3/PROJECT/Images_required/images.png")
        self.Label6.configure(image=self._img3)
        self.Label6.configure(text='''Label''')
        self.Label6.configure(width=212)

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.717, rely=0.642, height=256, width=252)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self._img4 = tk.PhotoImage(file="C:/Users/Sumit Mehta/Desktop/CSE 3/PROJECT/Images_required/Screenshot-14-9.png")
        self.Label7.configure(image=self._img4)
        self.Label7.configure(text='''Label''')
        self.Label7.configure(width=252)

if __name__ == '__main__':
    vp_start_gui()