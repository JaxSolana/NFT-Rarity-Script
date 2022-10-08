import tkinter as tk

def main():

    window= tk.Tk()
    window.title("Rarity Calculater")
    window.geometry("650x200")

    #text body
    label1 = tk.Label(window, text="Enter Trait Name:")

    label2 = tk.Label(window, text="Occurrences:")

    #location of text
    label1.place(x=50,y=30)
    label2.place(x=50,y=100)

    #Input field
    textbox1 = tk.Entry(window, width=40)

    #Location of Input field
    textbox1.place(x=200,y=32)

    #Empty text
    label3 = tk.Label(window, text=" ", fg='green', font='Helvetica 10 bold')

    #Location of empty text
    label3.place(x=180,y=100)

    #Functions for convertion
    def btn1_click():
        currentfile = 0
        Occurrences = 0
        endFilesPlusOne = 9999
        trait = textbox1.get()
        valuetrait = '"value": ' + '"' + trait + '"'

        while currentfile < endFilesPlusOne:
            file = str(currentfile) + ".json"

            # opening a text file
            file1 = open(file, "r")

            # setting flag and index to 0
            flag = 0

            # Loop through the file line by line
            for line in file1:

                # checking string is present in line or not
                if valuetrait in line:
                  flag = 1
                  break

            # checking condition for string found or not
            if flag == 1:
               Occurrences += 1

            # closing text file
            file1.close()
            currentfile += 1

        label3.configure(text = str(Occurrences))

    #Buttons
    btn1 = tk.Button(window, text="Get Occurrences", bg='green', fg='white', command=btn1_click)

    #Location of Button
    btn1.place(x=90,y=150)
    window.mainloop()


main()
