import tkinter as tk

def format_response(entry):
        s = entry.lower()
        my_key={'a': '?', 'b':1, 'c' : 2 , 'd' : 3 , 'e': 4, 'f' : 5,'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9 , 'k' : '!' , 'l' : '@','m' : '#' , 'n' : '$' , 'o' : '%' , 'p' : '^' , 'q' : '&' , 'r' : '*' , 's' : '(', 't' : ')' , 'u' : '-', 'v' : '=', 'w' : '_', 'x' : '+', 'y' : '~', 'z' : '.', ' ' : '[' }
        message = ""
        for i in s:
            message = message + str(my_key.get(i))
        new = (message)
        final_string = 'Original Text: %s \nEncoded Text: %s' % (entry,new)
        return final_string

def get_encode(entry):
    print(entry)
    print(format_response(entry))
    label['text'] = format_response(entry)

# main window
root = tk.Tk()

HEIGHT = 700
WIDTH = 800

canvas = tk.Canvas(root, height = 600, width = 1200)
canvas.pack()


frame_login = tk.Frame(root, bg = "#00b3b3", width = WIDTH, height = HEIGHT, bd =10 )  
frame_login.place(relx =0.4, rely =0.1, relwidth = 0.2, relheight = 0.3)

lbl_username = tk.Label(frame_login, text='Encoder:',font="arial" )
lbl_username.pack(padx= 40, fill = 'both') 

entry = tk.Entry(frame_login, bd=5)
entry.place(relx =0.2, rely = 0.18, relwidth = 0.6, relheight = 0.1)

btn_login=tk.Button(frame_login, text="enter", command = lambda: get_encode(entry.get()))
btn_login.place(relx =0.43, rely = 0.3, relwidth = 0.15, relheight = 0.1)

label = tk.Label(frame_login)
label.place(relx =0.2, rely = 0.5, relwidth = 0.6, relheight = 0.3)

####################################################################################################################################


def format_output(textbox):
    my_key={'?': 'a', str(1):'b', str(2) : 'c' , str(3) : 'd' , str(4): 'e', str(5) : 'f', str(6) : 'g', str(7) : 'h', str(8) : 'i', str(9) : 'j' , '!' : 'k' , '@' : 'l','#' : 'm' , '$' : 'n' , '%' : 'o' , '^' : 'p' , '&' : 'q' , '*' : 'r' , '(' : 's', ')' : 't' , '-' : 'u', '=' : 'v', '_' : 'w', '+' : 'x', '~' : 'y', '.' : 'z' , '[' : ' ' }
    stKey = ""
    for i in textbox:
        stKey = stKey + str(my_key.get(i))
    latest = stKey 
    finale_str = 'Encoded Text: %s \nDecoded Text: %s' % (textbox,latest)
    return finale_str

def get_decode(textbox):
    print(textbox)  
    label_2['text'] = format_output(textbox)
    

frame_decode = tk.Frame(root, bg = '#cc0066', width = WIDTH, height = HEIGHT, bd = 10 )
frame_decode.place(relx =0.4, rely =0.4, relwidth = 0.2, relheight = 0.3)

lbl_password= tk.Label(frame_decode,text="Decoder:",font="Arial")
lbl_password.pack(padx= 40, fill    = 'both')

textbox= tk.Entry(frame_decode, bd=5)
textbox.place(relx =0.2, rely = 0.18, relwidth = 0.6, relheight = 0.1)

# Add this code before the code that creates your "Login" button
btn_login=tk.Button(frame_decode, text="enter", command = lambda: get_decode(textbox.get()))
btn_login.place(relx =0.43, rely = 0.3, relwidth = 0.15, relheight = 0.1)

label_2 = tk.Label(frame_decode)
label_2.place(relx =0.2, rely = 0.5, relwidth = 0.6, relheight = 0.3)

root.mainloop()



