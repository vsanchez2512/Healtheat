from tkinter import *
from tkinter import messagebox
import os
import functions






class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.title("Healtheat")
        self.switch(Entering)
        self.geometry('400x400')
        self.config(bg = "black")


    def switch(self, frame_class):
        """Destroys current frame and replaces it with a chosen by the user"""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class Entering(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")

        """Frame widgets"""
        label = Label(self, text = "Welcome to HEALTHEAT!\n DO you want to Login or Register?"\
                      , bg = "black", fg = "white")
        label.pack()
        button = Button(self, text = "Login", width = 20, command = lambda: master.switch(Login))
        button.pack(padx = 10, pady = 10)
        button2 = Button(self, text = "Register", width = 20, command = lambda: master.switch(Register))
        button2.pack()
        button4 = Button(self, text = "Exit", width = 20, command = self.close)
        button4.pack(padx = 10, pady = 10)

    def close(self):
        """Close the app"""
        self.destroy()
        exit()

class Register(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")



        def register_user():
            username_info = entryusername.get()
            password_info = entrypw.get()
            entryusername.delete(0, END)
            entrypw.delete(0, END)

            file = open(username_info, "w")
            file.write(username_info + "\n")
            file.write(password_info + "\n")
            file.close()

            Label(register_user, text="Registration Success", fg="black", font=("calibri", 12)).pack()



        Label(self,text="Please enter details below to Register", bg="white").pack()
        Label(self,text="").pack()

        username = Label(self, text="Username: ", bg="black", fg="white")
        username.pack()
        entryusername = Entry(self, width=20, bg="white")
        entryusername.pack()

        pw = Label(self, text="Password: ", bg="black", fg="white")
        pw.pack()
        entrypw = Entry(self, width=20, bg="white")
        entrypw.pack()

        save = Button(self, text="Save", width=8, command=register_user)
        save.pack(padx=10, pady=10)

        self.button = Button(self, text="Back", width=8, bg="white", fg="black",
                             command=lambda: master.switch(Login))
        self.button.pack(padx=10, pady=10)






class Login(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")


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
                    Button(self, text="OK", command=lambda: master.switch(Menu)).pack()


                else:
                    Label(self, text="Invalid Password ").pack()
                    self.button = Button(self,  text="OK")
                    self.button.pack(padx=10, pady=10)



            else:
                Label(self, text="User Not Found").pack()
                self.button = Button(self, text="OK")
                self.button.pack(padx=10, pady=10)





        Label(self,text="Welcome back!", bg="white").pack()
        Label(self,text="").pack()

        username = Label(self, text="Username: ", bg="black", fg="white")
        username.pack()
        entryusername = Entry(self, width=20, bg="white")
        entryusername.pack()

        pw = Label(self, text="Password: ", bg="black", fg="white")
        pw.pack()
        entrypw = Entry(self, width=20, bg="white")
        entrypw.pack()

        enter = Button(self, text="Enter", width=8, command=login_verify)
        enter.pack(padx=10, pady=10)

        self.button = Button(self, text = "Back", width = 8, bg="white", fg="black", command = lambda: master.switch(Entering))
        self.button.pack(padx = 10, pady = 10)


class Menu(Frame):
    """Main menu"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")

        """Frame widgets"""
        label = Label(self, text = "Project Notes Presents Nutrition Calculator!\n Choose an option."\
                      , bg = "black", fg = "white")
        label.pack()
        button = Button(self, text = "Calculator", width = 20, command = lambda: master.switch(Calculator))
        button.pack(padx = 10, pady = 10)
        button2 = Button(self, text = "Add a product", width = 20, command = lambda: master.switch(File_Write))
        button2.pack()
        button3 = Button(self, text = "BMI Calculator", width = 20, command = lambda: master.switch(BMI))
        button3.pack(padx = 10, pady = 10)
        button4 = Button(self, text = "Exit", width = 20, command = self.close)
        button4.pack(padx = 10, pady = 10)


    def close(self):
        """Close the app"""
        self.destroy()
        exit()


class Calculator(Frame):
    """Writing nutritional values of the user defined food"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")

        def on_click():
            """Checking data and writing the results"""
            product = entryProduct.get()
            gram = entryGram.get()
            output.delete(0.0, END)

            Error = False
            try:
                gram = int(entryGram.get())
            except:
                Error = True
            try:
                x = int(product)
                Error = True
            except:
                pass
            if Error == True:
                messagebox.showerror("Error", "Please enter correct data!")
            else:
                functions.file_open()
                output.insert(END, functions.result(product, gram))

        """Frame widgets"""
        label = Label(self, text ="Enter a product that you ate.", bg = "black", fg = "white")
        label.pack()
        # user input, product
        label2 = Label(self, text = "Name: ", bg = "black", fg = "white")
        label2.pack()
        entryProduct = Entry(self, width = 20, bg = "white")
        entryProduct.pack()
        # user input, amount
        label3 = Label(self, text = "Amount: ", bg = "black", fg = "white")
        label3.pack()
        entryGram = Entry(self, width = 20, bg = "white")
        entryGram.pack()
        # submit
        submit = Button(self, text = "Submit", width = 8, command = on_click)
        submit.pack(padx = 10, pady = 10)
        # output
        label4 = Label(self, text = "These are the nutrition values:", bg = "black", fg = "white")
        label4.pack()
        output = Text(self, width = 20, height = 6, wrap = WORD, bg = "white")
        output.pack()
        #going back to menu
        self.button = Button(self, text = "Back", width = 8, bg="white", fg="black", command = lambda: master.switch(Menu))
        self.button.pack(padx = 10, pady = 10)


class File_Write(Frame):
    """User can add new new products and their values"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")

        def validate():
            """Checks is the user inputs correct data"""
            def write(name, kcal, protein, carb, fat):
                """Writes to file"""
                file = open("../../Downloads/PN-NutritionalCalculator/Products.txt", "a")
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
            # checking if kcal, protein, carb and fat are integers and productName is a string
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
                messagebox.showerror("Error", "Please enter correct data!")
            else:
                #writing to a file
                write(name, kcal, protein, carb, fat)

        """Frame widgets"""
        label = Label(self, text ="Enter the product name and its nutritional "\
                "values per 100 gram", bg = "black", fg = "white")
        label.pack()
        label1 = Label(self, text = "Name:", bg = "black", fg = "white")
        label1.pack()
        nameEntry = Entry(self, width = 20, bg = "white")
        nameEntry.pack()

        label2 = Label(self, text = "Calories:", bg = "black", fg = "white")
        label2.pack()
        kcalEntry = Entry(self, width = 20, bg = "white")
        kcalEntry.pack()

        label3 = Label(self, text = "Protein:", bg = "black", fg = "white")
        label3.pack()
        proteinEntry = Entry(self, width = 20, bg = "white")
        proteinEntry.pack()

        label4 = Label(self, text = "Carbs:", bg = "black", fg = "white")
        label4.pack()
        carbEntry = Entry(self, width = 20, bg = "white")
        carbEntry.pack()

        label5 = Label(self, text = "Fat:", bg = "black", fg = "white")
        label5.pack()
        fatEntry = Entry(self, width = 20, bg = "white")
        fatEntry.pack()

        submit = Button(self, text = "Submit", width = 8, command = validate)
        submit.pack(padx = 10, pady = 10)

        button3 = Button(self, text = "Back", width = 20,bg="white", fg="black", command = lambda: master.switch(Menu))
        button3.pack(padx = 10, pady = 10)

class BMI(Frame):
    """Writing nutritional values of the user defined food"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")

        def calculate_bmi(a=""):
            print(a)
            try:
                height = entryheight.get()
                weight = entryweight.get()
                height = float(height) / 100.0
                bmi = float(weight) / (height ** 2)
            except ZeroDivisionError:
                messagebox.showinfo("Result", "Please enter positive height!!")
            except ValueError:
                messagebox.showinfo("Result", "Please enter valid data!")
            else:
                if bmi <= 15.0:
                    res = "Your BMI is " + str(bmi) + "\nRemarks: Very severely underweight!!"
                    messagebox.showinfo("Result", res)
                elif 15.0 < bmi <= 16.0:
                    res = "Your BMI is " + str(bmi) + "\nRemarks: Severely underweight!"
                    messagebox.showinfo("Result", res)
                elif 16.0 < bmi < 18.5:
                    res = "Your BMI is " + str(bmi) + "\nRemarks: Underweight!"
                    messagebox.showinfo("Result", res)
                elif 18.5 <= bmi <= 25.0:
                    res = "Your BMI is " + str(bmi) + "\nRemarks: Normal."
                    messagebox.showinfo("Result", res)
                elif 25.0 < bmi <= 30:
                    res = "Your BMI is " + str(bmi) + "\nRemarks: Overweight."
                    messagebox.showinfo("Result", res)
                elif 30.0 < bmi <= 35.0:
                    res = "Your BMI is " + str(bmi) + "\nRemarks: Moderately obese!"
                    messagebox.showinfo("Result", res)
                elif 35.0 < bmi <= 40.0:
                    res = "Your BMI is " + str(bmi) + "\nRemarks: Severely obese!"
                    messagebox.showinfo("Result", res)
                else:
                    res = "Your BMI is " + str(bmi) + "\nRemarks: Super obese!!"
                    messagebox.showinfo("Result", res)


        """Frame widgets"""
        label = Label(self, text="Welcome to your BMI Calculator", bg="black", fg="white")
        label.pack()
        # user input, product
        label2 = Label(self, text="Weight (kg)", bg="black", fg="white")
        label2.pack()
        entryweight = Entry(self, width=20, bg="white")
        entryweight.pack()
        # user input, amount
        label3 = Label(self, text="Height(cm)", bg="black", fg="white")
        label3.pack()
        entryheight = Entry(self, width=20, bg="white")
        entryheight.pack()
        # submit
        submit = Button(self, text="Submit", width=8, command=calculate_bmi)
        submit.pack(padx=10, pady=10)
        # going back to menu
        self.button = Button(self, text="Back", width=8, bg="white", fg="black", command=lambda: master.switch(Menu))
        self.button.pack(padx=10, pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()