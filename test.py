from copy import copy


s = "deeedbbcccbdaa"
k = 3


def f(s: str, k: int) -> str:   
    lis = []
    for i in range(len(s) - k + 1):
        sub_string = ""        
        for j in range(i, i+k):
            sub_string += s[j]
        if all(element == sub_string[0] for element in sub_string):  
            start_index = s.index(sub_string)
            stop_index = start_index + k-1
            s = s[:start_index] + s[stop_index+1:]   
            result = copy(s)
            lis.append(result)
            f(result,k)
            break  
    return lis
                
print(f(s, k))


   
