# Logic report and data collection
import pandas
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class SercopReport:
    def __init__(self, table_content_page:WebElement):
        self.table_content_page=table_content_page
        self.table_row=self.pull_table()


    def pull_table(self):
        tr = []
        for row in self.table_content_page:
            content = row.find_elements(By.TAG_NAME, 'tr')
            for x in content:
                tr.append(x.find_elements(By.TAG_NAME,'td'))

        return tr


    
    def pull_row(self):
        data=[]

        for i in range(len(self.table_row)):
            data.append([x.text for x in self.table_row[i]])
        return data