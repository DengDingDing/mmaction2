import pickle

# 解析 .pkl 文件
with open('test.pkl', 'rb') as file:
    data = pickle.load(file)

# 输出加载的数据
print(data['frame_dir'])