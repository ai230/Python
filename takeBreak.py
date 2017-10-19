import webbrowser
import time

break_count = 0
total_break = 3

print("This program start on ", time.ctime())
while( break_count < total_break ):
    time.sleep(5)
    webbrowser.open("https://www.google.ca/")
    break_count = break_count + 1
