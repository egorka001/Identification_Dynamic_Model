import sympy as s

class MathCore:
    def __init__(self):
        #Символ для обозначения переменной времени
        self.time = s.Symbol('t')
        
        #Функция обобщённой координаты от времени
        self.q = [-1, 
                  s.Function('q_1', real=True)(self.time),
                  s.Function('q_2', real=True)(self.time),
                  s.Function('q_3', real=True)(self.time),
                  s.Function('q_4', real=True)(self.time),
                  s.Function('q_5', real=True)(self.time),
                  s.Function('q_6', real=True)(self.time)]
        
        #Функция обобщённой скорости от времени
        self.dq = [-1,
                   s.diff(self.q[1], self.time, real=True),
                   s.diff(self.q[2], self.time, real=True),
                   s.diff(self.q[3], self.time, real=True),
                   s.diff(self.q[4], self.time, real=True),
                   s.diff(self.q[5], self.time, real=True),
                   s.diff(self.q[6], self.time, real=True)]
        
        #Функция обобщённого ускорения от времени
        self.ddq = [-1,
                    s.diff(self.dq[1], self.time),
                    s.diff(self.dq[2], self.time),
                    s.diff(self.dq[3], self.time),
                    s.diff(self.dq[4], self.time),
                    s.diff(self.dq[5], self.time),
                    s.diff(self.dq[6], self.time)]
        
        #Символы отвечающие за массу звена
        self.m = [-1,
                  s.Symbol('m_1', real=True),
                  s.Symbol('m_2', real=True),
                  s.Symbol('m_3', real=True),
                  s.Symbol('m_4', real=True),
                  s.Symbol('m_5', real=True),
                  s.Symbol('m_6', real=True)]
        
        #Вектора перехода от СК звена к центру масс звена
        self.rc = [-1,
                   s.Matrix([[s.Symbol('r_x_c_1', real=True)],[s.Symbol('r_y_c_1', real=True)],[s.Symbol('r_z_c_1', real=True)]]),
                   s.Matrix([[s.Symbol('r_x_c_2', real=True)],[s.Symbol('r_y_c_2', real=True)],[s.Symbol('r_z_c_2', real=True)]]),
                   s.Matrix([[s.Symbol('r_x_c_3', real=True)],[s.Symbol('r_y_c_3', real=True)],[s.Symbol('r_z_c_3', real=True)]]),
                   s.Matrix([[s.Symbol('r_x_c_4', real=True)],[s.Symbol('r_y_c_4', real=True)],[s.Symbol('r_z_c_4', real=True)]]),
                   s.Matrix([[s.Symbol('r_x_c_5', real=True)],[s.Symbol('r_y_c_5', real=True)],[s.Symbol('r_z_c_5', real=True)]]),
                   s.Matrix([[s.Symbol('r_x_c_6', real=True)],[s.Symbol('r_y_c_6', real=True)],[s.Symbol('r_z_c_6', real=True)]])]
        
        #Тензоры инерций
        self.I = [-1]
        for i in range(1, 7):
            self.I.append(s.Matrix([[s.Symbol('I_xx_' + str(i), real=True), s.Symbol('I_xy_' + str(i), real=True), s.Symbol('I_xz_' + str(i), real=True)],
                                    [s.Symbol('I_xy_' + str(i), real=True), s.Symbol('I_yy_' + str(i), real=True), s.Symbol('I_yz_' + str(i), real=True)],
                                    [s.Symbol('I_xz_' + str(i), real=True), s.Symbol('I_yz_' + str(i), real=True), s.Symbol('I_zz_' + str(i), real=True)]]))
        
        #Общий вид записи DH-параметров
        self.DH = [-1, 
                   [s.pi, 0, 0, -675],
                   [s.pi / 2, 350, 0, 0],
                   [0, 1150, -s.pi / 2, 0],
                   [s.pi / 2, -41, 0, -1000],
                   [-s.pi / 2, 0, 0, 0],
                   [s.pi / 2, 0, 0, 0]]
        
                    
        #Вектор гравитации
        self.g = s.Matrix([[0], [0], [-9.8]])
        
        #Матрицы переходов
        self.T = [-1]
        for i in range(1, 7):
            Rx = s.Matrix([[1, 0, 0, 0],
                           [0, s.cos(self.DH[i][0]), -s.sin(self.DH[i][0]), 0],
                           [0, s.sin(self.DH[i][0]), s.cos(self.DH[i][0]), 0],
                           [0, 0, 0, 1]])
            Tx = s.Matrix([[1, 0, 0, self.DH[i][1]],
                           [0, 1, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])
            Rz = s.Matrix([[s.cos(self.DH[i][2] + self.q[i]), -s.sin(self.DH[i][2] + self.q[i]), 0, 0],
                           [s.sin(self.DH[i][2] + self.q[i]), s.cos(self.DH[i][2] + self.q[i]), 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])
            Tz = s.Matrix([[1, 0, 0, 0],
                           [0, 1, 0, 0],
                           [0, 0, 1, self.DH[i][3]],
                           [0, 0, 0, 1]])
            self.T.append(Rx * Tx * Rz * Tz)

        #Матрицы поворотов
        self.R = [-1]
        for i in range(1, 7):
            self.R.append(s.Matrix([[self.T[i][0], self.T[i][1], self.T[i][2]],
                                    [self.T[i][4], self.T[i][5], self.T[i][6]],
                                    [self.T[i][8], self.T[i][9], self.T[i][10]]]))
        
        #Вектор-столбец параллельного переноса
        self.tr = [-1]
        for i in range(1, 7):
            self.tr.append(s.Matrix([[self.T[i][3]], [self.T[i][7]], [self.T[i][11]]]))
        
        #Вектор угловой скорости относительно центра масс
        self.omega_n = [s.Matrix([[0],[0],[0]])]
        for i in range(1, 7):
            self.omega_n.append(self.R[i].transpose() * self.omega_n[i - 1] + s.Matrix([[0], [0], [self.dq[i]]]))
        
        #Вектор линейной скорости начала СК
        self.v_n = [s.Matrix([[0],[0],[0]])]
        for i in range(1, 7):
            self.v_n.append(self.R[i].transpose() * (self.v_n[i - 1] + s.Matrix.cross(self.omega_n[i - 1], self.tr[i])))
        
        #Вектор линейной скорости центра масс  
        self.v_cn = [-1]
        for i in range(1, 7):
            self.v_cn.append(self.v_n[i] + s.Matrix.cross(self.omega_n[i], self.rc[i]))
        
        #Кинетическая энергия отдельных звеньев
        self.K_n = [-1]
        for i in range(1, 7):
            self.K_n.append(s.Rational(1, 2) * (self.m[i] * (self.v_cn[i].norm() ** 2) + (self.omega_n[i].transpose() * self.I[i] * self.omega_n[i])[0]))
        
        #Полная кинетическая энергия тела
        self.K = self.K_n[1] + self.K_n[2] + self.K_n[3] + self.K_n[4] + self.K_n[5] + self.K_n[6]
        
        #Вектор ИСК к центру масс звена
        self.r_base_cn = [-1]
        for i in range(1, 7):
            temp_t = self.T[1]
            for j in range(2, i + 1):
                temp_t *= self.T[j]
            temp_t *= s.Matrix([[self.rc[i][0]],
                                [self.rc[i][1]],
                                [self.rc[i][2]],
                                [1]], real=True)
            self.r_base_cn.append(s.Matrix([[temp_t[0]], [temp_t[1]], [temp_t[2]]]))
        
        #Потенциальная энергия отдельных звеньев
        self.P_n = [-1]
        for i in range(1, 7):
            self.P_n.append(self.m[i] * (self.g.transpose() * self.r_base_cn[i])[0])
            
        #Потенциальная энергия системы
        self.P = self.P_n[1] + self.P_n[2] + self.P_n[3] + self.P_n[4] + self.P_n[5] + self.P_n[6]
        
        #Лагранжиан системы
        self.L = self.K - self.P

        #Уравнение Лагранжа второго рода 
        self.equation_right_part = [-1]
        self.equation_left_part = [-1]
        for i in range(1, 7): 
            self.equation_right_part.append(s.Derivative(self.L, self.q[i]).doit())
            self.equation_left_part.append(s.Derivative(s.Derivative(self.K, self.dq[i]).doit(), self.time).doit())
            
        self.temp_q = [-1,
                       s.Symbol('temp_q_1', real=True),
                       s.Symbol('temp_q_2', real=True),
                       s.Symbol('temp_q_3', real=True),
                       s.Symbol('temp_q_4', real=True),
                       s.Symbol('temp_q_5', real=True),
                       s.Symbol('temp_q_6', real=True)]
        
        self.temp_dq = [-1,
                        s.Symbol('temp_dq_1', real=True),
                        s.Symbol('temp_dq_2', real=True),
                        s.Symbol('temp_dq_3', real=True),
                        s.Symbol('temp_dq_4', real=True),
                        s.Symbol('temp_dq_5', real=True),
                        s.Symbol('temp_dq_6', real=True)]
        
        self.temp_ddq = [-1,
                        s.Symbol('temp_ddq_1', real=True),
                        s.Symbol('temp_ddq_2', real=True),
                        s.Symbol('temp_ddq_3', real=True),
                        s.Symbol('temp_ddq_4', real=True),
                        s.Symbol('temp_ddq_5', real=True),
                        s.Symbol('temp_ddq_6', real=True)]
        
        self.equation = [-1]
        
        for i in range(1, 7):
            right_part = self.equation_right_part[i].copy()
            right_part = right_part.subs([(self.dq[1], self.temp_dq[1]),
                                          (self.dq[2], self.temp_dq[2]),
                                          (self.dq[3], self.temp_dq[3]),
                                          (self.dq[4], self.temp_dq[4]),
                                          (self.dq[5], self.temp_dq[5]),
                                          (self.dq[6], self.temp_dq[6])])
            right_part = right_part.subs([(self.q[1], self.temp_q[1]),
                                          (self.q[2], self.temp_q[2]),
                                          (self.q[3], self.temp_q[3]),
                                          (self.q[4], self.temp_q[4]),
                                          (self.q[5], self.temp_q[5]),
                                          (self.q[6], self.temp_q[6])])
            right_part = right_part.replace(s.Subs(s.Derivative(self.temp_dq[i], s.Symbol('_xi')), s.Symbol('_xi'), self.temp_q[i]), 0)
            
            left_part = self.equation_left_part[i].copy()
            left_part = left_part.subs([(self.ddq[1], self.temp_ddq[1]),
                                        (self.ddq[2], self.temp_ddq[2]),
                                        (self.ddq[3], self.temp_ddq[3]),
                                        (self.ddq[4], self.temp_ddq[4]),
                                        (self.ddq[5], self.temp_ddq[5]),
                                        (self.ddq[6], self.temp_ddq[6])])
            left_part = left_part.evalf()
            left_part = left_part.subs([(self.dq[1], self.temp_dq[1]),
                                        (self.dq[2], self.temp_dq[2]),
                                        (self.dq[3], self.temp_dq[3]),
                                        (self.dq[4], self.temp_dq[4]),
                                        (self.dq[5], self.temp_dq[5]),
                                        (self.dq[6], self.temp_dq[6])])
            left_part = left_part.evalf()
            left_part = left_part.subs([(self.q[1], self.temp_q[1]),
                                        (self.q[2], self.temp_q[2]),
                                        (self.q[3], self.temp_q[3]),
                                        (self.q[4], self.temp_q[4]),
                                        (self.q[5], self.temp_q[5]),
                                        (self.q[6], self.temp_q[6])])
            left_part = left_part.subs([(self.time, 0), (s.Symbol('_xi'), 0)])
            left_part = left_part.doit(deep = True) 
            left_part = left_part.replace(s.Subs(s.Derivative(s.re(s.Symbol('_xi')), s.Symbol('_xi')), s.Symbol('_xi'), self.temp_dq[i]), 1)
            self.equation.append((right_part - left_part))
            for j in range(1, 7):
                self.equation[i] = self.equation[i].replace(s.Derivative(self.temp_dq[j], self.temp_q[j]), 0)
            self.equation[i] = self.equation[i].evalf(5)
            
            with open("equationGen" + str(i) + ".txt", 'w') as file:
                file.write(str(self.equation[i]))
            print('file ' + str(i) + 'done')
             
if __name__ == "__main__":   
    print("math core initialize started")
    EquationGenerator = MathCore()
    print("math core initialize ended")
                         