from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)  # розмір вікна
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1300, 782))
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet("background-color: rgb(187, 187, 189);")  # фон

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.input_block = QtWidgets.QGroupBox(self.centralwidget)  # блок вводу даних
        self.input_block.setGeometry(QtCore.QRect(20, 10, 1160, 225))
        self.input_block.setObjectName("input_block")

        self.buttons_block = QtWidgets.QGroupBox(self.centralwidget)  # блок кнопок
        self.buttons_block.setGeometry(QtCore.QRect(20, 240, 1160, 50))
        self.buttons_block.setObjectName("buttons_block")

        self.output_block = QtWidgets.QTextBrowser(self.centralwidget)  # блок виводу
        self.output_block.setFont(QFont('Courier New', 14))
        self.output_block.setGeometry(QtCore.QRect(20, 300, 1160, 370))
        self.output_block.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.output_block.setObjectName("output_block")

        self.input_file_txt = QtWidgets.QLineEdit(self.input_block)  # вхідний файл
        self.input_file_txt.setGeometry(QtCore.QRect(300, 10, 200, 22))
        self.input_file_txt.setDragEnabled(False)
        self.input_file_txt.setObjectName("input_file_txt")

        self.input_file_button = QtWidgets.QToolButton(self.input_block)  # кнопка вхідний файл
        self.input_file_button.setGeometry(QtCore.QRect(510, 10, 45, 22))
        self.input_file_button.setStyleSheet("background-color: rgb(138, 138, 138);")
        self.input_file_button.setObjectName("input_file_button")

        self.output_file_txt = QtWidgets.QLineEdit(self.input_block)  # вихідний файл
        self.output_file_txt.setGeometry(QtCore.QRect(645, 10, 200, 22))
        self.output_file_txt.setObjectName("output_file_txt")

        self.output_file_button = QtWidgets.QToolButton(self.input_block)  # кнопка вихідний файл
        self.output_file_button.setGeometry(QtCore.QRect(855, 10, 45, 22))
        self.output_file_button.setStyleSheet("background-color: rgb(138, 138, 138);")
        self.output_file_button.setObjectName("output_file_button")

        self.sample_size_txt = QtWidgets.QLabel(self.input_block)  # текст розмір вибірки
        self.sample_size_txt.setGeometry(QtCore.QRect(100, 40, 115, 22))
        self.sample_size_txt.setObjectName("sample_size_txt")

        self.sample_size_button = QtWidgets.QSpinBox(self.input_block)  # кнопка розмір вибірки
        self.sample_size_button.setAlignment(QtCore.Qt.AlignCenter)
        self.sample_size_button.setGeometry(QtCore.QRect(225, 40, 40, 22))
        self.sample_size_button.setMouseTracking(False)
        self.sample_size_button.setMinimum(1)
        self.sample_size_button.setMaximum(100)
        self.sample_size_button.setObjectName("sample_size_button")

        self.vectors_size_txt = QtWidgets.QLabel(self.input_block)  # текст розмірності векторів
        self.vectors_size_txt.setGeometry(QtCore.QRect(65, 70, 150, 22))
        self.vectors_size_txt.setObjectName("vectors_size_txt")

        self.vector_x1_txt = QtWidgets.QLabel(self.input_block)
        self.vector_x1_txt.setGeometry(QtCore.QRect(225, 70, 35, 22))
        self.vector_x1_txt.setObjectName("vector_x1_txt")

        self.vector_x1_button = QtWidgets.QSpinBox(self.input_block)
        self.vector_x1_button.setAlignment(QtCore.Qt.AlignCenter)
        self.vector_x1_button.setGeometry(QtCore.QRect(265, 70, 40, 22))
        self.vector_x1_button.setMouseTracking(False)
        self.vector_x1_button.setMinimum(1)
        self.vector_x1_button.setObjectName("vector_x1_button")

        self.vector_x2_txt = QtWidgets.QLabel(self.input_block)
        self.vector_x2_txt.setGeometry(QtCore.QRect(335, 70, 35, 22))
        self.vector_x2_txt.setObjectName("vector_x2_txt")

        self.vector_x2_button = QtWidgets.QSpinBox(self.input_block)
        self.vector_x2_button.setAlignment(QtCore.Qt.AlignCenter)
        self.vector_x2_button.setGeometry(QtCore.QRect(375, 70, 40, 22))
        self.vector_x2_button.setMinimum(1)
        self.vector_x2_button.setObjectName("vector_x2_button")

        self.vector_x3_txt = QtWidgets.QLabel(self.input_block)
        self.vector_x3_txt.setGeometry(QtCore.QRect(445, 70, 35, 22))
        self.vector_x3_txt.setObjectName("vector_x3_txt")

        self.vector_x3_button = QtWidgets.QSpinBox(self.input_block)
        self.vector_x3_button.setAlignment(QtCore.Qt.AlignCenter)
        self.vector_x3_button.setGeometry(QtCore.QRect(485, 70, 40, 22))
        self.vector_x3_button.setMinimum(1)
        self.vector_x3_button.setObjectName("vector_x3_button")

        self.vector_y_txt = QtWidgets.QLabel(self.input_block)
        self.vector_y_txt.setGeometry(QtCore.QRect(555, 70, 30, 22))
        self.vector_y_txt.setObjectName("vector_y_txt")

        self.vector_y_button = QtWidgets.QSpinBox(self.input_block)
        self.vector_y_button.setAlignment(QtCore.Qt.AlignCenter)
        self.vector_y_button.setGeometry(QtCore.QRect(590, 70, 40, 22))
        self.vector_y_button.setMinimum(1)
        self.vector_y_button.setObjectName("vector_y_button")

        self.polynom_txt = QtWidgets.QLabel(self.input_block)  # текст тип полінома
        self.polynom_txt.setGeometry(QtCore.QRect(110, 100, 105, 22))
        self.polynom_txt.setObjectName("polynom_txt")

        self.polynom_button = QtWidgets.QComboBox(self.input_block)  # кнопка тип полінома
        self.polynom_button.setGeometry(QtCore.QRect(225, 100, 120, 22))
        self.polynom_button.setObjectName("polynom_button")

        self.polynoms_degrees_txt = QtWidgets.QLabel(self.input_block)  # текст степені поліномів
        self.polynoms_degrees_txt.setGeometry(QtCore.QRect(85, 130, 130, 22))
        self.polynoms_degrees_txt.setObjectName("polynoms_degrees_txt")

        self.polynom_degree_x1_txt = QtWidgets.QLabel(self.input_block)  # текст степінь полінома х1
        self.polynom_degree_x1_txt.setGeometry(QtCore.QRect(225, 130, 35, 22))
        self.polynom_degree_x1_txt.setObjectName("polynom_degree_x1_text_2")

        self.x1_degree_button = QtWidgets.QSpinBox(self.input_block)  # кнопка степінь полінома х1
        self.x1_degree_button.setAlignment(QtCore.Qt.AlignCenter)
        self.x1_degree_button.setGeometry(QtCore.QRect(265, 130, 40, 22))
        self.x1_degree_button.setMouseTracking(False)
        self.x1_degree_button.setMinimum(1)
        self.x1_degree_button.setObjectName("x1_degree_button")

        self.polynom_degree_x2_txt = QtWidgets.QLabel(self.input_block)  # текст степінь полінома х2
        self.polynom_degree_x2_txt.setGeometry(QtCore.QRect(335, 130, 35, 22))
        self.polynom_degree_x2_txt.setObjectName("polynom_degree_x1_txt")

        self.x2_degree_button = QtWidgets.QSpinBox(self.input_block)  # кнопка степінь полінома х2
        self.x2_degree_button.setAlignment(QtCore.Qt.AlignCenter)
        self.x2_degree_button.setGeometry(QtCore.QRect(375, 130, 40, 22))
        self.x2_degree_button.setMinimum(1)
        self.x2_degree_button.setObjectName("x2_degree_button")

        self.polynom_degree_x3_txt = QtWidgets.QLabel(self.input_block)  # текст степінь полінома х3
        self.polynom_degree_x3_txt.setGeometry(QtCore.QRect(445, 130, 35, 22))
        self.polynom_degree_x3_txt.setObjectName("polynom_degree_x3_txt")

        self.x3_degree_button = QtWidgets.QSpinBox(self.input_block)  # кнопка степінь полінома х3
        self.x3_degree_button.setAlignment(QtCore.Qt.AlignCenter)
        self.x3_degree_button.setGeometry(QtCore.QRect(485, 130, 40, 22))
        self.x3_degree_button.setMinimum(1)
        self.x3_degree_button.setObjectName("x3_degree_button")

        self.weights_txt = QtWidgets.QLabel(self.input_block)  # текст ваги цільових функцій
        self.weights_txt.setGeometry(QtCore.QRect(55, 160, 160, 22))
        self.weights_txt.setObjectName("weights_txt")

        self.weights_button = QtWidgets.QComboBox(self.input_block)  # кнопка ваги цільових функцій
        self.weights_button.setGeometry(QtCore.QRect(225, 160, 120, 22))
        self.weights_button.setObjectName("weights_button")

        self.lambda_from_three_systems_button = QtWidgets.QCheckBox(self.input_block)  # кнопка лямбда з 3-х систем
        self.lambda_from_three_systems_button.setGeometry(QtCore.QRect(225, 190, 300, 22))
        self.lambda_from_three_systems_button.setObjectName("lambda_from_three_systems_button")

        self.plot_nomalized_button = QtWidgets.QCheckBox(self.input_block)  # кнопка нормалізований графік
        self.plot_nomalized_button.setGeometry(QtCore.QRect(580, 190, 170, 22))
        self.plot_nomalized_button.setObjectName("plot_nomalized_button")

        self.own_function_structure_button = QtWidgets.QCheckBox(self.input_block)  # кнопка власна структура
        self.own_function_structure_button.setGeometry(QtCore.QRect(805, 190, 280, 22))
        self.own_function_structure_button.setObjectName("own_function_structure_button")

        self.calculate_optimal_degrees_button = QtWidgets.QPushButton(self.buttons_block)
        self.calculate_optimal_degrees_button.setGeometry(QtCore.QRect(150, 10, 300, 25))
        self.calculate_optimal_degrees_button.setStyleSheet("background-color: rgb(138, 138, 138);")
        self.calculate_optimal_degrees_button.setObjectName("calculate_optimal_degrees_button")

        self.dependencies_button = QtWidgets.QPushButton(self.buttons_block)  # кнопка відновити функ залежності
        self.dependencies_button.setGeometry(QtCore.QRect(500, 10, 300, 25))
        self.dependencies_button.setStyleSheet("background-color: rgb(138, 138, 138);")
        self.dependencies_button.setObjectName("dependencies_button")

        self.plot_button = QtWidgets.QPushButton(self.buttons_block)  # кнопка графіка
        self.plot_button.setGeometry(QtCore.QRect(850, 10, 200, 25))
        self.plot_button.setStyleSheet("background-color: rgb(138, 138, 138);")
        self.plot_button.setObjectName("plot_button")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ЛР №3 СА"))
        self.lambda_from_three_systems_button.setText(_translate("MainWindow", "Визначити лямбда з трьох систем рівнянь"))
        self.plot_nomalized_button.setText(_translate("MainWindow", "Нормалізувати графік"))
        self.weights_txt.setText(_translate("MainWindow", "  Ваги цільових функцій:  "))
        self.plot_button.setText(_translate("MainWindow", "Побудувати графік"))
        self.input_file_button.setText(_translate("MainWindow", "Обрати"))
        self.output_file_button.setText(_translate("MainWindow", "Обрати"))
        self.input_file_txt.setPlaceholderText(_translate("MainWindow", "Вхідний файл"))
        self.input_file_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.output_file_txt.setPlaceholderText(_translate("MainWindow", "Вихідний файл"))
        self.output_file_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.sample_size_txt.setText(_translate("MainWindow", "  Розмір вибірки:  "))
        self.vector_x2_txt.setText(_translate("MainWindow", "  Х2:  "))
        self.vector_x3_txt.setText(_translate("MainWindow", "  Х3:  "))
        self.vector_x1_txt.setText(_translate("MainWindow", "  Х1:  "))
        self.vector_y_txt.setText(_translate("MainWindow", "  Y:  "))
        self.vectors_size_txt.setText(_translate("MainWindow", "  Розмірності векторів:  "))
        self.dependencies_button.setText(_translate("MainWindow", "Відновити функціональні залежності"))
        self.polynom_txt.setText(_translate("MainWindow", "  Тип полінома:  "))
        self.polynom_degree_x1_txt.setText(_translate("MainWindow", "  Х1:  "))
        self.polynom_degree_x2_txt.setText(_translate("MainWindow", "  Х2:  "))
        self.polynoms_degrees_txt.setText(_translate("MainWindow", "  Степені поліномів:  "))
        self.polynom_degree_x3_txt.setText(_translate("MainWindow", "  Х3:  "))
        self.calculate_optimal_degrees_button.setText(_translate("MainWindow", "Обрахувати оптимальні степені поліномів"))
        self.own_function_structure_button.setText(_translate("MainWindow", "Використати власну структуру функцій"))