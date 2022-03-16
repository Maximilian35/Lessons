a = float( input('Введите ваш оклад! ' ) )
b = float( input('Введите норму часов! ' ) )
w = float( input('Введите количество переработки! ' ) )

e = a / b
f = e * w
m = 0.2 * f
n = f + m
q = round(n)
print('Ваша грязная зарплата составила: ' + str(q) )


cost=' Зарплата '+' '+ str(q) # выбираем данные которые надо сохранить
print(cost) #выводим
my_filename=str( input(" Zarplata ")) # ФАЙЛ
data=cost
fext2='txt'# расширение файла
print(my_filename)
with open(my_filename + '.' + fext2, 'w', encoding='utf-8') as fp:# собираем то, что в файл попадет(data), +имя фйала(filename)+ расширение, открываем неа запись(w)
     print(data, file=fp, sep="\n")# запись в файл с переводом строки
     fp.close()# закрытие файла

input('Нажмите ENTER для выхода! ')