import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

import cat  # Это наш конвертированный файл дизайна

class ExampleApp(QtWidgets.QMainWindow, cat.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.browse_img)  # Выполнить функцию browse_folder
                                                            # при нажатии кнопки

    def browse_img(self):
        image = QtWidgets.QFileDialog.getOpenFileName(None,'OpenFile','',"Image file(*.jpg)")
        if image:
            imagePath = image[0]
            pixmap = QPixmap(imagePath)
            self.label.setPixmap(pixmap)
            self.show()
        # открыть диалог выбора директории и установить значение переменной
    
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()