#Write and test an efficient Java/Python method for finding the ten largest elements in an array of
#size n. What is the running time of your algorithm? Hint: Use an auxiliary array to store indices of
#largest elements and ignore previous found elements. Note that 10 is a constant.

def find_ten_largest(arr):
    top10 = [float('-inf')] * 10  # my array

    for num in arr:
        
        min_val = min(top10)
        if num > min_val:
            
            min_index = top10.index(min_val)
            top10[min_index] = num

    
    top10.sort(reverse=True)
    return top10


#run time O(n) or liner