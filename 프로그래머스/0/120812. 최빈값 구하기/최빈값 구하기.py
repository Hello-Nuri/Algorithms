def solution(array):
    cnt_dict = {}
    for item in array:
        cnt_dict[item]=cnt_dict.get(item,0)+1
    
    max_freq = max(cnt_dict.values())
    most_elements = [key for key,value in cnt_dict.items() if value == max_freq]
    answer = most_elements
    if len(most_elements)>1:
        return -1
    else:
        return most_elements[0]