from Word_List import WordList
import Gui
import Path
A = WordList("words.txt", "extra_words.txt")


print(A.all_word_lists[0])

def create_pic_list(word_list):
    pic_list = []
    for i in word_list:
        pic_list.append('Pics/{}.jpg'.format(i))
    return pic_list


delay = 5000
image_files = create_pic_list(A.all_word_lists[0])
app = Gui.App(image_files, delay)
app.show_slides()
app.run()