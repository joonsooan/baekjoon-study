import numpy # numpy 불러오기

def summary_f(data): # data는 리스트 자료형 
    
    answer_dict = {} # 통계랑을 나타내는 dictionary 선언

    answer_dict["Mean"] = numpy.mean(data)
    answer_dict["Median"] = numpy.median(data)

    data_dict = {}
    for num in data:
        if num in data_dict:
            data_dict[num] += 1
        else:
            data_dict[num] = 1
    
    mode = [k for k, v in data_dict.items() if max(data_dict.values()) == v]
    mode_sort = sorted(mode)
    answer_dict["Mode"] = mode_sort

    return answer_dict

data = [1, 2, 3]
print(summary_f(data))