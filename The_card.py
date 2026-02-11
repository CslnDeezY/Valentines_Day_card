import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence

class mainApp:
    
    bg_color = "#F26A8D"
    button_color_yes = "#3fa34d"
    button_hover_yes = "#3e8914"
    button_color_no = "#e5383b"
    button_hover_no = "#ba181b"
    simple_button_color = "#DD2D4A"
    simple_button_hover = "#880D1E"
    text_font = "Helvetica"
    text_color = "#fff3e6"
    text_size = 20
    text_format = "bold"
    
    
    
    def __init__(self, root):
        self.root = root
        self.root.title("For the most adorable Bulocika")
        self.root.geometry("1080x950")
        
        # Set appearance mode and color theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.root.configure(bg=self.bg_color)
        
        # Remove window border for rounded effect
        # self.root.overrideredirect(True)
        
        # init config
        self.initial_font_size_yes = 20
        self.initial_font_size_no = 20
        self.current_font_size_yes = self.initial_font_size_yes
        self.current_font_size_no = self.initial_font_size_no
        
        self.font_size_yes = (self.text_font, self.current_font_size_yes, self.text_format)
        self.font_size_no = (self.text_font, self.current_font_size_no, self.text_format)
        self.refused_count = 0;
        
        # animation timers
        self.after_id_start = None
        self.after_id_happy = None
        self.after_id_sad = None
        self.after_id_sad = None
        
        # dimensiuni butoane
        self.initial_yes_width = 100
        self.initial_yes_height = 50
        self.initial_no_width = 100
        self.initial_no_height = 50
        
        self.current_yes_width = self.initial_yes_width
        self.current_yes_height = self.initial_yes_height
        self.current_no_width = self.initial_no_width
        self.current_no_height = self.initial_no_height
        
        # setup the UI
        self.setup_initial_ui()
    
        
        
    # setup the UI
    def setup_initial_ui(self):
        
        # cancel any pending animation callbacks
        if self.after_id_start:
            self.root.after_cancel(self.after_id_start)
            self.after_id_start = None
        if self.after_id_happy:
            self.root.after_cancel(self.after_id_happy)
            self.after_id_happy = None
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # load the start image (static or animated GIF)
        try:
            img_start = Image.open("./Resources/waiting.gif")
            self.start_frame_delay = img_start.info.get("duration", 100)
            self.start_frames = [
                ImageTk.PhotoImage(frame.copy().resize((480, 480)))
                for frame in ImageSequence.Iterator(img_start)
            ]
            self.start_frame_index = 0
            self.photo_start = self.start_frames[0] if self.start_frames else None
        except Exception:
            self.start_frames = []
            self.photo_start = None
            
        # initialize the start label
        self.start_label = tk.Label(self.root, text="Whant you to be my valentine?", font=(self.text_font, self.text_size*2, self.text_format), bg=self.bg_color, fg=self.text_color)
        self.start_label.pack(pady=50)

        # show the GIF if it loaded
        self.image_label = tk.Label(self.root, image=self.photo_start, bg=self.bg_color)
        if self.photo_start:
            self.image_label.pack(pady=10)
            if len(self.start_frames) > 1:
                self.after_id_start = self.root.after(self.start_frame_delay, self.animate_gif)
        
        # create the buttons
        button_frame = ctk.CTkFrame(self.root, fg_color="transparent", bg_color="transparent")
        button_frame.pack(pady=40)
        
        # the Yes button
        self.yes_button = ctk.CTkButton(button_frame, text="Yes", 
                       font=self.font_size_yes, text_color=self.text_color,
                                   fg_color=self.button_color_yes, hover_color=self.button_hover_yes,
                                   corner_radius=30,
                                   width=self.current_yes_width, height=self.current_yes_height, 
                                   command=self.yes_clicked)
        self.yes_button.grid(row=0, column=0, padx=20)
        
        # the No button
        self.no_button = ctk.CTkButton(button_frame, text="No", 
                       font=self.font_size_no, text_color=self.text_color,
                                   fg_color=self.button_color_no, hover_color=self.button_hover_no,
                                   corner_radius=30,
                                   width=self.current_no_width, height=self.current_no_height, 
                                   command=self.no_clicked)
        self.no_button.grid(row=0, column=1, padx=20)
        
        
        
        
    # animating the start gif
    def animate_gif(self):
        if not self.start_frames or not self.image_label.winfo_exists():
            return
        self.start_frame_index = (self.start_frame_index + 1) % len(self.start_frames)
        self.image_label.configure(image=self.start_frames[self.start_frame_index])
        self.after_id_start = self.root.after(self.start_frame_delay, self.animate_gif)
    
    # animating the happy gif
    def animate_happy_gif(self):
        if not self.happy_frames or not self.happy_image_label.winfo_exists():
            return
        self.happy_frame_index = (self.happy_frame_index + 1) % len(self.happy_frames)
        self.happy_image_label.configure(image=self.happy_frames[self.happy_frame_index])
        self.after_id_happy = self.root.after(self.happy_frame_delay, self.animate_happy_gif)
    
    # animating the sad gif
    def animate_sad_gif(self):  
        if not self.sad_frames or not self.sad_image_label.winfo_exists():
            return
        self.sad_frame_index = (self.sad_frame_index + 1) % len(self.sad_frames)
        self.sad_image_label.configure(image=self.sad_frames[self.sad_frame_index])
        self.after_id_sad = self.root.after(self.sad_frame_delay, self.animate_sad_gif)
        
    def yes_clicked(self):  
        self.show_success_screen()
        
        
    def no_clicked(self):
        # reduce the size of the No button by 20%
        self.current_no_width = int(self.current_no_width * 0.8)
        self.current_no_height = int(self.current_no_height * 0.8)
        
        # increase the size of the Yes button by 20%
        self.current_yes_width = int(self.current_yes_width * 1.2)
        self.current_yes_height = int(self.current_yes_height * 1.2)
        
        # adjust font sizes proportionally
        self.current_font_size_no = max(8, int(self.initial_font_size_no * (self.current_no_width / self.initial_no_width)))
        self.current_font_size_yes = int(self.initial_font_size_yes * (self.current_yes_width / self.initial_yes_width))
        
        # check if the No button has reached 20% or less of its initial size
        if self.current_no_width <= self.initial_no_width * 0.2 or self.current_no_height <= self.initial_no_height * 0.2:
            self.show_error_screen()
        else:
            # update the button sizes and fonts
            self.no_button.configure(
                width=self.current_no_width, 
                height=self.current_no_height,
                font=(self.text_font, self.current_font_size_no, self.text_format)
            )
            self.yes_button.configure(
                width=self.current_yes_width, 
                height=self.current_yes_height,
                font=(self.text_font, self.current_font_size_yes, self.text_format)
            )


    def show_success_screen(self):
        # resize the window for the success screen
        self.root.geometry("900x800")
        
        # cancel any pending animation callbacks
        if self.after_id_start:
            self.root.after_cancel(self.after_id_start)
            self.after_id_start = None
        if self.after_id_happy:
            self.root.after_cancel(self.after_id_happy)
            self.after_id_happy = None
        
        # clear the current UI
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Happy GIF 
        try:
            img_happy = Image.open("./Resources/goodGirl.gif")
            self.happy_frame_delay = img_happy.info.get("duration", 100)
            self.happy_frames = [
                ImageTk.PhotoImage(frame.copy().resize((300, 300)))
                for frame in ImageSequence.Iterator(img_happy)
            ]
            self.happy_frame_index = 0
            self.photo_happy = self.happy_frames[0] if self.happy_frames else None
        except Exception:
            self.happy_frames = []
            self.photo_happy = None

        success_label = tk.Label(self.root, text="Yay! 💕", 
                                font=(self.text_font, 48, self.text_format),
                                bg=self.bg_color, fg=self.text_color)
        success_label.pack(pady=50)
        
        # show the happy GIF if it loaded
        self.happy_image_label = tk.Label(self.root, image=self.photo_happy, bg=self.bg_color)
        if self.photo_happy:
            self.happy_image_label.pack(pady=10)
            if len(self.happy_frames) > 1:
                self.after_id_happy = self.root.after(self.happy_frame_delay, self.animate_happy_gif)
        
        
        message_label = tk.Label(self.root, 
                                text="You made my day!\nI love you so much! 💖", 
                                font=(self.text_font, self.text_size, self.text_format),
                                bg=self.bg_color, fg=self.text_color,
                                justify="center")
        message_label.pack(pady=30)
        
        # button to close the application
        close_button = ctk.CTkButton(self.root, text="Close", 
                                    font=(self.text_font, self.text_size, self.text_format),
                                    text_color=self.text_color,
                                    fg_color=self.simple_button_color, 
                                    hover_color=self.simple_button_hover,
                                    corner_radius=30,
                                    width=150, height=60,
                                    command=self.root.destroy)
        close_button.pack(pady=50)
        
    def show_error_screen(self):
        # resize the window for the error screen
        self.root.geometry("900x700")
        
        # cancel any pending animation callbacks
        if self.after_id_start:
            self.root.after_cancel(self.after_id_start)
            self.after_id_start = None
        if self.after_id_happy:
            self.root.after_cancel(self.after_id_happy)
            self.after_id_happy = None
        if self.after_id_sad:
            self.root.after_cancel(self.after_id_sad)
            self.after_id_sad = None
        
        # clear the current UI
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # load sad GIF
        try:
            img_sad = Image.open("./Resources/Error.gif")
            self.sad_frame_delay = img_sad.info.get("duration", 100)
            self.sad_frames = [
                ImageTk.PhotoImage(frame.copy().resize((300, 300)))
                for frame in ImageSequence.Iterator(img_sad)
            ]
            self.sad_frame_index = 0
            self.photo_sad = self.sad_frames[0] if self.sad_frames else None
        except Exception:
            self.sad_frames = []
            self.photo_sad = None
        
        # show the sad GIF if it loaded
        self.sad_image_label = tk.Label(self.root, image=self.photo_sad, bg=self.bg_color)
        if self.photo_sad:
            self.sad_image_label.pack(pady=10)
            if len(self.sad_frames) > 1:
                self.after_id_sad = self.root.after(self.sad_frame_delay, self.animate_sad_gif)
        
        
        message_label = tk.Label(self.root, 
                                text="I guess you don't want to be my valentine. Goodbye! 💔\nI'm going to wipe your operating system!", 
                                font=(self.text_font, self.text_size, self.text_format),
                                bg=self.bg_color, fg=self.text_color,
                                justify="center")
        message_label.pack(pady=30)
        
        # button to close the application
        close_button = ctk.CTkButton(self.root, text="sudo rm -rf /", 
                                    font=(self.text_font, self.text_size, self.text_format),
                                    text_color=self.text_color,
                                    fg_color=self.simple_button_color, 
                                    hover_color=self.simple_button_hover,
                                    corner_radius=30,
                                    width=150, height=60,
                                    command=self.root.destroy)
        close_button.pack(pady=50)
        
# Start Application
if __name__ == "__main__":
    root = tk.Tk()
    app = mainApp(root)
    root.mainloop()