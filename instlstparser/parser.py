'''
Created on Sep 26, 2022

@author: bevrard
'''
import openpyxl as xlsx
import os

class parser(object):

    def __init__(self, path):
        '''
        Constructor
        '''
        self.xlsxpath=path
        self.wb = xlsx.load_workbook(self.xlsxpath)
        
        
    def parse(self):
        pass
        
        

if __name__=="__main__":
    print(os.getcwd())
    wb=xlsx.load_workbook("./VHC_INSTR_LIST_9-8.xlsx")
    print(wb.get_sheet_names())
    
        