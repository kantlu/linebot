
import tkinter as tk
import datetime
import subprocess                   # 可執行Linux command

root = tk.Tk()                      # 建立視窗物件
root.title('Novio.studio')          # 設定視窗標題
root.configure(background='#000')   # 設定背景色黑色
# 定義視窗的尺寸和位置
width = 960                         #是衝大小
height = 350
left = 40                           #視窗位置
top = 5
root.geometry(f'{width}x{height}+{left}+{top}')
# 設定所在時區 ( 台灣是 GMT+8 )
GMT = datetime.timezone(datetime.timedelta(hours=8))

# 在Python執行Linux指令
def PlaySound():
    subprocess.Popen(['mpg321', '-q', '/home/admin/buco.mp3']).wait()
#PlaySound()
    
# 在Python執行Linux指令
def Clock_HH():
    subprocess.Popen(['mpg321', '-q', '/home/admin/clock-alarm.mp3']).wait()
#Clock_HH()

# Mapping of the week day
#weekDaysMapping = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
weekDaysMapping = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
Date_Today = tk.StringVar()             # 建立文字變數，日期
Time_Now = tk.StringVar()               # 建立文字變數，時間
Today_week = tk.StringVar()             # 建立文字變數，星期
clock_h = int(datetime.datetime.now(tz=GMT).strftime('%M')) + 1 #以分鐘測試 %M

# 建立不斷改變文字變數的函式
def ShowTime():
    # Get today's date
    Date_a=datetime.datetime.now(tz=GMT).strftime("%Y-%m-%d")   #now(tz=GMT)
    # 取得目前的時間，格式使用 H:M:S
    Time_b = datetime.datetime.now(tz=GMT).strftime("%I:%M:%S  %p")  #now(tz=GMT)，strftime("%H:%M:%S")
    # 取得目前的星期0~6
    Week_c = datetime.datetime.today()
    # specified weekday and date time value
    dayOfTheWeek = weekDaysMapping[Week_c.weekday()]
    # 取得目前的時間秒數
    ss=datetime.datetime.now(tz=GMT).strftime('%S') 
    # 取得目前的時間小時
    hh=datetime.datetime.now(tz=GMT).strftime('%M') 
    
    Date_Today.set(Date_a)                  # 設定變數內容
    Time_Now.set(Time_b)                    # 設定變數內容
    Today_week.set(str(dayOfTheWeek))       # 設定變數內容
    root.after(1000, ShowTime)              # 視窗每隔 1000 毫秒再次執行一次 showTime()

    # 鬧鐘
    if str(Time_b) == "06:00:00  AM" and str(ss) == "00":
        PlaySound()
    
    # 整點報時
    global clock_h
    if str(hh) == str('{0:02d}'.format(clock_h)) and str(ss) == "00":
        Clock_HH()
        print(str('{0:02d}'.format(clock_h)) + "Playsound" )
        clock_h += 1
        if clock_h > 22 and clock_h < 6:
            clock_h = 7
    
#tk.Label(root, text='目前時間', font=('Arial',20)).pack()   # 放入第1個 Label 標籤
tk.Label(root, textvariable=Date_Today, font=('Arial',70), fg='#ffffff' ,background='black').pack()     # 放入第2個 Label 標籤，fg='#00ff00' navy
tk.Label(root, textvariable=Time_Now, font=('Arial',100), fg='#ffffff',background='black').pack()       # 放入第3個 Label 標籤，fg='#0000ff' blue
tk.Label(root, textvariable=Today_week , font=('Arial',45), fg='#ffff00',background='black').pack()     # 放入第4個 Label 標籤

ShowTime()         
root.mainloop()     # 自動刷新視窗畫面
