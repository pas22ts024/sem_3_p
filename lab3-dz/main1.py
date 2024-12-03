import tkinter as tk
from tkinter import ttk

def visual():
	def save_r1():
		entry_r1.config(state = 'readonly')


	def clear_r1():
		entry_r1.config(state = 'normal')
		entry_r1.delete('0', 'end')


	def save_r2():
		entry_r2.config(state = 'readonly')


	def clear_r2():
		entry_r2.config(state = 'normal')
		entry_r2.delete('0', 'end')


	def save_tip():
		vibor_soed.config(state = 'disabled')


	def clear_tip():
		vibor_soed.config(state = 'readonly')
		vibor_soed.delete('0', 'end')


	def clear_ans():
		label_ans.config(text = '')


	def podschet():
		r1 = entry_r1.get()
		r2 = entry_r2.get()
		tip = vibor_soed.get()
		try:
			r1 = int(r1)
			r2 = int(r2)
			if tip == 'Последовательное':
				ans = r1 + r2
				label_ans.config(text = str(ans))
			else:
				ans = 1 / (1 / r1 + 1 / r2)
				label_ans.config(text = str(ans))
		except:
			label_ans.config(text = 'Некорректный ввод')


	def end_prog():
		root.destroy()


	root = tk.Tk() #создание окна
	root.title('Подсчет сопротивления с двух резисторов') #заголовок
	root.geometry('900x600') #исходный размер
	label_vvod_1 = tk.Label(text = 'Введите сопротивление первого резистора')
	entry_r1 = tk.Entry() #создание поля для ввода
	btn_vvod_1 = ttk.Button(text = 'Ввод', command = save_r1) #создание кнопки
	btn_vvod_clear_r1 = ttk.Button(text = 'Очистить', command = clear_r1)
	label_vvod_1.grid(row = 0, column = 0, sticky = 'w')
	entry_r1.grid(row = 0, column = 1, sticky = 'w')
	btn_vvod_1.grid(row = 0, column = 2, sticky = 'w')
	btn_vvod_clear_r1.grid(row = 0, column = 3, sticky = 'w')
	label_vvod_2 = tk.Label(text = 'Введите сопротивление второго резистора')
	entry_r2 = tk.Entry() #создание поля для ввода
	btn_vvod_2 = ttk.Button(text = 'Ввод', command = save_r2) #создание кнопки
	btn_vvod_clear_r2 = ttk.Button(text = 'Очистить', command = clear_r2)
	label_vvod_2.grid(row = 1, column = 0, sticky = 'w')
	entry_r2.grid(row = 1, column = 1, sticky = 'w')
	btn_vvod_2.grid(row = 1, column = 2, sticky = 'w')
	btn_vvod_clear_r2.grid(row = 1, column = 3, sticky = 'w')
	label_soed = tk.Label(text = 'Выберите тип соединения')
	tip = ('Последовательное', 'Параллельное')
	vibor_soed = ttk.Combobox(values = tip, state = 'readonly') #создание мультивыбора
	btn_vibor = ttk.Button(text = 'Ввод', command = save_tip)
	vibor_soed_clear = ttk.Button(text = 'Очистить', command = clear_tip)
	label_soed.grid(row = 2, column = 0, sticky = 'w')
	vibor_soed.grid(row = 2, column = 1, sticky = 'w')
	btn_vibor.grid(row = 2, column = 2, sticky = 'w')
	vibor_soed_clear.grid(row = 2, column = 3, sticky = 'w')
	label_itog = tk.Label(text = 'Результат вычислений')
	label_ans = tk.Label(text = 'Не было вычислений')
	btn_ans = ttk.Button(text = 'Очистить', command = clear_ans)
	label_itog.grid(row = 3, column = 0, sticky = 'w')
	label_ans.grid(row = 3, column = 1, sticky = 'w')
	btn_ans.grid(row = 3, column = 2, sticky = 'w')
	btn_deyst = ttk.Button(text = 'Выполнить', command = podschet)
	btn_deyst.grid(row = 4, column = 0, sticky = 'w')
	btn_end = ttk.Button(text = 'Завершить выполнение программы', command = end_prog)
	btn_end.grid(row = 3, column = 4, sticky = 'w')
	root.mainloop()


visual()

