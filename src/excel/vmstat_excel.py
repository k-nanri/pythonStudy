import openpyxl

if __name__ == '__main__':

    # Excelファイルを新規作成
    wb = openpyxl.Workbook()
    # シート取得
    ws = wb.worksheets[0]

    with open("./src/excel/vmstat.log") as f:
        row = 1
        for line in f:
            lines = line.split(",")
            column = 1
            for item in lines:
                ws.cell(row, column).value = item.strip()
                column += 1
            
            row += 1

    # 保存
    wb.save("./src/excel/VmStat.xlsx")
