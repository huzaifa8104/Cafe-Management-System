from tkinter import *
from tkinter import messagebox
import sys
from PIL import Image
from datetime import datetime
import customtkinter as ctk
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Cafe Management System")
        self.geometry(f"{950}x{620}")

        self.head = ctk.CTkFont(family="Comic Sans MS",size=35, weight="bold")
        self.date_font = ctk.CTkFont(family="Comic Sans MS",size=20, weight="bold")
        self.main = ctk.CTkFont(size=20, weight="bold")
        self.cal_font = ctk.CTkFont(family="Comic Sans MS",size=20, weight="bold")

        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure((1, 2), weight=1)
        self.grid_rowconfigure(0, weight=0)

        items_var = []
        for i in range(1,15):
            items_var.append(IntVar())
            setattr(self, f"item_{i}",items_var[-1])

        #widgets
        self.frame_0 = ctk.CTkFrame(self, border_width=10,border_color="blue",corner_radius=15)
        self.frame_0.grid(row=0, column=0,columnspan=3, padx=15, pady=15, sticky="new")
        Heading = ctk.CTkLabel(self.frame_0, text = 'Cafe Management System', font=self.head, corner_radius=10)
        Heading.pack(pady=10)
        date = ctk.CTkLabel(self.frame_0,text=datetime.now(),font=self.date_font)
        date.pack()

        self.frame_1 = ctk.CTkScrollableFrame(self,corner_radius=15,label_font=ctk.CTkFont(size=35,weight="bold",family="Comic Sans MS"),scrollbar_button_hover_color="blue",label_text="CAFE ITEMS")
        self.frame_1.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.frame_1.grid_columnconfigure((0,1) ,weight=1)

        self.tea = ctk.CTkLabel(self.frame_1, text="TEA", font=ctk.CTkFont(family="Comic Sans MS",size=25, weight="bold", underline=2))
        self.tea.grid(row=0, column=0, columnspan=2,pady=10,sticky="nsew")

        self.green_tea = ctk.CTkLabel(self.frame_1, text="Green Tea",anchor="w", font=self.main)
        self.green_tea.grid(row=1, column=0, sticky="nsew")
        self.Green_Tea_ent = ctk.CTkEntry(self.frame_1,placeholder_text="")
        self.Green_Tea_ent.configure(textvariable=self.item_1)
        self.Green_Tea_ent.grid(row=1, column=1,padx=10,pady=10, sticky="nsew")        

        self.Milk_Tea = ctk.CTkLabel(self.frame_1, text="Milk Tea", font=self.main,anchor="w")
        self.Milk_Tea.grid(row=2, column=0,padx=0, sticky="nsew")
        self.Milk_Tea_ent = ctk.CTkEntry(self.frame_1,placeholder_text="")
        self.Milk_Tea_ent.configure(textvariable=self.item_2)
        self.Milk_Tea_ent.grid(row=2, column=1,padx=10,pady=10, sticky="nsew")

        self.Ginger_Tea = ctk.CTkLabel(self.frame_1, text="Ginger Tea", font=self.main,anchor="w")
        self.Ginger_Tea.grid(row=3, column=0, sticky="nsew")
        self.Ginger_Tea_ent = ctk.CTkEntry(self.frame_1,placeholder_text="")
        self.Ginger_Tea_ent.configure(textvariable=self.item_3)
        self.Ginger_Tea_ent.grid(row=3, column=1,padx=10,pady=10, sticky="nsew")

        self.Honey_Lemon = ctk.CTkLabel(self.frame_1, text="Honey Lemon", font=self.main,anchor="w")
        self.Honey_Lemon.grid(row=4, column=0, sticky="nsew")
        self.Honey_Lemon_ent = ctk.CTkEntry(self.frame_1,placeholder_text="")
        self.Honey_Lemon_ent.configure(textvariable=self.item_4)
        self.Honey_Lemon_ent.grid(row=4, column=1,padx=10,pady=10, sticky="nsew")

        self.coffee = ctk.CTkLabel(self.frame_1, text="COFFEE", font=ctk.CTkFont(family="Comic Sans MS",size=25, weight="bold", underline=2))
        self.coffee.grid(row=5, column=0, columnspan=2,pady=10,sticky="nsew")

        self.americano = ctk.CTkLabel(self.frame_1, text="Americano",anchor="w", font=self.main)
        self.americano.grid(row=6, column=0, sticky="nsew")
        self.Americano_ent = ctk.CTkEntry(self.frame_1,placeholder_text="")
        self.Americano_ent.configure(textvariable=self.item_5)
        self.Americano_ent.grid(row=6, column=1,padx=10,pady=10, sticky="nsew")        

        self.black_coffee = ctk.CTkLabel(self.frame_1, text="Black Coffe", font=self.main,anchor="w")
        self.black_coffee.grid(row=7, column=0,padx=0, sticky="nsew")
        self.Black_Coffee_ent = ctk.CTkEntry(self.frame_1,placeholder_text="")
        self.Black_Coffee_ent.configure(textvariable=self.item_6)
        self.Black_Coffee_ent.grid(row=7, column=1,padx=10,pady=10, sticky="nsew")

        self.latte = ctk.CTkLabel(self.frame_1, text="Latte", font=self.main,anchor="w")
        self.latte.grid(row=8, column=0, sticky="nsew")
        self.Latte_ent = ctk.CTkEntry(self.frame_1,placeholder_text="")
        self.Latte_ent.configure(textvariable=self.item_7)
        self.Latte_ent.grid(row=8, column=1,padx=10,pady=10, sticky="nsew")

        self.ice_blended = ctk.CTkLabel(self.frame_1, text="ICE BLENDED", font=ctk.CTkFont(family="Comic Sans MS",size=25, weight="bold", underline=2))
        self.ice_blended.grid(row=9, column=0, columnspan=2,pady=10,sticky="nsew")

        self.caramel = ctk.CTkLabel(self.frame_1, text="Caramel",anchor="w", font=self.main)
        self.caramel.grid(row=10, column=0, sticky="nsew")
        self.Caramel_ent = ctk.CTkEntry(self.frame_1,placeholder_text="")
        self.Caramel_ent.configure(textvariable=self.item_8)
        self.Caramel_ent.grid(row=10, column=1,padx=10,pady=10, sticky="nsew")        

        self.coffee_jelly = ctk.CTkLabel(self.frame_1, text="Coffe Jelly", font=self.main,anchor="w")
        self.coffee_jelly.grid(row=11, column=0,padx=0, sticky="nsew")
        self.Coffee_Jelly_ent = ctk.CTkEntry(self.frame_1,placeholder_text="")
        self.Coffee_Jelly_ent.configure(textvariable=self.item_9)
        self.Coffee_Jelly_ent.grid(row=11, column=1,padx=10,pady=10, sticky="nsew")

        self.vanila = ctk.CTkLabel(self.frame_1, text="Vanila", font=self.main,anchor="w")
        self.vanila.grid(row=12, column=0, sticky="nsew")
        self.Vanila_ent = ctk.CTkEntry(self.frame_1,placeholder_text="")
        self.Vanila_ent.configure(textvariable=self.item_10)
        self.Vanila_ent.grid(row=12, column=1,padx=10,pady=10, sticky="nsew")

        self.frappe = ctk.CTkLabel(self.frame_1, text="FRAPPE", font=ctk.CTkFont(family="Comic Sans MS",size=25, weight="bold", underline=2))
        self.frappe.grid(row=13, column=0, columnspan=2,pady=10,sticky="nsew")

        self.mocha = ctk.CTkLabel(self.frame_1, text="Mocha",anchor="w", font=self.main)
        self.mocha.grid(row=14, column=0, sticky="nsew")
        self.Mocha_ent = ctk.CTkEntry(self.frame_1,placeholder_text="")
        self.Mocha_ent.configure(textvariable=self.item_11)
        self.Mocha_ent.grid(row=14, column=1,padx=10,pady=10, sticky="nsew")        

        self.white_mocha = ctk.CTkLabel(self.frame_1, text="White Mocha", font=self.main,anchor="w")
        self.white_mocha.grid(row=15, column=0,padx=0, sticky="nsew")
        self.White_Mocha_ent = ctk.CTkEntry(self.frame_1,placeholder_text="")
        self.White_Mocha_ent.configure(textvariable=self.item_12)
        self.White_Mocha_ent.grid(row=15, column=1,padx=10,pady=10, sticky="nsew")

        self.caramel_freeze = ctk.CTkLabel(self.frame_1, text="Caramel Freeze", font=self.main,anchor="w")
        self.caramel_freeze.grid(row=16, column=0, sticky="nsew")
        self.Caramel_Freeze_ent = ctk.CTkEntry(self.frame_1,placeholder_text="")
        self.Caramel_Freeze_ent.configure(textvariable=self.item_13)
        self.Caramel_Freeze_ent.grid(row=16, column=1,padx=10,pady=10, sticky="nsew")

        self.toffee_nut = ctk.CTkLabel(self.frame_1, text="Toffee Nut", font=self.main,anchor="w")
        self.toffee_nut.grid(row=17, column=0, sticky="nsew")
        self.Toffee_Nut_ent = ctk.CTkEntry(self.frame_1,placeholder_text="")
        self.Toffee_Nut_ent.configure(textvariable=self.item_14)
        self.Toffee_Nut_ent.grid(row=17, column=1,padx=10,pady=10, sticky="nsew")


#================================ Frame 2 =======================================

        self.tabview = ctk.CTkTabview(self,corner_radius=15,segmented_button_selected_color="blue")
        self.tabview.grid(row=1, column=1, sticky="nsew")
        self.tabview.add("Tab 1")
        self.tabview.add("Tab 2")
        self.tabview.tab("Tab 1").grid_columnconfigure((0,1), weight=1)  # configure grid of individual tabs
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        self.item_cost_lb = ctk.CTkLabel(self.tabview.tab("Tab 1"),text="Items Cost",anchor="w",font=self.main)
        self.item_cost_lb.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.items_cost = ctk.CTkEntry(self.tabview.tab("Tab 1"))
        self.items_cost.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")

        self.service_cost_lb = ctk.CTkLabel(self.tabview.tab("Tab 1"),text="Service Cost",anchor="w",font=self.main)
        self.service_cost_lb.grid(row=1, column=0, padx=0, pady=20, sticky="nsew")
        self.service_cost = ctk.CTkEntry(self.tabview.tab("Tab 1"))
        self.service_cost.grid(row=1, column=1, padx=0, pady=20, sticky="nsew")

        self.sub_cost_lb = ctk.CTkLabel(self.tabview.tab("Tab 1"),text="Sub Cost",anchor="w",font=self.main)
        self.sub_cost_lb.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")
        self.sub_cost = ctk.CTkEntry(self.tabview.tab("Tab 1"))
        self.sub_cost.grid(row=2, column=1, padx=0, pady=0, sticky="nsew")

        self.paid_tax_lb = ctk.CTkLabel(self.tabview.tab("Tab 1"),text="Paid Tax",anchor="w",font=self.main)
        self.paid_tax_lb.grid(row=3, column=0, padx=0, pady=20, sticky="nsew")
        self.paid_tax = ctk.CTkEntry(self.tabview.tab("Tab 1"))
        self.paid_tax.grid(row=3, column=1, padx=0, pady=20, sticky="nsew")

        self.total_bill_lb = ctk.CTkLabel(self.tabview.tab("Tab 1"),text="Total Bill",anchor="w",font=self.main)
        self.total_bill_lb.grid(row=4, column=0, padx=0, pady=0, sticky="nsew")
        self.total_bill = ctk.CTkEntry(self.tabview.tab("Tab 1"))
        self.total_bill.grid(row=4, column=1, padx=0, pady=0, sticky="nsew")

        self.Total_Bills_btn = ctk.CTkButton(self.tabview.tab("Tab 1"),font=self.cal_font,text="Total",command=self.Total_Bill)
        self.Total_Bills_btn.grid(row=5, column=0,columnspan=2,sticky="nsew", padx=0, pady=20)
        self.clear_btn = ctk.CTkButton(self.tabview.tab("Tab 1"),font=self.cal_font,text="clear",command=self.Clear)
        self.clear_btn.grid(row=6, column=0,columnspan=2,sticky="nsew", padx=0, pady=0)

        self.textbox = ctk.CTkTextbox(self.tabview.tab("Tab 2"),height=250)
        self.textbox.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.print_btn = ctk.CTkButton(self.tabview.tab("Tab 2"),text="Print",font=self.cal_font,command=self.print_func)
        self.print_btn.grid(row=1, column=0,columnspan=2, padx=0, pady=20, sticky="nsew")
        self.exit_btn = ctk.CTkButton(self.tabview.tab("Tab 2"),text="Exit",font=self.cal_font,command=self.exit_app)
        self.exit_btn.grid(row=2, column=0,columnspan=2, padx=0, pady=0, sticky="nsew")

#======================================= Frame3 ===========================

        self.frame_3 = ctk.CTkFrame(self,corner_radius=15)
        self.frame_3.grid(row=1,column=2,sticky="nsew",padx=20,pady=20)
        self.frame_3.grid_columnconfigure((0,1,2,3), weight=1)
        
        self.calculator = ctk.CTkLabel(self.frame_3, text="Calculator", font=ctk.CTkFont(size=30,weight="bold",family="Comic Sans MS", underline=2))
        self.calculator.grid(row=0, column=0,padx=10,pady=10,sticky="nsew",columnspan=4)
        self.result = ctk.CTkEntry(self.frame_3,width=180,height=40)
        self.result.grid(row=1,column=0,sticky="nsew",padx=10,pady=10,columnspan=4)

        self.seven = ctk.CTkButton(self.frame_3,text="7",width=25,font=self.cal_font,corner_radius=25,command=self.seven)
        self.seven.grid(row=2,column=0,padx=5,pady=5,sticky="nsew")
        self.eight = ctk.CTkButton(self.frame_3,text="8",width=25,font=self.cal_font,corner_radius=25,command=self.eight)
        self.eight.grid(row=2,column=1,padx=0,pady=5,sticky="nsew")
        self.nine = ctk.CTkButton(self.frame_3,text="9",width=25,font=self.cal_font,corner_radius=25,command=self.nine)
        self.nine.grid(row=2,column=2,padx=5,pady=5,sticky="nsew")
        self.plus = ctk.CTkButton(self.frame_3,text="+",width=25,font=self.cal_font,corner_radius=25,command=self.plus)
        self.plus.grid(row=2,column=3,padx=0,pady=5,sticky="nsew")

        self.four = ctk.CTkButton(self.frame_3,text="4",width=25,font=self.cal_font,corner_radius=25,command=self.four)
        self.four.grid(row=3,column=0,padx=5,pady=5,sticky="nsew")
        self.five = ctk.CTkButton(self.frame_3,text="5",width=25,font=self.cal_font,corner_radius=25,command=self.five)
        self.five.grid(row=3,column=1,padx=0,pady=5,sticky="nsew")
        self.six = ctk.CTkButton(self.frame_3,text="6",width=25,font=self.cal_font,corner_radius=25,command=self.six)
        self.six.grid(row=3,column=2,padx=5,pady=5,sticky="nsew")
        self.minus = ctk.CTkButton(self.frame_3,text="-",width=25,font=self.cal_font,corner_radius=25,command=self.minus)
        self.minus.grid(row=3,column=3,padx=0,pady=5,sticky="nsew")

        self.one = ctk.CTkButton(self.frame_3,text="1",width=25,font=self.cal_font,corner_radius=25,command=self.one)
        self.one.grid(row=4,column=0,padx=5,pady=5,sticky="nsew")
        self.two = ctk.CTkButton(self.frame_3,text="2",width=25,font=self.cal_font,corner_radius=25,command=self.two)
        self.two.grid(row=4,column=1,padx=0,pady=5,sticky="nsew")
        self.three = ctk.CTkButton(self.frame_3,text="3",width=25,font=self.cal_font,corner_radius=25,command=self.three)
        self.three.grid(row=4,column=2,padx=5,pady=5,sticky="nsew")
        self.multiply = ctk.CTkButton(self.frame_3,text="x",width=25,font=self.cal_font,corner_radius=25,command=self.multiply)
        self.multiply.grid(row=4,column=3,padx=0,pady=5,sticky="nsew")

        self.clear_cal = ctk.CTkButton(self.frame_3,text="C",width=25,font=self.cal_font,corner_radius=25,command=self.clear_cal)
        self.clear_cal.grid(row=5,column=0,padx=5,pady=5,sticky="nsew")
        self.zero = ctk.CTkButton(self.frame_3,text="0",width=25,font=self.cal_font,corner_radius=25,command=self.zero)
        self.zero.grid(row=5,column=1,padx=0,pady=5,sticky="nsew")
        self.equal = ctk.CTkButton(self.frame_3,text="=",width=25,font=self.cal_font,corner_radius=25,command=self.equal)
        self.equal.grid(row=5,column=2,padx=5,pady=5,sticky="nsew")
        self.divide = ctk.CTkButton(self.frame_3,text="/",width=25,font=self.cal_font,corner_radius=25,command=self.divide)
        self.divide.grid(row=5,column=3,padx=0,pady=5,sticky="nsew")

        self.appearance_mode_fr = ctk.CTkLabel(self.frame_3, text="Appearance Mode:", font=ctk.CTkFont(size=20,weight="bold",family="Comic Sans MS"))
        self.appearance_mode_fr.grid(row=7, column=0,padx=10,pady=5,columnspan=4)
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.frame_3, font=ctk.CTkFont(size=20,weight="bold",family="Comic Sans MS"), values=[ "Light","Dark","System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.set("System")
        self.appearance_mode_optionemenu.grid(row=8, column=0,sticky="nsew",padx=10,pady=0,columnspan=4)
        self.scaling = ctk.CTkLabel(self.frame_3, text="UI Scaling:", font=ctk.CTkFont(size=20,weight="bold",family="Comic Sans MS"))
        self.scaling.grid(row=9, column=0,padx=10,pady=5,columnspan=4)
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.frame_3,font=ctk.CTkFont(size=20,weight="bold",family="Comic Sans MS"), values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.set("100%")
        self.scaling_optionemenu.grid(row=10, column=0,sticky="nsew",columnspan=4, padx=5, pady=0)


#================================= Print Frame ====================
        self.print_frame0 = ctk.CTkFrame(self, border_width=7,border_color="green",corner_radius=13)
        self.print_frame0.grid_columnconfigure(1, weight=1)
        # self.print_frame.grid_rowconfigure(1,weight=0)
        self.print_label = ctk.CTkLabel(self.print_frame0, text="File has been Temporarily Saved Successfully", font=self.main)
        self.print_label.grid(row=0, column=1, padx=30, pady=30)

        self.print_frame1 = ctk.CTkFrame(self, border_width=7,border_color="red",corner_radius=13)
        self.print_frame1.grid_columnconfigure(1, weight=1)
        # self.print_frame1.grid_rowconfigure(1,weight=0)
        self.print_label = ctk.CTkLabel(self.print_frame1, text="Connect to a Printer!!!", font=self.main)
        self.print_label.grid(row=0, column=1, padx=30, pady=30)
        self.back_button = ctk.CTkButton(self.print_frame1, text="Back",font= self.cal_font, command=self.previous_wind, width=200)
        self.back_button.grid(row=1, column=1, padx=30, pady=(20, 20))


#======================= Functions =====================

    def Total_Bill(self):
        items = {
                "Green_Tea": 30,
                "Milk_Tea": 20,
                "Ginger_Tea": 25,
                "Honey_Lemon": 35,
                "Americano": 150,
                "Black_Coffee": 120,
                "Latte": 200,
                "Caramel": 220,
                "Coffee_Jelly": 250,
                "Vanila": 230,
                "Mocha": 270,
                "White_Mocha": 300,
                "Caramel_Freeze": 350,
                "Toffee_Nut": 320,
        }

        self.total_cost = 0
        for item, price in items.items():
                entry = getattr(self, f"{item.replace(' ', '_')}_ent")
                if entry.get() != "":
                        cost = price * int(entry.get())
                        setattr(self, f"{item.replace(' ', '_')}_cost", cost)
                        self.total_cost += cost

        self.items_cost.delete(0, END) if self.items_cost.get() != "" else None
        self.items_cost.insert(END, self.total_cost)

        self.service_cost.delete(0, END) if self.service_cost.get() != "" else None
        self.service_cost.insert(END, 20)

        self.sub_cost.delete(0, END) if self.sub_cost.get() != "" else None
        self.sub_cost.insert(END, int(self.items_cost.get()) + int(self.service_cost.get()))
        
        self.paid_tax.delete(0, END) if self.paid_tax.get() != "" else None
        self.paid_tax.insert(END, float(self.sub_cost.get()) * 8 / 100)

        self.total_bill.delete(0, END) if self.total_bill.get() != "" else None
        self.total_bill.insert(END, float(self.sub_cost.get()) + float(self.paid_tax.get()))

        self.textbox.delete('1.0',END)
        self.textbox.insert(END,f"\t\t  Receipt")
        self.textbox.insert(END,f"\n\n=====================================")
        self.textbox.insert(END,f"\nItem\t\t\tQty.\tCost")

        items_present = []
        for i in range(1, 15):
            item_cost = 0
            for item, price in items.items():
                entry = getattr(self, f"{item.replace(' ', '_')}_ent")
                if entry.get() != "" and int(entry.get()) != 0:
                    cost = price * int(entry.get())
                    setattr(self, f"{item.replace(' ', '_')}_cost", cost)
                    item_cost += cost
            setattr(self, f"individual{i}cost", item_cost)
            if item_cost != 0:
                # self.textbox.insert(END, f"Individual {i}\n")
                for item, price in items.items():
                    if item not in items_present:
                        entry = getattr(self, f"{item.replace(' ', '_')}_ent")
                        if entry.get() != "" and int(entry.get()) != 0:
                            cost = price * int(entry.get())
                            item_name = item.replace("_", " ")
                            self.textbox.insert(END, f"\n{item_name}\t\t\t {entry.get()}\t  {cost}")
                            items_present.append(item)
        self.textbox.insert(END, f"\n-----------------------------------------------------------------------------------")
        self.textbox.insert(END, f"\nTotal Cost\t\t\t\t")
        self.textbox.insert(END, f"={self.total_cost}")
        self.textbox.insert(END, f"\nService Cost\t\t\t\t")
        self.textbox.insert(END, f"={self.service_cost.get()}")
        self.textbox.insert(END, f"\nSub Cost\t\t\t\t")
        self.textbox.insert(END, f"={self.sub_cost.get()}")
        self.textbox.insert(END, f"\nPaid Tax\t\t\t\t")
        self.textbox.insert(END, f"={self.paid_tax.get()}")
        self.textbox.insert(END, f"\nTotal\t\t\t\t")
        self.textbox.insert(END, f"={self.total_bill.get()}")

    def Clear(self):
        fields = [self.Green_Tea_ent, self.Milk_Tea_ent, self.Ginger_Tea_ent, self.Honey_Lemon_ent, 
                self.Americano_ent, self.Black_Coffee_ent, self.Latte_ent, self.Caramel_ent, 
                self.Coffee_Jelly_ent, self.Vanila_ent, self.Mocha_ent, self.White_Mocha_ent, 
                self.Caramel_Freeze_ent, self.Toffee_Nut_ent, self.items_cost, self.service_cost, 
                self.sub_cost, self.paid_tax, self.total_bill]
        for field in fields:
            field.delete(0, "end")
    
        line_number = self.textbox.index("1.0")
        end_of_file = self.textbox.index(END)
        self.textbox.delete(line_number, end_of_file)

    def insert_into_result(self, string):
        if 'error' in self.result.get() or '=' in self.result.get():
            self.result.delete(0, "end")
        self.result.insert("end", string)

    def nine(self):
        self.insert_into_result("9")

    def eight(self):
        self.insert_into_result("8")

    def seven(self):
        self.insert_into_result("7")

    def six(self):
        self.insert_into_result("6")

    def five(self):
        self.insert_into_result("5")

    def four(self):
        self.insert_into_result("4")

    def three(self):
        self.insert_into_result("3")

    def two(self):
        self.insert_into_result("2")

    def one(self):
        self.insert_into_result("1")

    def zero(self):
        self.insert_into_result("0")

    def plus(self):
        self.insert_into_result("+")

    def minus(self):
        self.insert_into_result("-")

    def multiply(self):
        self.insert_into_result("*")

    def divide(self):
            self.insert_into_result("/")


    def equal(self):
        input_str = self.result.get()
        if not input_str:
            self.result.insert("end", "error")
            return
        if input_str.startswith(('+', '*', '/')):
            self.result.delete(0, "end")
            self.result.insert("end", "error")
            return
        while input_str[0] == '0' and len(input_str) > 1 and input_str[1].isdigit():
            input_str = input_str[1:]
        try:
            self.res = eval(input_str)
        except:
            self.result.delete(0, "end")
            self.result.insert("end", "error")
            return
        self.result.delete(0, "end")
        self.result.insert("end", input_str + " = " + str(self.res))
   
    def clear_cal(self):
        self.result.delete(0,"end")

    
    def print_func(self):
        op=messagebox.askyesno("Print Bill","Do you want to Print the bill?")
        if op>0:
            self.of_data=self.textbox.get("1.0",END)
            f1=open("./Cafe_management_system/file_to_print/"+"temporary_file.txt","w")
            f1.write(self.of_data)
            f1.close
        else:
            return 
        
        self.frame_0.grid_forget()
        self.frame_1.grid_forget()
        self.tabview.grid_forget()
        self.frame_3.grid_forget()
        self.print_frame0.grid(row=0, column=1,columnspan=1,rowspan=1, padx=15, pady=15, sticky="nsew")  
        self.print_frame1.grid(row=1, column=1,columnspan=1,rowspan=1, padx=15, pady=15, sticky="new")  



    def previous_wind(self):
        self.print_frame0.grid_forget()  
        self.print_frame1.grid_forget()  
        self.frame_0.grid(row=0, column=0,columnspan=3, padx=15, pady=15, sticky="new")
        self.frame_1.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.tabview.grid(row=1, column=1, sticky="nsew")
        self.frame_3.grid(row=1,column=2,sticky="nsew",padx=20,pady=20)


    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)


    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)
    
    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
