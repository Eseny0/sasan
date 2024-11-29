import numpy as np
from tabulate import tabulate

class Output:

    @staticmethod
    def _show_lambda(lambda_matrix, dim_y):
        header = ['Y1', 'Y2', 'Y3', 'Y4']
        out = f"Матриця λ для Y:\n"
        out += tabulate(lambda_matrix.T, header[:dim_y], floatfmt=('.4f',)*lambda_matrix.shape[0],
                        tablefmt="double_outline")
        out += "\n\n"
        return out

    @staticmethod
    def _show_psi(psi, dim_y):
        out = ""
        for i in np.arange(dim_y):
            out += f"Матриця ψ для Y{i+1}:\n"
            sub_psi = np.vstack(psi[i])
            out += tabulate(sub_psi.T, floatfmt=('.4f',)*sub_psi.shape[0], tablefmt="double_outline")
            out += "\n"
        return out

    @staticmethod
    def _show_a(a, dim_y):
        header = ['Y1', 'Y2', 'Y3', 'Y4']
        out = f"Матриця a для Y:\n"
        out += tabulate(a.T, header[:dim_y], floatfmt=('.4f',)*a.shape[0], tablefmt="double_outline")
        out += "\n\n"
        return out

    @staticmethod
    def _show_phi(phi, dim_y):
        out = ""
        for i in np.arange(dim_y):
            out += f"Матриця Ф для Y{i + 1}:\n"
            sub_phi = np.vstack(phi[i])
            out += tabulate(sub_phi.T, floatfmt=('.4f',)*phi.shape[0], tablefmt="double_outline")
            out += "\n"
        return out

    @staticmethod
    def _show_c(c, dim_y):
        header = ['Y1', 'Y2', 'Y3', 'Y4']
        out = f"Матриця c для Y:\n"
        out += tabulate(c.T, header[:dim_y], floatfmt=('.4f',)*c.shape[0], tablefmt="double_outline")
        out += "\n\n"
        return out

    @staticmethod
    def __get_coefficient(a, c, lambda_matrix, dim, degrees, i, j, p):
        """Повертає коефіцієнт при T{p}(x{i}{j})."""
        _dim = dim[:i - 1]
        _deg = degrees[:i - 1]  # + 1
        coefficient = c[i - 1]
        coefficient *= a[sum(_dim) + j - 1]
        coefficient *= lambda_matrix[np.sum(np.multiply(_dim, _deg)) + p]
        return coefficient

    @staticmethod
    def _show_error(error, error_normalized, dim_y):
        header = ['Y1', 'Y2', 'Y3', 'Y4']
        out = "\n\nНормалізовані помилки:\n"
        error_normalized = np.reshape(error_normalized, (-1, 1))
        out += tabulate(error_normalized.T, header[:dim_y], floatfmt=('.4f',)*dim_y, tablefmt="double_outline")
        out += '\n\n'
        out += "Відновлені помилки:\n"
        error = np.reshape(error, (-1, 1))
        out += tabulate(error.T, header[:dim_y], floatfmt=('.4f',)*dim_y, tablefmt="double_outline")
        out += "\n"
        return out

    @classmethod
    def _psi_dep(cls, lambda_matrix, dim, degrees, polynomial_type, dim_y):
        if polynomial_type == 'S-поліном':
            s = "S"
        elif polynomial_type == 'С-поліном':
            s = 'С'
        elif polynomial_type == 'U-поліном':
            s = 'U'
        else:
            s = 'O'

        out = f'Зележності від поліномів:'
        for p in range(dim_y):  # кількість Y
            counter = 0
            for i in range(dim[0]):  # цикл для розмірностей X1
                out += f'\n\nψ1{i+1}_{p + 1}(x1{i+1}) = '
                for j in range(degrees[0]+1):
                    out += '[1 + ' + s + f'{j}(x1{i+1})]^{lambda_matrix[p][counter].round(5)} x '
                    counter += 1
                out = out[:-2]
                out += '- 1'

            for i in range(dim[1]):  # цикл для розмірностей X2
                out += f'\n\nψ2{i+1}_{p + 1}(x2{i+1}) = '
                for j in range(degrees[1]+1):
                    out += '[1 + ' + s + f'{j}(x2{i+1})]^{lambda_matrix[p][counter].round(5)} x '
                    counter += 1
                out = out[:-2]
                out += '- 1'

            for i in range(dim[2]):  # цикл для розмірностей X3
                out += f'\n\nψ3{i+1}_{p + 1}(x3{i+1}) = '
                for j in range(degrees[2]+1):
                    out += '[1 + ' + s + f'{j}(x3{i+1})]^{lambda_matrix[p][counter].round(5)} x '
                    counter += 1
                out = out[:-2]
                out += '- 1'
        return out

    @classmethod
    def _phi_dep(cls, a, dim, dim_y):
        out = '\n\nЗалежності від ψ:'
        for p in range(dim_y):
            counter = 0
            for i in range(3):  # цикл кількість X
                out += f'\n\nФ{p+1}{i+1}(x{i+1}) = '
                for j in range(dim[i]):
                    out += f'(1 + ψ{i+1}{j+1})^{a[p][counter].round(5)} x '
                    counter += 1
                out = out[:-2]
                out += '- 1'
        return out

    @classmethod
    def _F_dep(cls, c, dim, dim_y):
        out = '\n\nЗалежності від Ф_ij:'
        for p in range(dim_y):
            counter = 0
            out += f'\n\nФ{p+1}(x1, x2, x3) = '
            for i in range(len(dim)):
                out += f'[Ф{p+1}{i+1}(x{i+1}) + 1]^{c[p][counter].round(5)} x '
                counter += 1
            out = out[:-2]
            out += '- 1'
        return out

    @classmethod
    def _show_special(cls, solver, dim_y):
        """Отримує i-тий номер стовпця y та функцію виводу out. Виводить всі дані для y{i}."""
        lambda_matrix = solver.lambda_matrix
        psi = solver.psi
        a = solver.a
        phi = solver.phi
        c = solver.c
        error = solver.error
        error_normalized = solver.error_normalized
        dim = np.array((solver.dim_x1, solver.dim_x2, solver.dim_x3))
        degrees = np.array((solver.x1_degree, solver.x2_degree, solver.x3_degree))
        polynomial_type = solver.polynom
        out = cls._show_lambda(lambda_matrix, dim_y)
        out += cls._show_psi(psi, dim_y)
        out += cls._show_a(a, dim_y)
        out += cls._show_phi(phi, dim_y)
        out += cls._show_c(c, dim_y)
        out += cls._psi_dep(lambda_matrix, dim, degrees, polynomial_type, dim_y)
        out += cls._phi_dep(a, dim, dim_y)
        out += cls._F_dep(c, dim, dim_y)
        out += cls._show_error(error, error_normalized, dim_y)
        return out

    @classmethod
    def show(cls, solver):
        """Виводить дані на TextBrowser та записує їх у текстовий файл."""
        out = ""
        for i in (solver.dim_y,):
            out += cls._show_special(solver, i)
            out += "\n\n\n"
        with open(solver.output, 'w', encoding='utf-16') as fileout:
            fileout.write(out)
        return out

