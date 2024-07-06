'''
Шаг 1. Подготовить данные - два списка с числовыми значениями x и y, например, 
значения температуры по месяцам за год.
Шаг 2. Импортировать matplotlib.pyplot и создать график с помощью функции plot(), передав ей списки x и y. 
Это нарисует простой линейный график.
Шаг 3. Добавить название графика, подписи осей x и y, легенду и сетку с помощью функций из matplotlib - 
например, xlabel(), ylabel(), legend(), grid().
Шаг 4. Сохранить график в файл изображения и/или показать его с помощью matplotlib.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

num = 15
df_date = pd.date_range(start='2024-03-02', periods=num)
arr_temp = np.random.random((1, num)) * 20
print(df_date)
print(arr_temp)

df = pd.DataFrame(data=[df_date, arr_temp[0]]).T
df.columns = ['date', 'temperature']
df['date'] = pd.to_datetime(df['date']).dt.date
print(df)

plt.figure(figsize=(15, 5))
xx = df['date']
yy = df['temperature']
plt.title('График температур')
plt.plot(xx, yy, label='температура по дням')
plt.xlabel('дата', alpha=0.7)
plt.ylabel('температура')
plt.xticks(rotation=10)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
