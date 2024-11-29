import numpy as np
from solve import Solve


def get_auto_degree(ui, x1_max=10, x2_max=10, x3_max=10):
    """Методом підбору визначає найбільш оптимальні степені поліномів за критерієм Чебишева."""
    min_degrees = np.ones(3).astype(int)
    min_error = get_max_error(ui, min_degrees)
    for x1_deg in np.arange(1, x1_max+1):
        for x2_deg in np.arange(1, x2_max+1):
            for x3_deg in np.arange(1, x3_max+1):
                degrees = np.array((x1_deg, x2_deg, x3_deg)).astype(int)
                current_error = get_max_error(ui, degrees)
                if current_error < min_error:
                    min_degrees = np.copy(degrees)
                    min_error = current_error
    return min_degrees


def get_max_error(ui, degrees):
    """Повертає максимальну похибку за критерієм Чебишева."""
    solver = Solve(ui, degrees)
    return np.max(solver.error_normalized)
