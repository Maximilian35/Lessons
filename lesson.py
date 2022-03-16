# Функция НДС
def get_vat(payment, persent=20): # функции
	try: # если
		payment = float(payment) 
		vat = payment / 100 * persent  # налог формула
		vat = round(vat, 2) # округлени до сотых, после запятой 2 цифры
		return "Sum VAT: {}".format(vat) #вывод данных и формат флоат в стр
	except TypeError:  # Если выпадет ошибка
		return "Can't count. Check data!" # Вывод данных что ошибка

result = get_vat(400, 15)
print(result)

