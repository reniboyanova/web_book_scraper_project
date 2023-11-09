import tkinter as tk
from scraper import Scraper
from cli import Cli

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Book Scraper")
        self.root.geometry("300x640")

        self.wanted_tick = tk.IntVar()
        self.title_tick = tk.IntVar()
        self.descr_tick = tk.IntVar()
        self.genres_tick = tk.IntVar()
        self.price_tick = tk.IntVar()
        self.rating_tick = tk.IntVar()
        self.availability_tick = tk.IntVar()
        self.sort_tick = tk.IntVar()
        self.export_to_gsheet_tick = tk.IntVar()
        self.new_sheet_tick = tk.IntVar()

        self.wanted_entry_text = tk.StringVar()
        self.wanted_entry_text.set("titles.json")
        self.title_entry_text = tk.StringVar()
        self.title_entry_text.set("Velvet")
        self.descr_entry_text = tk.StringVar()
        self.descr_entry_text.set("the")
        self.genres_entry_text = tk.StringVar()
        self.genres_entry_text.set("History")
        self.price_entry_text = tk.StringVar()
        self.price_entry_text.set(">10")
        self.rating_entry_text = tk.StringVar()
        self.rating_entry_text.set(">1")
        self.availability_entry_text = tk.StringVar()
        self.availability_entry_text.set(">3")
        self.sort_entry_text = tk.StringVar()
        self.sort_entry_text.set("rating ascending")
        self.num_of_books_entry_text = tk.StringVar()
        self.num_of_books_entry_text.set("5")
        self.export_to_gsheet_entry_text = tk.StringVar()
        self.export_to_gsheet_entry_text.set("ScrapeSheet")

        self.initialize_labels()
        self.initialize_checkboxes()
        self.initialize_entries()
        self.pack_visual_elements()
        self.add_button()
        self.filter_dict = {}
        self.scraper = None
        self.gsheet_info = {"export":False, "new_sheet":False, "sheetname":""}

    def checkbox_behaviour(self, checkbox, entry, tick):
        if self.wanted_tick.get() == 1:
            entry.configure(state="disabled")
            checkbox.configure(state="disabled")
        else:
            checkbox.configure(state="normal")
            if tick.get() == 1:
                entry.configure(state="normal")
            else:
                entry.configure(state="disabled")

    def update_entries(self):
        self.title_check_box()
        self.descr_check_box()
        self.genres_check_box()
        self.price_check_box()
        self.rating_check_box()
        self.availability_check_box()
        self.sort_check_box()

    def wanted_check_box(self):
        if self.wanted_tick.get() == 1:
            self.wanted_entry.configure(state="normal")
            self.num_of_books_entry.configure(state="disabled")
        else:
            self.wanted_entry.configure(state="disabled")
            self.num_of_books_entry.configure(state="normal")
        self.update_entries()

    def title_check_box(self):
        self.checkbox_behaviour(self.title_check, self.title_entry, self.title_tick)

    def descr_check_box(self):
        self.checkbox_behaviour(self.descr_check, self.descr_entry, self.descr_tick)

    def genres_check_box(self):
        self.checkbox_behaviour(self.genres_check, self.genres_entry, self.genres_tick)

    def price_check_box(self):
        self.checkbox_behaviour(self.price_check, self.price_entry, self.price_tick)

    def rating_check_box(self):
        self.checkbox_behaviour(self.rating_check, self.rating_entry, self.rating_tick)

    def availability_check_box(self):
        self.checkbox_behaviour(self.availability_check, self.availability_entry, self.availability_tick)

    def sort_check_box(self):
        self.checkbox_behaviour(self.sort_check, self.sort_entry, self.sort_tick)

    def export_to_gsheet_check_box(self):
        if self.export_to_gsheet_tick.get() == 1:
            self.new_sheet_check.configure(state="normal")
            self.export_to_gsheet_entry.configure(state="normal")
        else:
            self.new_sheet_check.configure(state="disabled")
            self.export_to_gsheet_entry.configure(state="disabled")

    def new_sheet_check_box(self):
        if self.new_sheet_tick.get() == 1:
            self.gsheet_info["new_sheet"] = True
        else:
            self.gsheet_info["new_sheet"] = False

    def initialize_labels(self):
        self.label = tk.Label(self.root, text="SEARCH FILTERS:", font=("Times New Roman", 12))
        self.label_num_of_books = tk.Label(self.root, pady=5, text="Number of books(max 1000):", font=("Times New Roman", 12))
        self.label_creation_msg = tk.Label(self.root, font=("Times New Roman", 9))

    def initialize_checkboxes(self):
        self.wanted_check = tk.Checkbutton(self.root, text="Filter by List of Wanted Titles:",
                                           font=("Times New Roman", 12),
                                           variable=self.wanted_tick, onvalue=1, offvalue=0,
                                           command=self.wanted_check_box)
        self.title_check = tk.Checkbutton(self.root, text="Filter by Title", font=("Times New Roman", 12),
                                          variable=self.title_tick, onvalue=1, offvalue=0,
                                          command=self.title_check_box)
        self.descr_check = tk.Checkbutton(self.root, text="Filter by Description Keywords",
                                          font=("Times New Roman", 12),
                                          variable=self.descr_tick, onvalue=1, offvalue=0, command=self.descr_check_box)
        self.genres_check = tk.Checkbutton(self.root, text="Filter by Genres",
                                           font=("Times New Roman", 12),
                                           variable=self.genres_tick, onvalue=1, offvalue=0,
                                           command=self.genres_check_box)
        self.price_check = tk.Checkbutton(self.root, text="Filter by Price:",
                                          font=("Times New Roman", 12),
                                          variable=self.price_tick, onvalue=1, offvalue=0,
                                          command=self.price_check_box)
        self.rating_check = tk.Checkbutton(self.root, text="Filter by Rating:",
                                           font=("Times New Roman", 12),
                                           variable=self.rating_tick, onvalue=1, offvalue=0,
                                           command=self.rating_check_box)
        self.availability_check = tk.Checkbutton(self.root, text="Filter by Availability:",
                                                 font=("Times New Roman", 12),
                                                 variable=self.availability_tick, onvalue=1, offvalue=0,
                                                 command=self.availability_check_box)
        self.sort_check = tk.Checkbutton(self.root, text="Sort:",
                                                 font=("Times New Roman", 12),
                                                 variable=self.sort_tick, onvalue=1, offvalue=0,
                                                 command=self.sort_check_box)
        self.export_to_gsheet_check = tk.Checkbutton(self.root, text="Export to GSheet?(enter sheet name):",
                                                 font=("Times New Roman", 12),
                                                 variable=self.export_to_gsheet_tick, onvalue=1, offvalue=0,
                                                 command=self.export_to_gsheet_check_box)
        self.new_sheet_check = tk.Checkbutton(self.root, text="New Sheet",
                                                     font=("Times New Roman", 12),
                                                     variable=self.new_sheet_tick, onvalue=1, offvalue=0,
                                                     command=self.new_sheet_check_box, state="disabled")

    def initialize_entries(self):
        self.wanted_entry = tk.Entry(self.root, font=("Times New Roman", 12), state="disabled",
                                     textvariable=self.wanted_entry_text)
        self.title_entry = tk.Entry(self.root, width=2, font=("Times New Roman", 12), state="disabled",
                                    textvariable=self.title_entry_text)
        self.descr_entry = tk.Entry(self.root, width=2, font=("Times New Roman", 12), state="disabled",
                                    textvariable=self.descr_entry_text)
        self.genres_entry = tk.Entry(self.root, width=2, font=("Times New Roman", 12), state="disabled",
                                     textvariable=self.genres_entry_text)
        self.price_entry = tk.Entry(self.root, width=2, font=("Times New Roman", 12), state="disabled",
                                    textvariable=self.price_entry_text)
        self.rating_entry = tk.Entry(self.root, width=2, font=("Times New Roman", 12), state="disabled",
                                     textvariable=self.rating_entry_text)
        self.availability_entry = tk.Entry(self.root, width=2, font=("Times New Roman", 12), state="disabled",
                                           textvariable=self.availability_entry_text)
        self.sort_entry = tk.Entry(self.root, width=2, font=("Times New Roman", 12), state="disabled",
                                           textvariable=self.sort_entry_text)
        self.num_of_books_entry = tk.Entry(self.root, width=3, font=("Times New Roman", 12), state="normal",
                                           textvariable=self.num_of_books_entry_text)
        self.export_to_gsheet_entry = tk.Entry(self.root, width=3, font=("Times New Roman", 12), state="disabled",
                                           textvariable=self.export_to_gsheet_entry_text)
        self.generated_pass_box = tk.Entry(self.root, font=("Times New Roman", 12))

    def pack_visual_elements(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.rowconfigure(0, weight=1, minsize=10)
        self.root.rowconfigure(23, weight=1, minsize=10)

        self.label.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        self.wanted_check.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.wanted_entry.grid(row=3, column=1, sticky=tk.NSEW)

        self.title_check.grid(row=4, column=1, sticky="w")
        # self.label_title.grid(row=5, column=1, padx=8, sticky="w")
        self.title_entry.grid(row=5, column=1, sticky=tk.NSEW)

        self.descr_check.grid(row=6, column=1, sticky="w")
        # self.label_descr.grid(row=7, column=1, padx=8, sticky="w")
        self.descr_entry.grid(row=7, column=1, sticky=tk.NSEW)

        self.genres_check.grid(row=8, column=1, sticky="w")
        # self.label_genres.grid(row=9, column=1, padx=8, sticky="w")
        self.genres_entry.grid(row=9, column=1, sticky=tk.NSEW)

        self.price_check.grid(row=10, column=1, sticky="w")
        self.price_entry.grid(row=11, column=1, sticky=tk.NSEW)

        self.rating_check.grid(row=12, column=1, sticky="w")
        self.rating_entry.grid(row=13, column=1, sticky=tk.NSEW)

        self.availability_check.grid(row=14, column=1, sticky="w")
        self.availability_entry.grid(row=15, column=1, sticky=tk.NSEW)

        self.sort_check.grid(row=16, column=1, sticky="w")
        self.sort_entry.grid(row=17, column=1, sticky=tk.NSEW)

        self.label_num_of_books.grid(row=18, column=1, sticky="w")
        self.num_of_books_entry.grid(row=18, column=1, sticky="e")

        self.export_to_gsheet_check.grid(row=19, column=1, sticky="w")
        self.export_to_gsheet_entry.grid(row=20, column=1, sticky=tk.NSEW)
        self.new_sheet_check.grid(row=21, column=1, sticky=tk.NSEW)

        # self.no_sequentials_check.grid(row=12, column=1, pady=8, sticky="w")

    def open_window(self):
        self.root.mainloop()

    def add_button(self):
        self.button = tk.Button(self.root, text="SCRAPE", font=("Times New Roman", 14),
                                command=self.button_push)
        self.button.grid(row=23, column=1, pady=5, columnspan=2)

    def display_pass(self, passwrd):
        self.generated_pass_box.configure(state="normal", width=len(passwrd))
        self.generated_pass_box.delete(0, 999)
        self.generated_pass_box.insert(0, passwrd)
        self.generated_pass_box.configure(state="readonly")
        self.generated_pass_box.grid(row=11, column=1, columnspan=2)

    def pass_box_remove(self):
        self.generated_pass_box.grid_remove()

    def display_message(self, msg):
        self.label_creation_msg.configure(text=msg)
        self.label_creation_msg.grid(row=12, column=1, padx=5, pady=5, columnspan=2)

    def return_gsheet_info(self):
        return self.gsheet_info

    def set_class_arguments(self):
        filter = ""
        filter_list = []
        descr = ""
        description_list = []

        if self.wanted_entry.cget("state") == "normal":
            self.filter_dict["t"] = self.filter_dict["d"] = self.filter_dict["g"] = self.filter_dict["f"] = self.filter_dict["s"] = None
            self.filter_dict["w"] = self.wanted_entry_text.get()
        else:
            self.filter_dict["w"] = None
            if self.title_entry.cget("state") == "normal":
                self.filter_dict["t"] = self.title_entry_text.get()
            else:
                self.filter_dict["t"] = None
            if self.descr_entry.cget("state") == "normal":
                descr = self.descr_entry_text.get()
                description_list.append(descr)
                self.filter_dict["d"] = description_list
            else:
                self.filter_dict["d"] = None
            if self.genres_entry.cget("state") == "normal":
                self.filter_dict["g"] = self.genres_entry_text.get()
            else:
                self.filter_dict["g"] = None
            if self.price_entry.cget("state") == "normal" or self.rating_entry.cget("state") == "normal" or self.availability_entry.cget("state") == "normal":
                if self.price_entry.cget("state") == "normal":
                    print("price:", self.price_entry_text.get())
                    filter += "price" + self.price_entry_text.get()
                if self.rating_entry.cget("state") == "normal":
                    print("rating:", self.rating_entry_text.get())
                    if filter != "":
                        filter += ','
                    filter += "rating" + self.rating_entry_text.get()
                if self.availability_entry.cget("state") == "normal":
                    print("availability:", self.availability_entry_text.get())
                    if filter != "":
                        filter += ','
                    filter += "availability" + self.availability_entry_text.get()
                filter_list.append(filter)
                self.filter_dict["f"] = filter_list
            else:
                self.filter_dict["f"] = None
            if self.sort_entry.cget("state") == "normal":
                self.filter_dict["s"] = self.sort_entry_text.get().split(' ')
            else:
                self.filter_dict["s"] = None

        if self.num_of_books_entry.cget("state") == "normal":
            self.filter_dict["b"] = int(self.num_of_books_entry_text.get())
        else:
            self.filter_dict["b"] = 0

        if self.export_to_gsheet_entry.cget("state") == "normal":
            self.gsheet_info["export"] = True
            self.gsheet_info["sheetname"] = self.export_to_gsheet_entry_text.get()
            self.new_sheet_check_box()

    def button_push(self):
        self.set_class_arguments()

        print("filter dict = ", self.filter_dict)
        res = Cli(**self.filter_dict)
        print("res dict:", res.dct_with_filters)
        print("gsheet info:", self.gsheet_info)

        self.scraper = Scraper(res.dct_with_filters)
        self.scraper.gui_active = True
        self.scraper.import_to_sheets = self.gsheet_info["export"]
        self.scraper.sheetname = self.gsheet_info["sheetname"]
        self.scraper.new_sheet = self.gsheet_info["new_sheet"]
        self.scraper.run()

