import xlrd
from library.config import Config

# loc_path = r"C:\Users\Vidyashree M C\PycharmProjects\pythonProject\demowebshop_locators.xlsx"
# testdata_path = r"C:\Users\Vidyashree M C\PycharmProjects\pythonProject\demoweb_testdata.xlsx"

#
def read_locators(sheetname):
    workbook = xlrd.open_workbook(Config.LOC_PATH)
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()
    header = next(rows)
    d = {}
    for row in rows:
        d[row[0].value] = (row[1].value, row[2].value)

    return d
print(read_locators('reg_objects'))

#
#
# def read_testdata(sheetname):
#     workbook = xlrd.open_workbook(Config.TESTDATA_PATH)
#     worksheet = workbook.sheet_by_name(sheetname)
#     rows = worksheet.get_rows()
#     n_cols = worksheet.ncols
#     header = next(rows)
#
#     data = []
#
#     for row in rows:
#         t = ()
#         for i in range(n_cols):     # range(6) --> 0
#             t += (row[i].value,)
#
#         data.append(t)
#
#     return data
#
