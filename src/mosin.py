import tkinter as tk
from tkinter import *

from src.alibaba_search import search_info
from src.excel_handle import export_excel


def search():
    if seed_entry.get() is None:
        return
    export_excel(search_info(seed_entry.get()), seed_entry.get())


window = tk.Tk()
window.title('Mosin-nagam')
window.resizable(width=False, height=False)
window.geometry('900x80')



# 创建frame
frm_right = tk.Frame(window, height=880, width=1200)
frm_right.pack(side='left')

# *********************右半部分********************************
frm_right_top = tk.Frame(frm_right, height=60, width=1200, bg='white')
frm_right_top.pack(side='top')

frm_right_line = tk.Frame(frm_right, height=5, width=1200,)
frm_right_line.pack(side='top')


# frm_right_top label,text 等内容
frm_right_top_left = tk.Frame(frm_right_top, height=60, width=800, bg='white')
frm_right_top_left.place(x=1, y=1)

label1 = tk.Label(frm_right_top_left, text="搜索内容：", bg='white', font=("Helvetical", 10))
label1.place(x=10, y=15)


# 添加提示信息
e = StringVar()
e.set("请输入搜索引子")
global seed_entry
seed_entry = tk.Entry(frm_right_top_left, width=1200, textvariable=e, bg='LightYellow')
seed_entry.place(x=110, y=17)

savebtn = tk.Button(frm_right_top, text='查   询', bg='LightYellow', border=2, command=search)
savebtn.place(x=850, y=15)




window.mainloop()










