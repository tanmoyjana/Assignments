from nose.tools import *
from assignments.assignments2 import *
from values import *


def test_a_tale_of_three_cities():
    for key in at3c.keys():
        assert_equal(ATaleOfThreeCities().
                     connect(key[0],key[1],key[2],key[3],
                             key[4],key[5]),at3c[key])
def test_additiongame():
    for key in addition.keys():
        assert_equal(AdditionGame().
                     getMaximumPoints(key[0],key[1],key[2],key[3]),
                     addition[key])  
        

def test_accountbalance():
    for key in acntblnc.keys():
        assert_equal(AccountBalance().
                     processTransactions(key[0],key[1]),acntblnc[key])
def test_into_the_matrix():
    for key in intomatrix.keys():
        assert_equal(IntoTheMatrix().takePills(key[0],key[1]),intomatrix[key])
