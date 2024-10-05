from tkinter import*
from tkinter.colorchooser import askcolor
from tkinter import ttk
from PIL import Image, ImageTk
from random import*
from tkinter import filedialog,simpledialog,messagebox
fontt=10
def mainwin():
    win=Tk()
    win.title("NotePad")
    win.geometry("700x700")
    win.iconbitmap("notepad.ico")

    def resize_image(image_path, size):  
        with Image.open(image_path) as img:
            img = img.resize(size)  
            return ImageTk.PhotoImage(img)

        
    def open_file():
        py_exts = r"*.py  *.py3 *.pyc  *.pyo  *.pyw  *.pyx  *.pyd  *.pxd  *.pyi  *.pyi  *.pyz  *.pywz *.rpy  *.pyde *.pyp  *.pyt  *.xpy  *.ipynb"

        var=filedialog.askopenfile (initialdir='/',filetypes=[('txtfile','*.txt'),('all files','*.*'),("Excel file","*.xlsx"),
                                                            ("python files", py_exts)])
        data=var.read()
        textarea.insert(END,data)

    def save_file():
        py_exts = r"*.py  *.py3 *.pyc  *.pyo  *.pyw  *.pyx  *.pyd  *.pxd  *.pyi  *.pyi  *.pyz  *.pywz *.rpy  *.pyde *.pyp  *.pyt  *.xpy  *.ipynb"
        var=filedialog.asksaveasfile(initialdir="/",filetypes=[("txtfile","*.txt"),("all files","*.*"),("Excel file","*.xlsx"),
                                                               ("python files", py_exts)],defaultextension="*.txt")
        data=textarea.get("1.0",END)
        var.write(data)
        var.close()

    def save_as():
        # Ask user for file location and name
        py_exts = r"*.py  *.py3 *.pyc  *.pyo  *.pyw  *.pyx  *.pyd  *.pxd  *.pyi  *.pyi  *.pyz  *.pywz *.rpy  *.pyde *.pyp  *.pyt  *.xpy  *.ipynb"
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt", 
            filetypes=[("Text files", "*.txt"), ("All files", "*.*"),("Excel file","*.xlsx"),("python files", py_exts)],
            title="Save As"
        )
        if file_path:
            # Get text from Text widget
            text_content = textarea.get(1.0,END)
            
            # Save the content to the selected file
            with open(file_path, 'w') as file:
                file.write(text_content)
            print(f"File saved as {file_path}")

    
    def ch_font():
        fontwin=Toplevel(win)

        def color():
            chcolor1.pack_forget()
            chcolor=askcolor(title="Font color")
            fontwin.lift()
            colorbtn.config(bg=chcolor[1])
            fcolor.set(chcolor[1])
            chcolor1.pack_forget()
            return chcolor
            
        
        def cancel():
            fontwin.destroy()
        
        
        def ok():
            try:
                if fcolor.get()=="nill":
                    fsize=int(sett1.get())
                    ffont=sett.get()
                    textarea.config(font=(ffont,fsize))
                else:
                    fsize=int(sett1.get())
                    ffont=sett.get()
                    textarea.config(font=(ffont,fsize),fg=fcolor.get())
            except ValueError:
                if fcolor.get()=="nill":
                    ffont=sett.get()
                    textarea.config(font=(ffont))
                else:
                    ffont=sett.get()
                    textarea.config(font=(ffont),fg=fcolor.get())

        fontwin.geometry("400x300")
        fontwin.title("Fonts")
        fontwin.iconbitmap("settings.ico")

        flabel=Label(fontwin,text="Font:",font=('Bahnschrift',12,'bold'))
        flabel.place(x=5,y=5)

        opt = [
            # Serif fonts
            "Georgia", "Garamond", "Merryweather", "Palatino",
            
            # Sans-serif fonts
            "Arial", "Helvetica", "Verdana", "Tahoma", "Calibri", "Lato",
            
            # Monospace fonts
             "Consolas", "Monaco",
            
            # Slab serif fonts
             "Oswald", "Bitter",
            
            # Display fonts
            "Impact", "Roboto Condensed", "Lora",
            
            # Handwritten fonts
             "Pacifico", "Lobster", "Amatic SC",
            
            # Other popular fonts
             "Poppins", "Quicksand", "Anton", "Montserrat"]
      
        sett=StringVar()
        sett.set(value="Select")
        fontopt=ttk.Combobox(fontwin,value=opt,textvariable=sett,width=30)
        fontopt.place(x=50,y=10)

        opt2=[1,2,3,4,5,6,7,8,9,10,12,14,16,18,20,22,24,26,28,30,33,36,39,42,45,48]
        sett1=StringVar()
        sett1.set(value="Size")
        sizopt=ttk.Combobox(fontwin,value=opt2,textvariable=sett1,width=10)
        sizopt.place(x=270,y=10)

        colorbtn=Button(fontwin,text="Font Color",bg="#5499c7",command=color)
        colorbtn.place(x=5,y=40)

        

        okbtn=Button(fontwin,text="Ok",bg="#5499c7",width="10",command=ok)
        okbtn.place(x=200,y=40)

        cancelbtn=Button(fontwin,text="Cancel",bg="#5499c7",width="10",command=cancel)
        cancelbtn.place(x=300,y=40)

        fcolor=StringVar()
        fcolor.set("nill")
        chcolor1=Entry(fontwin,textvariable=fcolor)
        chcolor1.pack(side=BOTTOM)
        chcolor1.pack_forget()

        fontwin.mainloop()

    def update_count(*args):
        # Get the current text and update the count
        current_text = textarea.get("1.0",END).strip() 
        count_label.config(text=f"{len(current_text)} Character")


    def update_position(event):
        # Get the current cursor position
        cursor_index = textarea.index(INSERT)
        row, col = cursor_index.split('.')
        position_label.config(text=f"Row: {int(row)}, Col: {int(col) + 1}")  # Col is 0-based

    def newwin():
        mainwin()

    def zoomin():
        global fontt
        fontt=fontt+3
        print(fontt)
        textarea.config(font=100)
    
    def clear():
        textarea.delete("1.0",END)
        count_label.config(text="0 Character")
        position_label.config(text="Row:1 , Col:1")  # Col is 0-based
    
    def ldmod():
        status=on.get()
        if status=="Dark Mode":
            on.set(value="Light Mode")
            textarea.config(bg="#283747",fg="#fbfcfc")
            topframe.config(bg="#34495e")
            filebtn.config(bg="#34495e",fg="#fbfcfc")
            editbtn.config(bg="#34495e",fg="#fbfcfc")
            viewbtn.config(bg="#34495e",fg="#fbfcfc")
            clearbtn.config(bg="#34495e",fg="#fbfcfc")
            modbtn.config(bg="#34495e",fg="#fbfcfc")
            bottomframe.config(bg="#34495e")
            bottomframe2.config(bg="#34495e")
            count_label.config(bg="#34495e",fg="#fbfcfc")
            position_label.config(bg="#34495e",fg="#fbfcfc")


        elif status=="Light Mode":
            on.set(value="Dark Mode")
            textarea.config(bg="#fbfcfc",fg="#17202a")
            topframe.config(bg="#fbfcfc")
            filebtn.config(bg="#fbfcfc",fg="#17202a")
            editbtn.config(bg="#fbfcfc",fg="#17202a")
            viewbtn.config(bg="#fbfcfc",fg="#17202a")
            clearbtn.config(bg="#fbfcfc",fg="#17202a")
            modbtn.config(bg="#fbfcfc",fg="#17202a")
            bottomframe.config(bg="#fbfcfc")
            bottomframe2.config(bg="#fbfcfc")
            count_label.config(bg="#fbfcfc",fg="#17202a")
            position_label.config(bg="#fbfcfc",fg="#17202a")
    def huh_status():
        if var.get()==1:
            bottomframe2.pack_forget()
            bottomframe.pack(fill=X,side='bottom')
            bottomframe2.pack(fill=X,side='bottom')
            
        else:
            bottomframe.pack_forget()
    
    def src():
        findwin=Toplevel(win)
        def srcc():
            search_term=srcentry.get()
            if not search_term:
                return

            start_pos = "1.0"  # Start searching from the beginning of the text
            textarea.tag_remove("found", "1.0", END)  # Clear any previous search highlights

            found = False  # To track if any occurrence is found


            while True:
                start_pos = textarea.search(search_term, start_pos, stopindex=END, nocase=True)
                if not start_pos:
                    # messagebox.showinfo("Find", f"'{search_term}' not found!")
                    break

                end_pos = f"{start_pos}+{len(search_term)}c"
                textarea.tag_add("found", start_pos, end_pos)
                textarea.tag_config("found", foreground="red")  # Change the color of the found text
                start_pos = end_pos  # Move the search start position for the next iteration
            
            if found:
                messagebox.showinfo("Find", f"'{search_term}' found!")
            else:
                messagebox.showinfo("Find", f"'{search_term}' not found!")

        

        findwin.geometry("300x200")
        findwin.title("Search")
        findwin.iconbitmap("settings.ico")

        srclbl=Label(findwin,text="Enter the word to find:")
        srclbl.place(x=5,y=5)

        srcentry =Entry(findwin)
        srcentry.place(x=150,y=5)
        

        okbtn=Button(findwin,text="Find",command=srcc)
        okbtn.place(x=5,y=40)
        cnbtn=Button(findwin,text="Cancel")
        cnbtn.place(x=50,y=40)
        
        

    topframe=Frame(win,bg="#fbfcfc",relief="raised",bd=2,height=30)
    topframe.pack(fill=X,anchor='e')

    filebtn=Menubutton(topframe,text="File",width=6,relief='flat',cursor='hand2')
    filebtn.menu=Menu(filebtn,tearoff=0)
    filebtn['menu']=filebtn.menu

    filebtn.menu.add_command(label="New file",command=newwin)
    filebtn.menu.add_command(label="Save file",command=save_file)
    filebtn.menu.add_command(label="Save as",command=save_as)
    filebtn.menu.add_command(label="Open file",command=open_file)
    filebtn.place(x=0,y=0)



    editbtn=Menubutton(topframe,text="Edit",width=6,relief='flat',cursor='hand2')
    editbtn.menu=Menu(editbtn,tearoff=0)
    editbtn['menu']=editbtn.menu
    editbtn.menu.add_command(label="Font",command=ch_font)
    editbtn.menu.add_command(label="Find",command=src)
    editbtn.menu.add_command(label="Replace")
    editbtn.menu.add_command(label="Select all")
    editbtn.place(x=60,y=0)

    viewbtn=Menubutton(topframe,text="View",width=6,relief='flat',cursor='hand2')
    viewbtn.menu=Menu(viewbtn,tearoff=0)
    viewbtn['menu']=viewbtn.menu

    var=IntVar()
    var.set(1)
    submenu=Menu(viewbtn,tearoff=0)
    submenu.add_command(label="Zoom in",command=zoomin)
    submenu.add_command(label="Zoom out")
    viewbtn.menu.add_cascade(label="Zoom",menu=submenu)
    viewbtn.menu.add_checkbutton(label="Show Status bar",variable=var,command=huh_status)

    viewbtn.place(x=120,y=0)

    clearbtn=Button(topframe,text="Clear",command=clear,cursor="hand2",relief="sunken",height=1)
    clearbtn.pack(side=RIGHT,padx=20)
    on=StringVar(value="Dark Mode")

    modbtn=Button(topframe,text="Dark Mode",command=ldmod,cursor="hand2",textvariable=on,relief="sunken",height=1)
    modbtn.pack(side=RIGHT)


    textframe=Frame(win)
    textframe.pack(expand=True,fill=BOTH)


    text_var = StringVar()
    text_var.trace_add("write", update_count)

    textarea=Text(textframe)
    textarea.pack(expand=True,fill=BOTH,side=LEFT)

    def on_text_change(event):
        text_var.set(textarea.get("1.0",END).strip())
        update_count()

    textarea.bind("<KeyRelease>", lambda event: (update_count(), update_position(event)))
    scrollbary=Scrollbar(textframe,orient='vertical',command=textarea.yview,bg='#148f77')
    scrollbary.pack(side=RIGHT,fill=Y)
    textarea['yscrollcommand']=scrollbary.set


    bottomframe=Frame(win,relief="raised",bd=2,height=20)
    bottomframe.pack(fill=X,side='bottom')

    count_label = Label(bottomframe, text="0 Characters")
    count_label.pack(side=LEFT,padx=10)

    position_label = Label(bottomframe, text="Row: 1, Col: 1")
    position_label.pack(side=LEFT)

    bottomframe2=Frame(win,relief="raised",bd=2,height=19)
    bottomframe2.pack(fill=X,side='bottom')
    scrollbarx=Scrollbar(bottomframe2,orient='horizontal',command=textarea.xview,bg='#148f77')
    textarea['xscrollcommand']=scrollbarx.set
    scrollbarx.pack(fill=X)

    win.mainloop()

mainwin()