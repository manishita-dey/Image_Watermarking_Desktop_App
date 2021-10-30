import tkinter
from PIL import ImageTk, Image, ImageDraw, ImageFont
# To get the dialog box to open when required
from tkinter import filedialog, END
from tkinter import messagebox



def openfilename():
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askopenfilename(title='Open')
    return filename



def select_image():

    # Select the Imagename  from a folder
    x = openfilename()

    # opens the image
    img = Image.open(x)

    # resize the image and apply a high-quality down sampling filter
    img = img.resize((800, 400), Image.ANTIALIAS)

    # PhotoImage class is used to add image to widgets, icons etc
    img_final = ImageTk.PhotoImage(img)

    # create a label
    panel = tkinter.Label(window, image=img_final)

    # set the image as img_final
    panel.image = img_final
    panel.grid(row=1, column = 0, columnspan = 3)
    global image_var
    image_var = img


def text_watermark():


    # Creating New Text Layer
    image = image_var.convert("RGBA")
    txt = Image.new('RGBA', image.size,(255,255,255,0))

    #Creating text and font object
    text = input_text.get()
    font = ImageFont.truetype('arial.ttf', 60)

    # Create draw object (this is a handle that takes the opened image as argument)
    draw = ImageDraw.Draw(txt)

    # Positioning Text
    textwidth, textheight = draw.textsize(text, font)
    width, height = image.size
    x = width / 2 - textwidth / 2
    y = height/2- textheight +50

    # Applying text on image via draw object
    draw.text((x, y), text,fill =(255,255,255,100), font=font)

    # Combining Original image with text and Saving the new image
    watermarked = Image.alpha_composite(image,txt)
    saved_file_extension = filedialog.asksaveasfilename(title= 'Save As', defaultextension = '.png', initialfile = watermarked)
    watermarked.save(saved_file_extension)

    #     adding a message dialog box for letting user know that file was saved
    messagebox.showinfo('Saved', 'File Saved!')


def logo_watermark():
    # image = image_used.convert("RGBA")
    filename = filedialog.askopenfilename(title= 'Open')
    watermark = Image.open(filename)
    watermark = watermark.resize((100, 100), Image.ANTIALIAS)

    #position
    position = (0, 0)
    width, height = image_var.size

    #add watermarrk logo to your image
    transparent = Image.new('RGBA',(width, height),(0,0,0,0) )
    transparent.paste(image_var, position)
    transparent.paste(watermark, position, mask = watermark)
    transparent.show()

    global logo_img_var
    logo_img_var = transparent



def save_logo_img():
    # pass
    global logo_img_var
    saved_file_path = filedialog.asksaveasfilename(title='Save As', defaultextension='.png',
                                                        initialfile=logo_img_var)
    logo_img_var.save(saved_file_path)

#     adding a message dialog box for letting user know that file was saved
    messagebox.showinfo('Saved', 'File Saved!')


image_var = None

logo_img_var = None

window = tkinter.Tk()
window.title("Image Watermarking Desktop App")
window.config(padx=50, pady=50)
# Allow Window to be resizable
window.resizable(width = True, height = True)

# Button(To select image to be processed)
button = tkinter.Button(text="Select Image", command=select_image)
button.grid(row = 0, column = 1)


# Entry for watermark text
input_text = tkinter.Entry(width = 20)
input_text.insert(END, string= 'Enter watermark text')
input_text.focus()
input_text.grid(row = 2, column = 0)


#Button(To Apply text Watermark)
button_text = tkinter.Button(text='Apply text watermark', command = text_watermark)
button_text.grid(row = 3, column = 0 )


#Button(To apply logo watermark)
button_logo = tkinter.Button(text = 'Apply logo Watermark', command = logo_watermark)
button_logo.grid(row = 2, column = 2)

#Button to save logo watermarked image
button_save = tkinter.Button(text = 'Save Image', command = save_logo_img)
button_save.grid(row= 3, column = 2)



window.mainloop()
