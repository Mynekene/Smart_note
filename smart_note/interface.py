from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit,
    QListWidget, QLineEdit, QInputDialog, QMessageBox
)
from PyQt5.QtCore import Qt

app = QApplication([])
window = QWidget()
window.setFixedSize(900, 700)
window.setWindowTitle("Smart Note")

create_note = QPushButton("Create Note")
save_note = QPushButton("Save Note")
delete_note = QPushButton("Delete Note")
create_tag = QPushButton("Create Tag")
delete_tag = QPushButton("Delete Tag")
search_tag = QPushButton("Search Tag")
label_note = QLabel("")
label_tag = QLabel("")
note_list_widget = QListWidget("")
tag_list_widget = QListWidget("")
searching_tag_input = QLineEdit("")
text_edit = QInputDialog("")

layout1 

layout2

panel_layout

main_layout

window.show()
app.exec_()