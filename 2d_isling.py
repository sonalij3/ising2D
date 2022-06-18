import numpy as np
import pytest

def spin_lattice(N):
    '''
    N : int
    Returns NxN array with random spins either 0 or 1.
    '''
    lattice = np.random.randint(0, 2, size=(N,N))
    return lattice

def energy(L):
    '''
    L : lattice from spin_lattice() of size NxN
    Returns the ising model energy of the lattice L.
    '''
    J = 1 # Spin Spin Interaction Term
    En = 0.0 # Intialize Energy

    for i in range(L.shape[0]):
        for j in range(L.shape[1]):

            # Sums energy of all the neighbors on the right
            try:
                if L[i+1,j] == L[i,j]:
                    En += J
                elif L[i+1,j] != L[i,j]:
                    En -= J
            except:
                k = 0

            # Sums energy of all the neighbors down  
            try:
                if L[i,j+1] == L[i,j]:
                    En += J
                elif L[i,j+1] != L[i,j]:
                    En -= J
            except:
                k = 0

    return En

def test_lattice(N):
    '''
    Test for spin_lattice().
    Tests for that there are only two spin values in the lattice.
    '''
    L = spin_lattice(N)
    val = np.where(L > 1 )[0]
    sum = np.sum(val)  
    assert(sum==0)

    val = np.where( L< 0)[0]
    sum = np.sum(val) 
    assert(sum==0)
    return val



if __name__ == "__main__":
    L = spin_lattice(2)
    print(energy(np.zeros((2,2))))
    print(energy(np.zeros((2,2))) == energy(np.ones((2,2))))
