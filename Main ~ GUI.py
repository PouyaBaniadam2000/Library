import os
import sys
import pyperclip
from tkinter import filedialog
from tkinter import *
import random
from openpyxl import load_workbook
from pandas import DataFrame


def resource_path(relative_path):
    global base_path
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("Assets\\Images")

    return os.path.join(base_path, relative_path)


def main_menu():
    """Back-End of buttons start here"""

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

            global all_bar_codes
            global all_books

            all_bar_codes = []
            all_books = []

            for g in all_rows:
                all_bar_codes.append(str(g["bar_code"]))

            for h in all_rows:
                all_books.append(str(h["book_name"]))

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

    def search_book():
        global b61
        global back_btn
        global search_by_name_btn
        global search_by_bar_code_btn

        def search_by_name():
            global bg68
            global submit_btn
            global back_btn

            def submit():
                global return_to_main_menu_btn
                global save_as_txt_btn

                def save_as_txt_file():
                    file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[
                        ("Text file", ".txt"),
                        ("HTML file", ".html")
                    ])
                    file.write(saving_file)
                    file.close()

                name = book_name_entry.get()

                temp_list = []

                if name == "":
                    global bg65
                    global return_to_main_menu_btn
                    global back_btn

                    bg65 = PhotoImage(file=resource_path("cannotleavethebarcodeinputblank.png"))
                    bg65_label = Label(root, image=bg65)
                    bg65_label.place(x=0, y=0)

                    return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                    return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                    real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                          width=250, height=200, activebackground="black", border=0,
                                                          command=main_menu)
                    real_return_to_main_menu_btn.place(x=850, y=585)

                    back_btn = PhotoImage(file=resource_path("back_button.png"))
                    back_btn_label = Label(image=back_btn)

                    real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                           activebackground="black", border=0, command=search_by_name)
                    real_back_btn.place(x=400, y=585)


                else:

                    for _ in all_rows:
                        temp_list.append(str(_["book_name"]))

                    if name in temp_list:
                        global bg64
                        bg64 = PhotoImage(file=resource_path("bookinfo.png"))
                        bg64_label = Label(root, image=bg64)
                        bg64_label.place(x=0, y=0)

                        for g in all_rows:
                            if name in g["book_name"]:
                                break

                        book_name1 = g["book_name"]
                        author1 = g["author"]
                        release_date1 = g["release_date"]
                        bars_code1 = g["bar_code"]
                        how_many_sold1 = g["how_many_sold"]
                        how_many_left1 = g["how_many_left"]

                        book_name_label = Label(root, text=book_name1, border=0, background="#252525",
                                                font=("Andalus", 35), fg="white")
                        book_name_label.place(x=560, y=235)

                        author_label = Label(root, text=author1, border=0, background="#252525", font=("Andalus", 35),
                                             fg="white")
                        author_label.place(x=480, y=295)

                        release_date_label = Label(root, text=release_date1, border=0, background="#252525",
                                                   font=("Andalus", 35), fg="white")
                        release_date_label.place(x=550, y=355)

                        bar_code_label = Label(root, text=bars_code1, border=0, background="#252525",
                                               font=("Andalus", 35), fg="white")
                        bar_code_label.place(x=510, y=415)

                        how_many_sold_label = Label(root, text=how_many_sold1, border=0, background="#252525",
                                                    font=("Andalus", 35), fg="white")
                        how_many_sold_label.place(x=610, y=475)

                        how_many_left_label = Label(root, text=how_many_left1, border=0, background="#252525",
                                                    font=("Andalus", 35), fg="white")
                        how_many_left_label.place(x=610, y=535)

                        saving_file = f"Book name : {book_name1}\nAuthor : {author1}\nRelease date : {release_date1}\nBar-code : {bars_code1}\nHow many sold : {how_many_sold1}\nHow many left : {how_many_left1}"

                        return_to_main_menu_btn = PhotoImage(file=resource_path("greenreturntomainmenu_button.png"))
                        return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                        real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                              bg="#252525", width=250, height=200,
                                                              activebackground="#252525", border=0, command=main_menu)
                        real_return_to_main_menu_btn.place(x=1080, y=260)

                        save_as_txt_btn = PhotoImage(file=resource_path("saveastxt_button.png"))
                        save_as_txt_btn_label = Label(image=save_as_txt_btn)

                        real_save_as_txt_btn = Button(root, text="Start", image=save_as_txt_btn, bg="#252525",
                                                      width=280, height=220, activebackground="#252525", border=0,
                                                      command=save_as_txt_file)
                        real_save_as_txt_btn.place(x=1075, y=480)


                    else:
                        global bg66

                        bg66 = PhotoImage(file=resource_path("sorryitseemsthatthisbookdoesntexistsinyourlibrary.png"))
                        bg66_label = Label(root, image=bg66)
                        bg66_label.place(x=0, y=0)

                        return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                        return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                        real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                              bg="black", width=250, height=200,
                                                              activebackground="black", border=0, command=main_menu)
                        real_return_to_main_menu_btn.place(x=850, y=585)

                        back_btn = PhotoImage(file=resource_path("back_button.png"))
                        back_btn_label = Label(image=back_btn)

                        real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                               activebackground="black", border=0, command=search_by_name)
                        real_back_btn.place(x=400, y=585)

            bg68 = PhotoImage(file=resource_path("searchbyname_screen.png"))
            bg68_label = Label(root, image=bg68)
            bg68_label.place(x=0, y=0)

            submit_btn = PhotoImage(file=resource_path("submit_button.png"))
            submit_btn_label = Label(image=submit_btn)

            real_submit_btn = Button(root, text="Start", image=submit_btn, bg="#272727", width=250, height=200,
                                     activebackground="#272727", border=0, command=submit)
            real_submit_btn.place(x=845, y=585)

            back_btn = PhotoImage(file=resource_path("back_button.png"))
            back_btn_label = Label(image=back_btn)

            real_back_btn = Button(root, text="Start", image=back_btn, bg="#272727", width=250, height=200,
                                   activebackground="#272727", border=0, command=search_book)
            real_back_btn.place(x=400, y=585)

            book_name_entry = Entry(root, border=0, background="#3C3C3C", fg="red", font=("Andalus", 24))
            book_name_entry.place(x=770, y=410, width=258, height=33)

        def search_by_bar_code():
            global bg63
            global submit_btn
            global back_btn

            def submit():
                global return_to_main_menu_btn
                global save_as_txt_btn

                def save_as_txt_file():
                    file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[
                        ("Text file", ".txt"),
                        ("HTML file", ".html")
                    ])
                    file.write(saving_file)
                    file.close()

                barss_code = barss_code_entry.get()

                temp_list = []

                if barss_code == "":
                    global bg65
                    global return_to_main_menu_btn
                    global back_btn

                    bg65 = PhotoImage(file=resource_path("cannotleavethebarcodeinputblank.png"))
                    bg65_label = Label(root, image=bg65)
                    bg65_label.place(x=0, y=0)

                    return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                    return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                    real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                          width=250, height=200, activebackground="black", border=0,
                                                          command=main_menu)
                    real_return_to_main_menu_btn.place(x=850, y=585)

                    back_btn = PhotoImage(file=resource_path("back_button.png"))
                    back_btn_label = Label(image=back_btn)

                    real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                           activebackground="black", border=0, command=search_by_bar_code)
                    real_back_btn.place(x=400, y=585)


                else:

                    for _ in all_rows:
                        temp_list.append(str(_["bar_code"]))

                    if int(barss_code) in temp_list or str(barss_code) in temp_list:
                        global bg64
                        bg64 = PhotoImage(file=resource_path("bookinfo.png"))
                        bg64_label = Label(root, image=bg64)
                        bg64_label.place(x=0, y=0)

                        for g in all_rows:
                            if g["bar_code"] == str(barss_code) or g["bar_code"] == int(barss_code):
                                book_name1 = g["book_name"]
                                author1 = g["author"]
                                release_date1 = g["release_date"]
                                bars_code1 = g["bar_code"]
                                how_many_sold1 = g["how_many_sold"]
                                how_many_left1 = g["how_many_left"]

                        book_name_label = Label(root, text=book_name1, border=0, background="#252525",
                                                font=("Andalus", 35), fg="white")
                        book_name_label.place(x=560, y=235)

                        author_label = Label(root, text=author1, border=0, background="#252525", font=("Andalus", 35),
                                             fg="white")
                        author_label.place(x=480, y=295)

                        release_date_label = Label(root, text=release_date1, border=0, background="#252525",
                                                   font=("Andalus", 35), fg="white")
                        release_date_label.place(x=550, y=355)

                        bar_code_label = Label(root, text=bars_code1, border=0, background="#252525",
                                               font=("Andalus", 35), fg="white")
                        bar_code_label.place(x=510, y=415)

                        how_many_sold_label = Label(root, text=how_many_sold1, border=0, background="#252525",
                                                    font=("Andalus", 35), fg="white")
                        how_many_sold_label.place(x=610, y=475)

                        how_many_left_label = Label(root, text=how_many_left1, border=0, background="#252525",
                                                    font=("Andalus", 35), fg="white")
                        how_many_left_label.place(x=610, y=535)

                        saving_file = f"Book name : {book_name1}\nAuthor : {author1}\nRelease date : {release_date1}\nBar-code : {barss_code}\nHow many sold : {how_many_sold1}\nHow many left : {how_many_left1}"

                        return_to_main_menu_btn = PhotoImage(file=resource_path("greenreturntomainmenu_button.png"))
                        return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                        real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                              bg="#252525", width=250, height=200,
                                                              activebackground="#252525", border=0, command=main_menu)
                        real_return_to_main_menu_btn.place(x=1080, y=260)

                        save_as_txt_btn = PhotoImage(file=resource_path("saveastxt_button.png"))
                        save_as_txt_btn_label = Label(image=save_as_txt_btn)

                        real_save_as_txt_btn = Button(root, text="Start", image=save_as_txt_btn, bg="#252525",
                                                      width=280, height=220, activebackground="#252525", border=0,
                                                      command=save_as_txt_file)
                        real_save_as_txt_btn.place(x=1075, y=480)


                    else:
                        global bg66

                        bg66 = PhotoImage(file=resource_path("sorryitseemsthatthisbookdoesntexistsinyourlibrary.png"))
                        bg66_label = Label(root, image=bg66)
                        bg66_label.place(x=0, y=0)

                        return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                        return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                        real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                              bg="black", width=250, height=200,
                                                              activebackground="black", border=0, command=main_menu)
                        real_return_to_main_menu_btn.place(x=850, y=585)

                        back_btn = PhotoImage(file=resource_path("back_button.png"))
                        back_btn_label = Label(image=back_btn)

                        real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                               activebackground="black", border=0, command=search_by_bar_code)
                        real_back_btn.place(x=400, y=585)

            bg63 = PhotoImage(file=resource_path("searchbybarcode_screen.png"))
            bg63_label = Label(root, image=bg63)
            bg63_label.place(x=0, y=0)

            submit_btn = PhotoImage(file=resource_path("submit_button.png"))
            submit_btn_label = Label(image=submit_btn)

            real_submit_btn = Button(root, text="Start", image=submit_btn, bg="#272727", width=250, height=200,
                                     activebackground="#272727", border=0, command=submit)
            real_submit_btn.place(x=845, y=585)

            back_btn = PhotoImage(file=resource_path("back_button.png"))
            back_btn_label = Label(image=back_btn)

            real_back_btn = Button(root, text="Start", image=back_btn, bg="#272727", width=250, height=200,
                                   activebackground="#272727", border=0, command=search_book)
            real_back_btn.place(x=400, y=585)

            barss_code_entry = Entry(root, border=0, background="#3C3C3C", fg="red", font=("Andalus", 24))
            barss_code_entry.place(x=890, y=410, width=95, height=33)

        b61 = PhotoImage(file=resource_path("searchmethods_screen.png"))
        b61_label = Label(root, image=b61)
        b61_label.place(x=0, y=0)

        back_btn = PhotoImage(file=resource_path("back_button.png"))
        back_btn_label = Label(image=back_btn)

        real_back_btn = Button(root, text="Start", image=back_btn, bg="#00FFE0", width=270, height=220,
                               activebackground="#00FFE0", border=0, command=main_menu)
        real_back_btn.place(x=655, y=575)

        search_by_name_btn = PhotoImage(file=resource_path("searchbyname_button.png"))
        search_by_name_btn_label = Label(image=search_by_name_btn)

        real_search_by_name_btn = Button(root, text="Start", image=search_by_name_btn, bg="#242C2B", width=250,
                                         height=220, activebackground="#242C2B", border=0, command=search_by_name)
        real_search_by_name_btn.place(x=1150, y=375)

        search_by_bar_code_btn = PhotoImage(file=resource_path("searchbybarcode_button.png"))
        search_by_bar_code_btn_label = Label(image=search_by_bar_code_btn)

        real_search_by_bar_code_btn = Button(root, text="Start", image=search_by_bar_code_btn, bg="#00FFE0", width=270,
                                             height=250, activebackground="#00FFE0", border=0,
                                             command=search_by_bar_code)
        real_search_by_bar_code_btn.place(x=150, y=375)

    def add_book():

        global bg2
        global back_btn
        global submit_btn

        bg2 = PhotoImage(file=resource_path("newbookdataget_srcreen.png"))
        bg2_label = Label(root, image=bg2)
        bg2_label.place(x=0, y=0)

        back_btn = PhotoImage(file=resource_path("back_button.png"))
        back_btn_label = Label(image=back_btn)

        real_back_btn = Button(root, text="Start", image=back_btn, bg="#252525", width=250, height=200,
                               activebackground="#252525", border=0, command=main_menu)
        real_back_btn.place(x=465, y=575)

        def submit():
            new_name = book_name_entry.get()
            new_name = str(new_name)

            new_author = author_entry.get()
            new_author = str(new_author)

            new_release_date = release_date_entry.get()
            new_release_date = str(new_release_date)

            new_bar_code = bar_code_entry.get()
            new_bar_code = str(new_bar_code)

            new_how_many_sold = how_many_sold_entry.get()
            new_how_many_sold = str(new_how_many_sold)

            new_how_many_left = how_many_left_entry.get()
            new_how_many_left = str(new_how_many_left)

            temporary_dict = {"book_name": new_name, "author": new_author, "release_date": new_release_date,
                              "bar_code": new_bar_code, "how_many_sold": new_how_many_sold,
                              "how_many_left": new_how_many_left}

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

            if new_name == "":
                global return_to_main_menu_btn
                global back_btn

                global bg4
                bg4 = PhotoImage(file=resource_path("cannotassignanemptynewbookname.png"))
                bg4_label = Label(root, image=bg4)
                bg4_label.place(x=0, y=0)

                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                      width=250, height=200, activebackground="black", border=0,
                                                      command=main_menu)
                real_return_to_main_menu_btn.place(x=800, y=575)

                back_btn = PhotoImage(file=resource_path("back_button.png"))
                back_btn_label = Label(image=back_btn)

                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                       activebackground="black", border=0, command=add_book)
                real_back_btn.place(x=465, y=575)


            elif new_author == "":

                global bg5
                bg5 = PhotoImage(file=resource_path("cannotassignanemptynewauthorname.png"))
                bg5_label = Label(root, image=bg5)
                bg5_label.place(x=0, y=0)

                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                      width=250, height=200, activebackground="black", border=0,
                                                      command=main_menu)
                real_return_to_main_menu_btn.place(x=800, y=575)

                back_btn = PhotoImage(file=resource_path("back_button.png"))
                back_btn_label = Label(image=back_btn)

                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                       activebackground="black", border=0, command=add_book)
                real_back_btn.place(x=465, y=575)


            elif new_release_date == "":

                global bg6
                bg6 = PhotoImage(file=resource_path("cannotassignanemptynewreleasedate.png"))
                bg6_label = Label(root, image=bg6)
                bg6_label.place(x=0, y=0)

                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                      width=250, height=200, activebackground="black", border=0,
                                                      command=main_menu)
                real_return_to_main_menu_btn.place(x=800, y=575)

                back_btn = PhotoImage(file=resource_path("back_button.png"))
                back_btn_label = Label(image=back_btn)

                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                       activebackground="black", border=0, command=add_book)
                real_back_btn.place(x=465, y=575)


            elif new_bar_code == "":

                global bg7
                bg7 = PhotoImage(file=resource_path("cannotassignanemptynewbarcode.png"))
                bg7_label = Label(root, image=bg7)
                bg7_label.place(x=0, y=0)

                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                      width=250, height=200, activebackground="black", border=0,
                                                      command=main_menu)
                real_return_to_main_menu_btn.place(x=800, y=575)

                back_btn = PhotoImage(file=resource_path("back_button.png"))
                back_btn_label = Label(image=back_btn)

                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                       activebackground="black", border=0, command=add_book)
                real_back_btn.place(x=465, y=575)


            elif new_how_many_sold == "":

                global bg8
                bg8 = PhotoImage(file=resource_path("cannotassignanemptynewhowmanysold.png"))
                bg8_label = Label(root, image=bg8)
                bg8_label.place(x=0, y=0)

                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                      width=250, height=200, activebackground="black", border=0,
                                                      command=main_menu)
                real_return_to_main_menu_btn.place(x=800, y=575)

                back_btn = PhotoImage(file=resource_path("back_button.png"))
                back_btn_label = Label(image=back_btn)

                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                       activebackground="black", border=0, command=add_book)
                real_back_btn.place(x=465, y=575)


            elif new_how_many_left == "":

                global bg9
                bg9 = PhotoImage(file=resource_path("cannotassignanemptynewrhowmanyleft.png"))
                bg9_label = Label(root, image=bg9)
                bg9_label.place(x=0, y=0)

                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                      width=250, height=200, activebackground="black", border=0,
                                                      command=main_menu)
                real_return_to_main_menu_btn.place(x=800, y=575)

                back_btn = PhotoImage(file=resource_path("back_button.png"))
                back_btn_label = Label(image=back_btn)

                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                       activebackground="black", border=0, command=add_book)
                real_back_btn.place(x=465, y=575)


            elif str(new_bar_code) in final_all_bar_codes:
                global bg13
                bg13 = PhotoImage(file=resource_path("sorryitseemsthatthisbookalreadyexistsindatabase.png"))
                bg13_label = Label(root, image=bg13)
                bg13_label.place(x=0, y=0)

                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                      width=250, height=200, activebackground="black", border=0,
                                                      command=main_menu)
                real_return_to_main_menu_btn.place(x=800, y=575)

                back_btn = PhotoImage(file=resource_path("back_button.png"))
                back_btn_label = Label(image=back_btn)

                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                       activebackground="black", border=0, command=add_book)
                real_back_btn.place(x=465, y=575)



            elif not new_release_date.isdigit():
                global bg16
                bg16 = PhotoImage(file=resource_path("yourreleasedatecontainsacharactorwhichisnotnumeric.png"))
                bg16_label = Label(root, image=bg16)
                bg16_label.place(x=0, y=0)

                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                      width=250, height=200, activebackground="black", border=0,
                                                      command=main_menu)
                real_return_to_main_menu_btn.place(x=800, y=575)

                back_btn = PhotoImage(file=resource_path("back_button.png"))
                back_btn_label = Label(image=back_btn)

                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                       activebackground="black", border=0, command=add_book)
                real_back_btn.place(x=465, y=575)


            elif not new_bar_code.isdigit():
                global bg17
                bg17 = PhotoImage(file=resource_path("yourbarcodecontainsacharactorwhichisnotnumeric.png"))
                bg17_label = Label(root, image=bg17)
                bg17_label.place(x=0, y=0)

                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                      width=250, height=200, activebackground="black", border=0,
                                                      command=main_menu)
                real_return_to_main_menu_btn.place(x=800, y=575)

                back_btn = PhotoImage(file=resource_path("back_button.png"))
                back_btn_label = Label(image=back_btn)

                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                       activebackground="black", border=0, command=add_book)
                real_back_btn.place(x=465, y=575)


            elif (len(new_release_date)) != 4:
                global bg11
                bg11 = PhotoImage(file=resource_path("thereleasedatemusthaveexactly4numbers.png"))
                bg11_label = Label(root, image=bg11)
                bg11_label.place(x=0, y=0)

                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                      width=250, height=200, activebackground="black", border=0,
                                                      command=main_menu)
                real_return_to_main_menu_btn.place(x=800, y=575)

                back_btn = PhotoImage(file=resource_path("back_button.png"))
                back_btn_label = Label(image=back_btn)

                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                       activebackground="black", border=0, command=add_book)
                real_back_btn.place(x=465, y=575)


            elif len(new_bar_code) != 5:
                global bg12
                bg12 = PhotoImage(file=resource_path("thebarcodemusthaveexactly5numbers.png"))
                bg12_label = Label(root, image=bg12)
                bg12_label.place(x=0, y=0)

                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                      width=250, height=200, activebackground="black", border=0,
                                                      command=main_menu)
                real_return_to_main_menu_btn.place(x=800, y=575)

                back_btn = PhotoImage(file=resource_path("back_button.png"))
                back_btn_label = Label(image=back_btn)

                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                       activebackground="black", border=0, command=add_book)
                real_back_btn.place(x=465, y=575)



            else:
                all_rows.append(temporary_dict)

                # final_all_books.append(new_name)
                all_bar_codes.append(new_bar_code)
                # final_all_bar_codes.append(str(new_bar_code))

                df = DataFrame.from_dict(all_rows)
                df.to_excel("DataBase\\LibraryDataBase.xlsx")

                del temporary_dict

                global bg14
                bg14 = PhotoImage(file=resource_path("addedsuccesfully.png"))
                bg14_label = Label(root, image=bg14)
                bg14_label.place(x=0, y=0)

                return_to_main_menu_btn = PhotoImage(file=resource_path("greenreturntomainmenu_button.png"))
                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                      width=250, height=200, activebackground="black", border=0,
                                                      command=main_menu)
                real_return_to_main_menu_btn.place(x=615, y=575)

        book_name_entry = Entry(root, border=0, background="#171717", fg="red", font=("Andalus", 24))
        book_name_entry.place(x=660, y=225, width=555, height=30)

        author_entry = Entry(root, border=0, background="#171717", fg="red", font=("Andalus", 24))
        author_entry.place(x=590, y=280, width=615, height=30)

        release_date_entry = Entry(root, border=0, background="#171717", fg="red", font=("Andalus", 24))
        release_date_entry.place(x=655, y=335, width=550, height=30)

        bar_code_entry = Entry(root, border=0, background="#171717", fg="red", font=("Andalus", 24))
        bar_code_entry.place(x=635, y=390, width=575, height=30)

        how_many_sold_entry = Entry(root, border=0, background="#171717", fg="red", font=("Andalus", 24))
        how_many_sold_entry.place(x=730, y=445, width=485, height=30)

        how_many_left_entry = Entry(root, border=0, background="#171717", fg="red", font=("Andalus", 24))
        how_many_left_entry.place(x=730, y=500, width=490, height=30)

        submit_btn = PhotoImage(file=resource_path("submit_button.png"))
        submit_btn_label = Label(image=submit_btn)

        real_submit_btn = Button(root, text="Start", image=submit_btn, bg="#252525", width=250, height=200,
                                 activebackground="#252525", border=0, command=submit)
        real_submit_btn.place(x=800, y=575)

    def delete_book():

        def delete_by_name():

            def submit():

                def deleted_succesfully():
                    global bg25
                    global return_to_main_menu_btn

                    bg25 = PhotoImage(file=resource_path("deletedsuccesfully.png"))
                    bg25_label = Label(root, image=bg25)
                    bg25_label.place(x=0, y=0)

                    return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                    return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                    real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                          width=250, height=200, activebackground="black", border=0,
                                                          command=main_menu)
                    real_return_to_main_menu_btn.place(x=645, y=575)

                    for i in range(len(all_rows)):
                        if str(all_rows[i]["book_name"]) == str(book_to_be_removed):
                            del (all_rows[i])
                            break

                    df = DataFrame.from_dict(all_rows)
                    df.to_excel("DataBase\\LibraryDataBase.xlsx")

                global bg24
                global bg26
                global bg35
                global return_to_main_menu_btn
                global back_btn

                book_to_be_removed = book_name_entry.get()

                if book_to_be_removed == "":
                    bg35 = PhotoImage(file=resource_path("cannotleavethebooknameinputblank.png"))
                    bg35_label = Label(root, image=bg35)
                    bg35_label.place(x=0, y=0)

                    return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                    return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                    real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                          width=250, height=200, activebackground="black", border=0,
                                                          command=main_menu)
                    real_return_to_main_menu_btn.place(x=850, y=585)

                    back_btn = PhotoImage(file=resource_path("back_button.png"))
                    back_btn_label = Label(image=back_btn)

                    real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                           activebackground="black", border=0, command=delete_by_name)
                    real_back_btn.place(x=400, y=585)


                else:

                    temp_list = []

                    for i in all_rows:
                        temp_list.append(str(i["book_name"]))

                    if book_to_be_removed in temp_list:

                        bg24 = PhotoImage(
                            file=resource_path("youareabottodeleteabookandallofitsdatafromyourlibraryareyousure.png"))
                        bg24_label = Label(root, image=bg24)
                        bg24_label.place(x=0, y=0)

                        real_yeap_btn = Button(root, text="Yeap :)", font=("Andalus", 30), border=0,
                                               background="#A50000", activebackground="#A50000",
                                               command=deleted_succesfully)
                        real_yeap_btn.place(x=952, y=637, width=155, height=90)

                        real_nope_btn = Button(root, text="Nope :(", font=("Andalus", 30), border=0,
                                               background="#02CBE7", activebackground="#02CBE7", command=delete_by_name)
                        real_nope_btn.place(x=410, y=637, width=155, height=90)

                    else:
                        bg26 = PhotoImage(file=resource_path("sorryitseemsthatthisbookdoesntexistsinyourlibrary.png"))
                        bg26_label = Label(root, image=bg26)
                        bg26_label.place(x=0, y=0)

                        return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                        return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                        real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                              bg="black", width=250, height=200,
                                                              activebackground="black", border=0, command=main_menu)
                        real_return_to_main_menu_btn.place(x=850, y=585)

                        back_btn = PhotoImage(file=resource_path("back_button.png"))
                        back_btn_label = Label(image=back_btn)

                        real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                               activebackground="black", border=0, command=delete_by_name)
                        real_back_btn.place(x=400, y=585)

            global bg20
            global submit_btn
            global back_btn

            bg20 = PhotoImage(file=resource_path("booknamedelete_screen.png"))
            bg20_label = Label(root, image=bg20)
            bg20_label.place(x=0, y=0)

            submit_btn = PhotoImage(file=resource_path("submit_button.png"))
            submit_btn_label = Label(image=submit_btn)

            real_submit_btn = Button(root, text="Start", image=submit_btn, bg="#272727", width=250, height=200,
                                     activebackground="#272727", border=0, command=submit)
            real_submit_btn.place(x=845, y=585)

            back_btn = PhotoImage(file=resource_path("back_button.png"))
            back_btn_label = Label(image=back_btn)

            real_back_btn = Button(root, text="Start", image=back_btn, bg="#272727", width=250, height=200,
                                   activebackground="#272727", border=0, command=delete_book)
            real_back_btn.place(x=400, y=585)

            book_name_entry = Entry(root, border=0, background="#3C3C3C", fg="red", font=("Andalus", 24))
            book_name_entry.place(x=765, y=410, width=270, height=33)

        def delete_by_bar_code():

            def submit():
                global bg31
                global bg32
                global bg33
                global return_to_main_menu_btn
                global back_btn

                def deleted_succesfully():
                    global bg25
                    global return_to_main_menu_btn

                    bg25 = PhotoImage(file=resource_path("deletedsuccesfully.png"))
                    bg25_label = Label(root, image=bg25)
                    bg25_label.place(x=0, y=0)

                    return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                    return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                    real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                          width=250, height=200, activebackground="black", border=0,
                                                          command=main_menu)
                    real_return_to_main_menu_btn.place(x=645, y=575)

                    for i in range(len(all_rows)):
                        if all_rows[i]["bar_code"] == bar_code_to_be_removed:
                            del all_rows[i]
                            break

                    df = DataFrame.from_dict(all_rows)
                    df.to_excel("DataBase\\LibraryDataBase.xlsx")

                bar_code_to_be_removed = bar_codee_entry.get()

                if bar_code_to_be_removed == "":
                    bg33 = PhotoImage(file=resource_path("cannotleavethebarcodeinputblank.png"))
                    bg33_label = Label(root, image=bg33)
                    bg33_label.place(x=0, y=0)

                    return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                    return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                    real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                          width=250, height=200, activebackground="black", border=0,
                                                          command=main_menu)
                    real_return_to_main_menu_btn.place(x=850, y=585)

                    back_btn = PhotoImage(file=resource_path("back_button.png"))
                    back_btn_label = Label(image=back_btn)

                    real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                           activebackground="black", border=0, command=delete_by_bar_code)
                    real_back_btn.place(x=400, y=585)

                else:

                    temp_list = []

                    for i in all_rows:
                        temp_list.append(str(i["bar_code"]))

                    if bar_code_to_be_removed in temp_list:

                        bg31 = PhotoImage(
                            file=resource_path("youareabottodeleteabookandallofitsdatafromyourlibraryareyousure.png"))
                        bg31_label = Label(root, image=bg31)
                        bg31_label.place(x=0, y=0)

                        real_yeap_btn = Button(root, text="Yeap :)", font=("Andalus", 30), border=0,
                                               background="#A50000", activebackground="#A50000",
                                               command=deleted_succesfully)
                        real_yeap_btn.place(x=952, y=637, width=155, height=90)

                        real_nope_btn = Button(root, text="Nope :(", font=("Andalus", 30), border=0,
                                               background="#02CBE7", activebackground="#02CBE7",
                                               command=delete_by_bar_code)
                        real_nope_btn.place(x=410, y=637, width=155, height=90)

                    else:

                        bg32 = PhotoImage(file=resource_path("sorryitseemsthatthisbookdoesntexistsinyourlibrary.png"))
                        bg32_label = Label(root, image=bg32)
                        bg32_label.place(x=0, y=0)

                        return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                        return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                        real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                              bg="black", width=250, height=200,
                                                              activebackground="black", border=0, command=main_menu)
                        real_return_to_main_menu_btn.place(x=850, y=585)

                        back_btn = PhotoImage(file=resource_path("back_button.png"))
                        back_btn_label = Label(image=back_btn)

                        real_return_to_main_menu_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                              height=200, activebackground="black", border=0,
                                                              command=delete_by_bar_code)
                        real_return_to_main_menu_btn.place(x=400, y=585)

            global bg30
            global submit_btn
            global back_btn

            bg30 = PhotoImage(file=resource_path("barcodedelete_screen.png"))
            bg30_label = Label(root, image=bg30)
            bg30_label.place(x=0, y=0)

            submit_btn = PhotoImage(file=resource_path("submit_button.png"))
            submit_btn_label = Label(image=submit_btn)

            real_submit_btn = Button(root, text="Start", image=submit_btn, bg="#272727", width=250, height=200,
                                     activebackground="#272727", border=0, command=submit)
            real_submit_btn.place(x=845, y=585)

            back_btn = PhotoImage(file=resource_path("back_button.png"))
            back_btn_label = Label(image=back_btn)

            real_back_btn = Button(root, text="Start", image=back_btn, bg="#272727", width=250, height=200,
                                   activebackground="#272727", border=0, command=delete_book)
            real_back_btn.place(x=400, y=585)

            bar_codee_entry = Entry(root, border=0, background="#3C3C3C", fg="red", font=("Andalus", 24))
            bar_codee_entry.place(x=890, y=410, width=95, height=33)

        global bg2
        global back_btn
        global delete_by_name_btn
        global delete_by_bar_code_btn

        bg2 = PhotoImage(file=resource_path("deletebookmethod.png"))
        bg2_label = Label(root, image=bg2)
        bg2_label.place(x=0, y=0)

        back_btn = PhotoImage(file=resource_path("back_button.png"))
        back_btn_label = Label(image=back_btn)

        real_back_btn = Button(root, text="Start", image=back_btn, bg="#893434", width=250, height=200,
                               activebackground="#893434", border=0, command=main_menu)
        real_back_btn.place(x=660, y=575)

        delete_by_name_btn = PhotoImage(file=resource_path("deletebyname_button.png"))
        delete_by_name_btn_label = Label(image=delete_by_name_btn)

        real_delete_by_name_btn = Button(root, text="Start", image=delete_by_name_btn, bg="black", width=250,
                                         height=220, activebackground="black", border=0, command=delete_by_name)
        real_delete_by_name_btn.place(x=1150, y=375)

        delete_by_bar_code_btn = PhotoImage(file=resource_path("deletebybarcode_button.png"))
        delete_by_bar_code_btn_label = Label(image=delete_by_bar_code_btn)

        real_submit_btn = Button(root, text="Start", image=delete_by_bar_code_btn, bg="#893434", width=250, height=220,
                                 activebackground="#893434", border=0, command=delete_by_bar_code)
        real_submit_btn.place(x=150, y=375)

    def barcode_generator():

        def copy_to_clipboard():
            pyperclip.copy(code)
            spam = pyperclip.paste()

        global bg1
        global bar_cde_show_field
        global return_to_main_menu_btn
        global copy_to_clipboard_btn

        bg1 = PhotoImage(file=resource_path("barcodegenerator.png"))
        bg1_label = Label(root, image=bg1)
        bg1_label.place(x=0, y=0)

        return_to_main_menu_btn = PhotoImage(file=resource_path("greenreturntomainmenu_button.png"))
        return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

        real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="#6B3A00",
                                              width=250, height=200, activebackground="#6B3A00", border=0,
                                              command=main_menu)
        real_return_to_main_menu_btn.place(x=920, y=288)

        copy_to_clipboard_btn = PhotoImage(file=resource_path("copytoclipboard_button.png"))
        copy_to_clipboard_btn_label = Label(image=copy_to_clipboard_btn)

        real_copy_to_clipboard_btn = Button(root, text="Start", image=copy_to_clipboard_btn, bg="#6B3A00", width=250,
                                            height=200, activebackground="#6B3A00", border=0, command=copy_to_clipboard)
        real_copy_to_clipboard_btn.place(x=380, y=288)

        code = random.randint(10000, 99999)

        label_to_entry = Entry(root, font=("Andalus", 30), bd=0)
        label_to_entry.insert(0, code)
        label_to_entry.config(state="readonly")

        label_to_entry.place(x=725, y=360, width=115)

    def edit_book():
        global bg37
        global back_btn
        global edit_by_name_btn
        global edit_by_bar_code_btn

        def edit_by_book_name():
            global bg38
            global submit_btn
            global back_btn

            def submit():
                global bg40
                global bg41
                global back_btn
                global return_to_main_menu_btn

                book = book_name_entry.get()

                if book == "":
                    bg41 = PhotoImage(file=resource_path("cannotleavethebooknameinputblank.png"))
                    bg41_label = Label(root, image=bg41)
                    bg41_label.place(x=0, y=0)

                    return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                    return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                    real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                          width=250, height=200, activebackground="black", border=0,
                                                          command=main_menu)
                    real_return_to_main_menu_btn.place(x=850, y=585)

                    back_btn = PhotoImage(file=resource_path("back_button.png"))
                    back_btn_label = Label(image=back_btn)

                    real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                           activebackground="black", border=0, command=edit_by_book_name)
                    real_back_btn.place(x=400, y=585)

                else:
                    tempt_list = []
                    for _ in all_rows:
                        tempt_list.append(str(_["book_name"]))

                    if str(book) in tempt_list:
                        global bg42
                        global submit2_btn

                        def submit2():
                            global bg43
                            global return_to_main_menu_btn

                            new_name = books_name_entry.get()
                            new_author = authors_entry.get()
                            new_release_date = releases_date_entry.get()
                            new_bar_code = bars_code_entry.get()
                            new_how_many_sold = how_manys_sold_entry.get()
                            new_how_many_left = how_manys_left_entry.get()

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
                                global return_to_main_menu_btn
                                global back_btn

                                global bg4
                                bg4 = PhotoImage(file=resource_path("cannotassignanemptynewbookname.png"))
                                bg4_label = Label(root, image=bg4)
                                bg4_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif new_author == "":

                                global bg5
                                bg5 = PhotoImage(file=resource_path("cannotassignanemptynewauthorname.png"))
                                bg5_label = Label(root, image=bg5)
                                bg5_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif new_release_date == "":

                                global bg6
                                bg6 = PhotoImage(file=resource_path("cannotassignanemptynewreleasedate.png"))
                                bg6_label = Label(root, image=bg6)
                                bg6_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif new_bar_code == "":

                                global bg7
                                bg7 = PhotoImage(file=resource_path("cannotassignanemptynewbarcode.png"))
                                bg7_label = Label(root, image=bg7)
                                bg7_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif new_how_many_sold == "":

                                global bg8
                                bg8 = PhotoImage(file=resource_path("cannotassignanemptynewhowmanysold.png"))
                                bg8_label = Label(root, image=bg8)
                                bg8_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif new_how_many_left == "":

                                global bg9
                                bg9 = PhotoImage(file=resource_path("cannotassignanemptynewrhowmanyleft.png"))
                                bg9_label = Label(root, image=bg9)
                                bg9_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif str(new_bar_code) in final_all_bar_codes:
                                global bg13
                                bg13 = PhotoImage(file=resource_path("sorryitseemsthatthisbookalreadyexistsindatabase.png"))
                                bg13_label = Label(root, image=bg13)
                                bg13_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif not new_release_date.isdigit():
                                global bg16
                                bg16 = PhotoImage(file=resource_path("yourreleasedatecontainsacharactorwhichisnotnumeric.png"))
                                bg16_label = Label(root, image=bg16)
                                bg16_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif not new_bar_code.isdigit():
                                global bg17
                                bg17 = PhotoImage(file=resource_path("yourbarcodecontainsacharactorwhichisnotnumeric.png"))
                                bg17_label = Label(root, image=bg17)
                                bg17_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif (len(new_release_date)) != 4:
                                global bg11
                                bg11 = PhotoImage(file=resource_path("thereleasedatemusthaveexactly4numbers.png"))
                                bg11_label = Label(root, image=bg11)
                                bg11_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif len(new_bar_code) != 5:
                                global bg12
                                bg12 = PhotoImage(file=resource_path("thebarcodemusthaveexactly5numbers.png"))
                                bg12_label = Label(root, image=bg12)
                                bg12_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            else:
                                for _ in all_rows:
                                    if _["book_name"] == book:
                                        bg43 = PhotoImage(file=resource_path("editedsuccesfully_screen.png"))
                                        bg43label = Label(root, image=bg43)
                                        bg43label.place(x=0, y=0)

                                        return_to_main_menu_btn = PhotoImage(
                                            file=resource_path("greenreturntomainmenu_button.png"))
                                        return_to_main_menu_btn_label = Label(image=back_btn)

                                        real_return_to_main_menu_btn = Button(root, text="Start",
                                                                              image=return_to_main_menu_btn, bg="black",
                                                                              width=250, height=200,
                                                                              activebackground="black", border=0,
                                                                              command=main_menu)
                                        real_return_to_main_menu_btn.place(x=635, y=575)

                                        all_rows.remove(_)
                                        all_rows.append(temp_dict)

                                df = DataFrame.from_dict(all_rows)
                                df.to_excel("DataBase\\LibraryDataBase.xlsx")

                        bg42 = PhotoImage(file=resource_path("newbookdataget_srcreen.png"))
                        bg42label = Label(root, image=bg42)
                        bg42label.place(x=0, y=0)

                        books_name_entry = Entry(root, border=0, background="#171717", fg="red", font=("Andalus", 24))
                        books_name_entry.place(x=660, y=225, width=555, height=30)

                        authors_entry = Entry(root, border=0, background="#171717", fg="red", font=("Andalus", 24))
                        authors_entry.place(x=590, y=280, width=615, height=30)

                        releases_date_entry = Entry(root, border=0, background="#171717", fg="red",
                                                    font=("Andalus", 24))
                        releases_date_entry.place(x=655, y=335, width=550, height=30)

                        bars_code_entry = Entry(root, border=0, background="#171717", fg="red", font=("Andalus", 24))
                        bars_code_entry.place(x=635, y=390, width=575, height=30)

                        how_manys_sold_entry = Entry(root, border=0, background="#171717", fg="red",
                                                     font=("Andalus", 24))
                        how_manys_sold_entry.place(x=730, y=445, width=485, height=30)

                        how_manys_left_entry = Entry(root, border=0, background="#171717", fg="red",
                                                     font=("Andalus", 24))
                        how_manys_left_entry.place(x=730, y=500, width=490, height=30)

                        submit2_btn = PhotoImage(file=resource_path("submit_button.png"))
                        submit2_btn_label = Label(image=submit2_btn)

                        real_submit2_btn = Button(root, text="Start", image=submit2_btn, bg="#252525", width=250,
                                                  height=200, activebackground="#252525", border=0, command=submit2)
                        real_submit2_btn.place(x=800, y=575)

                        back_btn = PhotoImage(file=resource_path("back_button.png"))
                        back_btn_label = Label(image=back_btn)

                        real_back_btn = Button(root, text="Start", image=back_btn, bg="#252525", width=250, height=200,
                                               activebackground="#252525", border=0, command=edit_by_book_name)
                        real_back_btn.place(x=465, y=575)


                    else:
                        global bg34

                        bg34 = PhotoImage(file=resource_path("sorryitseemsthatthisbookdoesntexistsinyourlibrary.png"))
                        bg34_label = Label(root, image=bg34)
                        bg34_label.place(x=0, y=0)

                        return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                        return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                        real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                              bg="black", width=250, height=200,
                                                              activebackground="black", border=0, command=main_menu)
                        real_return_to_main_menu_btn.place(x=635, y=585)

            bg38 = PhotoImage(file=resource_path("booknameedit_screen.png"))
            bg38_label = Label(root, image=bg38)
            bg38_label.place(x=0, y=0)

            submit_btn = PhotoImage(file=resource_path("submit_button.png"))
            submit_btn_label = Label(image=submit_btn)

            real_submit_btn = Button(root, text="Start", image=submit_btn, bg="#272727", width=250, height=200,
                                     activebackground="#272727", border=0, command=submit)
            real_submit_btn.place(x=845, y=585)

            back_btn = PhotoImage(file=resource_path("back_button.png"))
            back_btn_label = Label(image=back_btn)

            real_back_btn = Button(root, text="Start", image=back_btn, bg="#272727", width=250, height=200,
                                   activebackground="#272727", border=0, command=edit_book)
            real_back_btn.place(x=400, y=585)

            book_name_entry = Entry(root, border=0, background="#3C3C3C", fg="red", font=("Andalus", 24))
            book_name_entry.place(x=765, y=410, width=270, height=33)

        def edit_by_bar_code():

            global bg38
            global submit_btn
            global back_btn

            def submit():
                global bg41
                global back_btn
                global return_to_main_menu_btn

                bar_code = bar_code_entry.get()

                if bar_code == "":
                    bg41 = PhotoImage(file=resource_path("cannotleavethebooknameinputblank.png"))
                    bg41_label = Label(root, image=bg41)
                    bg41_label.place(x=0, y=0)

                    return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                    return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                    real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="black",
                                                          width=250, height=200, activebackground="black", border=0,
                                                          command=main_menu)
                    real_return_to_main_menu_btn.place(x=850, y=585)

                    back_btn = PhotoImage(file=resource_path("back_button.png"))
                    back_btn_label = Label(image=back_btn)

                    real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                                           activebackground="black", border=0, command=edit_by_bar_code)
                    real_back_btn.place(x=400, y=585)

                else:
                    tempt_list = []
                    for _ in all_rows:
                        tempt_list.append(str(_["bar_code"]))

                    if str(bar_code) in tempt_list:
                        global bg42
                        global submit2_btn

                        def submit2():
                            global bg43
                            global return_to_main_menu_btn

                            new_name = books_name_entry.get()
                            new_author = authors_entry.get()
                            new_release_date = releases_date_entry.get()
                            new_bar_code = bars_code_entry.get()
                            new_how_many_sold = how_manys_sold_entry.get()
                            new_how_many_left = how_manys_left_entry.get()

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
                                global return_to_main_menu_btn
                                global back_btn

                                global bg4
                                bg4 = PhotoImage(file=resource_path("cannotassignanemptynewbookname.png"))
                                bg4_label = Label(root, image=bg4)
                                bg4_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif new_author == "":

                                global bg5
                                bg5 = PhotoImage(file=resource_path("cannotassignanemptynewauthorname.png"))
                                bg5_label = Label(root, image=bg5)
                                bg5_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif new_release_date == "":

                                global bg6
                                bg6 = PhotoImage(file=resource_path("cannotassignanemptynewreleasedate.png"))
                                bg6_label = Label(root, image=bg6)
                                bg6_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif new_bar_code == "":

                                global bg7
                                bg7 = PhotoImage(file=resource_path("cannotassignanemptynewbarcode.png"))
                                bg7_label = Label(root, image=bg7)
                                bg7_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif new_how_many_sold == "":

                                global bg8
                                bg8 = PhotoImage(file=resource_path("cannotassignanemptynewhowmanysold.png"))
                                bg8_label = Label(root, image=bg8)
                                bg8_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif new_how_many_left == "":

                                global bg9
                                bg9 = PhotoImage(file=resource_path("cannotassignanemptynewrhowmanyleft.png"))
                                bg9_label = Label(root, image=bg9)
                                bg9_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif str(new_bar_code) in final_all_bar_codes:
                                global bg13
                                bg13 = PhotoImage(file=resource_path("sorryitseemsthatthisbookalreadyexistsindatabase.png"))
                                bg13_label = Label(root, image=bg13)
                                bg13_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif not new_release_date.isdigit():
                                global bg16
                                bg16 = PhotoImage(file=resource_path("yourreleasedatecontainsacharactorwhichisnotnumeric.png"))
                                bg16_label = Label(root, image=bg16)
                                bg16_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif not new_bar_code.isdigit():
                                global bg17
                                bg17 = PhotoImage(file=resource_path("yourbarcodecontainsacharactorwhichisnotnumeric.png"))
                                bg17_label = Label(root, image=bg17)
                                bg17_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif (len(new_release_date)) != 4:
                                global bg11
                                bg11 = PhotoImage(file=resource_path("thereleasedatemusthaveexactly4numbers.png"))
                                bg11_label = Label(root, image=bg11)
                                bg11_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            elif len(new_bar_code) != 5:
                                global bg12
                                bg12 = PhotoImage(file=resource_path("thebarcodemusthaveexactly5numbers.png"))
                                bg12_label = Label(root, image=bg12)
                                bg12_label.place(x=0, y=0)

                                return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                                return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                                real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                                      bg="black", width=250, height=200,
                                                                      activebackground="black", border=0,
                                                                      command=main_menu)
                                real_return_to_main_menu_btn.place(x=800, y=575)

                                back_btn = PhotoImage(file=resource_path("back_button.png"))
                                back_btn_label = Label(image=back_btn)

                                real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250,
                                                       height=200, activebackground="black", border=0, command=add_book)
                                real_back_btn.place(x=465, y=575)


                            else:
                                global bg60
                                for _ in all_rows:
                                    if _["bar_code"] == bar_code:
                                        bg60 = PhotoImage(file=resource_path("editedsuccesfully_screen.png"))
                                        bg60label = Label(root, image=bg60)
                                        bg60label.place(x=0, y=0)

                                        return_to_main_menu_btn = PhotoImage(
                                            file=resource_path("greenreturntomainmenu_button.png"))
                                        return_to_main_menu_btn_label = Label(image=back_btn)

                                        real_return_to_main_menu_btn = Button(root, text="Start",
                                                                              image=return_to_main_menu_btn, bg="black",
                                                                              width=250, height=200,
                                                                              activebackground="black", border=0,
                                                                              command=main_menu)
                                        real_return_to_main_menu_btn.place(x=635, y=575)

                                        all_rows.remove(_)
                                        all_rows.append(temp_dict)

                                        df = DataFrame.from_dict(all_rows)
                                        df.to_excel("DataBase\\LibraryDataBase.xlsx")

                        bg42 = PhotoImage(file=resource_path("newbookdataget_srcreen.png"))
                        bg42label = Label(root, image=bg42)
                        bg42label.place(x=0, y=0)

                        books_name_entry = Entry(root, border=0, background="#171717", fg="red", font=("Andalus", 24))
                        books_name_entry.place(x=660, y=225, width=555, height=30)

                        authors_entry = Entry(root, border=0, background="#171717", fg="red", font=("Andalus", 24))
                        authors_entry.place(x=590, y=280, width=615, height=30)

                        releases_date_entry = Entry(root, border=0, background="#171717", fg="red",
                                                    font=("Andalus", 24))
                        releases_date_entry.place(x=655, y=335, width=550, height=30)

                        bars_code_entry = Entry(root, border=0, background="#171717", fg="red", font=("Andalus", 24))
                        bars_code_entry.place(x=635, y=390, width=575, height=30)

                        how_manys_sold_entry = Entry(root, border=0, background="#171717", fg="red",
                                                     font=("Andalus", 24))
                        how_manys_sold_entry.place(x=730, y=445, width=485, height=30)

                        how_manys_left_entry = Entry(root, border=0, background="#171717", fg="red",
                                                     font=("Andalus", 24))
                        how_manys_left_entry.place(x=730, y=500, width=490, height=30)

                        submit2_btn = PhotoImage(file=resource_path("submit_button.png"))
                        submit2_btn_label = Label(image=submit2_btn)

                        real_submit2_btn = Button(root, text="Start", image=submit2_btn, bg="#252525", width=250,
                                                  height=200, activebackground="#252525", border=0, command=submit2)
                        real_submit2_btn.place(x=800, y=575)

                        back_btn = PhotoImage(file=resource_path("back_button.png"))
                        back_btn_label = Label(image=back_btn)

                        real_back_btn = Button(root, text="Start", image=back_btn, bg="#252525", width=250, height=200,
                                               activebackground="#252525", border=0, command=edit_by_book_name)
                        real_back_btn.place(x=465, y=575)


                    else:
                        global bg34

                        bg34 = PhotoImage(file=resource_path("sorryitseemsthatthisbookdoesntexistsinyourlibrary.png"))
                        bg34_label = Label(root, image=bg34)
                        bg34_label.place(x=0, y=0)

                        return_to_main_menu_btn = PhotoImage(file=resource_path("returntomainmenu_button.png"))
                        return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

                        real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn,
                                                              bg="black", width=250, height=200,
                                                              activebackground="black", border=0, command=main_menu)
                        real_return_to_main_menu_btn.place(x=635, y=585)

            bg38 = PhotoImage(file=resource_path("barcodedit_screen.png"))
            bg38_label = Label(root, image=bg38)
            bg38_label.place(x=0, y=0)

            submit_btn = PhotoImage(file=resource_path("submit_button.png"))
            submit_btn_label = Label(image=submit_btn)

            real_submit_btn = Button(root, text="Start", image=submit_btn, bg="#272727", width=250, height=200,
                                     activebackground="#272727", border=0, command=submit)
            real_submit_btn.place(x=845, y=585)

            back_btn = PhotoImage(file=resource_path("back_button.png"))
            back_btn_label = Label(image=back_btn)

            real_back_btn = Button(root, text="Start", image=back_btn, bg="#272727", width=250, height=200,
                                   activebackground="#272727", border=0, command=edit_book)
            real_back_btn.place(x=400, y=585)

            bar_code_entry = Entry(root, border=0, background="#3C3C3C", fg="red", font=("Andalus", 24))
            bar_code_entry.place(x=890, y=410, width=95, height=33)

        bg37 = PhotoImage(file=resource_path("editbookmethod.png"))
        bg37_label = Label(root, image=bg37)
        bg37_label.place(x=0, y=0)

        back_btn = PhotoImage(file=resource_path("back_button.png"))
        back_btn_label = Label(image=back_btn)

        real_back_btn = Button(root, text="Start", image=back_btn, bg="black", width=250, height=200,
                               activebackground="black", border=0, command=main_menu)
        real_back_btn.place(x=660, y=575)

        edit_by_name_btn = PhotoImage(file=resource_path("editbybookname_button.png"))
        edit_by_name_btn_label = Label(image=edit_by_name_btn)

        real_edit_by_name_btn = Button(root, text="Start", image=edit_by_name_btn, bg="#893434", width=250, height=220,
                                       activebackground="#893434", border=0, command=edit_by_book_name)
        real_edit_by_name_btn.place(x=1150, y=375)

        edit_by_bar_code_btn = PhotoImage(file=resource_path("editbybarcode_button.png"))
        edit_by_bar_code_btn_label = Label(image=edit_by_bar_code_btn)

        real_edit_by_bar_code_btn = Button(root, text="Start", image=edit_by_bar_code_btn, bg="black", width=250,
                                           height=220, activebackground="black", border=0, command=edit_by_bar_code)
        real_edit_by_bar_code_btn.place(x=150, y=375)

    def all_books_and_barcodes():
        global all_books
        global books_name
        global bg67
        global save_as_txt_btn
        global save_as_txt_btn_bar_code
        global save_as_txt_btn_book
        global return_to_main_menu_btn

        def save_as_txt_file_bar_code():
            file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[
                ("Text file", ".txt"),
                ("HTML file", ".html")
            ])
            file.write(str(all_bar_codes))
            file.close()

        def save_as_txt_file_book():
            file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[
                ("Text file", ".txt"),
                ("HTML file", ".html")
            ])
            file.write(str(all_books))
            file.close()

        all_books = []
        all_bar_codes = []

        for books_name in all_rows:
            all_books.append(books_name["book_name"])

        for bar_codes in all_rows:
            all_bar_codes.append(bar_codes["bar_code"])

        bg67 = PhotoImage(file=resource_path("allbooksandbarcodes_screen.png"))
        bg67_label = Label(root, image=bg67)
        bg67_label.place(x=0, y=0)

        bar_codes_frame = Frame(root, border=0, background="#424141", borderwidth=0)
        bar_codes_frame.place(x=0, y=180, width=195, height=630)

        bar_code_scroll_bar = Scrollbar(bar_codes_frame, orient="vertical")
        bar_code_scroll_bar.pack(fill="y")

        bar_code_text = Listbox(bar_codes_frame, yscrollcommand=bar_code_scroll_bar.set, font=("Andalus", 30),
                                foreground="red", background="#424141", borderwidth=0, highlightthickness=0)

        for i in all_bar_codes:
            bar_code_text.insert(END, f"{i}")

        bar_code_text.place(x=20, y=0)
        bar_code_scroll_bar.config(command=bar_code_text.yview)

        books_frame = Frame(root, border=0, background="#424141", borderwidth=0)
        books_frame.place(x=1137, y=180, width=490, height=630)

        books_scroll_bar = Scrollbar(books_frame, orient="vertical")
        books_scroll_bar.pack(fill="y", side="right")

        book_text = Listbox(books_frame, yscrollcommand=bar_code_scroll_bar.set, font=("Andalus", 30), foreground="red",
                            background="#424141", borderwidth=0, highlightthickness=0)

        for i in all_books:
            book_text.insert(END, f"{i}")

        book_text.place(x=20, y=0)
        books_scroll_bar.config(command=book_text.yview)

        save_as_txt_btn_bar_code = PhotoImage(file=resource_path("silversaveastxt_button.png"))
        save_as_txt_btn_bar_code_label = Label(image=save_as_txt_btn_bar_code)

        real_save_as_txt_btn_bar_code = Button(root, text="Start", image=save_as_txt_btn_bar_code, bg="#785637",
                                               width=280, height=220, activebackground="#785637", border=0,
                                               command=save_as_txt_file_bar_code)
        real_save_as_txt_btn_bar_code.place(x=315, y=325)

        save_as_txt_btn_book = PhotoImage(file=resource_path("purplesaveastxt_button.png"))
        save_as_txt_btn_book_label = Label(image=save_as_txt_btn_book)

        real_save_as_txt_btn_book = Button(root, text="Start", image=save_as_txt_btn_book, bg="#785637", width=280,
                                           height=220, activebackground="#785637", border=0,
                                           command=save_as_txt_file_book)
        real_save_as_txt_btn_book.place(x=825, y=325, width=250, height=195)

        return_to_main_menu_btn = PhotoImage(file=resource_path("greenreturntomainmenu_button.png"))
        return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

        real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="#000000",
                                              width=250, height=200, activebackground="#000000", border=0,
                                              command=main_menu)
        real_return_to_main_menu_btn.place(x=600, y=600)

    def latest_updates():
        global return_to_main_menu_btn
        global save_as_txt_btn
        global bg34

        def save_as_txt_file():
            file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[
                ("Text file", ".txt"),
                ("HTML file", ".html")
            ])
            file.write(saving_file)
            file.close()

        bg34 = PhotoImage(file=resource_path("latestupdate_screen.png"))
        bg34_label = Label(root, image=bg34)
        bg34_label.place(x=0, y=0)

        update_list_of_dictionaries = []
        update_list_of_dictionaries.append(all_rows[-1])

        for _ in update_list_of_dictionaries:
            book_name = _["book_name"]
            author = _["author"]
            release_date = _["release_date"]
            bar_code = _["bar_code"]
            how_many_sold = _["how_many_sold"]
            how_many_left = _["how_many_left"]

        saving_file = f"Book name : {book_name}\nAuthor : {author}\nRelease date : {release_date}\nBar-code : {bar_code}\nHow many sold : {how_many_sold}\nHow many left : {how_many_left}"

        book_name_label = Label(root, text=book_name, border=0, background="#252525", font=("Andalus", 35), fg="white")
        book_name_label.place(x=560, y=235)

        author_label = Label(root, text=author, border=0, background="#252525", font=("Andalus", 35), fg="white")
        author_label.place(x=480, y=295)

        release_date_label = Label(root, text=release_date, border=0, background="#252525", font=("Andalus", 35),
                                   fg="white")
        release_date_label.place(x=550, y=355)

        bar_code_label = Label(root, text=bar_code, border=0, background="#252525", font=("Andalus", 35), fg="white")
        bar_code_label.place(x=510, y=415)

        how_many_sold_label = Label(root, text=how_many_sold, border=0, background="#252525", font=("Andalus", 35),
                                    fg="white")
        how_many_sold_label.place(x=610, y=475)

        how_many_left_label = Label(root, text=how_many_left, border=0, background="#252525", font=("Andalus", 35),
                                    fg="white")
        how_many_left_label.place(x=610, y=535)

        return_to_main_menu_btn = PhotoImage(file=resource_path("greenreturntomainmenu_button.png"))
        return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

        real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="#252525",
                                              width=250, height=200, activebackground="#252525", border=0,
                                              command=main_menu)
        real_return_to_main_menu_btn.place(x=1080, y=260)

        save_as_txt_btn = PhotoImage(file=resource_path("saveastxt_button.png"))
        save_as_txt_btn_label = Label(image=save_as_txt_btn)

        real_save_as_txt_btn = Button(root, text="Start", image=save_as_txt_btn, bg="#252525", width=280, height=220,
                                      activebackground="#252525", border=0, command=save_as_txt_file)
        real_save_as_txt_btn.place(x=1075, y=480)

    def book_counter():

        global bg36
        global return_to_main_menu_btn
        global copy_to_clipboard_btn

        def copy_to_clipboard():
            pyperclip.copy(len(all_rows))
            spam = pyperclip.paste()

        bg36 = PhotoImage(file=resource_path("totalbookscount.png"))
        bg36_label = Label(root, image=bg36)
        bg36_label.place(x=0, y=0)

        how_many_left_label = Label(root, text=len(all_rows), border=0, background="#B8B8B8", font=("Andalus", 35),
                                    fg="#000000")
        how_many_left_label.place(x=785, y=390)

        return_to_main_menu_btn = PhotoImage(file=resource_path("greenreturntomainmenu_button.png"))
        return_to_main_menu_btn_label = Label(image=return_to_main_menu_btn)

        real_return_to_main_menu_btn = Button(root, text="Start", image=return_to_main_menu_btn, bg="#252525",
                                              width=250, height=200, activebackground="#252525", border=0,
                                              command=main_menu)
        real_return_to_main_menu_btn.place(x=950, y=320)

        copy_to_clipboard_btn = PhotoImage(file=resource_path("copytoclipboard_button.png"))
        copy_to_clipboard_btn_label = Label(image=copy_to_clipboard_btn)

        real_copy_to_clipboard_btn = Button(root, text="Start", image=copy_to_clipboard_btn, bg="#252525", width=250,
                                            height=200, activebackground="#252525", border=0, command=copy_to_clipboard)
        real_copy_to_clipboard_btn.place(x=395, y=320)

    def exit():
        root.destroy()

    """Back-End of buttons start here"""

    bg = PhotoImage(file=resource_path("bg.png"))
    bg_label = Label(root, image=bg)
    bg_label.place(x=-10, y=0)

    read_from_excel()
    update()

    search_btn = PhotoImage(file=resource_path("search_button.png"))
    search_label = Label(image=search_btn)

    add_btn = PhotoImage(file=resource_path("add_button.png"))
    add_label = Label(image=add_btn)

    delete_btn = PhotoImage(file=resource_path("delete_button.png"))
    delete_label = Label(image=delete_btn)

    edit_btn = PhotoImage(file=resource_path("edit_button.png"))
    edit_label = Label(image=edit_btn)

    real_search_btn = Button(root, text="Start", image=search_btn, bg="#252525", activebackground="#252525", border=0,
                             command=search_book)
    real_search_btn.place(x=10, y=110)

    real_add_btn = Button(root, text="Start", image=add_btn, bg="#252525", activebackground="#252525", border=0,
                          command=add_book)
    real_add_btn.place(x=10, y=210)

    real_delete_btn = Button(root, text="Start", image=delete_btn, bg="#252525", activebackground="#252525", border=0,
                             command=delete_book)
    real_delete_btn.place(x=10, y=310)

    real_edit_btn = Button(root, text="Start", image=edit_btn, bg="#252525", activebackground="#252525", border=0,
                           command=edit_book)
    real_edit_btn.place(x=10, y=410)

    allbooksandbarcodes_btn = PhotoImage(file=resource_path("allbooksandbarcodes_button.png"))
    allbooksandbarcodes_label = Label(image=allbooksandbarcodes_btn)

    barcodegenerator_btn = PhotoImage(file=resource_path("barcodegenerator_button.png"))
    barcodegenerator_label = Label(image=barcodegenerator_btn)

    latestupdate_btn = PhotoImage(file=resource_path("latestupdate_button.png"))
    latestupdate_label = Label(image=latestupdate_btn)

    bookcounter_btn = PhotoImage(file=resource_path("bookcounter_button.png"))
    bookcounterh_label = Label(image=bookcounter_btn)

    real_allbooksandbarcodes_btn = Button(root, text="Start", image=allbooksandbarcodes_btn, bg="#252525",
                                          activebackground="#252525", border=0, command=all_books_and_barcodes)
    real_allbooksandbarcodes_btn.place(x=360, y=110)

    real_barcodegenerator_btn = Button(root, text="Start", image=barcodegenerator_btn, bg="#252525",
                                       activebackground="#252525", border=0, command=barcode_generator)
    real_barcodegenerator_btn.place(x=360, y=210)

    real_latestupdate_btn = Button(root, text="Start", image=latestupdate_btn, bg="#252525", activebackground="#252525",
                                   border=0, command=latest_updates)
    real_latestupdate_btn.place(x=360, y=310)

    real_bookcounter_btn = Button(root, text="Start", image=bookcounter_btn, bg="#252525", activebackground="#252525",
                                  border=0, command=book_counter)
    real_bookcounter_btn.place(x=360, y=410)

    exit_btn = PhotoImage(file=resource_path("exit_button.png"))
    exit_label = Label(image=exit_btn)

    real_exit_btn = Button(root, text="Start", image=exit_btn, bg="#252525", width=80, height=80,
                           activebackground="#252525", border=0, command=exit)
    real_exit_btn.place(x=195, y=450)

    root.mainloop()


root = Tk()
root.title('PyLibrary')
root.maxsize(width=475, height=550)
root.minsize(width=475, height=550)
root.iconbitmap(resource_path("Logo.ico"))

main_menu()

root.mainloop()
