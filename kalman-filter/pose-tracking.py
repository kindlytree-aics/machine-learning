import numpy as np
import csv

def kf_predict(x0, pk0, F, Q):
    xk = np.dot(F, x0)
    pk = np.dot(np.dot(F, pk0), F.T) + Q
    return (xk, pk)

def kf_update(xk, pk, Z, H, R):
    #S = self.R + np.dot(self.H, np.dot(self.P, self.H.T))#
    #K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))#求K'的公式，详见上述链接中求K的公式，K为卡尔曼增益
    #pk(6,6),H(3,6),3*3
    K = np.dot(np.dot(pk, H.T), np.linalg.pinv(np.dot(np.dot(H, pk), H.T) + R))
    #print(K.shape, pk.shape,H.shape, R.shape, Z[:3].shape)
    #K(6,3)Z(6,1)H(3,6),xk(6,1)
    ##print(K.shape,Z[:3].shape, H.shape,xk.shape)
    s = np.dot(K, Z[:3] - np.dot(H, xk))
    #print(xk[:3].shape, s.shape)
    x1 = xk + np.dot(K, Z[:3] - np.dot(H, xk))
    p1 = np.dot(np.eye(K.shape[0]) - np.dot(K, H), pk)
    return (x1, p1, K)


dt = 1 / 30
F = np.array([[1, 0, 0, dt, 0, 0],
              [0, 1, 0, 0, dt, 0],
              [0, 0, 1, 0, 0, dt],
              [0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 1]])  # 状态转移方程
H = np.array([[1, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0]])

Q = np.array([[1, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 1]])  # 外部干扰

#R = np.array([1/5]).reshape(1, 1)  # sigma1，测量的方差不变 #其中Q为状态噪声的方差，R为测量噪声的方差
R = np.array([[1,0,0],[0,1,0],[0,0,1]]).reshape(3, 3)#sigma1，测量的方差不变
x0 = np.array([33, -1, 750, 0, 0, 0]).reshape(6, 1)

# pk0 = np.array([[2269.5, 446.9, -459.8, 0, 0, 0],
#                [446.9, 401.1, -310, 0, 0, 0],
#                [-459.8, -310, 1249, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0]])

pk0 = np.array([[1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1]])

filtered_rows = []
with open("pose.csv", mode="r", encoding="utf-8") as f:
    for row in csv.reader(f, skipinitialspace=True):
        c1 = float(row[0])
        c2 = float(row[1])
        c3 = float(row[2])

        Z = np.array([c1, c2, c3, 0, 0, 0]).reshape(6, 1)

        xk, pk = kf_predict(x0, pk0, F, Q)
        print('xk shape is:', xk.shape)

        x1, pk0, K = kf_update(xk, pk, Z, H, R)

        x0 = x1
        filtered_rows.append(x0)

        

with open("tt.txt", mode="w", encoding="utf-8") as f1:
    for pose_i in filtered_rows:
        pose_i_str_list = [str(pose_i_item) for pose_i_item in pose_i]
        pose_i_str = ','.join(pose_i_str_list)
        f1.write(pose_i_str+'\n')
        # for i in range(len(x1)):
        #     f1.write(str(x1[i]).strip() + '\n')