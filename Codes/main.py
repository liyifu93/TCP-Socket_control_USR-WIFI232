import subprocess
import tkinter as tk

from PIL import Image, ImageTk

# Settings
font_type = "Bookman Old Style"
font_size = 35
# Create the main window
root = tk.Tk()
root.title("The George Washington University's Central Utiity Plant - Energy Management System")

# Set the window size
root.geometry("3000x2700")

# Create the left frame for the buttons
left_frame = tk.Frame(root)
left_frame.pack(side="left", fill="y")

# Create the right frame for the image
right_frame = tk.Frame(root)
right_frame.pack(side="right", fill="both", expand=True)

# Create the first button and pack it into the left frame
button1 = tk.Button(left_frame, text="Map", command=lambda: subprocess.call(["python", "script1.py"]))
button1.configure(font=(font_type, font_size, "bold"))
button1.pack(side="top", padx=20, pady=20)

# Create the second button and pack it into the left frame
button2 = tk.Button(left_frame, text="Footprint", command=lambda: subprocess.call(["python", "script2.py"]))
button2.configure(font=(font_type, font_size, "bold"))
button2.pack(side="top", padx=20, pady=20)

# Create the first button and pack it into the left frame
button3 = tk.Button(left_frame, text="Existing System", command=lambda: subprocess.call(["python", "script3.py"]))
button3.configure(font=(font_type, font_size, "bold"))
button3.pack(side="top", padx=20, pady=20)


# Create a text box and pack it into the left frame
text_box = tk.Entry(left_frame)
text_box.pack(side="bottom", padx=20, pady=10)
text_box.configure(font=(font_type, font_size-5, "bold"))
# Create a label for the text box
text_box_label = tk.Label(left_frame, text="Battery Capacity [kWh]")
text_box_label.pack(side="bottom", padx=20, pady=10)
text_box_label.configure(font=(font_type, font_size-5, "bold"))



# Create a text box and pack it into the left frame
text_box_2 = tk.Entry(left_frame)
text_box_2.pack(side="bottom", padx=20, pady=10)
text_box_2.configure(font=(font_type, font_size-5, "bold"))

# Create a label for the text box
text_box_2_label = tk.Label(left_frame, text="Solar Size [kW]")
text_box_2_label.pack(side="bottom", padx=20, pady=10)
text_box_2_label.configure(font=(font_type, font_size-5, "bold"))

# Create the second button and pack it into the left frame
button4 = tk.Button(left_frame, text="Upgrade", command=lambda: run_script())
button4.configure(font=(font_type, font_size, "bold"))
button4.pack(side="bottom", padx=20, pady=20)

def run_script():
    input_text = text_box.get()
    input_text_2 = text_box_2.get()
    subprocess.call(["python", "script4.py", input_text, input_text_2])


# Load the background image
background_image = Image.open("background.png")

# Calculate the new dimensions
original_width, original_height = background_image.size
new_width = 1700
aspect_ratio = original_width / original_height
new_height = int(new_width / aspect_ratio)

# Resize the image
background_image = background_image.resize((new_width, new_height), Image.ANTIALIAS)

# Create a PhotoImage object from the resized background image
background_photo = ImageTk.PhotoImage(background_image)

# Create the label to display the image and pack it into the right frame
image_label = tk.Label(right_frame, image=background_photo)
image_label.pack(fill="both", expand=True)

# Function to update the image
def update_image(image_path, default_image_path):
    try:
        # Load the new image
        new_image = Image.open(image_path)
    except FileNotFoundError:
        # Load the default image if the image path is not found
        new_image = Image.open(default_image_path)

    # Calculate the new dimensions
    original_width, original_height = new_image.size
    new_width = 1700
    aspect_ratio = original_width / original_height
    new_height = int(new_width / aspect_ratio)

    # Resize the image
    new_image = new_image.resize((new_width, new_height), Image.ANTIALIAS)

    # Create a PhotoImage object from the resized new image
    new_photo = ImageTk.PhotoImage(new_image)

    # Update the label with the new image
    image_label.configure(image=new_photo)
    image_label.image = new_photo

# Set the default image
update_image("background.png", "background.png")

# Bind the buttons to update the image
button1.bind("<Button-1>", lambda event: update_image("image1.png", "background.png"))
button2.bind("<Button-1>", lambda event: update_image("image2.png", "background.png"))
button3.bind("<Button-1>", lambda event: update_image("image3.png", "background.png"))
button4.bind("<Button-1>", lambda event: update_image("image4.png", "background.png"))

# Run the main loop
root.mainloop()

