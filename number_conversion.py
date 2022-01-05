# Adding GUI using the Tkinter module
import tkinter as tk
from types import NoneType


# Python program to print a given number in words

# string at index 0 is not used. This is to make list indexing easier 
one = [ "","one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ",
        "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ",
        "sixteen ", "seventeen ", "eighteen ", "nineteen "]

# strings at index 0 and 1 are not used. Still to maker list indexing easier
tens = [ "", "", "twenty ", "thirty ", "forty ",
        "fifty ", "sixty ", "seventy ", "eighty ",
        "ninety "]
def convert(num):
    num_string = str(num)
    l = len(num_string)
    if l < 3:
            if num//10 < 2:
                return(one[num])
            else:
                return(tens[num//10] + "" + one[num%10])
        
    # For numbers between 100 - 999
    if l == 3:
        if num%100 < 20:
            return(one[num//100]+"hundred and "+"" + one[num%100])
        else:
            return(one[num//100]+"hundred and "+tens[(num%100)//10] + "" + one[(num%100)%10])

def num_to_words(num):
    num_string = str(num)
    l = len(num_string)

    if num == 0:
        return("Zero")
    # For numbers between 1-99
    if l < 3:
        if num//10 < 2:
            return(one[num])
        else:
            return(tens[num//10] + "" + one[num%10])
    
    # For numbers between 100 - 999
    if l == 3:
        if num%100 < 20:
            return(one[num//100]+"hundred and "+"" + one[num%100])
        else:
            return(one[num//100]+"hundred and "+tens[(num%100)//10] + "" + one[(num%100)%10])

    # Numbers between 1,000 - 999,999
    if 3 < l <= 6:
        if num%1000 == 0:
            return(convert(num//1000)+"thousand")
        return(convert(num//1000)+"thousand, "+convert(num%1000))
    if 6 < l <= 9:
        if num%1000000 == 0:
            return(convert(num//1000000)+"million")
        if (num%1000000)%1000 == 0:
            return(convert(num//1000000)+"million, "+convert((num%1000000)//1000)+"thousand")
        if (num%1000000)%1000 == 0:
                return(convert(num//1000000)+"million, "+convert((num%1000)%1000))
        return(convert(num//1000000)+"million, "+convert((num%1000000)//1000)+"thousand, "+convert((num%1000)%1000))
    if 9 < l <= 12:
        if num%1000000000 == 0:
            return(convert(num//1000000000)+"billion")
        if (num%1000000000)%1000000 == 0:
            return(convert(num//1000000000)+"billion, "+convert((num%1000000000)//1000000)+"million")
        if ((num%1000000000)%1000000)%1000 == 0:
            return(convert(num//1000000000)+"billion, "+convert((num%1000000000)//1000000)+"million, "+convert(((num%1000000000)%1000000)//1000)+"thousand")
        return(convert(num//1000000000)+"billion, "+convert((num%1000000000)//1000000)+"million, "+convert(((num%1000000000)%1000000)//1000)+"thousand, "+convert((num%1000)%1000))
    if 12 < l <= 15:
        if num%1000000000000 == 0:
            return(convert(num//1000000000000)+"trillion")
        if (num%1000000000000)%1000000000 == 0:
            return(convert(num//1000000000000)+"trillion, "+convert((num%1000000000000)//1000000000)+"billion")
        if ((num%1000000000000)%1000000000)%1000000 == 0:
            return(convert(num//1000000000000)+"trillion, "+convert((num%1000000000000)//1000000000)+"billion, "+convert(((num%1000000000000)%1000000000)//1000000)+"million")
        if (((num%1000000000000)%1000000000)%1000000)%1000 == 0:
            return(convert(num//1000000000000)+"trillion, "+convert((num%1000000000000)//1000000000)+"billion, "+convert(((num%1000000000000)%1000000000)//1000000)+"million, "+convert(((num%1000000000)%1000000)//1000)+"thousand")
        return(convert(num//1000000000000)+"trillion, "+convert((num%1000000000000)//1000000000)+"billion, "+convert((num%1000000000)//1000000)+"million, "+convert(((num%1000000000)%1000000)//1000)+"thousand, "+convert((num%1000)%1000))

root = tk.Tk()   # Opens the GUI window
root.title = ("Number converter")


instructions = tk.Label(root, text="Python program to print a given number in words. Enter the number you want to convert", font="Raleway")
instructions.grid(columnspan=3, column=0, row=0)

my_input = tk.Entry(root, width=50, borderwidth=5)
my_input.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

def return_entry():
    """Gets and prints the content of the entry"""
    try:
        content = int(my_input.get())
        return content
    except:
        text_box = tk.Text(root, height=5, width=50, padx=15, pady=15)
        text_box.insert(1.0, "Please enter a real number")
        text_box.grid(column=1, row=3)

def printing():
    try:
        x = return_entry()
        y = num_to_words(x)
        text_box = tk.Text(root, height=5, width=50, padx=15, pady=15)
        text_box.insert(1.0, y)
        text_box.grid(column=1, row=3)
        print(y)
    except TypeError:
        text_box = tk.Text(root, height=5, width=50, padx=15, pady=15)
        text_box.insert(1.0, "Please enter a real number")
        text_box.grid(column=1, row=3)

convert_button = tk.Button(root, text="Convert", padx=30, pady=15, command=printing)
convert_button.grid(row=2, column=1, )

root.mainloop()     # Closes the GUI window
