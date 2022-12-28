import numpy as np
import csv

class KalmanFilter(object):
    def __init__(self, F = None, B = None, H = None, Q = None, R = None, P = None, x0 = None):

        if(F is None or H is None):
            raise ValueError("Set proper system dynamics.")

        self.n = F.shape[1]
        self.m = H.shape[1]

        self.F = F
        self.H = H
        self.B = 0 if B is None else B #干扰为0，加速度为0
        self.Q = np.eye(self.n) if Q is None else Q # 协方差的外部干扰
        self.R = np.eye(self.n) if R is None else R # R为测量方差，为定值
        self.P = np.eye(self.n) if P is None else P#初始变量的协方差为I
        self.x = np.zeros((self.n, 1)) if x0 is None else x0#初始值

    def predict(self, u = 0):
        self.x = np.dot(self.F, self.x) + np.dot(self.B, u) #x_k=F_k*x_{k-1}+B*u
        self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.Q #协方差更新Q为状态噪声的协方差
        return self.x

    def update(self, z):
        #print(z)
        y = z - np.dot(self.H, self.x)#公式中的(u1-u0)
        S = self.R + np.dot(self.H, np.dot(self.P, self.H.T))#
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))#求K'的公式，详见上述链接中求K的公式，K为卡尔曼增益
        self.x = self.x + np.dot(K, y)#更新后的x
        I = np.eye(self.n)
        self.P = np.dot(I - np.dot(K, self.H), self.P)#更新后的协方差P_k'

def pose_tracking():
    dt = 1.0/30
    #F = np.array([[1, dt, 0], [0, 1, dt], [0, 0, 1]])#状态转移方程
    F = np.array([[1, 0, 0, dt, 0, 0], 
                  [0, 1, 0, 0, dt, 1], 
                  [0, 0, 1, 0, 0, dt],
                  [0, 0, 0, 1, 0, 0], 
                  [0, 0, 0, 0, 1, 0], 
                  [0, 0, 0, 0, 0, 1]])
    H = np.array([[1, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0]]).reshape(3, 6)
    Q = np.array([[0.005, 0.005, 0.005, 0.005, 0.005, 0.005], 
                  [0.005, 0.005, 0.005, 0.005, 0.005, 0.005], 
                  [0.005, 0.005, 0.005, 0.005, 0.005, 0.005],
                  [0.005, 0.005, 0.005, 0.005, 0.005, 0.005],
                  [0.005, 0.005, 0.005, 0.005, 0.005, 0.005],
                  [0.005, 0.005, 0.005, 0.005, 0.005, 0.005]])#外部干扰
    #R = np.array([1]).reshape(1, 1)#sigma1，测量的方差不变
    R = np.array([[1,0,0],[0,1,0],[0,0,1]]).reshape(3, 3)#sigma1，测量的方差不变
    #其中Q为状态噪声的方差，R为测量噪声的方差
    #kf = KalmanFilter(F = F, H = H, Q = Q, R = R, P = None, x0=)
    predictions = []
    Z = []
    X = []
    with open("pose.csv", mode="r", encoding="utf-8") as f:
        last_row = None
        for row_idx, row in enumerate(csv.reader(f, skipinitialspace=True)):
            ci1 = float(row[0])
            ci2 = float(row[1])
            ci3 = float(row[2])
            ci4 = float(row[3])
            ci5 = float(row[4])
            ci6 = float(row[5])
            #Xi = [ci1, ci2, ci3, ci4, ci5, ci6]
            Xi = [ci1*0.001, ci2*0.001, ci3*0.001, 0, 0, 0]
            if row_idx >=1:
                Xi[3] = Xi[0]-last_row[0]
                Xi[4] = Xi[1]-last_row[1]
                Xi[5] = Xi[2]-last_row[2]
            Zi = [ci1*0.001, ci2*0.001, ci3*0.001, 0, 0, 0]
            X.append(Xi)
            Z.append(Zi)
            last_row = Xi

    with open("yrdy.txt", mode="w", encoding="utf-8") as f_test:
        for pose_i in X:
            pose_i_str_list = [str(pose_i_item) for pose_i_item in pose_i]
            pose_i_str = ','.join(pose_i_str_list)
            f_test.write(pose_i_str+'\n')

    kf = KalmanFilter(F = F, H = H, Q = Q, R = R, P = None, x0=X[1])
    for k in range(len(Z)-1):
        predictions.append(kf.predict()*1000)
        kf.update(Z[k+1][:3])

    with open("pose_filtered.txt", mode="w", encoding="utf-8") as f1:
        for pose_i in predictions:
            pose_i_str_list = [str(pose_i_item) for pose_i_item in pose_i]
            pose_i_str = ','.join(pose_i_str_list)
            f1.write(pose_i_str+'\n')
    # import matplotlib.pyplot as plt
    # plt.plot(range(len(measurements)), measurements, label = 'Measurements')
    # plt.plot(range(len(predictions)), np.array(predictions), label = 'Kalman Filter Prediction')
    # plt.plot(range(len(real_state)), real_state, label = 'Real statement' )
    # plt.legend()
    # plt.show()

if __name__ == '__main__':
    pose_tracking()