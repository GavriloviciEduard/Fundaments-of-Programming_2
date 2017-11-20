import os
import test.apd
import test.apd_np
import domain.vec_o
import ui.in_out_functions
import domain.vec_o_npy
 

NULL='NULL'


def menu():    
    
    """
        menu=>
            IN: -
            OUT: -
            DESC: The function creates a menu.
    """
    
   
    repo=ui.in_out_functions.read_repo()
    
    while True:

        os.system("cls")
        
        print("-----------------------------MENU-----------------------------\n")
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
        

def menu_numpy():
    
    """
        menu_numpy=>
            IN: -
            OUT: -
            DESC: The function creates a menu.
    """
    
   
    repo=ui.in_out_functions.read_repo()
    
    while True:

        os.system("cls")
        
        print("-----------------------------NUMPY-MENU-----------------------------\n")
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
            test.apd_np.test_add_scalar_and_vector_numpy()
            s=ui.in_out_functions.read_scalar()
            v=ui.in_out_functions.read_vector()
            repo.append(v)
            for v in repo:
                rez=domain.vec_o_npy.add_scalar_and_vector_numpy(v,s)
                print(v,"+",s,"=",rez)

        elif opt=='2':
            test.apd_np.test_add_vectors_numpy()
            v1=ui.in_out_functions.read_vector()
            for v2 in repo:
                rez=domain.vec_o_npy.add_vectors_numpy(v1, v2)
                if rez!=NULL:
                    print(v1,"+",v2,"=",rez)
                else:
                    print("Operation failed!")
        
        elif opt=='3':
            test.apd_np.test_sub_vectors_numpy()
            v1=ui.in_out_functions.read_vector()
            for v2 in repo:
                rez=domain.vec_o_npy.sub_vectors_numpy(v1, v2)
                if rez!=NULL:
                    print(v1,"-",v2,"=",rez)
                else:
                    print("Operation failed!")
        
        elif opt=='4':
            test.apd_np.test_mult_vectors_numpy()
            v1=ui.in_out_functions.read_vector()
            for v2 in repo:
                rez=domain.vec_o_npy.mult_vectors_numpy(v1, v2)
                if rez!=NULL:
                    print(v1,"*",v2,"=",rez)
                else:
                    print("Operation failed!")
                
        elif opt=='5':
            test.apd_np.test_sum_vector_numpy()
            v=ui.in_out_functions.read_vector()
            rez=domain.vec_o_npy.sum_vector_numpy(v)
            print("The sum of",v,"is",rez)
            for v in repo:
                rez=domain.vec_o_npy.sum_vector_numpy(v)
                print("The sum of",v,"is",rez)
                
            
        elif opt=='6':
            test.apd_np.test_prod_vector_numpy()
            v=ui.in_out_functions.read_vector()
            rez=domain.vec_o_npy.prod_vector_numpy(v)
            print("The product of",v,"is",rez)
            for v in repo:
                rez=domain.vec_o_npy.prod_vector_numpy(v)
                print("The product of",v,"is",rez)
                
            
        elif opt=='7':
            test.apd_np.test_avg_vector_numpy()
            v=ui.in_out_functions.read_vector()
            rez=domain.vec_o_npy.avg_vector_numpy(v)
            print("The average of",v,"is",rez)
            for v in repo:
                rez=domain.vec_o_npy.avg_vector_numpy(v)
                print("The average of",v,"is",rez)
                
                
            
        elif opt=='8':
            test.apd_np.test_min_vector_numpy()
            v=ui.in_out_functions.read_vector()
            rez=domain.vec_o_npy.min_vector_numpy(v)
            print("The minimum of",v,"is",rez)
            for v in repo:
                rez=domain.vec_o_npy.min_vector_numpy(v)
                print("The minimum of",v,"is",rez)
                
            
        elif opt=='9':
            test.apd_np.test_max_vector_numpy()
            v=ui.in_out_functions.read_vector()
            rez=domain.vec_o_npy.max_vector_numpy(v)
            print("The maximum of",v,"is",rez)
            for v in repo:
                rez=domain.vec_o_npy.max_vector_numpy(v)
                print("The maximum of",v,"is",rez)
                
            
        
        elif opt=='0':
            break
            
        else:
            print("Option not found! Try again!")
        
        input("Press any key...")
    
        
        
def select():
    
        
    opt=input("If you want to use Numpy press 'n/N':")
        
    if opt=='n' or opt=='N':
        menu_numpy()
            
    else:
        menu()
            
        
        

    
    
