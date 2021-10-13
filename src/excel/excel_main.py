import openpyxl

if __name__ == '__main__':

    # ファイルをロード
    workbook = openpyxl.load_workbook("src/excel/data.xlsx")
    sheet = workbook["Sheet1"]

    i = 1
    while True:

        value = sheet.cell(row=i, column=1).value
        print(value)
        if value is None or len(value) == 0:
            break

        i = i + 1
