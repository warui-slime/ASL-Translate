import tkinter as tk
import mysql.connector
import os

connection = mysql.connector.connect(host='localhost', database='',user='',password='')
mycursor = connection.cursor()

win=tk.Tk()
wi, he = win.winfo_screenwidth(), win.winfo_screenheight()
win.geometry(f"{wi}x{he}")
win ["bg"]="PaleGreen"
win.title("ASL TRANSLATOR")

#Title of the project 
title_asl=tk.Label(text="ASL TRANSLATOR",font=("lucida handwriting",50))
title_asl.pack(side=tk.TOP,padx=18,pady=12)


def add_images(img_command):
    exec(img_command)



def text_fnc(event = ""):
    canvas1.delete("all")
    main_txt = [val for val in htext.get().upper() if val.isalpha()]
    if len(main_txt) > 24:
        canvas1.create_text(100,30,text="Word Limit Reached!",font="ComicSansMS 14")
        return ""
    for ch in main_txt:
        cnt = 1
        if main_txt.count(ch) > 1:
            for change in range(len(main_txt)):
                if main_txt[change] == ch:
                    main_txt[change] = f"{main_txt[change]}{cnt}"
                    cnt += 1
                    

    img_commmand = ""
    img_commmand += f"global {','.join(main_txt)}\n"
    img_x = 0
    img_y = 0

    for i in main_txt:
        mycursor.execute(f"SELECT IMAGE FROM IMAGES WHERE ID = '{''.join([tex for tex in i if tex.isalpha()])}'")
        mysq_command = mycursor.fetchall()[0][0]
        with open(f"{i}.png","wb") as fi:
            fi.write(mysq_command)
        img_commmand += f"{i} = tk.PhotoImage(file='{i}.png')\n"
        img_commmand += f"canvas1.create_image( ({img_x,img_y}), image = {i},anchor = tk.NW)\n"
        img_commmand += f"os.remove('{i}.png')\n"
        img_x += 120
        if img_x >= 700:
            img_y += 120
            img_x=0
    try:               
        add_images(img_commmand) 
    except Exception:
        pass           
    
    
hlabel = tk.Label(win,text="ENTER TEXT HERE",bg="PaleGreen",font="LucidaBold 17")
hlabel.pack(side=tk.TOP)

htext = tk.Entry(win,font="LucidaBold 13")
htext.pack(side=tk.TOP,padx=18,pady=12)

hconvert = tk.Button(win,text= "CONVERT",font = "LucidaBold 10",command=text_fnc)
hconvert.pack(side = tk.TOP)
win.bind("<Return>",text_fnc)

hframe =tk.Frame(win,bg="white")
canvas1 = tk.Canvas( hframe, width = 800,height = 500)

canvas1.pack(pady = 10)
hframe.pack(pady=10)

win.mainloop()