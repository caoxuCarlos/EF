import numpy as np
import pandas as pd
import time
import tkinter as tk
def show_recomendation():
    get_from_day_heat=day_heat_entry.get()
    rec_b.set(round(int(get_from_day_heat)*0.3,1))
    rec_l.set(round(int(get_from_day_heat)*0.3,1))
    rec_p.set(round(int(get_from_day_heat) * 0.15, 1))
    rec_d.set(round(int(get_from_day_heat) * 0.25, 1))

def test():
    stape_food_01 = staple_food_entry.get()
    meat_egg_milk_01 = mem_entry.get()
    vegetable_fruit_01 = vf_entry.get()
    fat_01 = fat_entry.get()
    import re
    pttn = r'(\w{1,})'
    port1 = re.findall(pttn, stape_food_01)
    port2 = re.findall(pttn, meat_egg_milk_01)
    port3 = re.findall(pttn, vegetable_fruit_01)
    port4 = re.findall(pttn, fat_01)
    total_number = len(port1) * len(port2) * len(port3) * len(port4) * 10000
    tip = '最多需要运算' + str(int(total_number/10000)) + '万次.\n通常仅需几秒,请耐心等待.\n在最极端情况下, \n需要约' + str(int(total_number * 27 / 10000)) + 's 输出结果.'
    reminder.set(tip)

def process():
    try:
        stape_food_01 = staple_food_entry.get()
        meat_egg_milk_01 = mem_entry.get()
        vegetable_fruit_01 = vf_entry.get()
        fat_01 = fat_entry.get()
        import re
        pttn = r'(\w{1,})'
        port1 = re.findall(pttn, stape_food_01)
        port2 = re.findall(pttn, meat_egg_milk_01)
        port3 = re.findall(pttn, vegetable_fruit_01)
        port4 = re.findall(pttn, fat_01)

        port5_p_lb = float(protein_lower_bound_entry.get())
        port6_p_ub = float(protein_upper_bound_entry.get())
        port7_cp = float(cp_ratio_entry.get())
        port8_heat = float(total_heat_entry.get())
        import numpy as np
        import pandas as pd
        import time
        start = time.time()
        # assumed user input
        input_staple_food = port1
        input_meat_egg_milk = port2
        input_vegetable_fruit = port3
        input_fat = port4
        repetition = 10000
        total_heat = port8_heat
        required_cp_ratio = port7_cp
        required_protein = [port5_p_lb, port6_p_ub]

        def food_data():
            """
            input all data in one function
            :return: all food data in a dataframe
            """
            import pandas as pd
            warehouseA = []
            # 主食
            warehouseA.append(('米饭', 0.33, 25.86, 2.6, '', 0, 1000000))
            warehouseA.append(('面条', 3.3, 40.02, 7.22, '', 0, 1000000))
            warehouseA.append(('全麦面包', 1.07, 12.26, 2.37, '', 0, 1000000))
            warehouseA.append(('红薯/地瓜', 0.05, 20.12, 1.57, '', 0, 1000000))
            # 肉蛋奶
            warehouseA.append(('鸡胸肉(不吃皮)', 3.54, 0, 30.76, '', 0, 1000000))
            warehouseA.append(('煮熟的鸡蛋白', 0.17, 0.73, 10.86, '', 0, 660))
            warehouseA.append(('牛奶', 4.88, 11.49, 8.03, '', 0, 10000))
            warehouseA.append(('荷包蛋', 9.9, 0.77, 12.53, '', 0, 660))
            warehouseA.append(('煮鸡蛋', 10.57, 1.12, 12.53, '', 0, 660))
            warehouseA.append(('牛排', 15.01, 0, 27.29, '', 0, 100000))
            warehouseA.append(('牛肉', 19.54, 0, 26.33, '', 0, 100000))
            warehouseA.append(('羊肉', 20.77, 0, 24.32, '', 0, 100000))
            warehouseA.append(('羊排', 17.55, 0, 15.86, '', 0, 100000))
            warehouseA.append(('猪肉', 17.04, 0, 27.34, '', 0, 100000))
            warehouseA.append(('猪排', 6.85, 0, 13.12, '', 0, 100000))
            # 蔬果
            warehouseA.append(('柚子', 0.04, 9.62, 0.76, '', 0, 10000))
            warehouseA.append(('生菜', 0.08, 1.63, 0.5, '', 0, 10000))
            warehouseA.append(('菠菜', 0.39, 3.63, 2.86, '', 0, 100000))
            warehouseA.append(('甘蓝菜', 0.3, 8.95, 3.38, '', 0, 100000))
            warehouseA.append(('花椰菜', 0.1, 5.3, 1.98, '', 0, 100000))
            warehouseA.append(('黄瓜(带皮)', 0.33, 10.93, 1.96, '', 0, 100000))
            warehouseA.append(('大豆/黄豆', 4.45, 6.53, 8.47, '', 0, 100000))
            warehouseA.append(('蘑菇', 0.34, 3.28, 3.09, '', 0, 100000))
            warehouseA.append(('南瓜', 0.1, 6.5, 1, '', 0, 100000))
            warehouseA.append(('草莓', 0.3, 7.68, 0.67, '', 0, 100000))
            warehouseA.append(('橙子', 0.16, 15.39, 1.23, '', 0, 100000))
            warehouseA.append(('牛油果', 14.66, 8.53, 2, '', 0, 100000))
            warehouseA.append(('菠萝', 0.12, 12.63, 0.54, '', 0, 100000))
            warehouseA.append(('哈密瓜', 0.19, 8.16, 0.84, '', 0, 100000))
            warehouseA.append(('黑莓', 0.49, 9.61, 1.39, '', 0, 100000))
            warehouseA.append(('橘子', 0.22, 9.34, 0.57, '', 0, 100000))
            warehouseA.append(('蓝莓', 0.33, 14.49, 0.74, '', 0, 100000))
            warehouseA.append(('李子', 0.28, 11.42, 0.7, '', 0, 100000))
            warehouseA.append(('荔枝', 0.44, 16.53, 0.83, '', 0, 100000))
            warehouseA.append(('芒果', 0.27, 17, 0.51, '', 0, 100000))
            warehouseA.append(('猕猴桃', 0.52, 14.66, 1.14, '', 0, 100000))
            warehouseA.append(('苹果', 0.17, 13.81, 0.26, '', 0, 100000))
            warehouseA.append(('葡萄', 0.16, 18.1, 0.72, '', 0, 100000))
            warehouseA.append(('香蕉', 0.33, 22.84, 1.09, '', 0, 100000))
            # 油脂
            warehouseA.append(('橄榄油', 100, 0, 0, '', 0, 50))
            warehouseA.append(('核桃', 65.21, 13.71, 15.23, '', 0, 200))
            warehouseA.append(('花生', 49.24, 16.13, 25.8, '', 0, 200))
            warehouseA.append(('开心果', 44.44, 27.97, 20.61, '', 0, 200))
            warehouseA.append(('杏仁', 50.64, 19.74, 21.26, '', 0, 200))
            warehouseA.append(('腰果', 47.77, 30.16, 16.84, '', 0, 200))
            warehouseA.append(('植物油', 100, 0, 0, '', 0, 50))
            warehouseA.append(('菜籽油', 100, 0, 0, '', 0, 50))
            warehouseA.append(('葵花籽油', 100, 0, 0, '', 0, 50))
            return pd.DataFrame(warehouseA,
                                columns=['name', 'fat', 'carbohydrate', 'protein', 'notes', 'lower_b', 'upper_b'])

        warehouse = food_data()

        # use function to return a wanted dataframe, which is
        # selected from warehouse though user input
        def find_required_staple_food(staple_food_available):
            """
            from warehouse find available staple food
            following 3 functions are in the same way
            :param staple_food_available: a list of staple food name, like ['米饭','全麦面包']
            :return: dataframe of available staple
            """
            staple_food_to_be_concatenated = []
            for i in range(len(staple_food_available)):
                staple_food_to_be_concatenated.append(
                    warehouse[warehouse.name.str.contains(staple_food_available[i], regex=False)])
            return pd.concat(staple_food_to_be_concatenated)

        def find_required_meat_egg_milk(meat_egg_milk_available):
            """
            just like find_required_staple_food function above
            :param meat_egg_milk_available:
            :return:
            """
            meat_egg_milk_to_be_concatenated = []
            for i in range(len(meat_egg_milk_available)):
                meat_egg_milk_to_be_concatenated.append(
                    warehouse[warehouse.name.str.contains(meat_egg_milk_available[i], regex=False)])
            return pd.concat(meat_egg_milk_to_be_concatenated)

        def find_required_vegetable_fruit(vegetable_fruit_available):
            """
            just like find_required_staple_food function above
            :param vegetable_fruit_available:
            :return:
            """
            vegetable_fruit_to_be_concatenated = []
            for i in range(len(vegetable_fruit_available)):
                vegetable_fruit_to_be_concatenated.append(
                    warehouse[warehouse.name.str.contains(vegetable_fruit_available[i], regex=False)])
            return pd.concat(vegetable_fruit_to_be_concatenated)

        def find_required_fat(fat_available):
            """
            just like find_required_staple_food function above
            :param fat_available:
            :return:
            """
            fat_to_be_concatenated = []
            for i in range(len(fat_available)):
                fat_to_be_concatenated.append(warehouse[warehouse.name.str.contains(fat_available[i], regex=False)])
            return pd.concat(fat_to_be_concatenated)

        # make dataframes sorted by main types of foods
        staple_food_df = find_required_staple_food(input_staple_food)
        staple_food_df.index = [x for x in range(staple_food_df.shape[0])]
        meat_egg_milk_df = find_required_meat_egg_milk(input_meat_egg_milk)
        meat_egg_milk_df.index = [x for x in range(meat_egg_milk_df.shape[0])]
        vegetable_fruit_df = find_required_vegetable_fruit(input_vegetable_fruit)
        vegetable_fruit_df.index = [x for x in range(vegetable_fruit_df.shape[0])]
        fat_df = find_required_fat(input_fat)
        fat_df.index = [x for x in range(fat_df.shape[0])]

        # make index and make all possible combination in a list
        def make_index(A, B, C, D):
            import pandas as pd
            factor_a = B * C * D
            factor_b = C * D
            factor_c = D
            index_df = pd.DataFrame(np.zeros((A * B * C * D, 4)))
            for a in range(1, A + 1):
                for b in range(1, B + 1):
                    for c in range(1, C + 1):
                        for d in range(1, D + 1):
                            position = (a - 1) * factor_a + (b - 1) * factor_b + (c - 1) * factor_c + (d - 1)
                            index_df.loc[position] = [a, b, c, d]
            return index_df - 1

        index_df = make_index(staple_food_df.shape[0], meat_egg_milk_df.shape[0], vegetable_fruit_df.shape[0],
                              fat_df.shape[0])

        combinations = []  # a list of dataframes, each dataframe is a certain choice
        for i in range(index_df.shape[0]):
            a = index_df.iloc[i, 0]
            b = index_df.iloc[i, 1]
            c = index_df.iloc[i, 2]
            d = index_df.iloc[i, 3]
            combinations.append(
                pd.DataFrame([staple_food_df.loc[a], meat_egg_milk_df.loc[b], vegetable_fruit_df.loc[c], fat_df.loc[d]],
                             index=[0, 1, 2, 3]))

        # concatenate with the core
        def core_f(data, total_heat):
            """
            make one result according to one combination of 4 kind of food
            and the total heat required
            :param data: a quite special dataframe
            :param total_heat: in kcal
            :return: [tuple,dataframe]
            """
            import numpy as np
            import pandas as pd
            def weight_generator(number):
                """
                generate a random weight vector
                :param number: size of the vector
                :return: a 1-D ndarray like weight vector
                """
                import numpy as np
                w = np.random.random(number)
                return w / sum(w)

            n_matrix = (np.array(data.iloc[:, 1:4], dtype=float).T) / 100
            # result_g1=np.zeros((repetition,))
            one_weight = weight_generator(data.shape[0])
            one_gram_heat = np.dot(np.dot(n_matrix, one_weight), np.array([9, 4, 4]))
            ef_mass = total_heat / one_gram_heat

            fat_taken = (np.dot(n_matrix, one_weight) * ef_mass)[0]
            carbohydrate_taken = (np.dot(n_matrix, one_weight) * ef_mass)[1]
            protein_taken = (np.dot(n_matrix, one_weight) * ef_mass)[2]
            three_elements = (fat_taken, carbohydrate_taken, protein_taken)

            staple_taken = ef_mass * one_weight[0]
            meat_egg_mike_taken = ef_mass * one_weight[1]
            vegetable_fruit_taken = ef_mass * one_weight[2]
            fat_taken = ef_mass * one_weight[3]
            food_mass_list = [(data['name'][0], staple_taken, data['lower_b'][0], data['upper_b'][0]),
                              (data['name'][1], meat_egg_mike_taken, data['lower_b'][1], data['upper_b'][1]),
                              (data['name'][2], vegetable_fruit_taken, data['lower_b'][2], data['upper_b'][2]),
                              (data['name'][3], fat_taken, data['lower_b'][3], data['upper_b'][3])]
            food_mass = pd.DataFrame(food_mass_list, columns=['food', 'taken', 'lower_bound', 'upper_bound'],
                                     index=[0, 1, 2, 3])

            return [three_elements, food_mass]

        # [ls,df]=core_f(combinations[1],2500)

        for j in range(len(combinations)):
            results = []
            for i in range(repetition):
                [ls, df] = core_f(combinations[j], total_heat)
                condition1 = required_protein[0] < ls[2] < required_protein[1]
                condition2 = (df.shape == df.query('lower_bound<taken<upper_bound').shape)
                condition3 = (required_cp_ratio * (0.9) < (ls[1] / ls[2]) < required_cp_ratio * (1.1))

                if condition1 and condition2 and condition3:
                    results.append([ls, df])
                if len(results) != 0:
                    break
            if len(results) != 0:
                break

        end = time.time()

        if len(results) == 0:
            output = '抱歉, 换组食物试试吧.'
        else:
            output = '你好,我是EF,快来看看我为你找到的食谱吧:\n'
            output += results[0][1].iloc[0, 0] + ' ' + str(round(results[0][1].iloc[0, 1], 1)) + 'g\n'
            output += results[0][1].iloc[1, 0] + ' ' + str(round(results[0][1].iloc[1, 1], 1)) + 'g\n'
            output += results[0][1].iloc[2, 0] + ' ' + str(round(results[0][1].iloc[2, 1], 1)) + 'g\n'
            output += results[0][1].iloc[3, 0] + ' ' + str(round(results[0][1].iloc[3, 1], 1)) + 'g\n'
            output += '\n你将摄入:\n'
            output += str(round(results[0][0][0])) + ' g 脂肪\n'
            output += str(round(results[0][0][1])) + ' g 碳水化合物\n'
            output += str(round(results[0][0][2])) + ' g 蛋白质\n'
            output += '\n本次耗时' + str(round(end - start, 3)) + ' s\n\n'
    except:
        output='抱歉, 请输入合适的内容后重新试试吧'

    tk.Text.insert(text_box, tk.END, output)



ef=tk.Tk()
ef.title('ef_v1.3')
ef.geometry('1400x880')
# guide at beginning
day_heat_label=tk.Label(ef,text='请输入今日所需总能量     ',font=("Helvetica", 15))
day_heat_label.grid(row=0,column=0)
day_heat_entry=tk.Entry(ef,bd =2,font=("Helvetica", 15))
day_heat_entry.grid(row=0,column=1)
see_recomendation=tk.Button(ef,text="显示推荐",command=show_recomendation).grid(row=0,column=2)
recommendation=tk.Label(ef,text='推荐摄入量:\n(早30%,午30%,晚25%,加餐15%)',font=("Helvetica", 15))
recommendation.grid(row=1,column=0)
rec_b=tk.IntVar()
b_label=tk.Label(ef,text='早餐:',font=("Helvetica", 15))
b_entry=tk.Entry(ef,textvariable=rec_b,font=("Helvetica", 15))
b_label.grid(row=2,column=0)
b_entry.grid(row=2,column=1)
rec_l=tk.IntVar()
l_label=tk.Label(ef,text='午餐:',font=("Helvetica", 15))
l_entry=tk.Entry(ef,textvariable=rec_l,font=("Helvetica", 15))
l_label.grid(row=2,column=2)
l_entry.grid(row=2,column=3)
rec_p=tk.IntVar()
p_label=tk.Label(ef,text='加餐:',font=("Helvetica", 15))
p_entry=tk.Entry(ef,textvariable=rec_p,font=("Helvetica", 15))
p_label.grid(row=3,column=0)
p_entry.grid(row=3,column=1)
rec_d=tk.IntVar()
d_label=tk.Label(ef,text='晚餐:',font=("Helvetica", 15))
d_entry=tk.Entry(ef,textvariable=rec_d,font=("Helvetica", 15))
d_label.grid(row=3,column=2)
d_entry.grid(row=3,column=3)

# real things
blank=tk.Label(ef,text="  ",font=("Helvetica", 30))
blank.grid(row=4,column=0)
total_heat_label=tk.Label(ef,text="该餐总热量:",font=("Helvetica", 15))
total_heat_label.grid(row=5,column=0)
total_heat_entry=tk.Entry(ef,bd =2,font=("Helvetica", 15))
total_heat_entry.grid(row=5,column=1)

cp_ratio_label=tk.Label(ef,text="碳水/蛋白质:",font=("Helvetica", 15))
cp_ratio_label.grid(row=5,column=2)
cp_ratio_entry=tk.Entry(ef,bd =2,font=("Helvetica", 15))
cp_ratio_entry.grid(row=5,column=3)

protein_lower_bound_label=tk.Label(ef,text="最少蛋白质克数:",font=("Helvetica", 15))
protein_lower_bound_label.grid(row=6,column=0)
protein_lower_bound_entry=tk.Entry(ef,bd =2,font=("Helvetica", 15))
protein_lower_bound_entry.grid(row=6,column=1)

protein_upper_bound_label=tk.Label(ef,text="最多蛋白质克数:",font=("Helvetica", 15))
protein_upper_bound_label.grid(row=6,column=2)
protein_upper_bound_entry=tk.Entry(ef,bd =2,font=("Helvetica", 15))
protein_upper_bound_entry.grid(row=6,column=3)

blank2=tk.Label(ef,text="  ",font=("Helvetica", 30))
blank2.grid(row=7,column=0)

staple_food_label=tk.Label(ef,text="主食:",font=("Helvetica", 15))
staple_food_label.grid(row=8,column=0)
staple_food_entry=tk.Entry(ef,bd =2,font=("Helvetica", 15))
staple_food_entry.grid(row=8,column=1)

calcualte=tk.Button(ef,text="时间检测",command=test)
calcualte.grid(row=8,column=2)

mem_label=tk.Label(ef,text="肉蛋奶:",font=("Helvetica", 15))
mem_label.grid(row=9,column=0)
mem_entry=tk.Entry(ef,bd =2,font=("Helvetica", 15))
mem_entry.grid(row=9,column=1)

reminder=tk.StringVar()
total_calcualtion_number=tk.Label(ef, textvariable=reminder, font=("Helvetica", 15))
total_calcualtion_number.grid(row=9, column=3)

vf_label=tk.Label(ef,text="蔬果:",font=("Helvetica", 15))
vf_label.grid(row=10,column=0)
vf_entry=tk.Entry(ef,bd =2,font=("Helvetica", 15))
vf_entry.grid(row=10,column=1)



fat_label=tk.Label(ef,text="脂肪:",font=("Helvetica", 15))
fat_label.grid(row=11,column=0)
fat_entry=tk.Entry(ef,bd =2,font=("Helvetica", 15))
fat_entry.grid(row=11,column=1)

calcualte=tk.Button(ef,text="开始计算",command=process)
calcualte.grid(row=11,column=2)


text_box_label=tk.Label(ef,text="食谱",font=("Helvetica", 15))
text_box_label.grid(row=12,column=0)
text_box=tk.Text(ef,height=10,width=30,font=("Helvetica",15))
text_box.grid(row=12,column=1)


ef.mainloop()

