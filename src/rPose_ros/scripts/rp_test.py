import numpy as np
# import sympy
import time
# import numba
fx = 320.0
fy = 320.0
cx = 320.0
cy = 240.0
r = 100.0
pose_delta_arr=np.array([5.0,5.0,5.0])
class BoundingBox:
    def __init__(self, xmin, ymin, xmax, ymax):
        self.xmin=xmin
        self.ymin=ymin
        self.xmax=xmax
        self.ymax=ymax

def get_4points2d(bbox):
    xmid = (bbox.xmin+bbox.xmax)/2; ymid = (bbox.ymin+bbox.ymax)/2
    a1 = (bbox.xmin-cx)/fx
    a2 = (xmid-cx)/fx
    a3 = (bbox.xmax-cx)/fx
    a4 = a2
    a0 = a2
    b1 = (ymid-cy)/fy
    b2 = (bbox.ymin-cy)/fy
    b3 = b1
    b0 = b1
    b4 = (bbox.ymax-cy)/fy
    return [a0, a1, a2, a3, a4], [b0, b1, b2, b3, b4]

def up_constraint(delta, limit=1000):
    if(delta[0]>limit): return np.array([limit])
    elif(delta[0]<-limit): return np.array([-limit])
    else: return delta
# @numba.jit(nopython=True) 
def newton_iter(a_, b_, iter_num = 50):
        # initial
        # pose_delta_arr=np.array([5,5,5])
        # depth_avg = (depth_u_+depth_v_)/2
        '''
        # stero method
        pose = np.array([[depth_avg], [depth_avg-50], [depth_avg-25], [depth_avg+25], [depth_avg+50], [1], [1], [1]])
        for j in range(iter_num):
            # print("--------------iter %d---------------" % j)
            J = np.zeros((8,8))
            pose = pose.T[0]
            for i in range(4):
                J[i][0] = -2*a_[0]*(a_[i+1]*pose[i+1]-a_[0]*pose[0]) - 2*b_[0]*(b_[i+1]*pose[i+1]-b_[0]*pose[0]) - 2*(pose[i+1]-pose[0])
                J[i][i+1] = 2*a_[i+1]*(a_[i+1]*pose[i+1]-a_[0]*pose[0]) + 2*b_[i+1]*(b_[i+1]*pose[i+1]-b_[0]*pose[0]) + 2*(pose[i+1]-pose[0])
            for i in range(4):
                J[i+4][0] = -pose[5]*a_[0] - pose[6]*b_[0] - pose[7]
                J[i+4][i+1] = pose[5]*a_[i+1] + pose[6]*b_[i+1] + pose[7]
                J[i+4][5] = a_[i+1]*pose[i+1] - a_[0]*pose[0]
                J[i+4][6] = b_[i+1]*pose[i+1] - b_[0]*pose[0]
                J[i+4][7] = pose[i+1] - pose[0]
            # print("J is:\n", J, "\t rank is:", np.linalg.matrix_rank(J))
            J_inv = np.linalg.inv(J)
            # print("J_inv is:\n", J_inv)
            f = np.zeros((8,1))
            for i in range(4):
                f[i][0] = (a_[i+1]*pose[i+1]-a_[0]*pose[0])**2 + (b_[i+1]*pose[i+1]-b_[0]*pose[0])**2 + (pose[i+1]-pose[0])**2 - r**2
            for i in range(4):
                f[i+4][0] = pose[5]*(a_[i+1]*pose[i+1]-a_[0]*pose[0]) + pose[6]*(b_[i+1]*pose[i+1]-b_[0]*pose[0]) + pose[7]*(pose[i+1]-pose[0])
            pose_delta = J_inv @ f
            # store 3 delta number in a row
            pose_delta_arr[j%3]=abs(pose_delta[0])
            # if the average number of 3 continuous delta is less than 1, iteration ends in advance
            if(np.mean(pose_delta_arr)<=1 and j>=5): 
                # rospy.loginfo("depth_avg_esti:{}".format(depth_avg))
                # rospy.loginfo("iter_num:{}".format(j))
                # rospy.loginfo("depth:{}".format(pose[0][0]))
                break
            else: pose = pose - pose_delta
        '''
        # cos method
        pose_ = np.array([[1], [1]])
        pose_delta_arr=np.array([5.0,5.0,5.0])
        cos_ac = (1+a_[0]**2+b_[0]**2+1+a_[1]**2+b_[1]**2-(a_[0]-a_[1])**2-(b_[0]-b_[1])**2)/(2*(1+a_[0]**2+b_[0]**2)**0.5*(1+a_[1]**2+b_[1]**2)**0.5)
        cos_ab = (1+a_[1]**2+b_[1]**2+1+a_[2]**2+b_[2]**2-(a_[1]-a_[2])**2-(b_[1]-b_[2])**2)/(2*(1+a_[1]**2+b_[1]**2)**0.5*(1+a_[2]**2+b_[2]**2)**0.5)
        cos_bc = (1+a_[0]**2+b_[0]**2+1+a_[2]**2+b_[2]**2-(a_[0]-a_[2])**2-(b_[0]-b_[2])**2)/(2*(1+a_[0]**2+b_[0]**2)**0.5*(1+a_[2]**2+b_[2]**2)**0.5)
        print("cos_abc:",cos_ab,cos_bc,cos_ac)
        u=1/(2);w=1/(2)
        for j in range(iter_num):
            print("--------------iter %d---------------" % j)
            J = np.zeros((2,2))
            pose = pose_.T[0]
            J[0,0]=-2*u*pose[0]+2*u*pose[1]*cos_ab; J[0][1]=2*(1-u)*pose[1]-2*cos_bc+2*u*pose[0]*cos_ab
            J[1,0]=2*(1-w)*pose[0]-2*cos_ac+2*w*pose[1]*cos_ab; J[1][1]=-2*w*pose[1]+2*w*pose[0]*cos_ab
            # print("J is:\n", J, "\t rank is:", np.linalg.matrix_rank(J))
            J_inv = np.linalg.inv(J)
            # print("J_inv is:\n", J_inv)
            f = np.zeros((2,1))
            f[0][0]=(1-u)*pose[1]**2-u*pose[0]**2-2*cos_bc*pose[1]+2*u*pose[0]*pose[1]*cos_ab+1
            f[1][0]=(1-w)*pose[0]**2-w*pose[1]**2-2*cos_ac*pose[0]+2*w*pose[0]*pose[1]*cos_ab+1
            pose_delta = J_inv @ f
            # store 3 delta number in a row
            # print("pose_delta",pose_delta_arr)
            pose_delta_arr[j%3]=abs(pose_delta[0])
            # if the average number of 3 continuous delta is less than 1, iteration ends in advance
            if(np.mean(pose_delta_arr)<=0.0005 and j>=5): 
                # rospy.loginfo("depth_avg_esti:{}".format(depth_avg))
                # rospy.loginfo("iter_num:{}".format(j))
                # rospy.loginfo("depth:{}".format(pose[0][0]))
                break
            else: 
                pose_ = pose_ - pose_delta
                # print("pose_[0][0]",pose_[0][0])
                # if(pose_[0][0]<0): pose_[0][0]=-pose_[0][0]
                # if(pose_[1][0]<0): pose_[1][0]=-pose_[1][0]
            # print(pose_)
        
        result1 = r/((1+pose_[0][0]**2-2*pose_[0][0]*cos_ac)**0.5)
        result2 = r/((1+pose_[1][0]**2-2*pose_[1][0]*cos_bc)**0.5)
        print("result1: %d, result2: %d" % (result1, result2))
        return (result1+result2)/2


def main():
    bbox1 = BoundingBox(348.0, 90.0, 445.0, 191.0)
    bbox2 = BoundingBox(299.0, 165.0, 334.0, 200.0)
    bbox3 = BoundingBox(325.0, 202.0, 345.0, 222.0)
    bbox4 = BoundingBox(326.0, 202.0, 345.0, 222.0)
    a_, b_ = get_4points2d(bbox1)
    t0 = time.time()
    pose = newton_iter(a_, b_, 150)
    t1 = time.time()
    print("time_use is:", t1-t0, "\n final pose is:", pose)
    # pose = newton_iter(a_, b_, 12)
    # t2 = time.time()
    # print("time_use is:", t2-t0, "\n final pose is:", pose)

if __name__ == "__main__":
    main()