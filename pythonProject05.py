from datetime import datetime
import os

class NewsGenerator():
    def __init__(self, file=None , data_type=None, text=None , city=None , expiry_date=None):
        self.file = file
        self.data_type = data_type
        self.text = text
        self.city = city
        self.expiry_date = expiry_date


    #create a file
    def create_ad(self,data_type):
        self.file = open("demofile.txt", "a")
        if os.path.getsize('demofile.txt') == 0:
           self.file.write("News feed:\n")

        self.text = input("Enter the text: ")

        if data_type == 'News':
            self.city = input("Enter the city: ")
            self.create_news(self.text, self.city)

        else:
            self.expiry_date = input("Enter the expiry date YYYY/MM/DD: ")
            self.create_private_ad(self.text, self.expiry_date)


        self.file.close()


    def create_news(self,text,city):
        self.file.write("News:......................\n" + text + "\n" + city + ',' + datetime.now().strftime("%Y/%m/%d %H:%M:%S")+"\n\n\n")


    def create_private_ad(self,text,expiry_date):
        self.file.write("Private Ad:......................\n" + text + "\n" + "Actual until "+ expiry_date + ',' + str((datetime.strptime(expiry_date, "%Y/%m/%d")-datetime.now()).days) + " days left "+ "\n\n\n")












count = 0
Gen1 = NewsGenerator()

while count < 3 :
    count +=1
    Gen1.data_type = input("Enter the type of data: News - Private Ad: ")
    Gen1.create_ad(Gen1.data_type)










