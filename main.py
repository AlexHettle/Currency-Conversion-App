
from tkinter import *
import requests
#Global variables used to determine which currencies are chosen
global left_buttons
global right_buttons
left_buttons=[1,0,0,0]
right_buttons=[1,0,0,0]
#####################################################################
#ENTER YOUR API KEY HERE, GET API KEY AT https://exchangeratesapi.io/
#####################################################################
#APIKEY = ################################


#A function that looks at what buttons are pressed, takes in the amount the user input,
#and converts the currencies using exchangeratesapi.io
def get_conversion(left,right):
    try:
        amount=amount_entry.get()
        currencies=["USD","CAD","EUR","GBP"]
        left_currency=currencies[left.index(1)]
        right_currency=currencies[right.index(1)]
        if left_currency==right_currency:
            conversion_display.configure(text=(str(round(float(amount),2))+" "+left_currency+"\n=\n"+str(round(float(amount),2))+" "+right_currency))
        else:
            url="https://api.apilayer.com/exchangerates_data/latest?apikey="+APIKEY+"&base="+left_currency+"&symbols="+right_currency
            response=requests.get(url)
            data = response.json()
            conversion_display.configure(text=(str(round(float(amount),2))+" "+data["base"]+"\n=\n"+str(round(float(amount)*data["rates"][right_currency],2))+" "+right_currency))
        global left_buttons
        global right_buttons
        left_buttons=left
        right_buttons=right
    except:
        conversion_display.configure(text=("Invalid entry"))
#sets up the buttons on the left when user starts the app
def initialize_left_button_lights():
    the_canvas.create_oval(22,185,32,195,fill="grey")
    the_canvas.create_oval(62,185,72,195,fill="grey")
    the_canvas.create_oval(102,185,112,195,fill="grey")
    the_canvas.create_oval(142,185,152,195,fill="grey")
    
    
    
    the_canvas.create_oval(22,228,32,238,fill="grey")
    the_canvas.create_oval(62,228,72,238,fill="grey")
    the_canvas.create_oval(102,228,112,238,fill="grey")
    the_canvas.create_oval(142,228,152,238,fill="grey")
#sets up the buttons on the right when user starts the app
def initialize_right_button_lights():
    the_canvas.create_oval(342,185,352,195,fill="grey")
    the_canvas.create_oval(382,185,392,195,fill="grey")
    the_canvas.create_oval(422,185,432,195,fill="grey")
    the_canvas.create_oval(462,185,472,195,fill="grey")
    
    
    the_canvas.create_oval(342,228,352,238,fill="grey")
    the_canvas.create_oval(382,228,392,238,fill="grey")
    the_canvas.create_oval(422,228,432,238,fill="grey")
    the_canvas.create_oval(462,228,472,238,fill="grey")
#When a currency button is pressed, this function regulates the yellow lights above
#and below the buttons and alters the button global variables accordingly
def regulate_buttons_and_lights(side,button_number,left,right):
    if side=="LEFT" and left[button_number]!=1:
        left=[0,0,0,0]
        left[button_number]=1
        initialize_left_button_lights()
        the_canvas.create_oval(22+(button_number*40),185,32+(button_number*40),195,fill="#f9fe01")
        the_canvas.create_oval(22+(button_number*40),228,32+(button_number*40),238,fill="#f9fe01")

        global left_buttons
        left_buttons=left
    if side=="RIGHT" and right[button_number]!=1:
        right=[0,0,0,0]
        right[button_number]=1
        initialize_right_button_lights()
        the_canvas.create_oval(342+(button_number*40),185,352+(button_number*40),195,fill="#f9fe01")
        the_canvas.create_oval(342+(button_number*40),228,352+(button_number*40),238,fill="#f9fe01")

        global right_buttons
        right_buttons=right
#This chunk of code sets up the GUI
window=Tk()
window.title("Currency-Converter")
window.geometry("498x250")
window.resizable(False, False)
the_canvas=Canvas(window,width=500,height=250, highlightthickness=0,bg="#5fb14e")
the_canvas.place(x=0,y=0)
title=Label(text="Currency-Converter",font=("fixedsys",20),fg="White",bg="#47843a")
title.pack(side=TOP)
enter_button=Button(text="CONVERT",font=("fixedsys",10),command=lambda:get_conversion(left_buttons,right_buttons),bg="#47843a",fg="white")
enter_button.place(x=86,y=151)
amount_entry=Entry(window,width=40,borderwidth=5)
amount_entry.place(x=156,y=150)
conversion_display=Label(text="0.00 USD\n=\n0.00 USD",font=("fixedsys",20),justify=CENTER,bg="#47843a",fg="white")
conversion_display.pack(side=TOP)
convert_to=Label(text="CONVERT TO",font=("fixedsys",10),justify=CENTER,bg="#4EB16F",fg="White")
convert_to.place(x=210,y=200)
USDL=Button(text="USD",font=("fixedsys",10),command=lambda:regulate_buttons_and_lights("LEFT",0,left_buttons,right_buttons))
USDL.place(x=10,y=200)
CADL=Button(text="CAD",font=("fixedsys",10),command=lambda:regulate_buttons_and_lights("LEFT",1,left_buttons,right_buttons))
CADL.place(x=50,y=200)
EURL=Button(text="EUR",font=("fixedsys",10),command=lambda:regulate_buttons_and_lights("LEFT",2,left_buttons,right_buttons))
EURL.place(x=90,y=200)
GBPL=Button(text="GBP",font=("fixedsys",10),command=lambda:regulate_buttons_and_lights("LEFT",3,left_buttons,right_buttons))
GBPL.place(x=130,y=200)
USDR=Button(text="USD",font=("fixedsys",10),command=lambda:regulate_buttons_and_lights("RIGHT",0,left_buttons,right_buttons))
USDR.place(x=330,y=200)
CADR=Button(text="CAD",font=("fixedsys",10),command=lambda:regulate_buttons_and_lights("RIGHT",1,left_buttons,right_buttons))
CADR.place(x=370,y=200)
EURR=Button(text="EUR",font=("fixedsys",10),command=lambda:regulate_buttons_and_lights("RIGHT",2,left_buttons,right_buttons))
EURR.place(x=410,y=200)
GBPR=Button(text="GBP",font=("fixedsys",10),command=lambda:regulate_buttons_and_lights("RIGHT",3,left_buttons,right_buttons))
GBPR.place(x=450,y=200)
the_canvas.create_rectangle(-1,190,501,252,fill="#47843a")
the_canvas.create_rectangle(-1,-1,502,55,fill="#47843a",outline="")
the_canvas.create_rectangle(67,55,427,190,fill="#47843a",outline="")
the_canvas.create_polygon(27,190,67,145,427,145,467,190,fill="#47843a")
the_canvas.create_rectangle(0,0,67,55,fill="#4EB16F",outline = "")
the_canvas.create_rectangle(427,0,500,55,fill="#4EB16F",outline = "")
the_canvas.create_rectangle(0,191,500,251,fill="#4EB16F",outline = "")
the_canvas.create_rectangle(10,10,57,47,fill="#f9fe01")
the_canvas.create_rectangle(10,57,57,77,fill="#f9fe01")
the_canvas.create_rectangle(10,87,57,107,fill="#f9fe01")
the_canvas.create_rectangle(10,117,57,137,fill="#f9fe01")
the_canvas.create_rectangle(437,10,487,47,fill="#f9fe01")
the_canvas.create_rectangle(437,57,487,77,fill="#f9fe01")
the_canvas.create_rectangle(437,87,487,107,fill="#f9fe01")
the_canvas.create_rectangle(437,117,487,137,fill="#f9fe01")
the_canvas.create_rectangle(-1,233,498,252,fill="#47843a")
initialize_left_button_lights()
the_canvas.create_oval(22,185,32,195,fill="#f9fe01")
the_canvas.create_oval(22,228,32,238,fill="#f9fe01")
initialize_right_button_lights()
the_canvas.create_oval(342,185,352,195,fill="#f9fe01")
the_canvas.create_oval(342,228,352,238,fill="#f9fe01")
window.mainloop()
