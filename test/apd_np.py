import domain.vec_o_npy

#TEST MODULE

def test_add_scalar_and_vector_numpy():

    assert domain.vec_o_npy.add_scalar_and_vector_numpy([1,2,3],2)==[3,4,5]
    assert domain.vec_o_npy.add_scalar_and_vector_numpy([1,2,3],0)==[1,2,3]
    assert domain.vec_o_npy.add_scalar_and_vector_numpy([1,2,3,4,5,6],10)==[11,12,13,14,15,16]
    assert domain.vec_o_npy.add_scalar_and_vector_numpy([1,2,3],-2)==[-1,0,1]
    assert domain.vec_o_npy.add_scalar_and_vector_numpy([0,0,0,0],3)==[3,3,3,3]


def test_add_vectors_numpy():

    assert domain.vec_o_npy.add_vectors_numpy([1,2,3],[2])=='NULL'
    assert domain.vec_o_npy.add_vectors_numpy([1,2,3],[1,2,3])==[2,4,6]
    assert domain.vec_o_npy.add_vectors_numpy([1,2,3],[4,5,6])==[5,7,9]
    assert domain.vec_o_npy.add_vectors_numpy([1,2,3],[-1,-1,-1])==[0,1,2]
    assert domain.vec_o_npy.add_vectors_numpy([1,2,3],[0,-1,-2])==[1,1,1]

def test_sub_vectors_numpy():

    assert domain.vec_o_npy.sub_vectors_numpy([1,2,3],[4,5,5])==[-3,-3,-2]
    assert domain.vec_o_npy.sub_vectors_numpy([1,2,3],[4,5])=='NULL'
    assert domain.vec_o_npy.sub_vectors_numpy([1,2,3],[1,2,3])==[0,0,0]
    assert domain.vec_o_npy.sub_vectors_numpy([1,2,3],[-1,-2,-3])==[2,4,6]
    assert domain.vec_o_npy.sub_vectors_numpy([1,2,3],[0,0,0])==[1,2,3]

def test_mult_vectors_numpy():

    assert domain.vec_o_npy.mult_vectors_numpy([1,2,3],[4,5,5])==29
    assert domain.vec_o_npy.mult_vectors_numpy([1,2,3],[4,5])=='NULL'
    assert domain.vec_o_npy.mult_vectors_numpy([1,2,3],[1,2,3])==14
    assert domain.vec_o_npy.mult_vectors_numpy([1,2,3],[10,10,10])==60
    assert domain.vec_o_npy.mult_vectors_numpy([1,2,3],[0,0,0])==0
    
def test_sum_vector_numpy():
    
    assert domain.vec_o_npy.sum_vector_numpy([1,2,3])==6
    assert domain.vec_o_npy.sum_vector_numpy([1,1,1,1,1])==5
    assert domain.vec_o_npy.sum_vector_numpy([0,0,0,-1,-4])==-5
    assert domain.vec_o_npy.sum_vector_numpy([0,0,0,4,4,4])==12
    assert domain.vec_o_npy.sum_vector_numpy([0])==0
    
def test_prod_vector_numpy():
    
    assert domain.vec_o_npy.prod_vector_numpy([1,2,3])==6
    assert domain.vec_o_npy.prod_vector_numpy([1,1,1,4,54,5346,423,0])==0
    assert domain.vec_o_npy.prod_vector_numpy([-1,-2,-3])==-6
    assert domain.vec_o_npy.prod_vector_numpy([9])==9
    assert domain.vec_o_npy.prod_vector_numpy([1,2,3,-1])==-6
    
def test_avg_vector_numpy():
    
    assert domain.vec_o_npy.avg_vector_numpy([1,2,3])==2
    assert domain.vec_o_npy.avg_vector_numpy([1,2,3,4])==2.5
    assert domain.vec_o_npy.avg_vector_numpy([1,1,1,1])==1
    assert domain.vec_o_npy.avg_vector_numpy([100,200,300])==200
    assert domain.vec_o_npy.avg_vector_numpy([0])==0
    
def test_min_vector_numpy():
    
    assert domain.vec_o_npy.min_vector_numpy([1,2,3,4,6,43534,64,53,423])==1
    assert domain.vec_o_npy.min_vector_numpy([43534,64,53,423])==53
    assert domain.vec_o_npy.min_vector_numpy([1,2,3,4,6,43534,64,53,423,-1])==-1
    assert domain.vec_o_npy.min_vector_numpy([1,2,3,4,6,43534,64,53,423,0,6,-2])==-2
    assert domain.vec_o_npy.min_vector_numpy([1])==1
    
   
def test_max_vector_numpy():
    
    assert domain.vec_o_npy.max_vector_numpy([1,2,3,4,6,43534,64,53,423])==43534
    assert domain.vec_o_npy.max_vector_numpy([43534,64,53,423])==43534
    assert domain.vec_o_npy.max_vector_numpy([1,2,3,4,6,43534,64,53,423,-1])==43534
    assert domain.vec_o_npy.max_vector_numpy([1,2,3,4,6,43534,64,53,423,0,6,-2])==43534
    assert domain.vec_o_npy.max_vector_numpy([-1,-2,-55,-99])==-1
    
    
    
    
    
    
