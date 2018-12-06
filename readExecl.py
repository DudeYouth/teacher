import xlrd
import xlwt
import json
def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'./map.xls')

    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_index(0) # sheet索引从0开始
    data = {}
    # sheet的名称，行数，列数
    # sheet2.nrows,sheet2.ncols
    i = 1
    while i < sheet2.nrows:
        key = sheet2.cell(i,0).value+','+sheet2.cell(i,1).value
        value = sheet2.cell(i,4).value+','+sheet2.cell(i,5).value
        data[key] = value
        i+=1
    strs = json.dumps(data)
    f = open (r'./data.json','w')
    print (strs,file = f)
read_excel()
