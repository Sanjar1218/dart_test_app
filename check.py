from openpyxl import Workbook
import sys

def check():
    f = open("test.json", 'r')
    lst = []
    for i in f.readlines():
        if i.find(''':"success"''') != -1:
            lst.append(1)
        if i.find('''"failure"''') != -1:
            lst.append(0)
    lst.pop(0)
    return lst

def findFile():
    f = open("test.json", 'r')
    lst = []
    for i in f.readlines():
        b = i.find("url")
        e = i.find('''"type":"testStart"''')
        if b < e:
            file_name = i[b+6:e-8].split('/')[-1]
            lst.append(file_name)
    lst.pop(0)
    return lst


if __name__ == "__main__":
    wb = Workbook()

    ws = wb.active
    ws.append(["name",] + findFile())
    ws.append([sys.argv[1]] + check())

    wb.save("check.xlsx")