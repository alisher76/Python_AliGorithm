
# ### Problem
# 
# Add two numbers 
def sumTwoNumbers(a,b):
    return a + b

from nose.tools import assert_equal 

class SolutionTest(object):
    
    def test01(self,solution):
        assert_equal(solution(4,4),8)
        print("test 01 passed")

    def test02(self,solution):
        assert_equal(solution(5,6),11)
        print("test 02 passed")
        
# Running the tests
t1 = SolutionTest()
t1.test01(sumTwoNumbers)

t2 = SolutionTest()
t1.test02(sumTwoNumbers)
