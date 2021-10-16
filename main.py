def d_vide(divident, divider):
    '''
    This function calculates
    quotient remainder 
    using subtraction method
    '''
    quotient = 0
    remainder = 0
    while divident >= divider: # 1
        quotient += 1 
        divident = divident - divider
        remainder = divident
    return quotient, remainder # 2

def main_program():
    try: 
        divident = int(input("Enter divident : ")) # 3
        divider = int(input("Enter divider : "))
        if divident <= 0 or divider <= 0: # 4
            raise Exception # 5 
        else:
            result = d_vide(divident, divider) # 6
            print("Quotient = " + repr(result[0]) + "\nRemainder = " + repr(result[1])) # 7
    except:
        CRED = '\033[91m' # 8 
        CEND = '\033[0m'
        print(CRED + "Input Error !" + CEND)
    
main_program() # 9 

# DOCUMENTAION
# 1. Loops till divident is not less than divider
# 2. multiple return, data type is tuple
# 3. user input as well as parsing into integer
# 4. ascertaining if input values are 0 or negative
# 5. it raises an exception for exception block
# 6. d_vide funciton is called and returned tuple is stored
# 7. result output
# 8. for color output
# 9. Executing the main program
