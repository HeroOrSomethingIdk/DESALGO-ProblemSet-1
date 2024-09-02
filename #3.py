def gcdCalculator(a, b):

    if b == 0: #Stops the recrusion since if one number becomes 0, the other is the GCD
        return a
    else:
        return gcdCalculator(b, a % b) #if b is not 0, the function recursively calls itself with b and a % b, 
                                       #continuing until b is 0, at which point a is returned as the GCD.


a = int(input("Enter the first number: ")) #User inputs
b = int(input("Enter the second number: "))

gcdResult = gcdCalculator(a, b) #Calls the gcdCalculator function
print(f"The GCD of {a} and {b} is {gcdResult}") # Prints the result# for question 3
