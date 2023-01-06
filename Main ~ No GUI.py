import random
from openpyxl import load_workbook
from pandas import DataFrame


def read_from_excel():
    global all_rows
    global book
    book = load_workbook("DataBase\\LibraryDataBase.xlsx")
    global sheet
    sheet = book.active
    rows = sheet.rows

    headers = [cell.value for cell in next(rows)]

    all_rows = []

    for row in rows:
        data = {}
        for book, cell in zip(headers, row):
            data[book] = cell.value
        all_rows.append(data)

    all_bar_codes = []

    # for g in all_rows:
    #     all_bar_codes.append(str(g["bar_code"]))

    # print(all_bar_codes)


def list_of_all_books():
    global all_books
    all_books = []
    global books_name
    print(
        "********************************************************************************************************************************************")
    print("\n")
    for books_name in all_rows:
        all_books.append(books_name["book_name"])

    print("Here are all the books we have in the DataBase:")
    print("\n")
    for _ in all_books:
        print(_, end="\n")
    print("\n")
    print(
        "********************************************************************************************************************************************")


def list_of_bar_codes():
    global all_bar_codes
    all_bar_codes = []
    global bar_codes
    for bar_codes in all_rows:
        all_bar_codes.append(int(bar_codes["bar_code"]))


def search_for_book():
    print("\n")
    print("1.Search by name     2.Search by bar-code")
    method = input("1 / 2 : ")
    print("\n")

    if method == "1":
        print(
            "********************************************************************************************************************************************")
        name = input("Enter the book you are looking for : ")
        print(
            "********************************************************************************************************************************************")
        for t in all_rows:
            if t["book_name"] == name:
                print("\n")
                print("The book you are searching for has the following datas in data base :")
                break
        for i in all_rows:
            if i["book_name"] == name:
                print(
                    "********************************************************************************************************************************************")
                print("Name :", i["book_name"])
                print("Author :", i["author"])
                print("Release-date :", i["release_date"])
                print("Bar-Code :", i["bar_code"])
                print("Numbers sold :", i["how_many_sold"])
                print("Numbers left :", i["how_many_left"])
                print(
                    "********************************************************************************************************************************************")
                break

        else:
            print("\n")
            print(
                "********************************************************************************************************************************************")
            print("Sorry! we either ran out of this book or never had it.")
            print(
                "********************************************************************************************************************************************")

    elif method == "2":
        print(
            "********************************************************************************************************************************************")
        bar_code = input("Enter the bar-code of the book you are looking for : ")
        print(
            "********************************************************************************************************************************************")

        for g in all_rows:
            if g["bar_code"] == bar_code:
                print("\n")
                print("The book you are searching for has the following datas in data base :")
                break

        for r in all_rows:
            if r["bar_code"] == bar_code:
                print(
                    "********************************************************************************************************************************************")
                print("Name :", r["book_name"])
                print("Author :", r["author"])
                print("Release-date :", r["release_date"])
                print("Bar-Code :", r["bar_code"])
                print("Numbers sold :", r["how_many_sold"])
                print("Numbers left :", r["how_many_left"])
                print(
                    "********************************************************************************************************************************************")
                break
        else:
            print("\n")
            print(
                "********************************************************************************************************************************************")
            print("Sorry! we either ran out of this book or never had it.")
            print(
                "********************************************************************************************************************************************")

    # else:
    # print("********************************************************************************************************************************************")
    # print("Sorry ! Right now , We have only 2 options available for you : (1.Search by name     2.Search by bar-code)")
    # print("********************************************************************************************************************************************")


def edit_excel():
    print("")
    print("1.Edit by name     2.Edit by bar-code")
    method = input("1 / 2 : ")
    if method == "1":
        print("\n")
        book = input("Which book do you wanna edit : ")
        if book not in all_books or book not in final_all_books:
            print(
                "********************************************************************************************************************************************")
            print("It seems this book you wanna edit , does't exists in the DataBase !")
            print(
                "********************************************************************************************************************************************")

        else:
            for w in all_rows:
                if w["book_name"] == book:
                    print("\n")
                    print("You can start editing")
                    print("\n")
                    print(
                        "********************************************************************************************************************************************")
                    new_name = input('Enter a new "book-name" : ')
                    print(
                        "********************************************************************************************************************************************")
                    new_author = input('Enter a new "author-name" : ')
                    print(
                        "********************************************************************************************************************************************")
                    new_release_date = input('Enter a new "release-date" : ')
                    print(
                        "********************************************************************************************************************************************")
                    new_bar_code = input('Enter a new "bar-code" : ')
                    print(
                        "********************************************************************************************************************************************")
                    new_how_many_sold = input('Enter a new "How many solds" number : ')
                    print(
                        "********************************************************************************************************************************************")
                    new_how_many_left = input('Enter a new "How many left" number : ')
                    print(
                        "********************************************************************************************************************************************")
                    print("\n")

            zero_list = []
            zero_counter = 0
            for _ in new_bar_code:
                if _ == "0":
                    zero_list.append(_)
                    zero_counter += 1
                else:
                    break

            zero_list_to_string = "".join(zero_list)
            new_bar_code = zero_list_to_string + new_bar_code[zero_counter:]

            temp_dict = {"book_name": new_name, "author": new_author, "release_date": new_release_date,
                         "bar_code": new_bar_code, "how_many_sold": new_how_many_sold,
                         "how_many_left": new_how_many_left}

            if new_name == "":
                print(
                    "********************************************************************************************************************************************")
                print('Can not assign an empty "new-book-name" !')
                print(
                    "********************************************************************************************************************************************")
                return 0
            elif new_author == "":
                print(
                    "********************************************************************************************************************************************")
                print('Can not assign an empty "new-author-name" !')
                print(
                    "********************************************************************************************************************************************")
                return 0
            elif new_release_date == "":
                print(
                    "********************************************************************************************************************************************")
                print('Can not assign an empty "new-release-date" !')
                print(
                    "********************************************************************************************************************************************")
                return 0
            elif new_bar_code == "":
                print(
                    "********************************************************************************************************************************************")
                print('Can not assign an empty "new-bar-code" !')
                print(
                    "********************************************************************************************************************************************")
                return 0
            elif new_how_many_sold == "":
                print(
                    "********************************************************************************************************************************************")
                print('Can not assign an empty "new-how-many-sold" !')
                print(
                    "********************************************************************************************************************************************")
                return 0
            elif new_how_many_left == "":
                print(
                    "********************************************************************************************************************************************")
                print('Can not assign an empty "new-how-many-left" !')
                print(
                    "********************************************************************************************************************************************")
                return 0

            elif len(new_release_date) != 4:
                print(
                    "********************************************************************************************************************************************")
                print('Your "release-date" should only contain 4 digits !')
                print(
                    "********************************************************************************************************************************************")


            elif len(new_bar_code) != 5:
                print(
                    "********************************************************************************************************************************************")
                print('Your "bar-code" should only contain 5 digits !')
                print(
                    "********************************************************************************************************************************************")

            else:
                temp_bar_code_list = []
                for o in all_rows:
                    temp_bar_code_list.append(o["bar_code"])

                if new_bar_code in temp_bar_code_list:
                    print(
                        "********************************************************************************************************************************************")
                    print("Sorry ! It seem that this barcode has already been taken.")
                    print(
                        "********************************************************************************************************************************************")


                else:
                    for _ in all_rows:
                        if _["book_name"] == book:
                            all_rows.remove(_)

                    all_rows.append(temp_dict)

                    df = DataFrame.from_dict(all_rows)
                    df.to_excel("DataBase\\LibraryDataBase.xlsx")
                    print(
                        "********************************************************************************************************************************************")
                    print('Updated Succesfully !')
                    print(
                        "********************************************************************************************************************************************")

    if method == "2":

        temp_list2 = []

        for m in all_rows:
            temp_list2.append(m["bar_code"])

        print("\n")
        bar_code = input("Which book do you wanna edit : ")
        if bar_code not in temp_list2:
            print(
                "********************************************************************************************************************************************")
            print("It seems this book you wanna edit , does't exists in the DataBase !")
            print(
                "********************************************************************************************************************************************")

        else:
            for e in all_rows:
                if e["bar_code"] == bar_code:
                    print("\n")
                    print("You can start editing")
                    print("\n")
                    print(
                        "********************************************************************************************************************************************")
                    new_name = input('Enter a new "book-name" : ')
                    print(
                        "********************************************************************************************************************************************")
                    new_author = input('Enter a new "author-name" : ')
                    print(
                        "********************************************************************************************************************************************")
                    new_release_date = input('Enter a new "release-date" : ')
                    print(
                        "********************************************************************************************************************************************")
                    new_bar_code = input('Enter a new "bar-code" : ')
                    print(
                        "********************************************************************************************************************************************")
                    new_how_many_sold = input('Enter a new "How many solds" number : ')
                    print(
                        "********************************************************************************************************************************************")
                    new_how_many_left = input('Enter a new "How many left" number : ')
                    print(
                        "********************************************************************************************************************************************")
                    print("\n")

            zero_list = []
            zero_counter = 0
            for z in new_bar_code:
                if z == "0":
                    zero_list.append(z)
                    zero_counter += 1
                else:
                    break

            zero_list_to_string = "".join(zero_list)
            new_bar_code = zero_list_to_string + new_bar_code[zero_counter:]

            temp_dict = {"book_name": new_name, "author": new_author, "release_date": new_release_date,
                         "bar_code": new_bar_code, "how_many_sold": new_how_many_sold,
                         "how_many_left": new_how_many_left}

            if new_name == "":
                print(
                    "********************************************************************************************************************************************")
                print('Can not assign an empty "new-book-name" !')
                print(
                    "********************************************************************************************************************************************")
                return 0

            elif new_author == "":
                print(
                    "********************************************************************************************************************************************")
                print('Can not assign an empty "new-author-name" !')
                print(
                    "********************************************************************************************************************************************")
                return 0

            elif new_release_date == "":
                print(
                    "********************************************************************************************************************************************")
                print('Can not assign an empty "new-release-date" !')
                print(
                    "********************************************************************************************************************************************")
                return 0

            elif new_bar_code == "":
                print(
                    "********************************************************************************************************************************************")
                print('Can not assign an empty "new-bar-code" !')
                print(
                    "********************************************************************************************************************************************")
                return 0

            elif new_how_many_sold == "":
                print(
                    "********************************************************************************************************************************************")
                print('Can not assign an empty "new-how-many-sold" !')
                print(
                    "********************************************************************************************************************************************")
                return 0

            elif new_how_many_left == "":
                print(
                    "********************************************************************************************************************************************")
                print('Can not assign an empty "new-how-many-left" !')
                print(
                    "********************************************************************************************************************************************")
                return 0

            elif len(new_release_date) != 4:
                print(
                    "********************************************************************************************************************************************")
                print('Your "release-date" should only contain 4 digits !')
                print(
                    "********************************************************************************************************************************************")


            elif len(new_bar_code) != 5:
                print(
                    "********************************************************************************************************************************************")
                print('Your "bar-code" should only contain 5 digits !')
                print(
                    "********************************************************************************************************************************************")

            else:
                temp_bar_code_list = []
                for o in all_rows:
                    temp_bar_code_list.append(o["bar_code"])

                if new_bar_code in temp_bar_code_list:
                    print(
                        "********************************************************************************************************************************************")
                    print("Sorry ! It seem that this barcode has already been taken.")
                    print(
                        "********************************************************************************************************************************************")


                else:
                    for r in all_rows:
                        if r["bar_code"] == bar_code:
                            all_rows.remove(r)

                    all_rows.append(temp_dict)

                    df = DataFrame.from_dict(all_rows)
                    df.to_excel("DataBase\\LibraryDataBase.xlsx")
                    print(
                        "********************************************************************************************************************************************")
                    print('Updated Succesfully !')
                    print(
                        "********************************************************************************************************************************************")

    # else:
    # print("\n")
    # print("********************************************************************************************************************************************")
    # print("Sorry ! Right now , We have only 2 options available for you (1.Edit by name     2.Edit by bar-code)")
    # print("********************************************************************************************************************************************")


def del_book():
    print("\n")
    print("1.Delete by name     2.Delete by bar-code")
    method = input("1 / 2 : ")
    print("\n")

    if method == "1":
        book_to_be_removed = input("Enter the book-name you wish to delete : ")
        for i in range(len(all_rows)):
            if all_rows[i]["book_name"] == book_to_be_removed:
                print(
                    "********************************************************************************************************************************************")
                sure = input(
                    "You are about to delete a book and all data related to that. Are you sure yo wanna continue (Y / N) : ")
                print(
                    "********************************************************************************************************************************************")
                sure = sure.lower()
                if sure == "y":
                    # all_books.remove(all_rows[i]["book_name"])
                    # final_all_books.remove(all_rows[i]["book_name"])
                    # all_bar_codes.remove(all_rows[i]["bar_code"])
                    # final_all_bar_codes.remove(all_rows[i]["bar_code"])

                    del all_rows[i]
                    print("\n")
                    print(
                        "********************************************************************************************************************************************")
                    print("Deleted Succesfully !")
                    print(
                        "********************************************************************************************************************************************")
                    break
                elif sure == "n":
                    pass

        df = DataFrame.from_dict(all_rows)
        df.to_excel("DataBase\\LibraryDataBase.xlsx")

    if method == "2":
        bar_code_to_be_removed = input("Enter the bar-code of the book you wish to delete : ")
        for j in range(len(all_rows)):
            if all_rows[j]["bar_code"] == bar_code_to_be_removed:
                print(
                    "********************************************************************************************************************************************")
                sure = input(
                    "You are about to delete a book and all data related to that. Are you sure yo wanna continue (Y / N) : ")
                print(
                    "********************************************************************************************************************************************")
                sure = sure.lower()
                if sure == "y":
                    # all_books.remove(all_rows[i]["book_name"])
                    # final_all_books.remove(all_rows[i]["book_name"])
                    # all_bar_codes.remove(all_rows[i]["bar_code"])
                    # final_all_bar_codes.remove(all_rows[i]["bar_code"])

                    del all_rows[j]
                    print("\n")
                    print(
                        "********************************************************************************************************************************************")
                    print("Deleted Succesfully !")
                    print(
                        "********************************************************************************************************************************************")
                    break
                if sure == "n":
                    pass
                    break
    # else:
    # print("********************************************************************************************************************************************")
    # print("Sorry ! Right now , We have only 2 options available for you (1.Delete by name     2.Delete by bar-code)")
    # print("********************************************************************************************************************************************")

    df = DataFrame.from_dict(all_rows)
    df.to_excel("DataBase\\LibraryDataBase.xlsx")


def add_book():
    global new_bar_code
    print(
        "********************************************************************************************************************************************")
    new_name = input('Enter a new "book-name" : ')
    print(
        "********************************************************************************************************************************************")
    new_author = input('Enter a new "author-name" : ')
    print(
        "********************************************************************************************************************************************")
    new_release_date = input('Enter a new "release-date" : ')
    print(
        "********************************************************************************************************************************************")
    new_bar_code = input('Enter a new "bar-code" : ')
    print(
        "********************************************************************************************************************************************")
    new_how_many_sold = input('Enter a new "How many solds" number : ')
    print(
        "********************************************************************************************************************************************")
    new_how_many_left = input('Enter a new "How many left" number : ')
    print(
        "********************************************************************************************************************************************")
    print("\n")
    temporary_dict = {"book_name": new_name, "author": new_author, "release_date": new_release_date,
                      "bar_code": new_bar_code, "how_many_sold": new_how_many_sold, "how_many_left": new_how_many_left}

    zero_list = []
    zero_counter = 0
    for _ in new_bar_code:
        if _ == "0":
            zero_list.append(_)
            zero_counter += 1
        else:
            break

    zero_list_to_string = "".join(zero_list)
    new_bar_code = zero_list_to_string + new_bar_code[zero_counter:]

    print(final_all_bar_codes)

    if new_name == "":
        print(
            "********************************************************************************************************************************************")
        print('Can not assign an empty "new-book-name" !')
        print(
            "********************************************************************************************************************************************")
        return 0

    elif new_author == "":
        print(
            "********************************************************************************************************************************************")
        print('Can not assign an empty "new-author-name" !')
        print(
            "********************************************************************************************************************************************")
        return 0

    elif new_release_date == "":
        print(
            "********************************************************************************************************************************************")
        print('Can not assign an empty "new-release-date" !')
        print(
            "********************************************************************************************************************************************")
        return 0
    elif new_bar_code == "":
        print(
            "********************************************************************************************************************************************")
        print('Can not assign an empty "new-bar-code" !')
        print(
            "********************************************************************************************************************************************")
        return 0

    elif new_how_many_sold == "":
        print(
            "********************************************************************************************************************************************")
        print('Can not assign an empty "new-how-many-sold" !')
        print(
            "********************************************************************************************************************************************")
        return 0

    elif new_how_many_left == "":
        print(
            "********************************************************************************************************************************************")
        print('Can not assign an empty "new-how-many-left" !')
        print(
            "********************************************************************************************************************************************")
        return 0

    elif int(new_bar_code) in final_all_bar_codes:
        print(
            "********************************************************************************************************************************************")
        print("Sorry ! It seems that this book already exists in DataBase.")
        print(
            "********************************************************************************************************************************************")

    elif not new_release_date.isdigit():
        print(
            "********************************************************************************************************************************************")
        print("Release date is not numeric !")
        print(
            "********************************************************************************************************************************************")

    elif not new_bar_code.isdigit():
        print(
            "********************************************************************************************************************************************")
        print("Bar-codeis not numeric !")
        print(
            "********************************************************************************************************************************************")

    elif (len(new_release_date)) != 4:
        print(
            "********************************************************************************************************************************************")
        print('The "release-date" must have exactly 4 number !')
        print(
            "********************************************************************************************************************************************")

    elif len(new_bar_code) != 5:
        print(
            "********************************************************************************************************************************************")
        print('The "bar-code" must have exactly 5 numbers !')
        print(
            "********************************************************************************************************************************************")

    else:
        all_rows.append(temporary_dict)

        all_books.append(new_name)
        final_all_books.append(new_name)
        all_bar_codes.append(new_bar_code)
        final_all_bar_codes.append(str(new_bar_code))

        print(
            "********************************************************************************************************************************************")
        print("Added Succesfully!")
        print(
            "********************************************************************************************************************************************")

        df = DataFrame.from_dict(all_rows)
        df.to_excel("DataBase\\LibraryDataBase.xlsx")

        del temporary_dict


def what_to_do():
    print("\n")
    print(
        "1.Search     2.Add     3.Delete     4.Edit     5.Show all bar-codes     6.Show all books     7.Book counter     8.Last update     9.Code generator    10.Exit")
    task = input("1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 : ")
    print("\n")
    task = task.lower()
    if task == "1":
        search_for_book()
    elif task == "2":
        add_book()
    elif task == "3":
        del_book()
    elif task == "4":
        edit_excel()
    elif task == "5":
        print("\n")
        print("Here is a list of all bar-codes for you : ")
        print(
            "********************************************************************************************************************************************")
        for _ in all_rows:
            if len(str(_["bar_code"])) == 5:
                print(_["bar_code"], end="\n")
        print(
            "********************************************************************************************************************************************")
        print("\n")
    elif task == "6":
        print("\n")
        print("Here is a list of all books for you : ")
        print(
            "********************************************************************************************************************************************")
        for x in all_rows:
            print(x['book_name'], end="\n")
        # print(set(all_rows))
        print(
            "********************************************************************************************************************************************")
        print("\n")
    elif task == "7":
        book_count()

    elif task == "8":
        lates_add()

    elif task == "9":
        code_generate()

    elif task == "10":
        exit()
    else:
        print(
            "********************************************************************************************************************************************")
        print(
            'Sorry ! This task is not available yet. please choose between : (1.Search     2.Edit     3.Show all bar-codes    4.Show all books     5.Show all bar-codes     6.Show all books     7.Book counter     8.Last update     9.Code generator     10.Exit)')
        print(
            "********************************************************************************************************************************************")


def update():
    for books_name in all_rows:
        all_books.append(books_name["book_name"])
    for bar_codes in all_rows:
        all_bar_codes.append(int(bar_codes["bar_code"]))

    global final_all_books
    final_all_books = []
    [final_all_books.append(x) for x in all_books if x not in final_all_books]

    global final_all_bar_codes
    final_all_bar_codes = []
    [final_all_bar_codes.append(x) for x in all_bar_codes if x not in final_all_bar_codes]


def book_count():
    print(
        "********************************************************************************************************************************************")
    print("Total books in DataBase :", len(all_rows))
    print(
        "********************************************************************************************************************************************")


def lates_add():
    update_list_of_dictionaries = []
    update_list_of_dictionaries.append(all_rows[-1])

    for _ in update_list_of_dictionaries:
        print("\n")
        print(
            "********************************************************************************************************************************************")
        print('The last "book-name" that has been updated :', _["book_name"])
        print('The last "author-name" that has been updated :', _["author"])
        print('The last "release-date" that has been updated :', _["release_date"])
        print('The last "bar-code" that has been updated :', _["bar_code"])
        print('The last "how many sold that has been updated :', _["how_many_sold"])
        print('The last "how many left" that has been updated :', _["how_many_left"])
        print(
            "********************************************************************************************************************************************")


def code_generate():
    list = []
    for i in range(10000, 99999):
        list.append(i)

    code = random.sample(list, 1)

    try:
        for _ in code:
            print(
                "********************************************************************************************************************************************")
            print("Copy this number : ", end="")
            print(_)
            print(
                "********************************************************************************************************************************************")


    except:
        print(
            "********************************************************************************************************************************************")
        print('All barcodes from "10000" ~ "99999 have been chosen ! Try to choose something from "00000" ~ "09999".')
        print(
            "********************************************************************************************************************************************")


status = True
read_from_excel()
list_of_all_books()
list_of_bar_codes()

while status:
    update()
    read_from_excel()
    what_to_do()
