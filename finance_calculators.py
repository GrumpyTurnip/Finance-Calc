#This is a program to compute financial infomation in two ways: 
# 1) Investment interest, Both simple and compount
# 2) Bond repayment, using value, fixed interest rate and term.
print ("Hello, welcome to your financial calculator simulation, which of the following would you like to look at ?\n Investment - to calculate the amount of interest you'll earn on your investment \n Bond - to calculate the amount you'll have to pay on a home loan \n \n Enter either 'investment' or 'bond' from the menu above to proceed:")
#Asks user for desired menu input, defines variables to check against
menu_selection = input("")
menu_inv = "investment"
menu_bond = "bond"
import math
#Selects calculation to run
if menu_selection.lower() == menu_inv:
    #Start of investment calc/loop. Defines user criteria based on the following inputs:
    deposit = float(input("Please enter the investment value (in pounds)"))
    interest_rate = 0.01*float(input("Please enter the interest rate (as a percentage)")) #puts % in decimal format
    term = int(input("Please enter the investment term (in whole years)")) #ensures a whole year is accounted for
    interest_type = input("Would you like this to be calculated as 'compound' interest ?\n(to answer yes input any character, otherwise leave blank and 'simple' interest will be used")
    if interest_type:
        #compound interest calc
        roi = deposit*math.pow((1+(interest_rate)),term)
        print("Your return over " +str(term)+" years is "+str(round(roi,2))) #prints roi statement in pounds and pence for the given term
    else:
        #simple interest calc
        roi = deposit*(1+(interest_rate*term))
        print("Your return over " +str(term)+" years is "+str(round(roi,2))) #similar to above

elif menu_selection.lower() == menu_bond:
    #Start of bond calc/loop. Defines user criteria based on inputs:
    loan = float(input("Please enter the bond/assest/home value (in pounds)"))
    interest_rate = 0.01*float(input("Please enter the repayment interest rate (as a percentage)")) #puts % in decimal format
    m_int_rate = interest_rate/12
    term = int(input("Please enter the repayment term (in months)")) #ensures a whole month is accounted for
    #repayment calculation
    repayment = (m_int_rate * loan)/(1 - (math.pow((1 + (m_int_rate)),-term)))
    print("Your monthly repayments would be " +str(round(repayment,2))+" over "+str(term) + " months") #similar to the above print statements
else:
    #User feedback if input isn't recognised.
    print ("\n Sorry, I didn't recognise the calculation you'd like to perform, please try again")

