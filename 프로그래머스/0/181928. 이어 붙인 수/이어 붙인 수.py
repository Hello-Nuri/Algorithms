def solution(num_list):
    even = []
    odd = []
    odd_added = ''
    even_added = ''
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even.append(num_list[i])
        else:
            odd.append(num_list[i])
    for i in range(len(odd)):
        odd_added += (str(odd[i]))
    for i in range(len(even)):
        even_added += (str(even[i]))
        
    return int(odd_added)+int(even_added)
