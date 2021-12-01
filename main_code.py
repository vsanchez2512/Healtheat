from tkinter import *
from tkinter import messagebox
import os
import functions
from PIL import ImageTk, Image






class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.title("Loveat")
        self.ruin(Entering)
        self.geometry('400x400')
        self.config(bg = "darkturquoise")


    def ruin(self, frame_class):
        ##Replaces the current frame with one chosen by the user.
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class Entering(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "darkturquoise")


        #Widgets for framing
        Label(self, text = "Welcome to LOVEAT!\n Do you want to Login or Register?"\
                      , bg="darkturquoise", fg="white").pack()

        # Import Logo
        logo = "logo.jpeg"
        img = Image.open(logo)
        imgResized = img.resize((150, 150), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(imgResized)
        image.photo = image
        logoLabel = Label(self, image=image)
        logoLabel.pack()


        Button(self, text = "Login", width = 25, command = lambda: master.ruin(Login)).pack(padx = 15, pady = 10)
        Button(self, text = "Register", width = 25, command = lambda: master.ruin(Register)).pack()
        Button(self, text = "Exit", width = 25, command = self.close).pack(padx = 15, pady = 15)



    def close(self):
        self.destroy()
        exit()

class Register(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "darkturquoise")



        def register_user():
            username_info = entryusername.get()
            password_info = entrypw.get()
            entryusername.delete(0, END)
            d

            file = open(username_info, "w")
            file.write(username_info + "\n")
            file.write(password_info + "\n")
            file.close()

            Label(register_user, text="Registration Success", fg="black", font=("calibri", 13)).pack()



        Label(self,text="Please enter details below to register", bg="white").pack()


        username = Label(self, text="Username: ", bg="darkturquoise", fg="white")
        username.pack()
        entryusername = Entry(self, width=25, bg="white")
        entryusername.pack()

        pw = Label(self, text="Password: ", bg="darkturquoise", fg="white")
        pw.pack()
        entrypw = Entry(self, width=25, bg="white")
        entrypw.pack()

        save = Button(self, text="Save", width=10, command=register_user)
        save.pack(padx=15, pady=15)

        self.button = Button(self, text="Back", width=8, bg="white", fg="black",
                             command=lambda: master.ruin(Login))
        self.button.pack(padx=15, pady=15)






class Login(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "darkturquoise")


        def login_verify():
            username1 = entryusername.get()
            password1 = entrypw.get()
            entryusername.delete(0, END)
            entrypw.delete(0, END)

            list_of_files = os.listdir()
            if username1 in list_of_files:
                file1 = open(username1, "r")
                verify = file1.read().splitlines()
                if password1 in verify:
                    Label(self, text="Login Success").pack()
                    Button(self, text="OK", command=lambda: master.ruin(Main_menu)).pack()


                else:
                    Label(self, text="Invalid Password ").pack()
                    Button(self,  text="OK").pack(padx=15, pady=15)



            else:
                Label(self, text="User Not Found").pack()
                Button(self, text="OK").pack(padx=15, pady=15)





        Label(self,text="Welcome back to the sign-in page! ", bg="white").pack()


        username = Label(self, text="Username: ", bg="darkturquoise", fg="white")
        username.pack()
        entryusername = Entry(self, width=25, bg="white")
        entryusername.pack()

        pw = Label(self, text="Password: ", bg="darkturquoise", fg="white")
        pw.pack()
        entrypw = Entry(self, width=25, bg="white")
        entrypw.pack()

        enter = Button(self, text="Enter", width=10, command=login_verify)
        enter.pack(padx=15, pady=15)

        self.button = Button(self, text = "Back", width = 10, bg="white", fg="black", command = lambda: master.ruin(Entering))
        self.button.pack(padx = 15, pady = 15)


class Main_menu(Frame):
    #Main menu
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "darkturquoise")

        #Widgets for framing
        Label(self, text = "Welcome to the main page!\n Choose an option..."\
                      , bg="darkturquoise", fg="white").pack()

        Button(self, text = "Macro Calculator", width = 25, command = lambda: master.ruin(Nutri_calc)).pack(padx = 15, pady = 15)
        Button(self, text = "Add an Aliment", width = 25, command = lambda: master.ruin(Add_list)).pack()
        Button(self, text = "BMI Calculator", width = 25, command = lambda: master.ruin(BMI)).pack(padx = 15, pady = 15)
        Button(self, text = "Exit", width = 25, command = self.close).pack(padx = 15, pady = 15)


    def close(self):
        self.destroy()
        exit()


class Nutri_calc(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "darkturquoise")

        def check():
            #verifying the input of the user
            product = entryProduct.get()
            gram = entryGram.get()
            output.delete(0.0, END)

            Error = False
            try:
                gram = int(entryGram.get())
            except:
                Error = True
            try:
                int(product)
                Error = True
            except:
                pass
            if Error == True:
                messagebox.showerror("Error", "Please provide accurate information!")
            else:
                functions.Open_file()
                output.insert(END, functions.macro(product, gram))

        #Widgets for framing
        Label(self, text ="Of which product do you want to get the details?", bg="darkturquoise", fg="white").pack()
        # user input, product
        Label(self, text = "Name of you product: ", bg="darkturquoise", fg="white").pack()
        entryProduct = Entry(self, width = 25, bg = "white")
        entryProduct.pack()
        # user input, amount
        Label(self, text = "Amount in grams: ",bg="darkturquoise", fg="white").pack()
        entryGram = Entry(self, width = 25, bg = "white")
        entryGram.pack()
        # submit
        submit = Button(self, text = "Submit", width = 10, command = check)
        submit.pack(padx = 15, pady = 15)
        # output
        Label(self, text = "These are the nutrition values:", bg="darkturquoise", fg="white").pack()
        output = Text(self, width = 25, height = 8, wrap = WORD, bg = "white")
        output.pack()
        #going back to menu
        self.button = Button(self, text = "Back", width = 10, bg="white", fg="black", command = lambda: master.ruin(Main_menu))
        self.button.pack(padx = 15, pady = 15)


class Add_list(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "darkturquoise")

        def validate():
            #verifying the input of the user
            def write(name, kcal, protein, carb, fat):
                # add the food to the list
                file = open("./Products.csv", "a")
                productValue = "%s,%s:%s:%s:%s" % (name, kcal, protein, carb, fat)
                file.write("\n" + productValue)
                file.close()
                #Emptying inputs
                nameEntry.delete(0, END)
                kcalEntry.delete(0, END)
                proteinEntry.delete(0, END)
                carbEntry.delete(0, END)
                fatEntry.delete(0, END)

            error = False
            # kcal, protein, carbohydrate, and fat are all numbers, and productName is a string
            try:
                name = int(nameEntry.get())
                error = True
            except:
                 name = nameEntry.get()
            try:
                kcal = int(kcalEntry.get())
                protein = int(proteinEntry.get())
                carb = int(carbEntry.get())
                fat = int(fatEntry.get())
            except:
                error = True
            if error == True:
                messagebox.showerror("Error", "Please provide accurate information!")
            else:
                #writing to a file
                write(name, kcal, protein, carb, fat)

        #Widgets for framing
        Label(self, text ="Enter the product's name and nutritional information  "\
                "\n per 100 gram", bg="darkturquoise", fg="white").pack()
        Label(self, text = "Name of the aliment:", bg="darkturquoise", fg="white").pack()
        nameEntry = Entry(self, width = 25, bg = "white")
        nameEntry.pack()

        Label(self, text = "Calories (kcal):", bg="darkturquoise", fg="white").pack()
        kcalEntry = Entry(self, width = 25, bg = "white")
        kcalEntry.pack()

        Label(self, text = "Protein (g):", bg="darkturquoise", fg="white").pack()
        proteinEntry = Entry(self, width = 25, bg = "white")
        proteinEntry.pack()

        Label(self, text = "Carbs(g):", bg="darkturquoise", fg="white").pack()
        carbEntry = Entry(self, width = 25, bg = "white")
        carbEntry.pack()

        Label(self, text = "Fat (g):", bg="darkturquoise", fg="white").pack()
        fatEntry = Entry(self, width = 25, bg = "white")
        fatEntry.pack()

        submit = Button(self, text = "Submit", width = 10, command = validate)
        submit.pack(padx = 15, pady = 15)

        button3 = Button(self, text = "Back", width = 25,bg="white", fg="black", command = lambda: master.ruin(Main_menu))
        button3.pack(padx = 15, pady = 15)

class BMI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "darkturquoise")

        def calculate_bmi():
            try:
                height = entryheight.get()
                weight = entryweight.get()
                height = float(height) / 100.0
                bmi = float(weight) / (height ** 2)
            except ZeroDivisionError:
                messagebox.showinfo("Result", "Please enter a real height!")
            except ValueError:
                messagebox.showinfo("Result", "Please provide accurate information!")
            else:
                if bmi <= 15.0:
                    res = "Your BMI is " + str(bmi) + "\nRemarks: Very Undernourished, be careful!! Loveat could help you."
                    messagebox.showinfo("Result", res)
                elif 15.0 < bmi <= 16.0:
                    res = "Your BMI is " + str(bmi) + "\nRemarks: Severely skinny!"
                    messagebox.showinfo("Result", res)
                elif 16.0 < bmi < 18.5:
                    res = "Your BMI is " + str(bmi) + "\nRemarks: Skinny!"
                    messagebox.showinfo("Result", res)
                elif 18.5 <= bmi <= 25.0:
                    res = "Your BMI is " + str(bmi) + "\nRemarks: Average"
                    messagebox.showinfo("Result", res)
                elif 25.0 < bmi <= 30:
                    res = "Your BMI is " + str(bmi) + "\nRemarks: Corpulent"
                    messagebox.showinfo("Result", res)
                elif 30.0 < bmi <= 35.0:
                    res = "Your BMI is " + str(bmi) + "\nRemarks: Overweight"
                    messagebox.showinfo("Result", res)
                elif 35.0 < bmi <= 40.0:
                    res = "Your BMI is " + str(bmi) + "\nRemarks: Obese"
                    messagebox.showinfo("Result", res)
                else:
                    res = "Your BMI is " + str(bmi) + "\nRemarks: It is time to use Loveat more! You are way too heavy!"
                    messagebox.showinfo("Result", res)


        #Widgets for framing
        Label(self, text="Heyy! Welcome to your BMI Calculator!!", bg="darkturquoise", fg="white").pack()
        # user input, product
        Label(self, text="How much do you weight?(Weight-kg)", bg="darkturquoise", fg="white").pack()
        entryweight = Entry(self, width=25, bg="white")
        entryweight.pack()
        # user input, amount
        Label(self, text="How tall are you? (Height-cm)", bg="darkturquoise", fg="white").pack()
        entryheight = Entry(self, width=25, bg="white")
        entryheight.pack()
        # enter
        enter = Button(self, text="Enter", width=8, command=calculate_bmi)
        enter.pack(padx=15, pady=15)
        # back to main menu
        self.button = Button(self, text="Back", width=8, bg="white", fg="black", command=lambda: master.ruin(Main_menu))
        self.button.pack(padx=15, pady=15)

if __name__ == "__main__":
    loveat = Application()
    loveat.mainloop()