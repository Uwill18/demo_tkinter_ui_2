import tkinter

if __name__ == '__main__':
    window = tkinter.Tk()
    window.title("WGUPS DELIVERY TRACKER")
    window.geometry('600x400')
    window.configure(bg="black")


    def bonjour():
        print("Bonjour Le Monde!")
        salutations()


    def salutations():
        print("And Salutations " + "NEW USER" + "!")


    frame = tkinter.Frame(window)
    frame.pack()
    frame.configure(bg="black")

    label = tkinter.Label(frame, text="DELIVERY STATUS", bg="white", fg="blue", width=75)
    label.grid(row=0, column=0, columnspan=3,  pady=20)
    button = tkinter.Button(frame, text="ALL PACKAGES", bg="#003057", fg="silver", activebackground="#327DA9",
                            activeforeground="white", width=75, command=bonjour)
    button.grid(row=2, column=0, columnspan=3, pady=20)
    button2 = tkinter.Button(frame, text="DELIVERED", bg="#003057", fg="silver", activebackground="#327DA9",
                             activeforeground="white", width=75, command=bonjour)
    button2.grid(row=4, column=0, columnspan=3, pady=20)
    button3 = tkinter.Button(frame, text="EN ROUTE", bg="#003057", fg="silver", activebackground="#327DA9",
                             activeforeground="white", width=75, command=bonjour)
    button3.grid(row=6, column=0, columnspan=3, pady=20)
    button4 = tkinter.Button(frame, text="AT HUB", bg="#003057", fg="silver", activebackground="#327DA9",
                             activeforeground="white", width=75, command=bonjour)
    button4.grid(row=8, column=0, columnspan=3, pady=20)

    window.mainloop()
