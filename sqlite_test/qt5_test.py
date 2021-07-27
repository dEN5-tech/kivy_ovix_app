import sys
# Класс QUrl предоставляет удобный интерфейс для работы с Urls
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget
# Класс QQuickView предоставляет возможность отображать QML файлы.
from PyQt5.QtQuick import QQuickView
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# Объект QQuickView, в который грузится UI для отображения
app = QApplication([])
w = QLabel('Hello World!\n' * 10)
w.setFont(QFont('Arial', 40))
scroll_area = QScrollArea(target="flick_panel")
scroll_area.setWidget(w)
view = QQuickView()
view.setSource(QUrl('qt5_test_qml.qml'))
view.show()
app.exec_()