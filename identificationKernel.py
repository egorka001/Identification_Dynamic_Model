from math import radians, sqrt
from scipy.optimize import minimize
import random as rnd

from linkFormulaNo1 import linkFormulaNo1
from linkFormulaNo2 import linkFormulaNo2
from linkFormulaNo3 import linkFormulaNo3
from linkFormulaNo4 import linkFormulaNo4
from linkFormulaNo5 import linkFormulaNo5
from linkFormulaNo6 import linkFormulaNo6

class DataReader:
    def __init__(self):
        self.q = []
        self.dq = []
        self.ddq = []
        self.torque = []
        
    def readDataFromFile(self, filename):
        #Считываение сырых данных из файла
        with open(filename, 'r') as file:
            raw_data = file.readlines()
            raw_data = raw_data[1:]
            for i in range(len(raw_data)):
                raw_data[i] = raw_data[i].split('\t')
                raw_data[i] = raw_data[i][0:6] + raw_data[i][29:35] + raw_data[i][60:66]
                for j in range(len(raw_data[i])):
                    raw_data[i][j] = float(raw_data[i][j].replace(',', '.'))
         
            #Запись координат в моменты времени
            for i in range(3, len(raw_data) - 1):
                if i % 3 == 0:
                    self.q.append(raw_data[i][0:6])
            
            #Запись скоростей
            for i in range(3, len(raw_data) - 1):
                if i % 3 == 0:
                    self.dq.append(raw_data[i][12:])
            
            #Запись ускорений
            for i in range(3, len(raw_data) - 1):
                if i % 3 == 0:
                    self.ddq.append([(raw_data[i + 1][12] - raw_data[i - 1][12]) * 1000 / 8,
                                    (raw_data[i + 1][13] - raw_data[i - 1][13]) * 1000 / 8,
                                    (raw_data[i + 1][14] - raw_data[i - 1][14]) * 1000 / 8,
                                    (raw_data[i + 1][15] - raw_data[i - 1][15]) * 1000 / 8,
                                    (raw_data[i + 1][16] - raw_data[i - 1][16]) * 1000 / 8,
                                    (raw_data[i + 1][17] - raw_data[i - 1][17]) * 1000 / 8])
            
            #Запись моментов
            for i in range(3, len(raw_data) - 1):
                if i % 3 == 0:
                    self.torque.append(raw_data[i][6:13])
                    
            #Перевод в радианы
            for i in range(len(self.torque)):
                for j in range(6):
                    self.q[i][j] = radians(self.q[i][j])
                    self.dq[i][j] = radians(self.dq[i][j]+1e-6)
                    self.ddq[i][j] = radians(self.ddq[i][j]+1e-6)
                self.q[i] = [-1] + self.q[i]
                self.dq[i] = [-1] + self.dq[i]
                self.ddq[i] = [-1] + self.ddq[i]

class IdentificationCore:
    def __init__(self):
        pass
    
    def ident(self, zero_point, q, dq, ddq, torque):
        res = minimize(objective, zero_point, args=(q, dq, ddq, torque), method='BFGS-B', jac=grad)
        print(res.x)

def objective(dynamic_parameters, q, dq, ddq, real_troque):
    l2error = 0
    
    for i in range(len(real_troque)):
        theor_torque = []
        
        theor_torque.append(linkFormulaNo1(q[i][1], q[i][2], q[i][3], q[i][4], q[i][5], q[i][6],                      
                                           dq[i][1], dq[i][2], dq[i][3], dq[i][4], dq[i][5], dq[i][6],
                                           ddq[i][1], ddq[i][2], ddq[i][3], ddq[i][4], ddq[i][5], ddq[i][6],
                                           dynamic_parameters[0], dynamic_parameters[1],
                                           dynamic_parameters[2], dynamic_parameters[3],
                                           dynamic_parameters[4], dynamic_parameters[5],
                                           dynamic_parameters[6], dynamic_parameters[7],
                                           dynamic_parameters[8], dynamic_parameters[9],
                                           dynamic_parameters[10], dynamic_parameters[11],
                                           dynamic_parameters[12], dynamic_parameters[13],
                                           dynamic_parameters[14], dynamic_parameters[15],
                                           dynamic_parameters[16], dynamic_parameters[17],
                                           dynamic_parameters[18], dynamic_parameters[19],
                                           dynamic_parameters[20], dynamic_parameters[21],
                                           dynamic_parameters[22], dynamic_parameters[23],
                                           dynamic_parameters[24], dynamic_parameters[25],
                                           dynamic_parameters[26], dynamic_parameters[27],
                                           dynamic_parameters[28], dynamic_parameters[29],
                                           dynamic_parameters[30], dynamic_parameters[31],
                                           dynamic_parameters[32], dynamic_parameters[33],
                                           dynamic_parameters[34], dynamic_parameters[35],
                                           dynamic_parameters[36], dynamic_parameters[37],
                                           dynamic_parameters[38], dynamic_parameters[39],
                                           dynamic_parameters[40], dynamic_parameters[41],
                                           dynamic_parameters[42], dynamic_parameters[43],
                                           dynamic_parameters[44], dynamic_parameters[45],
                                           dynamic_parameters[46], dynamic_parameters[47],
                                           dynamic_parameters[48], dynamic_parameters[49],
                                           dynamic_parameters[50], dynamic_parameters[51],
                                           dynamic_parameters[52], dynamic_parameters[53],
                                           dynamic_parameters[54], dynamic_parameters[55],
                                           dynamic_parameters[56], dynamic_parameters[57],
                                           dynamic_parameters[58], dynamic_parameters[59],
                                           dynamic_parameters[60], dynamic_parameters[61],
                                           dynamic_parameters[62], dynamic_parameters[63],
                                           dynamic_parameters[64], dynamic_parameters[65],
                                           dynamic_parameters[66], dynamic_parameters[67],
                                           dynamic_parameters[68], dynamic_parameters[69],
                                           dynamic_parameters[70], dynamic_parameters[71]))

        theor_torque.append(linkFormulaNo2(q[i][1], q[i][2], q[i][3], q[i][4], q[i][5], q[i][6],                         
                                           dq[i][1], dq[i][2], dq[i][3], dq[i][4], dq[i][5], dq[i][6],
                                           ddq[i][1], ddq[i][2], ddq[i][3], ddq[i][4], ddq[i][5], ddq[i][6],
                                           dynamic_parameters[0], dynamic_parameters[1],
                                           dynamic_parameters[2], dynamic_parameters[3],
                                           dynamic_parameters[4], dynamic_parameters[5],
                                           dynamic_parameters[6], dynamic_parameters[7],
                                           dynamic_parameters[8], dynamic_parameters[9],
                                           dynamic_parameters[10], dynamic_parameters[11],
                                           dynamic_parameters[12], dynamic_parameters[13],
                                           dynamic_parameters[14], dynamic_parameters[15],
                                           dynamic_parameters[16], dynamic_parameters[17],
                                           dynamic_parameters[18], dynamic_parameters[19],
                                           dynamic_parameters[20], dynamic_parameters[21],
                                           dynamic_parameters[22], dynamic_parameters[23],
                                           dynamic_parameters[24], dynamic_parameters[25],
                                           dynamic_parameters[26], dynamic_parameters[27],
                                           dynamic_parameters[28], dynamic_parameters[29],
                                           dynamic_parameters[30], dynamic_parameters[31],
                                           dynamic_parameters[32], dynamic_parameters[33],
                                           dynamic_parameters[34], dynamic_parameters[35],
                                           dynamic_parameters[36], dynamic_parameters[37],
                                           dynamic_parameters[38], dynamic_parameters[39],
                                           dynamic_parameters[40], dynamic_parameters[41],
                                           dynamic_parameters[42], dynamic_parameters[43],
                                           dynamic_parameters[44], dynamic_parameters[45],
                                           dynamic_parameters[46], dynamic_parameters[47],
                                           dynamic_parameters[48], dynamic_parameters[49],
                                           dynamic_parameters[50], dynamic_parameters[51],
                                           dynamic_parameters[52], dynamic_parameters[53],
                                           dynamic_parameters[54], dynamic_parameters[55],
                                           dynamic_parameters[56], dynamic_parameters[57],
                                           dynamic_parameters[58], dynamic_parameters[59],
                                           dynamic_parameters[60], dynamic_parameters[61],
                                           dynamic_parameters[62], dynamic_parameters[63],
                                           dynamic_parameters[64], dynamic_parameters[65],
                                           dynamic_parameters[66], dynamic_parameters[67],
                                           dynamic_parameters[68], dynamic_parameters[69],
                                           dynamic_parameters[70], dynamic_parameters[71]))
        
        theor_torque.append(linkFormulaNo3(q[i][1], q[i][2], q[i][3], q[i][4], q[i][5], q[i][6],                         
                                           dq[i][1], dq[i][2], dq[i][3], dq[i][4], dq[i][5], dq[i][6],
                                           ddq[i][1], ddq[i][2], ddq[i][3], ddq[i][4], ddq[i][5], ddq[i][6],
                                           dynamic_parameters[0], dynamic_parameters[1],
                                           dynamic_parameters[2], dynamic_parameters[3],
                                           dynamic_parameters[4], dynamic_parameters[5],
                                           dynamic_parameters[6], dynamic_parameters[7],
                                           dynamic_parameters[8], dynamic_parameters[9],
                                           dynamic_parameters[10], dynamic_parameters[11],
                                           dynamic_parameters[12], dynamic_parameters[13],
                                           dynamic_parameters[14], dynamic_parameters[15],
                                           dynamic_parameters[16], dynamic_parameters[17],
                                           dynamic_parameters[18], dynamic_parameters[19],
                                           dynamic_parameters[20], dynamic_parameters[21],
                                           dynamic_parameters[22], dynamic_parameters[23],
                                           dynamic_parameters[24], dynamic_parameters[25],
                                           dynamic_parameters[26], dynamic_parameters[27],
                                           dynamic_parameters[28], dynamic_parameters[29],
                                           dynamic_parameters[30], dynamic_parameters[31],
                                           dynamic_parameters[32], dynamic_parameters[33],
                                           dynamic_parameters[34], dynamic_parameters[35],
                                           dynamic_parameters[36], dynamic_parameters[37],
                                           dynamic_parameters[38], dynamic_parameters[39],
                                           dynamic_parameters[40], dynamic_parameters[41],
                                           dynamic_parameters[42], dynamic_parameters[43],
                                           dynamic_parameters[44], dynamic_parameters[45],
                                           dynamic_parameters[46], dynamic_parameters[47],
                                           dynamic_parameters[48], dynamic_parameters[49],
                                           dynamic_parameters[50], dynamic_parameters[51],
                                           dynamic_parameters[52], dynamic_parameters[53],
                                           dynamic_parameters[54], dynamic_parameters[55],
                                           dynamic_parameters[56], dynamic_parameters[57],
                                           dynamic_parameters[58], dynamic_parameters[59],
                                           dynamic_parameters[60], dynamic_parameters[61],
                                           dynamic_parameters[62], dynamic_parameters[63],
                                           dynamic_parameters[64], dynamic_parameters[65],
                                           dynamic_parameters[66], dynamic_parameters[67],
                                           dynamic_parameters[68], dynamic_parameters[69],
                                           dynamic_parameters[70], dynamic_parameters[71]))
        
        theor_torque.append(linkFormulaNo4(q[i][1], q[i][2], q[i][3], q[i][4], q[i][5], q[i][6],                         
                                           dq[i][1], dq[i][2], dq[i][3], dq[i][4], dq[i][5], dq[i][6],
                                           ddq[i][1], ddq[i][2], ddq[i][3], ddq[i][4], ddq[i][5], ddq[i][6],
                                           dynamic_parameters[0], dynamic_parameters[1],
                                           dynamic_parameters[2], dynamic_parameters[3],
                                           dynamic_parameters[4], dynamic_parameters[5],
                                           dynamic_parameters[6], dynamic_parameters[7],
                                           dynamic_parameters[8], dynamic_parameters[9],
                                           dynamic_parameters[10], dynamic_parameters[11],
                                           dynamic_parameters[12], dynamic_parameters[13],
                                           dynamic_parameters[14], dynamic_parameters[15],
                                           dynamic_parameters[16], dynamic_parameters[17],
                                           dynamic_parameters[18], dynamic_parameters[19],
                                           dynamic_parameters[20], dynamic_parameters[21],
                                           dynamic_parameters[22], dynamic_parameters[23],
                                           dynamic_parameters[24], dynamic_parameters[25],
                                           dynamic_parameters[26], dynamic_parameters[27],
                                           dynamic_parameters[28], dynamic_parameters[29],
                                           dynamic_parameters[30], dynamic_parameters[31],
                                           dynamic_parameters[32], dynamic_parameters[33],
                                           dynamic_parameters[34], dynamic_parameters[35],
                                           dynamic_parameters[36], dynamic_parameters[37],
                                           dynamic_parameters[38], dynamic_parameters[39],
                                           dynamic_parameters[40], dynamic_parameters[41],
                                           dynamic_parameters[42], dynamic_parameters[43],
                                           dynamic_parameters[44], dynamic_parameters[45],
                                           dynamic_parameters[46], dynamic_parameters[47],
                                           dynamic_parameters[48], dynamic_parameters[49],
                                           dynamic_parameters[50], dynamic_parameters[51],
                                           dynamic_parameters[52], dynamic_parameters[53],
                                           dynamic_parameters[54], dynamic_parameters[55],
                                           dynamic_parameters[56], dynamic_parameters[57],
                                           dynamic_parameters[58], dynamic_parameters[59],
                                           dynamic_parameters[60], dynamic_parameters[61],
                                           dynamic_parameters[62], dynamic_parameters[63],
                                           dynamic_parameters[64], dynamic_parameters[65],
                                           dynamic_parameters[66], dynamic_parameters[67],
                                           dynamic_parameters[68], dynamic_parameters[69],
                                           dynamic_parameters[70], dynamic_parameters[71]))
        
        theor_torque.append(linkFormulaNo5(q[i][1], q[i][2], q[i][3], q[i][4], q[i][5], q[i][6],                         
                                           dq[i][1], dq[i][2], dq[i][3], dq[i][4], dq[i][5], dq[i][6],
                                           ddq[i][1], ddq[i][2], ddq[i][3], ddq[i][4], ddq[i][5], ddq[i][6],
                                           dynamic_parameters[0], dynamic_parameters[1],
                                           dynamic_parameters[2], dynamic_parameters[3],
                                           dynamic_parameters[4], dynamic_parameters[5],
                                           dynamic_parameters[6], dynamic_parameters[7],
                                           dynamic_parameters[8], dynamic_parameters[9],
                                           dynamic_parameters[10], dynamic_parameters[11],
                                           dynamic_parameters[12], dynamic_parameters[13],
                                           dynamic_parameters[14], dynamic_parameters[15],
                                           dynamic_parameters[16], dynamic_parameters[17],
                                           dynamic_parameters[18], dynamic_parameters[19],
                                           dynamic_parameters[20], dynamic_parameters[21],
                                           dynamic_parameters[22], dynamic_parameters[23],
                                           dynamic_parameters[24], dynamic_parameters[25],
                                           dynamic_parameters[26], dynamic_parameters[27],
                                           dynamic_parameters[28], dynamic_parameters[29],
                                           dynamic_parameters[30], dynamic_parameters[31],
                                           dynamic_parameters[32], dynamic_parameters[33],
                                           dynamic_parameters[34], dynamic_parameters[35],
                                           dynamic_parameters[36], dynamic_parameters[37],
                                           dynamic_parameters[38], dynamic_parameters[39],
                                           dynamic_parameters[40], dynamic_parameters[41],
                                           dynamic_parameters[42], dynamic_parameters[43],
                                           dynamic_parameters[44], dynamic_parameters[45],
                                           dynamic_parameters[46], dynamic_parameters[47],
                                           dynamic_parameters[48], dynamic_parameters[49],
                                           dynamic_parameters[50], dynamic_parameters[51],
                                           dynamic_parameters[52], dynamic_parameters[53],
                                           dynamic_parameters[54], dynamic_parameters[55],
                                           dynamic_parameters[56], dynamic_parameters[57],
                                           dynamic_parameters[58], dynamic_parameters[59],
                                           dynamic_parameters[60], dynamic_parameters[61],
                                           dynamic_parameters[62], dynamic_parameters[63],
                                           dynamic_parameters[64], dynamic_parameters[65],
                                           dynamic_parameters[66], dynamic_parameters[67],
                                           dynamic_parameters[68], dynamic_parameters[69],
                                           dynamic_parameters[70], dynamic_parameters[71]))
        
        theor_torque.append(linkFormulaNo6(q[i][1], q[i][2], q[i][3], q[i][4], q[i][5], q[i][6],                         
                                           dq[i][1], dq[i][2], dq[i][3], dq[i][4], dq[i][5], dq[i][6],
                                           ddq[i][1], ddq[i][2], ddq[i][3], ddq[i][4], ddq[i][5], ddq[i][6],
                                           dynamic_parameters[0], dynamic_parameters[1],
                                           dynamic_parameters[2], dynamic_parameters[3],
                                           dynamic_parameters[4], dynamic_parameters[5],
                                           dynamic_parameters[6], dynamic_parameters[7],
                                           dynamic_parameters[8], dynamic_parameters[9],
                                           dynamic_parameters[10], dynamic_parameters[11],
                                           dynamic_parameters[12], dynamic_parameters[13],
                                           dynamic_parameters[14], dynamic_parameters[15],
                                           dynamic_parameters[16], dynamic_parameters[17],
                                           dynamic_parameters[18], dynamic_parameters[19],
                                           dynamic_parameters[20], dynamic_parameters[21],
                                           dynamic_parameters[22], dynamic_parameters[23],
                                           dynamic_parameters[24], dynamic_parameters[25],
                                           dynamic_parameters[26], dynamic_parameters[27],
                                           dynamic_parameters[28], dynamic_parameters[29],
                                           dynamic_parameters[30], dynamic_parameters[31],
                                           dynamic_parameters[32], dynamic_parameters[33],
                                           dynamic_parameters[34], dynamic_parameters[35],
                                           dynamic_parameters[36], dynamic_parameters[37],
                                           dynamic_parameters[38], dynamic_parameters[39],
                                           dynamic_parameters[40], dynamic_parameters[41],
                                           dynamic_parameters[42], dynamic_parameters[43],
                                           dynamic_parameters[44], dynamic_parameters[45],
                                           dynamic_parameters[46], dynamic_parameters[47],
                                           dynamic_parameters[48], dynamic_parameters[49],
                                           dynamic_parameters[50], dynamic_parameters[51],
                                           dynamic_parameters[52], dynamic_parameters[53],
                                           dynamic_parameters[54], dynamic_parameters[55],
                                           dynamic_parameters[56], dynamic_parameters[57],
                                           dynamic_parameters[58], dynamic_parameters[59],
                                           dynamic_parameters[60], dynamic_parameters[61],
                                           dynamic_parameters[62], dynamic_parameters[63],
                                           dynamic_parameters[64], dynamic_parameters[65],
                                           dynamic_parameters[66], dynamic_parameters[67],
                                           dynamic_parameters[68], dynamic_parameters[69],
                                           dynamic_parameters[70], dynamic_parameters[71]))

        for j in range(6):
            l2error += (real_troque[i][j] - theor_torque[j]) ** 2
 
    l2error = sqrt(float(l2error))    
    
    print(l2error)
    return l2error

def grad(dynamic_parametrs, q, dq, ddq, real_torque):
    gradient = []
    eps = 1e-9
    
    for i in range(len(dynamic_parametrs)):
        temp_params = dynamic_parametrs.copy()
        temp_params[i] += eps
        gradient.append((objective(temp_params, q, dq, ddq, real_torque) - objective(dynamic_parametrs, q, dq, ddq, real_torque)) / eps)
    
    print('gradient calculated')
    return gradient

def generate_points(Reader, counter):
    rnd_list = rnd.sample(range(len(Reader.torque)), counter)
        
    sample_q = []
    sample_dq = []
    sample_ddq = []
    real_torque = []
    
    for i in rnd_list:
        sample_q.append(Reader.q[i])
        sample_dq.append(Reader.dq[i])
        sample_ddq.append(Reader.ddq[i])
        real_torque.append(Reader.torque[i])
        
    print('calculation simulation torque ended')
    
    return (sample_q, sample_dq, sample_ddq, real_torque)

if __name__ == "__main__":
    Reader = DataReader()
    print("readDataFromFile stated")
    Reader.readDataFromFile("trainData.txt")
    print("readDataFromFile ended")
    
    print(len(Reader.torque))
    
    (q, dq, ddq, sim_torque, real_torque) = generate_points(Reader, 1)
    
    zero_dynamic_parameters = [1] * 72
    
    Identification = IdentificationCore()
    Identification.ident(zero_dynamic_parameters, q, dq, ddq, real_torque)
    