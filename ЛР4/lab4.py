import tkinter as tk
from tkinter import ttk

def visual():
	def save_number():
		entry_chislo.config(state = 'readonly')


	def save_vibor():
		vibor.config(state = 'disabled')


	def clear_number():
		entry_chislo.config(state = 'normal')
		entry_chislo.delete('0', 'end')


	def clear_vibor():
		vibor.config(state = 'readonly')
		vibor.delete('0', 'end')


	def clear_all():
		entry_chislo.config(state = 'normal')
		entry_chislo.delete('0', 'end')
		vibor.config(state = 'readonly')
		vibor.delete('0', 'end')


	def perevod():
		vib = vibor.get()
		number = entry_chislo.get()
		if vib == 'Из 10-й в 3-ю':
			ans = ten_to_third(number)
		else:
			ans = third_to_ten(number)
		label_ans.config(text = ans)


	def end_prog():
		root.destroy()

	
	def add_from_box():
		entry_chislo.insert('end' , vibor_chisla.get())


	def clear_vivod():
		label_ans.config(text = '')


	root = tk.Tk() #создание окна
	root.title('Перевод из 10-й системы в 3-ю и обратно') #заголовок
	root.geometry('900x600') #исходный размер
	label_info = tk.Label(text = 'Работу выполнил Александр Пыжьянов \n группа ИУ5Ц-52Б') #создание текстового объекта
	label_info.grid(row = 0, column = 0) #расположение объекта
	label_vvod = tk.Label(text = 'Введите число для перевода')
	entry_chislo = tk.Entry() #создание поля для ввода
	chisla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '.')
	vibor_chisla = ttk.Combobox(values = chisla, state = 'readonly') #создание мультивыбора
	btn_vvod = ttk.Button(text = 'Ввод', command = save_number) #создание кнопки
	btn_vvod_clear = ttk.Button(text = 'Очистить', command = clear_number)
	btn_vvod_box = ttk.Button(text = 'Добавить', command = add_from_box)
	label_vvod.grid(row = 1, column = 0, sticky = 'w')
	entry_chislo.grid(row = 1, column = 1, sticky = 'w')
	btn_vvod.grid(row = 1, column = 2, sticky = 'w')
	btn_vvod_clear.grid(row = 1, column = 3, sticky = 'w')
	vibor_chisla.grid(row = 1, column = 4, sticky = 'w')
	btn_vvod_box.grid(row = 1, column = 5, sticky = 'w')
	label_vibor = tk.Label(text = 'Выберите, из какой СС в какую перевод')
	vibor = ttk.Combobox(values = ('Из 10-й в 3-ю', 'Из 3-й в 10-ю'), state = 'readonly')
	btn_vibor = ttk.Button(text = 'Ввод', command = save_vibor)
	btn_vibor_clear = ttk.Button(text = 'Очистить', command = clear_vibor)
	label_vibor.grid(row = 2, column = 0, sticky = 'w')
	vibor.grid(row = 2, column = 1, sticky = 'w')
	btn_vibor.grid(row = 2, column = 2, sticky = 'w')
	btn_vibor_clear.grid(row = 2, column = 3, sticky = 'w')
	btn_clear_all = ttk.Button(text = 'Очистить все поля', command = clear_all)
	btn_clear_all.grid(row = 3, column = 0, sticky = 'w')
	btn_deyst = ttk.Button(text = 'Перевести число', command = perevod)
	btn_deyst.grid(row = 4, column = 0, sticky = 'w')
	label_rez = tk.Label(text = 'Результат перевода: ')
	label_rez.grid(row = 5, column = 0, sticky = 'w')
	label_ans = tk.Label(text = 'Не было вычислений')
	label_ans.grid(row = 5, column = 1, sticky = 'w')
	btn_end = ttk.Button(text = 'Завершить выполнение программы', command = end_prog)
	btn_end.grid(row = 6, column = 0, sticky = 'w')
	btn_clear_vivod = ttk.Button(text = 'Очистить', command = clear_vivod)
	btn_clear_vivod.grid(row = 5, column = 2, sticky = 'w')
	root.mainloop()


def ten_to_third(x):
	try:
		x = float(x)
		cel = int(x)
		drob = x - cel
		ans_cel = ''
		ans_drob = ''
		while cel > 0:
			d = cel % 3 
			cel //= 3
			ans_cel += str(d)
		ans_cel = ans_cel[::-1]
		k = 0
		while drob != int(drob) and k < 10:
			drob = drob - int(drob)
			drob *= 3
			tec = int(drob)
			ans_drob += str(tec)
			k += 1
		if drob != 0:
			ans_drob += str(int(drob))
		if drob == 0:
			ans = ans_cel
		else:
			ans = ans_cel + '.' + ans_drob
	except:
		ans = 'Введено некорректное число'
	return ans


def third_to_ten(x):
	try:
		test = float(x)
		ans = 0
		f = True
		bad = '3456789'
		if '.' in x:
			tochka = x.index('.')
			d = len(x) - (len(x) - tochka) - 1
			for i in x:
				if i != '.':
					ans += int(i) * (3 ** d)
					d -= 1
					if i in bad:
						f = False
		else:
			d = len(x) - 1
			for i in x:
				ans += int(i) * (3 ** d)
				d -= 1
				if i in bad:
					f = False
		if not f:
			ans = 'Число не в троичной системе счисления'
	except:
		ans = 'Введено некорректное число'
	return ans


visual()
