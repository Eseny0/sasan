from scipy import special
import numpy as np
from numpy.polynomial import Polynomial as pm

class Polynomial:
    def __init__(self, polynomial_type):
        # Обираємо поліном для розрахунку коефіцієнтів згідно з налаштуваннями.
        if polynomial_type == "U-поліном":
            self._get_coefficients = lambda n: np.array(self.u_poly(n))
        elif polynomial_type == "S-поліном":
            self._get_coefficients = lambda n: np.array(self.s_poly(n))
        elif polynomial_type == "C-поліном":
            self._get_coefficients = lambda n: np.array(self.c_poly(n))
        elif polynomial_type == "O-поліном":
            self._get_coefficients = lambda n: np.array(self.own_poly(n))
        else:
            exit("Polynomial type is not defined!")

    def get_polynomial_sum_coefficients(self, degree, polynomial_multiplier=None):
        """Повертає коефіцієнти суми полиномів степенів від 0 до degree включно."""
        if polynomial_multiplier is None:
            polynomial_multiplier = np.ones(degree+1)
        polynomial_sum_coefficients = np.zeros(degree+1)
        for deg in np.arange(degree+1):
            # Обраховуємо коефіцієнти полиному потрібного степеню.
            polynomial = self._get_coefficients(deg) * polynomial_multiplier[deg]
            # Сумуємо коефіцієнты полінома потрібного степеню з коефіцієнтами попередніх поліномів.
            for position in np.arange(1, deg+2):
                polynomial_sum_coefficients[-position] += polynomial[-position]
        return np.flipud(polynomial_sum_coefficients)

    @staticmethod
    def u_poly(self, n):
        basis = [pm([1])]
        for i in range(n):
            if i == 0:
                basis.append(pm([0, 2]))
                continue
            basis.append(pm([0, 2]) * basis[-1] - basis[-2])
        return basis[-1].coef[::-1]

    @staticmethod
    def s_poly(self, n):
        basis = [pm([1])]
        for i in range(n):
            if i == 0:
                basis.append(pm([0, 1]))
                continue
            basis.append(pm([0, 1]) * basis[-1] - basis[-2])
        return basis[-1].coef[::-1]

    @staticmethod
    def c_poly(self, n):
        basis = [pm([2])]
        for i in range(n):
            if i == 0:
                basis.append(pm([0,1]))
                continue
            basis.append(pm([0, 1]) * basis[-1] - basis[-2])
        return basis[-1].coef[::-1]

    @staticmethod
    def own_poly(self, n):
        basis = [pm([1])]
        for i in range(n):
            if i == 0:
                basis.append(pm([-1, 0, 1]))
                continue
            basis.append(pm([-1, 0, 1]) * basis[-1] - basis[-2])
        return basis[-1].coef[::-1]