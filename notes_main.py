#начни тут создавать приложение с умными заметками
from PyQt5.QtWidgets import QInputDialog ,QLabel, QApplication, QWidget, QHBoxLayout, QTextEdit, QVBoxLayout, QPushButton,QLineEdit,QListWidget
from PyQt5.QtCore import Qt
import json

def del_note():
	if lis.selectedItems():
		key = lis.selectedItems()[0].text()
		del notes[key]
		lis.clear()
		lis.addItems(notes)
		text.clear()
		lis1.clear()
		with open('notes_data.json','w') as file:
			json.dump(notes,file,
			sort_keys=True,
			ensure_ascii=False)


def show_note():
	key = lis.selectedItems()[0].text()
	text.setText(notes[key]['текст'])
	lis1.clear()
	lis1.addItems(notes[key]['теги'])

def add_note():
	notes_name, result = QInputDialog.getText(

		window, ' Добавление заметок','Название:'
	)
	if result:
		notes[notes_name]= {
			'текст': '',
			'теги': []
		}
		lis.addItem(notes_name)
		with open('notes_data.json','w') as file:
			json.dump(notes,file,
			sort_keys=True,
			ensure_ascii=False)

def save_note():
	if lis.selectedItems():
		key = lis.selectedItems()[0].text()
		notes[key]['текст'] = text.toPlainText()
		with open('notes_data.json','w') as file:
			json.dump(notes,file,
			sort_keys=True,
			ensure_ascii=False)

def add_tag():
	if lis.selectedItems():
		key = lis.selectedItems()[0].text()
		tag = lab.text()
		if tag != '' and not tag in notes[key]['теги']:
			notes[key]['теги'].append(tag)
			lis1.addItem(tag)
			lab.clear()
			with open('notes_data.json','w') as file:
				json.dump(notes,file,
				sort_keys=True,
				ensure_ascii=False)
	

def del_tag():
	if lis1.selectedItems():
		key = lis.selectedItems()[0].text()
		tag = lis1.selectedItems()[0].text()
		notes[key]['теги'].remove(tag)
		lis1.clear()
		lis1.addItems(notes[key]['теги'])
		with open('notes_data.json','w') as file:
				json.dump(notes,file,
				sort_keys=True,
				ensure_ascii=False)
	
def search_tag():
	tag = lab.text()
	if tag and but.text() == 'Искать заметки по тегу':
		notes_filtered = dict()
		for key in notes:
			if tag in notes[key]['теги']:
				notes_filtered[key] = notes[key]
		but.setText('Сбросить поиск')
		lis.clear()
		lis1.clear()
		text.clear()
		lis1.addItems(notes_filtered)
	else:
		lab.clear()
		but.setText('Искать заметки по тегу')
		lis1.clear()
		lis1.addItems(notes)


app = QApplication([])
window = QWidget()
v_line = QVBoxLayout()
v_line1 = QVBoxLayout()

h_line = QHBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()

text = QTextEdit()
lis = QListWidget()
lis1 = QListWidget()
label = QLabel('Список заметок')
label1 = QLabel('Список тегов')
lab = QLineEdit()
lab.setPlaceholderText('Введите текст')
but = QPushButton('Искать заметки по тегу')
but1 = QPushButton('Создать заметку')
but2 = QPushButton('Удалить заметку')
but3 = QPushButton('Сохранить заметку')
but4 = QPushButton('Добавить к заметке')
but5 = QPushButton('Открепить от заметки')

v_line.addWidget(text)
v_line1.addWidget(label)
v_line1.addWidget(lis)
h_line.addWidget(but1)
h_line.addWidget(but2)
v_line1.addLayout(h_line)
v_line1.addWidget(but3)
v_line1.addWidget(label1)
v_line1.addWidget(lis1)
v_line1.addWidget(lab)
h_line1.addWidget(but4)
h_line1.addWidget(but5)
v_line1.addLayout(h_line1)
v_line1.addWidget(but)
h_line2.addLayout(v_line)
h_line2.addLayout(v_line1)
window.setLayout(h_line2)

with open ('notes_data.json','r') as file:
	notes = json.load(file)


lis.addItems(notes)
lis.itemClicked.connect(show_note)
but.clicked.connect(search_tag)
but1.clicked.connect(add_note)
but2.clicked.connect(del_note)
but3.clicked.connect(save_note)
but4.clicked.connect(add_tag)
but5.clicked.connect(del_tag)
window.show()
app.exec_()
