# f = open("file.txt", "r", encoding="UTF-8")
# print(f.read(5))
# f.seek(0)
# print(f.read(5))
# print(f.readline())
# print(f.readline())
# print(f.readlines())
# for line in f.readlines():
    # print(line.replace("\n", ""))
    # print(line, end="")


# f = open("file_write.txt", "w", encoding="UTF-8")
# c = ["wdwadawd", "dwada", "dwhthh"]
# f.writelines(c)


# with open("file.txt", "r", encoding="UTF-8") as f:
#     print(f.read())
# print(f.read())

# TODO: Task №1
# lines = 0
# c = open("files/people.txt", "r", encoding="UTF-8")
# for line in c.readlines():
#      lines += 1
#      print(f'{lines}. {line}', end = "")
# c.close()

# TODO: Task 2
# people_file = open("files/people.txt", "r", encoding="UTF-8")
# age_file = open("files/ages.txt", "r", encoding="UTF-8")
# people_list = [line.replace("\n", "") for line in people_file]
# age_list = [line.replace("\n", "") for line in age_file]
# for i in range(len(people_list)):
#     print(f"{people_list[i]} - {age_list[i]}")



# TODO: Task 3
# cars = open("files/cars.txt", "w", encoding="UTF-8")
# n = int(input("Введите количество машин - "))
# for i in range(1, n + 1):
#     model = input("Введите модель машины - ")
#     colour = input("Введите цвет машины - ")
#     year = input("Введите год выпуска машины - ")
#     cars.write(f"{i} {model} {colour} {year}\n")
#     print("Машина записана "



# TODO: Task 4
# hobbies_file = open("files/hobbies.txt", "r", encoding="UTF-8")
# d = dict()
# for line in hobbies_file:
#     hobbie = line.split()[1]
#     d[hobbie] = []
#
# hobbies_file.seek(0)
#
# for line in hobbies_file:
#     name = line.split()[0]
#     hobbie = line.split()[1]
#     d[hobbie].append(name)

# print(*d["футбол"])
# names_list = list(d.keys())
# names_list.sort()
# for name in names_list:
#     print(f"{name} - {len(d[name])}")

#TODO: Task 5
# mark_file = open("files/marks.txt", "r", encoding="UTF-8")
# mark_dict = {}
# for line in mark_file:
#     name = line.split()[0]
#     mark_list = [int(mark) for mark in line.split()[1:]]
#     mark_dict[name] = mark_list
#
# average_dict = {}
# for name, marks in mark_dict.items():
#     average_dict[name]= round(sum(marks) / len(marks), 2)
# for name, marks in mark_dict.items():
#     if 2 not in marks:
#         print(name)

# max_average = max(average_dict.values())
# for name, average in average_dict.items():
#     if average == max_average:
#         print(name)
# count_five_list = []
#
# mark_file.seek(0)
# for line in mark_file:
#     mark_list = [int(mark) for mark in line.split()[1:]]
#     count_five_list.append(mark_list.count(5))
# max_count_five = max(count_five_list)
# for name, marks in mark_dict.items():
#     if marks.count(5) == max_count_five:
#         print(name)
# mark_file.close()

# Todo: Task 6
# def averege_season(season):
#     file = open("files/" + season + ".txt", "r", encoding="UTF-8")
#     sum_weath = 0
#     count_weath = 0
#     for line in file:
#         _list = [int(wint) for wint in line.split()[1:]]
#         sum_weath += sum(_list)
#         count_weath += len(_list)
#     file.close()
#     return f"{season} - {round(sum_weath / count_weath, 2)}"
#
#
# seasons_list = ["winter", "spring", "summer", "autumn"]
# all_seasons = open("files/all_seasons.txt", "w", encoding="UTF-8")
# for season in seasons_list:
#     all_seasons.write(f"{averege_season(season)}\n")
# print(all_seasons)
# all_seasons.close()





# for i in range(len(c)):
#     for j in range(len(c)):
#         if i + j == len(c) - 1:
#             print(c[i][j])

# for s in c:
#     print(sum(s))
# for j in range(len(c)):
#     s = 0
#     for i in range(len(c)):
#         s += c[i][j]
#     print(s)
# TODO : Task 8
# training_file = open("files/trainings.txt",  "r", encoding="UTF=8")
# sum_training = 0
# for day in training_file:
#     sum_training += int(day.split()[-2])
# print(sum_training)

# days_dict = {}
# for line in training_file:
#     day = line.split()[0]
#     hour = int(line.split()[-2])
#     days_dict[day] = days_dict.get(day, 0) + hour
# print(days_dict)


# training_dict = {}
# for line in training_file:
#     day = line.split()[0]
#     training_dict[day] = [0, 0]
#
# training_file.seek(0)
#
# for line in training_file:
#     day = line.split()[0]
#     hour = int(line.split()[-2])
#     training_dict[day][0] += hour
#     training_dict[day][1] += 1
#
# day_dict = {}
# for day, list_ in training_dict.items():
#     day_dict[day] = round(list_[0] / list_[1], 2)
#
# max_ = 0
# max_day = ""
# for day, k in day_dict.items():
#     if k > max_:
#         max_ = k
#         max_day = day
# print(max_day)

# lazy_dict = {}
# for line in training_file:
#     month = int(line.split()[1].split(".")[1])
#     hour = int(line.split()[-2])
#     if hour == 0:
#         lazy_dict[month] = lazy_dict.get(month, 0) + 1
#
# max_month = ""
# max_day = 0
# for month, day in lazy_dict.items():
#     if day > max_day:
#         max_day = day
#         max_month = month
#
#
# month_dict={ 1 : "January",
#        2 : "February",
#        3 : "March",
#        4 : "April",
#        5 : "May",
#        6 : "June",
#        7 : "July",
#        8 : "August",
#        9 : "September",
#        10 : "October",
#        11 : "November",
#        12 : "December"
# }
# print(month_dict[max_month])


# from random import randint
#
#
# def new_matrix(size, r):
#     matrix = []
#     for _ in range(size):
#         matrix.append([randint(r[0], r[1]) for i in range(size)])
#     return matrix
#
#
# def matrix_to_file(matrix, matrix_name):
#     matrix_file = open(matrix_name, "w", encoding="UTF-8")
#     for line in matrix:
#         matrix_file.write("\t".join(map(str, line)) + "\n")
#     matrix_file.close()


# def sum_matrix(matrix):
#     s = 0
#     for el in matrix:
#         s += sum(el)
#     return s


# def sum_line(matrix, matrix_name):
#     matrix_file = open(matrix_name, "a", encoding="UTF-8")
#     matrix_file.write("\n2.\n")
#     for line in matrix:
#         matrix_file.write(str(sum(line))+"\n")
#     matrix_file.close()


#
# def sum_column(matrix):
#     sum_col = []
#     for j in range(len(matrix)):
#         s = 0
#         for i in range(len(matrix)):
#             s += matrix[i][j]
#         sum_col.append(s)
#     return sum_col
#
#
# def max_element(matrix):
#     max_ = 0
#     for l in matrix:
#         for n in l:
#             if n > max_:
#                 max_ = n
#     return max_
#
# def min_element(matrix):
#     min_ = matrix[0][0]
#     for l in matrix:
#         for n in l:
#             if n < min_:
#                 min_ = n
#     return min_
#
#
# n = int(input("Введите количество матриц? "))
# r = list(map(int, input("Введите диапазон: ").split()))
# size = 5
# for i in range(1, n + 1):
#     matrix_name = 'matrix_files/' + 'matrix' + str(i) + ".txt"
#     matrix = new_matrix(size, r)
#     matrix_to_file(matrix, matrix_name)
#
#     matrix_file = open(matrix_name, "a", encoding="UTF-8")
    # matrix_file.write(f"\n1.{sum_matrix(matrix)}")
    # sum_line(matrix, matrix_name)
    # sum_c = sum_column(matrix)
    # matrix_file.write("\n3.\n")
    # for s in sum_c:
    #     matrix_file.write(str(s)+"\n")
    # matrix_file.write(f"\n4. {min_element(matrix)}")
    # matrix_file.write(f"\n5. {max_element(matrix)}")
    #
    # size *= 2

# TODO: TASK 9
def menu():
    print("1 - Вывести всех сотрудников")
    print("2 - Добавить сотрудника")
    print("3 - Вывести по зарплате(диапазон)")
    print("4 - Вывести по должности")
    print("5 - Повысить по должности(%)")
    print("6 - Сокращение по стажу")
    print("7 - Завершить работу")


def print_workers(db):
    db_file = open(db, "r", encoding="UTF-8")
    print()
    for worker in db_file:
        print(worker, end="")
    print("\n")
    db_file.close()


def add_worker(db):
    name = input("Введите фамилию: ")
    post = input("Введите должность: ")
    salary = input("Введите зарплату в рублях: ")
    years = input("Введите стаж: ")
    db_file = open(db, "a", encoding="UTF-8")
    db_file.write(f"\n{name} {post} {salary} {years}")
    print(f"{name} добавлен в базу\n")
    db_file.close()


def print_salary(db):
    db_file = open(db, "r", encoding="UTF-8")
    print()
    salary_range = list(map(int, input("Введите диапазон зарплаты через пробел: ").split()))
    for line in db_file:
        salary = int(line.split()[-2])
        if salary_range[0] <= salary <=salary_range[1]:
            name = line.split()[0]
            post = line.split()[1]
            print(f"{name} {post} {salary}")
    print()
    db_file.close()


def print_post(db):
    db_file = open(db, "r", encoding="UTF-8")
    print()
    post_find = input("Введите должность: ")
    for line in db_file:
        post = line.split()[1]
        if post == post_find:
            name = line.split()[0]
            print(name)
    print()
    db_file.close()


def up_salary_by_post_to_list(db):
    db_file = open(db, "r", encoding="UTF-8")
    print()
    post_find = input("Введите должность: ")
    percent_index = int(input("Введите процент индексации: "))
    workers_list = []
    for line in db_file:
        post = line.split()[1]
        name = line.split()[0]
        salary = int(line.split()[-2])
        years = line.split()[-1]
        if post == post_find:
            salary *= (1 + percent_index / 100)
        workers_list.append(str(f"{name} {post} {int(salary)} {years}"))
    db_file.close()
    return workers_list


def del_worker_by_post_to_list(db):
    db_file = open(db, "r", encoding="UTF-8")
    print()
    years_find = int(input("Введите минимальный допустимый стаж: "))
    workers_list = []
    for line in db_file:
        post = line.split()[1]
        name = line.split()[0]
        salary = line.split()[-2]
        years = int(line.split()[-1])
        if years >= years_find:
            workers_list.append(str(f"{name} {post} {salary} {years}"))
    print(f"\nСотрудники меньше стажа {years_find}, были уволены")
    db_file.close()
    return workers_list


def write_from_list_to_file(worker_list):
    db_file = open(db, "w", encoding="UTF-8")
    for worker in worker_list:
        db_file.write(worker + "\n")
    db_file.close()


db = input("Введите базу данных: ") + ".txt"
try:
    db_file = open(db, "r", encoding="UTF-8")

    while True:
        menu()
        answer = int(input("Введите номер: "))
        if answer == 7:
            print("Работа завершена")
            break
        elif answer == 1:
            print_workers(db)
        elif answer == 2:
            add_worker(db)
        elif answer == 3:
            print_salary(db)
        elif answer == 4:
            print_post(db)
        elif answer == 5:
            write_from_list_to_file(up_salary_by_post_to_list(db))
        elif answer == 6:
            write_from_list_to_file(del_worker_by_post_to_list(db))


except:
    print("Нет такой базы данных/ошибка")






