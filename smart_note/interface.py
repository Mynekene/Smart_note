from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit,
    QListWidget, QLineEdit, QInputDialog, QMessageBox
)
from PyQt5.QtCore import Qt

app = QApplication([])
window = QWidget()
window.setFixedSize(1000, 620)
window.setWindowTitle("Smart Note")

create_note = QPushButton("Create Note")
save_note = QPushButton("Save Note")
delete_note = QPushButton("Delete Note")
create_tag = QPushButton("Create Tag")
delete_tag = QPushButton("Delete Tag")
search_tag = QPushButton("Search Tag")
label_note = QLabel("Note List")
label_tag = QLabel("Tag List")
note_list_widget = QListWidget()
tag_list_widget = QListWidget()
searching_tag_input = QInputDialog()
text_edit = QTextEdit()
text_edit.setDisabled(True)

layout1 = QHBoxLayout()
layout1.addWidget(create_note)
layout1.addWidget(save_note)

layout2 = QHBoxLayout()
layout2.addWidget(delete_note)
layout2.addWidget(create_tag)

panel_layout = QHBoxLayout()
panel_layout.addWidget(label_note)
panel_layout.addWidget(label_tag)
panel_layout.addWidget(note_list_widget)
panel_layout.addWidget(tag_list_widget)
panel_layout.addWidget(searching_tag_input)
panel_layout.addWidget(text_edit)
panel_layout.addWidget(delete_tag)
panel_layout.addWidget(search_tag)

main_layout = QVBoxLayout()
main_layout.addLayout(panel_layout)

window.show()
