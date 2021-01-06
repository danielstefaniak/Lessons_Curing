from sympy import *


def make_matrix(base_symbol):
    m_empty = [[0]*3]*3
    base_idx = ["-1", "", "+1"]
    out_matrix = Matrix(m_empty)
    for ii in range(3):
        for jj in range(3):
            x_idx = "i" + base_idx[ii]
            y_idx = "j" + base_idx[jj]
            idx = "_{%s;%s}" % (x_idx, y_idx)
            _s = symbols(base_symbol + idx)
            out_matrix[ii, jj] = _s
    return out_matrix


def make_matrix_interpoints(base_symbol):
    m_empty = [[0]*2]*2
    base_idx = [r"-\frac{1}{2}", r"+\frac{1}{2}"]
    out_matrix = Matrix(m_empty)
    for ii in range(2):
        for jj in range(2):
            x_idx = "i" + base_idx[ii]
            y_idx = "j" + base_idx[jj]
            idx = "_{%s;%s}" % (x_idx, y_idx)
            _s = symbols(base_symbol + idx)
            out_matrix[ii, jj] = _s
    return out_matrix


def make_discrete_matrix(base_symbol, Nx, Ny):
    m_empty = [[0]*Ny]*Nx
    out_matrix = Matrix(m_empty)
    for ii in range(Nx):
        for jj in range(Ny):
            idx = "_{%d;%d}" % (ii, jj)
            #idx = "_{%d}" % (ii + jj*Nx)
            #idx = "_{%d+%dN_x=%d}" % (ii, jj, ii + jj*Nx)
            _s = symbols(base_symbol + idx)
            out_matrix[ii, jj] = _s
    return out_matrix


def matrix_2_1dlist(m):
    size = 1
    for _dim in m.shape:
        size *= _dim
    return list(m.reshape(1, size))


def factor_T(expr, T_now, T_next):
    return expr.factor(matrix_2_1dlist(T_now) + matrix_2_1dlist(T_next))