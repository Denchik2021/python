for i in range(1, 101): 	#создаем цикл  FOR от 1 до 100 и перебираем его
	if 10 < i < 20:		#если переменная i меньше 20 и больше 10
		print(f"{i} процентов")		#то выводим Процентов
	elif i % 10 == 1:	#если остаток от деления приравнивается к еденице
		print(f"{i} процент")	#то выводить Процент
	elif i % 10 == 2 or i % 10 == 3 or i % 10  == 4:	#если остаток от деления равняется 2 или 3 или 4
		print(f"{i} процента")	#то выводить Процента
	else:
		print(f"{i} процентов")  #в любых других случаях выводить Процентов