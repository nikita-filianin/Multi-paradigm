from goto import with_goto


@with_goto
def main():

	lower_register_chars = "abcdefghijklmnopqrstuvwxyz"
	upper_register_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	max_words_num = 100

	# Обмеження по кількості слів та символів на сторінку тексту
	num_of_words_on_page = 255
	num_of_chars_on_page = 1800

	# Зчитування з файлу
	with open("text2.txt", "r") as file:
		text = file.read()
	text += "$"

	# Перевірка та форматування тексту (заміна великих літер на малі,
	# заміна переходів на новий рядок на звичайні пробіли, уникнення символів та чисел)
	temp = ""
	i = 0
	label.check_row
	if text[i] in lower_register_chars:
		temp += text[i]
	elif text[i] in upper_register_chars:
		t = 0
		label.upper_reg_converter
		if text[i] != upper_register_chars[t]:
			t += 1
			goto.upper_reg_converter
		temp += lower_register_chars[t]
	elif text[i] == "\n" or text[i] == " ":
		temp += " "
	elif text[i] == "$":
		text = temp + "$"
		goto.end_check_row
	i += 1
	goto.check_row

	label.end_check_row

	# Лічильники
	word = ""
	curr_page = 1
	chars_counter = 0		# Лічильник символів
	words_counter = 0		# Лічильник слів
	res_words_count = -1
	res = [[None, 0, []]] 	# Вивід слова, кількість повторень, номера сторінок із цим словом
	i = 0
	label.check_word
	if text[i] == " ":
		t = 0
		words_counter += 1
		if words_counter >= num_of_words_on_page or chars_counter >= num_of_chars_on_page:
			curr_page += 1
			chars_counter -= num_of_chars_on_page
			words_counter = 0
		label.res_maker
		if word == res[t][0]:
			res[t][1] += 1
			if curr_page not in res[t][2]:
				res[t][2] += [curr_page]
			word = ""
			i += 1
			goto.check_word
		elif res[t][0] is None:
			res[t][0] = word
			res[t][1] = 1
			res[t][2] += [curr_page]
			res += [[None, 0, []]]
			res_words_count += 1
			word = ""
			i += 1
			goto.check_word
		else:
			t += 1
			goto.res_maker
	elif text[i] == "$":
		res = res[:-1]
		goto.end_check_word
	else:
		word += text[i]
	i += 1
	chars_counter += 1
	goto.check_word

	label.end_check_word

	# Уникнення виводу слів, що повторюються занадто часто. В цьому випадку ліміт = 100 повторів
	i = 0
	label.avoid_words
	if res[i][1] > max_words_num or res[i][0] == "":
		res_words_count -= 1
		del res[i]
	else:
		i += 1
	if i >= res_words_count:
		goto.end_avoid_words
	goto.avoid_words

	label.end_avoid_words

	# Сортування результатів за допомогою Bubble Sort
	i = 0
	label.sort_loop_1
	j = 0

	label.sort_loop_2
	if j >= res_words_count - i:
		goto.end_sort_loop_2
	if res[j][0] > res[j + 1][0]:
		res[j], res[j + 1] = res[j + 1], res[j]
	j += 1
	goto.sort_loop_2

	label.end_sort_loop_2
	i += 1
	if i - 1 >= res_words_count:
		goto.end_sort_loop_1
	goto.sort_loop_1

	label.end_sort_loop_1

	# Вивід результатів у консоль
	i = 0
	label.print_res
	print(f"{res[i][0]} - {res[i][1]} time(s) - {res[i][2]}")
	if i < res_words_count:
		i += 1
		goto.print_res
	return


main()
