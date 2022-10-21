import openpyxl


def read_excel(fileName):
    wb = openpyxl.load_workbook(fileName)
    wsheet = wb.active
    yield from wsheet.iter_rows(values_only=True)