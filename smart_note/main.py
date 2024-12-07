from interface import *
from create_json import *
name_file = "data.json"

try:
    data = read_json(name_file)
except:
    data = dict()

def error(txt):
    ms = QMessageBox()
    ms.setText(txt)
    ms.exec_()

def show_note():
    note_list_widget.addItems(list(data.keys()))
def show_tag(name_note):
    tag_list_widget.clear()
    tag_list_widget.addItems(data[name_note]["TAG"])

def add_note():
    name_note = QInputDialog().getText(QInputDialog, "Назва нотатку", "Введіть назву")[0]
    data[name_note] = {"TEXT":  "","TAG": []}
    write_json(name_file, data)
    note_list_widget.addItem(name_note)

def save_file():
    try:
        name_note = note_list_widget.currentItem().text()
        data[name_note]["TEXT"] = text_edit.toPlainText()
        write_json(name_file, data)
    except:
        error("Щоб зберегти, спочатку оберіть нотаток")

def remove_note():
    try:
        name_note = note_list_widget.currentItem().text()
        del data[name_note]
        write_json(name_file, data)
        note_list_widget.clear()
        show_note()
        text_edit.setPlainText("")
        text_edit.setDisabled(True)
    except:
        error("Щоб видалити, спочатку оберіть нотаток")

def add_tag():
    try:
        name_note = note_list_widget.currentItem().text()
        name_tag = QInputDialog().getText(QInputDialog(), "Введення тега", "Введіть назву тега")[0]
        data[name_note][name_tag].append(name_tag)
        write_json(name_note, data)
        tag_list_widget.addItem(name_tag)
    except:
        error("Щоб створити тег, спочатку оберіть нотаток")
    
def remove_tag():
    try:
        name_note = note_list_widget.currentItem().text()
        name_tag = tag_list_widget.currentItem().text()
        data[name_note][name_tag].append(name_tag)
        write_json(name_note, data)
        show_tag(name_file)
    except:
        error("Щоб видалити тег, спочатку оберіть нотаток")


def show_text():
    text_edit.setDisabled(False)
    name_note = note_list_widget.currentItem().text()
    text_edit

app.exec_()
