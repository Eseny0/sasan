import matplotlib.pyplot as plt
import numpy as np
from solve import Solve


class Graph:
    def __init__(self, ui):
        solver = Solve(ui)
        self.plot_normalized = self._is_normalized(solver.plot_normalized)
        self.estimate = self._get_estimate(solver)
        self.error = self._get_error(solver)
        self.y = self._get_y(solver)
        self.sample_size = solver.sample_size

    @staticmethod
    def _get_y(solver):
        if solver.plot_normalized:
            return solver.y_normalized
        else:
            return solver.y

    @staticmethod
    def _is_normalized(plot_normalized):
        """Повертає True, якщо потрібно зробити нормалізований графік."""
        return plot_normalized

    def _get_estimate(self, solver):
        """Повертає стовпець наближень у в залежності від налаштувань."""
        if self.plot_normalized:
            return solver.estimate_normalized
        else:
            return solver.estimate
            
    def _get_error(self, solver):
        """Повертає похибку (нормалізовану чи звичайну)."""
        if self.plot_normalized:
            return solver.error_normalized
        else:
            return solver.error

    def plot_graph(self):
        samples = np.arange(1, self.sample_size+1)
        number_of_graphs = self.error.size
        fig, axes = plt.subplots(2, number_of_graphs, squeeze=False)
        for i in np.arange(number_of_graphs):
            axes[0][i].plot(samples, self.y[i], label=f'Y{i+1}', color='#006400')
            axes[0][i].plot(samples, self.estimate[i], linestyle='dashed', label=f'Ф{i+1}', color='#FF6347')
            axes[0][i].set_title(f"Похибка: {self.error[i].round(4)}")
            axes[0][i].legend()
            axes[0][i].grid()
            axes[1][i].plot(samples, np.abs(self.y[i] - self.estimate[i]), label='Похибка', color='#FF4500')
            axes[1][i].legend()
            axes[1][i].grid()
        fig.show()
