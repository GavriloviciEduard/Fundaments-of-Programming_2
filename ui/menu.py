import os
import test.apd
import domain.vec_o
import ui.in_out_functions

NULL='NULL'

repo=[]

def menu():    
    
    """
        menu=>
            IN: -
            OUT: -
            DESC: The function creates a menu.
    """
    
    global repo
    repo=ui.in_out_functions.read_repo()
    
    while True:

        os.system("cls")

        print("1.Add a scalar to a vector(the read vector is added to the repository).")
        print("2.Add two vectors.")
        print("3.Subtract two vectors.")
        print("4.Multiplication.")
        print("5.Sum of elements in a vector.")
        print("6.Product of elements in a vector.")
        print("7.Average of elements in a vector.")
        print("8.Minimum of a vector.")
        print("9.Maximum of a vector.")
        print("0.Exit")

        opt=input("Select an option:")

        if opt=='1':
            test.apd.test_add_scalar_and_vector()
            s=ui.in_out_functions.read_scalar()
            v=ui.in_out_functions.read_vector()
            repo.append(v)
            for v in repo:
                rez=domain.vec_o.add_scalar_and_vector(v,s)
                print(v,"+",s,"=",rez)

        elif opt=='2':
            test.apd.test_add_vectors()
            v1=ui.in_out_functions.read_vector()
            for v2 in repo:
                rez=domain.vec_o.add_vectors(v1, v2)
                if rez!=NULL:
                    print(v1,"+",v2,"=",rez)
                else:
                    print("Operation failed!")
        
        elif opt=='3':
            test.apd.test_sub_vectors()
            v1=ui.in_out_functions.read_vector()
            for v2 in repo:
                rez=domain.vec_o.sub_vectors(v1, v2)
                if rez!=NULL:
                    print(v1,"-",v2,"=",rez)
                else:
                    print("Operation failed!")
        
        elif opt=='4':
            test.apd.test_mult_vectors()
            v1=ui.in_out_functions.read_vector()
            for v2 in repo:
                rez=domain.vec_o.mult_vectors(v1, v2)
                if rez!=NULL:
                    print(v1,"*",v2,"=",rez)
                else:
                    print("Operation failed!")
                
        elif opt=='5':
            test.apd.test_sum_vector()
            v=ui.in_out_functions.read_vector()
            rez=domain.vec_o.sum_vector(v)
            print("The sum of",v,"is",rez)
            for v in repo:
                rez=domain.vec_o.sum_vector(v)
                print("The sum of",v,"is",rez)
                
            
        elif opt=='6':
            test.apd.test_prod_vector()
            v=ui.in_out_functions.read_vector()
            rez=domain.vec_o.prod_vector(v)
            print("The product of",v,"is",rez)
            for v in repo:
                rez=domain.vec_o.prod_vector(v)
                print("The product of",v,"is",rez)
                
            
        elif opt=='7':
            test.apd.test_avg_vector()
            v=ui.in_out_functions.read_vector()
            rez=domain.vec_o.avg_vector(v)
            print("The average of",v,"is",rez)
            for v in repo:
                rez=domain.vec_o.avg_vector(v)
                print("The average of",v,"is",rez)
                
                
            
        elif opt=='8':
            test.apd.test_min_vector()
            v=ui.in_out_functions.read_vector()
            rez=domain.vec_o.min_vector(v)
            print("The minimum of",v,"is",rez)
            for v in repo:
                rez=domain.vec_o.min_vector(v)
                print("The minimum of",v,"is",rez)
                
            
        elif opt=='9':
            test.apd.test_max_vector()
            v=ui.in_out_functions.read_vector()
            rez=domain.vec_o.max_vector(v)
            print("The maximum of",v,"is",rez)
            for v in repo:
                rez=domain.vec_o.max_vector(v)
                print("The maximum of",v,"is",rez)
                
            
        
        elif opt=='0':
            break
            
        else:
            print("Option not found! Try again!")
        
        input("Press any key...")
        

        

    
    
