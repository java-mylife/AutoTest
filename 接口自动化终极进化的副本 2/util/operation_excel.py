# coding:utf-8
import xlrd
from xlutils.copy import copy


class OperationExcel:
    def __init__(self, file_name=None, sheet_id=None):  # 初始化构造函数，传了参数，调用类（类的实例化）的时候也要传递参数，这里不传默认为。。文件sheet 0
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = "../dataconfig/case1.xls"
            self.sheet_id = 0
        self.data = self.get_data()

        # 打开并获取sheet内容

    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables
        # 通过sheet内容，获取行数

    def get_lines(self):
        tables = self.data
        return tables.nrows

        # 获取某一单元格内容

    def get_cell_value(self, row, col):
        # a = {}
        # a = self.data.cell_value(row,col)
        # print type(a)
        return self.data.cell_value(row, col)

        # 写入数据

    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)  # 打开文件
        write_data = copy(read_data)  # 复制一份
        sheet_data = write_data.get_sheet(0)  # 打开 我复制文件的sheet 0 页
        sheet_data.write(row, col, value)  # 在 sheet 0页  写入数据
        write_data.save(self.file_name)  # 写完的数据 保存到源文件、因为写入的数据，不保留之前的内容需要保存到源文件结合在一起。

    def get_rows_data(self, case_id):  # 跟对应的caseid找到对应行的内容
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_values(row_num)
        return  row_data

    def get_row_num(self,case_id):          # 根据对应的caseid找到对应的行号
        num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            # num = num +1
            if case_id in col_data:
                return num
            num = num + 1


    def get_row_values(self, row):  # 根据行号找到行的内容
            tables = self.data
            row_data = tables.row_values(row)
            return row_data
    def get_cols_data(self,col_id=None):  #获取某一列的内容
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == "__main__":
    opers = OperationExcel("../dataconfig/case1.xls", 0)
    # print opers.get_cell_value(1,5)
    # print  opers.get_row_values(3)
    print opers.get_row_num("Imooc-04"),opers.get_row_values(4)
# data = xlrd.open_workbook('../dataconfig/case1.xls')
# tables = data.sheets()[0]
# print tables.nrows
# print tables.cell_value(1,5)
