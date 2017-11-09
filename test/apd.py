import domain.vec_o

#TEST MODULE

def test_add_scalar_and_vector():

    assert domain.vec_o.add_scalar_and_vector([1,2,3],2)==[3,4,5]
    assert domain.vec_o.add_scalar_and_vector([1,2,3],0)==[1,2,3]
    assert domain.vec_o.add_scalar_and_vector([1,2,3,4,5,6],10)==[11,12,13,14,15,16]
    assert domain.vec_o.add_scalar_and_vector([1,2,3],-2)==[-1,0,1]
    assert domain.vec_o.add_scalar_and_vector([0,0,0,0],3)==[3,3,3,3]


def test_add_vectors():

    assert domain.vec_o.add_vectors([1,2,3],[2])=='NULL'
    assert domain.vec_o.add_vectors([1,2,3],[1,2,3])==[2,4,6]
    assert domain.vec_o.add_vectors([1,2,3],[4,5,6])==[5,7,9]
    assert domain.vec_o.add_vectors([1,2,3],[-1,-1,-1])==[0,1,2]
    assert domain.vec_o.add_vectors([1,2,3],[0,-1,-2])==[1,1,1]

def test_sub_vectors():

    assert domain.vec_o.sub_vectors([1,2,3],[4,5,5])==[-3,-3,-2]
    assert domain.vec_o.sub_vectors([1,2,3],[4,5])=='NULL'
    assert domain.vec_o.sub_vectors([1,2,3],[1,2,3])==[0,0,0]
    assert domain.vec_o.sub_vectors([1,2,3],[-1,-2,-3])==[2,4,6]
    assert domain.vec_o.sub_vectors([1,2,3],[0,0,0])==[1,2,3]

def test_mult_vectors():

    assert domain.vec_o.mult_vectors([1,2,3],[4,5,5])==29
    assert domain.vec_o.mult_vectors([1,2,3],[4,5])=='NULL'
    assert domain.vec_o.mult_vectors([1,2,3],[1,2,3])==14
    assert domain.vec_o.mult_vectors([1,2,3],[10,10,10])==60
    assert domain.vec_o.mult_vectors([1,2,3],[0,0,0])==0
    
def test_sum_vector():
    
    assert domain.vec_o.sum_vector([1,2,3])==6
    assert domain.vec_o.sum_vector([1,1,1,1,1])==5
    assert domain.vec_o.sum_vector([0,0,0,-1,-4])==-5
    assert domain.vec_o.sum_vector([0,0,0,4,4,4])==12
    assert domain.vec_o.sum_vector([0])==0
    
def test_prod_vector():
    
    assert domain.vec_o.prod_vector([1,2,3])==6
    assert domain.vec_o.prod_vector([1,1,1,4,54,5346,423,0])==0
    assert domain.vec_o.prod_vector([-1,-2,-3])==-6
    assert domain.vec_o.prod_vector([9])==9
    assert domain.vec_o.prod_vector([1,2,3,-1])==-6
    
def test_avg_vector():
    
    assert domain.vec_o.avg_vector([1,2,3])==2
    assert domain.vec_o.avg_vector([1,2,3,4])==2.5
    assert domain.vec_o.avg_vector([1,1,1,1])==1
    assert domain.vec_o.avg_vector([100,200,300])==200
    assert domain.vec_o.avg_vector([0])==0
    
def test_min_vector():
    
    assert domain.vec_o.min_vector([1,2,3,4,6,43534,64,53,423])==1
    assert domain.vec_o.min_vector([43534,64,53,423])==53
    assert domain.vec_o.min_vector([1,2,3,4,6,43534,64,53,423,-1])==-1
    assert domain.vec_o.min_vector([1,2,3,4,6,43534,64,53,423,0,6,-2])==-2
    assert domain.vec_o.min_vector([1])==1
    
   
def test_max_vector():
    
    assert domain.vec_o.max_vector([1,2,3,4,6,43534,64,53,423])==43534
    assert domain.vec_o.max_vector([43534,64,53,423])==43534
    assert domain.vec_o.max_vector([1,2,3,4,6,43534,64,53,423,-1])==43534
    assert domain.vec_o.max_vector([1,2,3,4,6,43534,64,53,423,0,6,-2])==43534
    assert domain.vec_o.max_vector([-1,-2,-55,-99])==-1
    
    
    
    
