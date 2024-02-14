# taking the elements of sets from user.
s1 = set(map(int,input("enter your integer numbers ").split()))
s2 = set(map(int,input("enter your integer numbers ").split()))

def common_elements(set1, set2):
    return set1.intersection(set2)
'''
intersection method returns the intersection of both sets that’s mean if there a number in both 
stes it will return it 
'''



print(common_elements(s1, s2))



