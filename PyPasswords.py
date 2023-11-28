from guizero import App, Text, TextBox, Box, PushButton
import random
import string

def clear_form():
    txt_qty.value = "1"
    txt_len.value = "14"
    txt_output.value = ""

def generate_password():
    quantity = txt_qty.value
    length = txt_len.value
    
    errors = []

    # both fields are required
    if quantity == "":
        errors.append("* Quantity of passwords - Required.")      
    if length == "":
        errors.append("* Password Length - Required.")

    # must be numeric
    if quantity != "" and not quantity.isdigit():
        errors.append("* Quantity of passwords - Numeric value required.")
    if length != "" and not length.isdigit():
        errors.append("* Password Length - Numeric value required.")
        
    if errors != []:
        error_message = "\n".join(errors)
        app.error("Missing required fields...", error_message)
        return
    
    quantity = int(quantity)
    length = int(length)   
    
    passwords = []
    for _ in range(quantity):
        # random string of letters, digits, and punction/special characters
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        passwords.append(password)
    
    txt_output.value = "\n".join(passwords)

# this is the actual window itself of the gui.
app = App(title="Password Generator - Assignment3 - ColeCianflone",width=545, height=500)

# set the title/header region of the window at the top, parent = app.
title_box = Box(app, width="fill", align="top")
Text(title_box, text="Strong passwords are very important to ensure your personal cyber security.\nGenerate some good ones...")

# set the text below the title/header region, parent = app.
content_box = Box(app, align="top", width="fill")
Text(content_box, text="\nEnter the quantity of passwords you wish to generate\n along with the password length\n\n")

# we use a hidden box to act as padding for the fields, parent = content_box
left_pad_content = Box(content_box, layout="auto", width="150", align="left")

# the form_box houses the two fields, parent = content_box
form_box = Box(content_box,layout="grid", width="fill", height="fill", align="top")

# parent = form_box, which is a child of context_box, which is a child of app
Text(form_box, grid=[0,0], text="Qty of passwords :")
txt_qty = TextBox(form_box, grid=[1,0], text="1", width="fill")
Text(form_box, grid=[0,1], text="Password length  :")
txt_len = TextBox(form_box, grid=[1,1], text="14", width="fill")

#left_pad_textbox = Box(app, layout="auto", width="100", align="left")
Text(form_box, grid=[0,2], text="")
txt_output = TextBox(content_box, multiline=True, align="left",width=32, height=5, scrollbar=True, visible= True)

bottom_box = Box(app, align="bottom", width="fill")

# we use a hidden box to act as left padding for the buttons
left_pad_bottom = Box(bottom_box, layout="auto", width="210", align="left")
bottom_pad_bottom = Box(bottom_box, layout="auto", width="fill",height="35", align="bottom")
buttons_box = Box(bottom_box,width="fill", align="bottom")

generate_button = PushButton(buttons_box, text="Generate", align="left", width="5", command=generate_password)
clear_button = PushButton(buttons_box, text="Clear", align="left",width="5", command=clear_form)  

app.display()