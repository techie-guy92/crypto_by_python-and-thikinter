import sys
sys.path.insert(0,"C:/Users/Administrator/Downloads/IT/Python Project/__pycache__")
import My_Codes.DataBase_Connector as sql
from tkinter import * 
import main
import data_base



#------------------------------------Functions--------------------------------------------------

flag=False


class Crypto_App:

        def coins_calculated_by_toman(self):
                global flag

                if flag == False:
                        zipfile_toman=zip(main.coin_names,main.toman_coins)
                        for name,price in zipfile_toman:
                                self.display.insert(END,f"{name}: {price}\n")
                                flag=True
        
                elif flag == True:
                        self.display.delete("1.0", END)
                        flag=False


        def coins_calculated_by_usdt(self):
                global flag

                if flag == False:
                        zipfile_usdt=zip(main.coin_names,main.usdt_coins)
                        for name,price in zipfile_usdt:
                                self.display.insert(END,f"{name}: {price}\n")
                                flag=True

                elif flag == True:
                        self.display.delete("1.0", END)
                        flag=False

        
        def usdt_rate(self):
                global flag
                if flag == False:
                        self.display.insert(END,f"""USDT Rate in tgju: {main.usdt_tgju}
USDT Rate in arzdigita: {main.usdt_arzdigital2}
USDT Rate in ramzarz: {main.usdt_ramzarz}""")
                        flag=True
        
                elif flag == True:
                        self.display.delete("1.0", END)
                        flag=False


        def save_data(self):
                global flag
                new_toman_list=main.final_toman_list
                new_usdt_list=main.final_usdt_list
                usdt=main.usdt_tgju

                if flag == False:
                
                        try:
                                sql.db_table("dbcoin_rates",f"Insert into T_USDT(Coin_Name,Toman_rate,USDT_rate,Date) values('USDT',{usdt},{1},now())")
                                sql.db_table("dbcoin_rates",f"Insert into T_BTC(Coin_Name,Toman_rate,USDT_rate,Date) values('BTC',{new_toman_list[0]},{new_usdt_list[0]},now())")
                                sql.db_table("dbcoin_rates",f"Insert into T_ETH(Coin_Name,Toman_rate,USDT_rate,Date) values('ETH',{new_toman_list[1]},{new_usdt_list[1]},now())")
                                sql.db_table("dbcoin_rates",f"Insert into T_BNB(Coin_Name,Toman_rate,USDT_rate,Date) values('BNB',{new_toman_list[2]},{new_usdt_list[2]},now())")
                                sql.db_table("dbcoin_rates",f"Insert into T_SOL(Coin_Name,Toman_rate,USDT_rate,Date) values('SOL',{new_toman_list[8]},{new_usdt_list[8]},now())")
                                sql.db_table("dbcoin_rates",f"Insert into T_ADA(Coin_Name,Toman_rate,USDT_rate,Date) values('ADA',{new_toman_list[6]},{new_usdt_list[6]},now())")
                                sql.db_table("dbcoin_rates",f"Insert into T_DOT(Coin_Name,Toman_rate,USDT_rate,Date) values('DOT',{new_toman_list[7]},{new_usdt_list[7]},now())")
                                sql.db_table("dbcoin_rates",f"Insert into T_XRP(Coin_Name,Toman_rate,USDT_rate,Date) values('XRP',{new_toman_list[4]},{new_usdt_list[4]},now())")
                                sql.db_table("dbcoin_rates",f"Insert into T_AVAX(Coin_Name,Toman_rate,USDT_rate,Date) values('AVAX',{new_toman_list[9]},{new_usdt_list[9]},now())")
                                sql.db_table("dbcoin_rates",f"Insert into T_XLM(Coin_Name,Toman_rate,USDT_rate,Date) values('XLM',{new_toman_list[3]},{new_usdt_list[3]},now())")
                                sql.db_table("dbcoin_rates",f"Insert into T_DogeCoin(Coin_Name,Toman_rate,USDT_rate,Date) values('DogeCoin',{new_toman_list[5]},{new_usdt_list[5]},now())")
                                self.display.insert(END,"Coins data have been saved")
                                flag=True

                        except:
                                self.display.insert(END,"Ooops!!!\nThere was something went wrong")
        
                elif flag == True:
                        self.display.delete("1.0", END)
                        flag=False


       

#--------------------------------------GUI--------------------------------------------------
        
        def __init__(self):
        

                self.root=Tk()

                self.root.title("  Coin Rates")
                self.root.config(bg="#00a1a1")
                self.root.iconbitmap("Files/Icons/btc (2).ico")


                w=300
                h=330
                sw=self.root.winfo_screenwidth()
                sh=self.root.winfo_screenheight()
                x=(sw/2)-(w/2)
                y=(sh/2)-(h/2)
                self.root.geometry("%dx%d+%d+%d"%(w,h,x,y))
                self.root.resizable(width=False,height=False)


                # self.display=Label(root,text="",font=("tahoma",10),bg="yellow",fg="#000000",relief=RIDGE,width=40,height=15)
                self.display=Text(self.root,font=("tahoma",10),bg="yellow",fg="#000000",relief=RIDGE,width=40,height=15)

                self.Coins_by_Toman=Button(self.root,text="Coins by Toman",bg="#a1a1a1",fg="#000000",width=12,command=self.coins_calculated_by_toman)
                self.Coins_by_USDT=Button(self.root,text="Coins by USDT",bg="#a1a1a1",fg="#000000",width=12,command=self.coins_calculated_by_usdt)
                self.USDT_rate=Button(self.root,text="USDT rate",bg="#a1a1a1",fg="#000000",width=12,command=self.usdt_rate)
                self.Save=Button(self.root,text="Save Data",bg="#a1a1a1",fg="#000000",width=12,command=self.save_data)


                self.display.place(x=7,y=50)
                self.Coins_by_Toman.place(x=3,y=5)
                self.Coins_by_USDT.place(x=103,y=5)
                self.USDT_rate.place(x=203,y=5)
                self.Save.place(x=103,y=300)


                self.root.mainloop()



#-------------------------------------------------------------------------------------------------------------------------


my_form=Crypto_App()