
def read_vector():
    
    """
    read_vector=>
                input:-
                output: A list of integers 'vector'.
                desc.: The function reads and returns the a list of integers 'vector'.
    """

    vector=[]

    n=0

    while True:
        try:
            while not(n):
                n=int(input("Give the number of elements of the vector:"))
            break
        except ValueError :
            print("Not a valid value! Try again!")

    while n:
        while True:
            try:
                x=int(input("Give an element of the vector:"))
                vector.append(x)
                n-=1
                break
            except ValueError :
                print("Not a valid value! Try again!")
                
                
        


    return vector

def read_scalar():
    
    """
    read_scalar=>
                input:-
                output: An integer 's'.
                desc.: The function reads and returns an integer 's'.
    """
    
    while True:
        try:
            s=int(input("Give a scalar:"))
            return s
        except ValueError:
            print("Not a valid value! Try again!")

    