import pandas as pd
import datetime
x = datetime.datetime.now()

df =  pd.DataFrame({'Tên':    ["Trần Quốc Đạt","Lê Trần Minh Hiếu","Đỗ Nguyễn Ngọc Bích"],
                   'CPU': [ "80%","70%","90%"],
                   'RAM':["60%","50%","70%"],
                   "Thời Gian":[x,x,x]
})

writer = pd.ExcelWriter("pandas_datetime.xlsx",
                        engine='xlsxwriter',
                        datetime_format='mmm d yyyy hh:mm:ss',
                        date_format='mmmm dd yyyy')


df.to_excel(writer, sheet_name='Sheet1')

writer.save()
