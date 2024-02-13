from bs4 import BeautifulSoup
import requests
import pandas as pd

class FetcherMain:
    def __init__(self, url):
        self.url : str = url
        self.res = requests.get(self.url)
        self.soup = BeautifulSoup(self.res.content, 'html.parser')
        
    def see_res(self):
        print(self.res)
        if self.soup:
            print('The Soup is ready!')
        else:
            print('Soup is not avalable')
        
    def get_tag(self, tag):
        self.tag : str = tag
        tags = self.soup.find_all(self.tag)
        if tags:
            return tags
        else:
            print('Check if tag exists ?! ')
            
    def get_tags_in_table(self, table, tags):
        self.table = table
        self.tags : str = tags
        
        tags_intable = self.table.find_all(self.tags)
        if tags_intable:
            return tags_intable
        else:
            print('Tags are not found !!!')
            
    def cleaner(self, html):
        self.html = html
        clean_obj = [x.get_text() for x in self.html]
        if clean_obj:
            return clean_obj
        else:
            print('I cant clean OOOOO')
            
    def slicer(self, obj, st, fn, jump):
        self.obj = obj
        self.st = st
        self.fn = fn
        self.jump = jump
        
        try:
            sliced_obj = self.obj[self.st:self.fn:self.jump]
            if sliced_obj:
                return sliced_obj
        except Exception as e:
            print("An error occurred:", e)
        
    def pandas_frame(self, var_obj):
        self.var_obj = var_obj
        try:
            df = pd.DataFrame(self.var_obj)
            return df
        except Exception as e:
            print(f"An error ocurred {e}")
            
    def rename_df_col(self, df, old_name, new_name):
        self.df = df
        self.old_name = old_name
        self.new_name = new_name
        try:
            self.df.rename(columns={self.old_name:self.new_name}, inplace= True)
        except Exception as e:
            print(f"Error has occured {e}")
            




 