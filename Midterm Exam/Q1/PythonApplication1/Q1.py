#Write and test a Java/Python recursive method for finding the maximum element in an
#array, A, of n elements. What is your running time? Hint: an array of size 1 would be the stop
#condition. The implementation is similar to linearSum method in lecture 5 examples. You can
#use the Math.max method for finding the maximum of two numbers

def find_max(A, n):
    
    if n == 1:
        return A[0]
    
    
    max_of_rest = find_max(A, n - 1)
    
   
    return max(A[n - 1], max_of_rest)



