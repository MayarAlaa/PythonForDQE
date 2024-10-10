from collections import Counter
import csv
import json
import re
from datetime import datetime
from pythonProject04_part2 import capitalize_sentences
import os
import sys

class NewsGenerator:
    def __init__(self, file_path="demofile.txt"):
        self.file_path = file_path
        self.header_added = False
        self.add_header()

    def add_header(self):
        if not os.path.exists(self.file_path) or os.path.getsize(self.file_path) == 0:
            with open(self.file_path, "w") as file:
                file.write("News feed:\n")
            self.header_added = True

    def get_input(self):
        text = input("Enter the text: ")
        return capitalize_sentences(text)

    def create_news(self, text, city):
        time_stamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        news_entry = f"News:......................\n{text}\n{city}, {time_stamp}\n\n\n"
        self.write_to_file(news_entry)

    def create_private_ad(self, text, expiry_date):
        days_left = (datetime.strptime(expiry_date, "%Y/%m/%d") - datetime.now()).days
        ad_entry = f"Private Ad:......................\n{text}\nActual until {expiry_date}, {days_left} days left\n\n\n"
        self.write_to_file(ad_entry)

        
    def write_to_file(self, content):
        with open(self.file_path, "a") as file:
            file.write(content)

        self.count_letters_csv()
        self.count_words_csv()   

    def count_words_csv(self):
           #count words
           with open(self.file_path,'r') as f:
                content = f.read()
                words = re.split(r'[ ,:\n]+', content.lower()) 
                count_words = Counter(words)


           headers = ['word','count']

           with open('word_count.csv','w') as f:
                word_count_writer = csv.DictWriter(f,fieldnames=headers,delimiter='|')

                word_count_writer.writeheader()

                for word,count in count_words.items():

                    word_count_writer.writerow({'word': word , 'count':count})

    def count_letters_csv(self):
               with open (self.file_path,'r') as f:
                      content = f.read()
                      filtered_text = [char for char in content if char.isalpha()]
                      count_letters = Counter(filtered_text)
    


           # Merging and calculating percentages
               final_data = {}
               for letter, count in count_letters.items():
                   upper_letter = letter.upper()  # Normalize to uppercase for consistency
                   if upper_letter not in final_data:
                       final_data[upper_letter] = {'count_all': 0, 'count_uppercase': 0, 'percentage': 0}
                   final_data[upper_letter]['count_all'] += count
                   if letter.isupper():
                       final_data[upper_letter]['count_uppercase'] += count


           # Calculate percentages
               for letter, data in final_data.items():
                   if data['count_all'] > 0:
                       data['percentage'] = f"{round((data['count_uppercase'] / data['count_all']) * 100,2)}%"


               with open('letters_count.csv', 'w') as f:
                    writer = csv.writer(f) 

                    writer.writerow(['Letter', 'Total Count', 'Uppercase Count', 'Percentage Uppercase'])

                    for letter , data in sorted(final_data.items()):
                         writer.writerow([letter, data['count_all'],data['count_uppercase'], data['percentage']])


class ConsoleNewsGenerator(NewsGenerator):
    def create_ad(self):
        text = self.get_input()
        data_type = input("Enter the type of data: News - Private Ad: ")
        if data_type == 'News':
            city = input("Enter the city: ")
            self.create_news(text, city)
        else:
            expiry_date = input("Enter the expiry date YYYY/MM/DD: ")
            self.create_private_ad(text, expiry_date)
        
        

class TxtFileNewsGenerator(NewsGenerator):
    def create_ad(self, input_file_path):
        if not input_file_path:
            input_file_path = 'c:/Users/Mayar_Saleh/Desktop/Mayar/DQE training/Python for DQE/Module8/input.txt'  # Default path

        try:
            with open(input_file_path, 'r') as file:
              while True:
                content_type = file.readline().strip()

                if 'eof' in content_type:
                    break

                text = capitalize_sentences(file.readline().strip())
                if 'News' in content_type:
                    city = file.readline().strip()
                    self.create_news(text, city)
                elif 'Private Ad' in content_type:
                    expiry_date = file.readline().strip()
                    self.create_private_ad(text, expiry_date)

            os.remove(input_file_path)

        except Exception as e:
            print(f"Error reading file: {str(e)}")



class JsonFileNewsGenerator(NewsGenerator):
    def create_ad(self, input_file_path):
        if not input_file_path:
            input_file_path = 'c:/Users/Mayar_Saleh/Desktop/Mayar/DQE training/Python for DQE/Module8/input.json'  # Default path

            try:
                content = json.load(open(input_file_path))

                for key in content.keys():
                     text = capitalize_sentences(content[key]["text"].strip())

                     if content[key]["publication_type"].lower() == 'news':
                          city = content[key]["city"].strip()
                          self.create_news(text, city)

                     elif content[key]["publication_type"].lower() == 'ads':
                          expiry_date = content[key]["date"].strip()
                          self.create_private_ad(text, expiry_date)                        
                
                os.remove(input_file_path)

            except Exception as e:
                print(f"Error reading file: {str(e)}")

       



def main():
    source = input("Get data from: Console - File: ").strip().lower()
    if source == "console":
        gen = ConsoleNewsGenerator()
        gen.create_ad()
    elif source == "file":
        input_file_ext = input("Please provide the file type: text , json: ")
        input_file_path = input("Please provide the file path if available or else press enter: ")

        if input_file_ext == 'text':
               gen = TxtFileNewsGenerator()
               gen.create_ad(input_file_path)

        elif input_file_ext == 'json':
               gen = JsonFileNewsGenerator()
               gen.create_ad(input_file_path)
        
        

if __name__ == "__main__":
    main()