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
        return(convert(num//1000000)+"million, "+convert((num%1000000)//1000)+"thousand, "+convert((num%1000)%1000))
    if 9 < l <= 12:
        return(convert(num//1000000000)+"billion, "+convert((num%1000000000)//1000000)+"million, "+convert(((num%1000000000)%1000000)//1000)+"thousand, "+convert((num%1000)%1000))
    if 12 < l <= 15:
        return(convert(num//1000000000000)+"trillion, "+convert((num%1000000000000)//1000000000)+"billion, "+convert((num%1000000000)//1000000)+"million, "+convert(((num%1000000000)%1000000)//1000)+"thousand, "+convert((num%1000)%1000))
    
ans = "Y"
while ans.lower() == "y":
    try:
        num = int(input("Input a number to convert: "))
        print(num_to_words(num))
        ans = input("Type 'Y' or 'y' to continue and any other key to quit: ")
    except ValueError:
        print("Please enter a correct number!!!")
        ans = input("Type 'Y' or 'y' to continue and any other key to quit: ")
