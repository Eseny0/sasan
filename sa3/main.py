#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from interface import Ui_MainWindow
from solve import Solve
from out import Output
from plot import Graph
from search_degree import get_auto_degree


class UI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.polynom_button.addItems(["U-поліном", "S-поліном", "C-поліном", 'O-поліном'])
        self.weights_button.addItems(["Середнє", "МаксМін"])
        self.input_file_button.clicked.connect(self.choose_input)
        self.output_file_button.clicked.connect(self.choose_output)
        self.dependencies_button.clicked.connect(self.execute)
        self.plot_button.clicked.connect(self.plot)
        self.calculate_optimal_degrees_button.clicked.connect(self.auto_degree)
        self.vector_x1_button.setValue(2)
        self.vector_x2_button.setValue(2)
        self.vector_x3_button.setValue(3)
        self.vector_y_button.setValue(4)
        self.sample_size_button.setValue(40)
        self.x1_degree_button.setValue(3)
        self.x2_degree_button.setValue(3)
        self.x3_degree_button.setValue(3)

    def choose_input(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open data file', '.', 'Data file (*.txt)')[0]
        self.input_file_txt.setText(filename)

    def choose_output(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open data file', '.', 'Data file (*.txt)')[0]
        self.output_file_txt.setText(filename)

    def execute(self):
        self.dependencies_button.setEnabled(False)
        solver = Solve(self)
        self.output_block.setText(Output.show(solver))
        self.dependencies_button.setEnabled(True)

    def plot(self):
        """Відмальовка графіка."""
        self.plot_button.setEnabled(False)
        plotter = Graph(self)
        plotter.plot_graph()
        self.plot_button.setEnabled(True)

    def auto_degree(self):
        """Оцінка оптимальних степенів полінома."""
        self.calculate_optimal_degrees_button.setEnabled(False)
        degrees = get_auto_degree(self)
        self.output_block.setText(
            f"Оптимальні степені поліномів:"
            f"\nX1: {degrees[0]}\nX2: {degrees[1]}\nX3: {degrees[2]}"
        )
        self.calculate_optimal_degrees_button.setEnabled(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = UI()
    MainWindow.show()

    sys.exit(app.exec_())
