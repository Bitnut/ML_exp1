# first line: 1
@mem.cache
def get_data():
    data = load_svmlight_file("/home/picher/workSpace/ML_exp/australian_scale.txt",14,dtype=float64)
    return data[0], data[1]
