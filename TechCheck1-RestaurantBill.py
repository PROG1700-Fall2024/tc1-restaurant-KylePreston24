#PROG 1700 – Tech Check #1
#Variables, Operators, Input/Output & Casting

# Restaurant Bill 
# You will create a console-based Python program that will calculate the amount of the tip, the tax, and the 
# total amount of a restaurant bill. The program will prompt the user to input the original amount of the bill. 
# The program will then output the amount of the tax (15% of the original amount) and a tip (20% of the original amount). 
# Finally, the program will output the new total of the bill.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
#    code for applying in meal cost
    meal = float(input("Enter in meal cost amount"))

    #tax rate is 15% of meal cost, or meal *0.15
    tax = meal * (15/100)



    # Tip amount for this program is 20% of meal cost or meal * 0.20
    tip= meal * (20/100)


    # code for total amount

    total = meal + tax + tip

     print("Tax Amount", tax)
    print("Tip Amount", tip)
    print("Total Amount", total)








    # YOUR CODE ENDS HERE

main()