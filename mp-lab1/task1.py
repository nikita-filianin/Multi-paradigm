from goto import with_goto


@with_goto
def main():

    lower_register_chars = "abcdefghijklmnopqrstuvwxyz"
    upper_register_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    taboo_words = ["of", "the", "to", "a", "or", "i", "it", "is", "no", "and", "but", "how", "that", "who", "one"]
    max_words_num = 10

    # Зчитування з файлу
    with open("text1.txt", "r") as file:
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

    word = ""
    res = [[None, 0]]   # Кількість повторів кожного зі слів
    i = 0
    label.check_word
    if text[i] == " ":
        if word in taboo_words:
            word = ""
            i += 1
            goto.check_word
        t = 0
        label.res_maker
        if word == res[t][0]:
            res[t][1] += 1
            word = ""
            i += 1
            goto.check_word
        elif res[t][0] is None:
            res[t][0] = word
            res[t][1] = 1
            res += [[None, 0]]
            word = ""
            i += 1
            goto.check_word
        else:
            t += 1
            goto.res_maker
    elif text[i] == "$":
        res = res[:-1]
        res_words_count = t
        goto.end_check_word
    else:
        word += text[i]
    i += 1
    goto.check_word
    label.end_check_word

    # Сортування результатів за допомогою Bubble Sort
    i = 0
    label.sort_loop_1
    j = 0
    label.sort_loop_2
    if j >= res_words_count - i:
        goto.end_sort_loop_2
    if res[j][1] < res[j + 1][1]:
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
    print(f"\nMost common words: \n")
    label.print_res
    print(f"{i + 1}) {res[i][0]} - {res[i][1]}")
    if i < res_words_count and i < max_words_num - 1:
        i += 1
        goto.print_res
    return


main()
