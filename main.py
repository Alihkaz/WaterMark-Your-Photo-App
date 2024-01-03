#-----------------Imports------------#
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *  #Ttk wrapper , This module provides classes to allow using Tk themed widget set.
from tkinter import messagebox, END
from PIL import Image, ImageDraw, ImageFont


main = Tk()
main.geometry("500x500")
main.title('Water Mark your Image')





#------------------------watermarking image using LOGO inputed by the user ----------------------------------------------


def watermark_using_logo():

    logo_Window = tk.Toplevel() #creating a new window using Toplevel method using the main window we created from tkinter class 
    logo_Window.title("New Logo Window")
    logo_Window.geometry("500x500")
    Label(logo_Window, text="Watermark Using Logo").pack()

    #first entry in the new window :
    photo_data = tk.Label(logo_Window, text="Photo To Edit")
    photo_data.pack()

    photo_to_edit = tk.Entry(logo_Window, width=50)
    photo_to_edit.pack()

    p_upload_button = tk.Button(logo_Window, text='Upload Your File' , width=20, command=lambda: upload_img('i'))
    p_upload_button.pack()


    #second entry in the new window :
    logo_l = tk.Label(logo_Window, text="Logo")
    logo_l.pack()

    logo_to_put = tk.Entry(logo_Window, width=50)
    logo_to_put.pack()

    l_upload_button = tk.Button(logo_Window, text='Upload File' , width=20, command=lambda: upload_img('l'))
    l_upload_button.pack()




    #third entry in the new window :
    logo_label = tk.Label(logo_Window, text="Watermark name")
    logo_label.pack()

    label_input = tk.Entry(logo_Window, width=50)
    label_input.pack()

    t_upload_button = tk.Button(logo_Window, text='Watermark Photo',width=20, command=lambda: WMLOGO())
    t_upload_button.config(fg='green')
    t_upload_button.pack()





    def upload_img(type):

        if type == 'i':

            photo_to_edit.delete(0, END)
            label_input.delete(0, END)

            image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])

            photo_name = image_path.split('/')
            photo_name = photo_name[len(photo_name)-1] #extracting only the image name without the whole path , and its the first item in splitted list

            photo_to_edit.insert(0, image_path)
            label_input.insert(0, f"watermark_{photo_name}")


        else:

            logo_to_put.delete(0, END)
            img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
            logo_to_put.insert(0, img_path)



    def WMLOGO():


        p_data = photo_to_edit.get()
        l_data = logo_to_put.get()
        t_data = label_input.get()

        if len(p_data) < 1:
            messagebox.showwarning(message="You didn't provide a proper data for photo")

        elif len(l_data) < 1:
            messagebox.showwarning(message="You didn't provide a proper data for the text")

        elif len(t_data) < 1:
            messagebox.showwarning(message="You didn't provide a proper photo after watermark")
            
        else:
            image = Image.open(p_data)
            logo = Image.open(l_data)
            logo = logo.resize((200, 200))
            marked_image = image.copy()
            marked_image.paste(logo, (50, 50))
            marked_image.save(t_data)


#------------------------watermarking image using text inputed by the user ----------------------------------------------

def watermark_using_text():

    Text_Window = tk.Toplevel() #creating a new window using Toplevel method using the main window we created from tkinter class 
    Text_Window.title("New Window")
    Text_Window.geometry("500x500")
    Label(Text_Window, text="Watermark Using Text").pack()

    
    #first entry in the new window :
    photo_data = tk.Label(Text_Window, text="Photo To Edit")
    photo_data.pack()

    photo_to_edit = tk.Entry(Text_Window, width=50)
    photo_to_edit.pack()

    p_upload_button = tk.Button(Text_Window, text='Upload Your File' , width=20, command=lambda: upload_img('i'))
    p_upload_button.pack()



    #second entry in the new window :
    txt_label = tk.Label(Text_Window, text="Text To Post ")
    txt_label.pack()

    txt_data = tk.Entry(Text_Window, width=50)
    txt_data.pack()


     #Third entry in the new window :
    name_l = tk.Label(Text_Window, text="Watermark name")
    name_l.pack()

    name_data = tk.Entry(Text_Window, width=50)
    name_data.pack()

    confirm_button = tk.Button(Text_Window, text='Watermark Photo',width=20, command=lambda:WMText())
    confirm_button.config(fg='green')
    confirm_button.pack()



    def upload_img():

        photo_to_edit.delete(0, END)
        name_data.delete(0, END)
        image_path = filedialog.askopenfilename(filetypes=[('Jpg Files', '*.jpg')])

        p_name = image_path.split('/')
        p_name = p_name[len(p_name)-1]

        photo_to_edit.insert(0, image_path)
        name_data.insert(0, f"watermark_{p_name}")



    def WMText():

        p_data = photo_to_edit.get()
        t_data = txt_data.get()
        W_data = name_data.get()

        if len(p_data) < 1:
            messagebox.showwarning(message="You didn't provide a proper data for photo")

        elif len(t_data) < 1:
            messagebox.showwarning(message="You didn't provide a proper data for the text")

        elif len(W_data) < 1:
            messagebox.showwarning(message="You didn't provide a proper photo after watermark")
            

        else:
            image = Image.open(p_data)
            marked_image = image.copy()
            draw = ImageDraw.Draw(marked_image)
            font = ImageFont.truetype("arial.ttf", 50)
            draw.text((0, 0), t_data, (255, 255, 255), font=font)
            marked_image.save(W_data)



#----------------------------------------------UI Setup---------------------------------------------------------

canvas = tk.Canvas(width=600, height=500)
canvas.grid(row=0, column=0, rowspan=18, columnspan=4)

label = Label(main, text="Please Choose :" , font=('Arial', 12, 'bold') )
label.grid(row=1, column=4, sticky='nesw')

txt_btn = tk.Button(main ,text="Watermark using text", font=('Arial', 12, 'bold') , command=watermark_using_text)
txt_btn.grid(row=3, column=4,columnspan=2, sticky='nesw')

logo_btn = tk.Button(main , text="Watermark using logo" , font=('Arial', 12, 'bold'), command=watermark_using_logo)
logo_btn.grid(row=4, column=4,columnspan=2, sticky='nesw')

main.mainloop()