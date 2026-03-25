# Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them 
# and is also sorted.

# In the previous example, we declared n = arr1.length and m = arr2.length. Here, we are saying n = arr1.length + arr2.length.
# Why have we changed the definition? Remember that when it comes to big O, we are allowed to define the variables as 
# we see fit. We could certainly stick to using n, m. In that case, 
# the time complexity of the sorting approach would be 
# O((n+m)⋅log(m+n))O((n+m)⋅log(m+n)) and the time complexity of the approach we are about to cover would be 
#   O(n+m)O(n+m). It makes no difference either way, but one justification we could give here is t
#   hat since we are combining the arrays, the total length is a significant number, so it makes sense to 
#   represent it as n.
# Keeping the definition as n = arr1.length and m = arr2.length is fine as well.

def combine(arr1, arr2):
    # ans is the answer
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1
    
    return ans