class Options:
    def __init__(self, ui):
        self.input = self.__input(ui)
        self.output = self.__output(ui)
        self.sample_size = self.__sample_size(ui)
        self.dim_x1 = self.__dim_x1(ui)
        self.dim_x2 = self.__dim_x2(ui)
        self.dim_x3 = self.__dim_x3(ui)
        self.dim_y = self.__dim_y(ui)
        self.polynom = self.__polynom(ui)
        self.x1_degree = self.__x1_degree(ui)
        self.x2_degree = self.__x2_degree(ui)
        self.x3_degree = self.__x3_degree(ui)
        self.weights = self.__weights(ui)
        self.lambda_options = self.__lambda_options(ui)
        self.plot_normalized = self.__plot_normalized(ui)
        self.own_function = self.__own_function(ui)

    def __input(self, ui):
        _input = ui.input_file_txt.text()
        return _input

    def __output(self, ui):
        _output = ui.output_file_txt.text()
        return _output

    def __sample_size(self, ui):
        return ui.sample_size_button.value()

    def __dim_x1(self, ui):
        return ui.vector_x1_button.value()

    def __dim_x2(self, ui):
        return ui.vector_x2_button.value()

    def __dim_x3(self, ui):
        return ui.vector_x3_button.value()

    def __dim_y(self, ui):
        return ui.vector_y_button.value()

    def __polynom(self, ui):
        return ui.polynom_button.currentText()

    def __x1_degree(self, ui):
        return ui.x1_degree_button.value()

    def __x2_degree(self, ui):
        return ui.x2_degree_button.value()

    def __x3_degree(self, ui):
        return ui.x3_degree_button.value()

    def __weights(self, ui):
        return ui.weights_button.currentText()

    def __lambda_options(self, ui):
        return ui.lambda_from_three_systems_button.isChecked()

    def __what_y_plot(self, ui):
        return ui.what_y_plot.value()

    def __plot_normalized(self, ui):
        return ui.plot_nomalized_button.isChecked()

    def __own_function(self, ui):
        return ui.own_function_structure_button.isChecked()