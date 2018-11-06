import Get_Data
from appJar import gui

newList = Get_Data.coin_list


def press(btn):
    if btn == "Continue":
        result = app.getListBox("list1")
        print(result)
    else:
        app.stop()


app=gui()
app.setFont(20)
app.addListBox("list1", newList)
app.setListBoxMulti("list1", multi=True)
app.addButton("Continue",  press)
app.addButton("Exit", press)
app.go()