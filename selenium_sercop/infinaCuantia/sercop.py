import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import infinaCuantia.constants as const
from infinaCuantia.report_sercop import SercopReport
import pandas as pd


class Sercop(webdriver.Chrome):
    def __init__(self, path_driver=r'C:\Projects\test\drivers\chromedriver.exe', teardown=False):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        service = Service(executable_path=path_driver)
        self.teardown = teardown
        super().__init__(service=service, options=chrome_options)
        os.environ['PATH'] += os.pathsep + path_driver

        self.maximize_window()
        self.implicitly_wait(8)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def get_url_sercop(self):
        self.get(const.BASE_URL)

    def next_page(self):
        next_button = self.find_element(By.ID, "table_id_next")
        next_button.click()

    # Data extraction
    def sercop_report(self):
        test=[]
        content_table=self.find_elements(By.CSS_SELECTOR, "tbody")
        report = SercopReport(content_table)
        data=report.pull_row()
        self._save_in_disk(data)

        print(data)

    def _save_in_disk(self, data):
        cols=['Tipo de Necesidad',	'Código Necesidad de Contratación',	'Fecha de Publicación',	'Provincia - Cantón',	'Descripción del Objeto de compra',	'Estado de la Necesidad',	'Fecha límite para la entrega de proformas',	'Entidad Contratante',	'Dirección de Entrega', 'Contacto']
        df=pd.DataFrame(data,columns=cols)
        return df.to_csv('database/data.csv')