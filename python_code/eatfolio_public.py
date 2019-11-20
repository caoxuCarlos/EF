# 你好, 欢迎使用 EF 饮食计算器
# 你只需要改两个数字就可以使用了:

heat_required = 2500 # 请把数字2500改成你所需要摄入的总能量
required_cp_ratio=2.5 # 如果你希望碳水提供的能量是蛋白质提供的能能量的三倍, 就把2改成3


# 按照这个格式添加你需要的食物数据
# '鸡胸肉': [7.72, 0, 29.55] 的意思是:
# 食物名称:鸡胸肉
# 每100g鸡胸肉含有7.72g脂肪
# 每100g鸡胸肉含有0g碳水化合物
# 每100g鸡胸肉含有29.55g脂肪
# 如果要添加数据, 需要在   '蒸南瓜': [0.07, 5.33, 0.8]    后面加入一条新数据
# 注意, 每个食物的数据之间要用逗号隔开

data_dict = {'鸡胸肉': [7.72, 0, 29.55], '米饭': [0.33, 25.86, 2.60], '红薯': [0.05, 20.45, 1.57], '牛排': [15.01, 0, 27.29], '蒸南瓜': [0.07, 5.33, 0.8],'面包':[3.29,50.61,7.64],'可口可乐':[0,10.6,0]}

# 下面的不需要看
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
#－－－－－－－－－－－
import numpy as np
import pandas as pd
import time
start=time.time()
def data_function(data_dict):
    data = pd.DataFrame(data_dict)
    data.shape[1]
    for i in range(data.shape[0]):
        data.loc[i] = pd.to_numeric(data.iloc[i, :], errors='coerce')
    data_ndarray = np.array([data.iloc[0], data.iloc[1], data.iloc[2]])
    df = pd.DataFrame(np.zeros((data.shape[1], 1)))
    df.columns = ['food_type']
    df['food_type'] = data.columns
    df['fat'] = pd.Series(data_ndarray[0, :])
    df['carbohydrate'] = pd.Series(data_ndarray[1, :])
    df['protein'] = pd.Series(data_ndarray[2, :])
    return df

nutrition_information=data_function(data_dict)
nutrition_information['heat_per_gram']= (nutrition_information['fat'] * 9 + nutrition_information['carbohydrate'] * 4 + nutrition_information['protein'] * 4) / 100
food_type_num=nutrition_information.shape[0]

def weight_generator(number):
    w=np.random.random(number)
    return w/sum(w)

fat=np.array(nutrition_information.iloc[:, 1])
carbohydrate=np.array(nutrition_information.iloc[:, 2])
protein=np.array(nutrition_information.iloc[:, 3])
nutrition_matrix= np.array([fat, carbohydrate, protein]) / 100

play_times=12000
fcp0=np.zeros((play_times, 3))
weight_container=np.zeros((play_times,food_type_num))


for i in range(play_times):
    w=weight_generator(food_type_num)
    fcp0[i, :]= np.dot(nutrition_matrix, w)
    weight_container[i,:]=w

fcp1=pd.DataFrame()
fcp1['fat']=fcp0[:,0]
fcp1['carb']=fcp0[:,1]
fcp1['protein']=fcp0[:,2]

permitted_volatility_percentage=0.05
fcp2=pd.DataFrame()
fcp2['p_f']=fcp1['protein']/fcp1['fat']
fcp2['c_p']=fcp1['carb']/fcp1['protein']
fcp2['lower_b']=required_cp_ratio*(1-permitted_volatility_percentage)
fcp2['upper_b']=required_cp_ratio*(1+permitted_volatility_percentage)

proper_ratio_position=np.array(fcp2.query('lower_b<c_p<upper_b').index)

if proper_ratio_position.shape[0]<5:
    print('请再运行一次')
else:
    ratio_with_best_pf_positon = fcp2.loc[fcp2.query('lower_b<c_p<upper_b').index].iloc[:, 0].idxmax()
    the_one = weight_container[ratio_with_best_pf_positon]

    heat = np.array(nutrition_information['heat_per_gram'])

    per_gram_heat = np.dot(the_one,heat)

    eatfolio_mass = heat_required / per_gram_heat
    components = eatfolio_mass * the_one
    output='你好, 欢迎使用EF, 你的食谱如下:\n'
    for i in range(nutrition_information.shape[0]):
        output= output +'\n' + str(nutrition_information.iloc[i, 0]) + ' ' + str(round(components[i], 1)) + 'g'
    fat_taken = str(round((np.dot(nutrition_matrix, the_one) * eatfolio_mass)[0], 1))
    carbohydrate_taken = (str(round((np.dot(nutrition_matrix, the_one) * eatfolio_mass)[1], 1)))
    protein_taken = str(round((np.dot(nutrition_matrix, the_one) * eatfolio_mass)[2], 1))
    output += "\n\n你将摄入:"
    output += '\n' + fat_taken + 'g 脂肪'
    output += '\n' + carbohydrate_taken + 'g 碳水化合物'
    output += '\n' + protein_taken + 'g 蛋白质'
    end=time.time()
    duration=round(end-start,4)
    print(output)
    print(f'\n运行用时:{duration}s')
    print('计算使用食物营养成分来源如下:')
    print('https://www.fatsecret.cn/%E7%83%AD%E9%87%8F%E8%90%A5%E5%85%BB/search?q=')