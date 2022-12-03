from test_module import test
from ex2 import Divisors
from ex3 import ListSum
def isSocial(nums):
    i = -1
    social = True
    while i < len(nums)-1 and social: # cannot use ex 3 since the areFriendly function is bidirectional
        social = ListSum(Divisors(nums[i])[:-1]) == nums[i+1]
        i+=1
    return social

# –- Unit tests –-
if __name__== '__main__':
      
    test(isSocial([220, 284]) == True)
    test(isSocial([14288, 15472, 14536, 14264, 12496]) == True)
    test(isSocial([14316, 19116, 31704, 47616, 83328, 177792, 295488, 629072, \
                        589786, 294896, 358336, 418904, 366556, 274924, 275444, \
                        243760, 376736, 381028, 285778, 152990, 122410, 97946, \
                        48976, 45946, 22976, 22744, 19916, 17716]) == True)
    test(isSocial([28158165, 29902635, 30853845, 29971755]) == True)
