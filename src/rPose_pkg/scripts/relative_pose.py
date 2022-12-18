#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import numpy as np
from rPose_ros.msg import BoundingBoxes
from std_msgs.msg import Float64MultiArray

class RPose_Dect:
    def __init__(self):
        self.fx = 320
        self.fy = 320
        self.cx = 320
        self.cy = 240
        self.height = 480
        self.width = 640
        self.depthScale = 0.5

        # TODO: define the radius of all kinds of circle
        self.r_c = 100.0 # radius of Ccircle(cm)
        self.r_s = 100.0 # radius of Scircle(cm)

        # self.J = np.zeros((8,8))
        # self.J_inv = np.zeros((8,8))
        self.J = np.zeros((2,2))
        self.J_inv = np.zeros((2,2))

        self.bounding_box_topic = '/yolov5/BoundingBoxes'
        self.bounding_box_sub = rospy.Subscriber(self.bounding_box_topic,BoundingBoxes,self.bbox_sub_callback)

        self.rPose_topic = '/rPose_ros/rPose'
        self.rPose_pub = rospy.Publisher(self.rPose_topic, Float64MultiArray, queue_size = 1)

    def get_4points2d(self, boundingBoxes):
        #TODO:determine the r
        r = self.r_c
        bboxes = boundingBoxes.bounding_boxes
        a_list=[]; b_list=[];depth_u=[];depth_v=[];cnt=0
        for bbox in bboxes:
            xmid = (bbox.xmin+bbox.xmax)/2; ymid = (bbox.ymin+bbox.ymax)/2
            a1 = (bbox.xmin-self.cx)/self.fx
            a2 = (xmid-self.cx)/self.fx
            # a3 = (bbox.xmax-self.cx)/self.fx
            # a4 = a2
            a0 = a2
            b1 = (ymid-self.cy)/self.fy
            b2 = (bbox.ymin-self.cy)/self.fy
            # b3 = b1
            b0 = b1
            # b4 = (bbox.ymax-self.cy)/self.fy
            # depth_u.append(self.fx*2*r/(bbox.xmax-bbox.xmin))
            # depth_v.append(self.fy*2*r/(bbox.ymax-bbox.ymin))
            a_list.append([a0, a1, a2])
            b_list.append([b0, b1, b2])
            cnt+=1
        # return a_list, b_list, cnt, depth_u, depth_v
        return a_list, b_list, cnt

    # default number of iteration is 50
    def newton_iter(self, a_, b_, r, iter_num = 50):
        # initial
        self.pose_delta_arr=np.array([5,5,5])
        # depth_avg = (depth_u_+depth_v_)/2
        # stero method
        '''
        self.pose = np.array([[depth_avg], [depth_avg-50], [depth_avg-25], [depth_avg+25], [depth_avg+50], [1], [1], [1]])
        for j in range(iter_num):
            # print("--------------iter %d---------------" % j)
            self.J = np.zeros((8,8))
            pose = self.pose.T[0]
            for i in range(4):
                self.J[i][0] = -2*a_[0]*(a_[i+1]*pose[i+1]-a_[0]*pose[0]) - 2*b_[0]*(b_[i+1]*pose[i+1]-b_[0]*pose[0]) - 2*(pose[i+1]-pose[0])
                self.J[i][i+1] = 2*a_[i+1]*(a_[i+1]*pose[i+1]-a_[0]*pose[0]) + 2*b_[i+1]*(b_[i+1]*pose[i+1]-b_[0]*pose[0]) + 2*(pose[i+1]-pose[0])
            for i in range(4):
                self.J[i+4][0] = -pose[5]*a_[0] - pose[6]*b_[0] - pose[7]
                self.J[i+4][i+1] = pose[5]*a_[i+1] + pose[6]*b_[i+1] + pose[7]
                self.J[i+4][5] = a_[i+1]*pose[i+1] - a_[0]*pose[0]
                self.J[i+4][6] = b_[i+1]*pose[i+1] - b_[0]*pose[0]
                self.J[i+4][7] = pose[i+1] - pose[0]
            # print("J is:\n", J, "\t rank is:", np.linalg.matrix_rank(J))
            self.J_inv = np.linalg.inv(self.J)
            # print("J_inv is:\n", J_inv)
            self.f = np.zeros((8,1))
            for i in range(4):
                self.f[i][0] = (a_[i+1]*pose[i+1]-a_[0]*pose[0])**2 + (b_[i+1]*pose[i+1]-b_[0]*pose[0])**2 + (pose[i+1]-pose[0])**2 - r**2
            for i in range(4):
                self.f[i+4][0] = pose[5]*(a_[i+1]*pose[i+1]-a_[0]*pose[0]) + pose[6]*(b_[i+1]*pose[i+1]-b_[0]*pose[0]) + pose[7]*(pose[i+1]-pose[0])
            self.pose_delta = self.J_inv @ self.f
            # store 3 delta number in a row
            self.pose_delta_arr[j%3]=abs(self.pose_delta[0])
            # if the average number of 3 continuous delta is less than 1, iteration ends in advance
            if(np.mean(self.pose_delta_arr)<=1 and j>=5): 
                # rospy.loginfo("depth_avg_esti:{}".format(depth_avg))
                # rospy.loginfo("iter_num:{}".format(j))
                # rospy.loginfo("depth:{}".format(self.pose[0][0]))
                break
            else: self.pose = self.pose - self.pose_delta
        return self.pose[0][0]
        '''
        # cos method
        self.pose = np.array([[1], [1]])
        self.pose_delta_arr=np.array([5,5,5])
        cos_ac = (1+a_[0]**2+b_[0]**2+1+a_[1]**2+b_[1]**2-(a_[0]-a_[1])**2-(b_[0]-b_[1])**2)/(2*(1+a_[0]**2+b_[0]**2)**0.5*(1+a_[1]**2+b_[1]**2)**0.5)
        cos_ab = (1+a_[1]**2+b_[1]**2+1+a_[2]**2+b_[2]**2-(a_[1]-a_[2])**2-(b_[1]-b_[2])**2)/(2*(1+a_[1]**2+b_[1]**2)**0.5*(1+a_[2]**2+b_[2]**2)**0.5)
        cos_bc = (1+a_[0]**2+b_[0]**2+1+a_[2]**2+b_[2]**2-(a_[0]-a_[2])**2-(b_[0]-b_[2])**2)/(2*(1+a_[0]**2+b_[0]**2)**0.5*(1+a_[2]**2+b_[2]**2)**0.5)
        u=1/(2);w=1/(2)
        for j in range(iter_num):
            # print("--------------iter %d---------------" % j)
            self.J = np.zeros((2,2))
            pose = self.pose.T[0]
            self.J[0,0]=-2*u*pose[0]+2*u*pose[1]*cos_ab; self.J[0][1]=2*(1-u)*pose[1]-2*cos_bc+2*u*pose[0]*cos_ab
            self.J[1,0]=2*(1-w)*pose[0]-2*cos_ac+2*w*pose[1]*cos_ab; self.J[1][1]=-2*w*pose[1]+2*w*pose[0]*cos_ab
            # print("J is:\n", J, "\t rank is:", np.linalg.matrix_rank(J))
            self.J_inv = np.linalg.inv(self.J)
            # print("J_inv is:\n", J_inv)
            self.f = np.zeros((2,1))
            self.f[0][0]=(1-u)*pose[1]**2-u*pose[0]**2-2*cos_bc*pose[1]+2*u*pose[0]*pose[1]*cos_ab+1
            self.f[1][0]=(1-w)*pose[0]**2-w*pose[1]**2-2*cos_ac*pose[0]+2*w*pose[0]*pose[1]*cos_ab+1
            self.pose_delta = self.J_inv @ self.f
            # store 3 delta number in a row
            self.pose_delta_arr[j%3]=abs(self.pose_delta[0])
            # if the average number of 3 continuous delta is less than 1, iteration ends in advance
            if(np.mean(self.pose_delta_arr)<=0.0005 and j>=5): 
                # rospy.loginfo("depth_avg_esti:{}".format(depth_avg))
                # rospy.loginfo("iter_num:{}".format(j))
                # rospy.loginfo("depth:{}".format(self.pose[0][0]))
                break
            else: self.pose = self.pose - self.pose_delta
        result1 = r/(1+self.pose[0][0]**2-2*self.pose[0][0]*cos_ac)**0.5
        result2 = r/(1+self.pose[1][0]**2-2*self.pose[1][0]*cos_bc)**0.5
        # print("result1: %d, result2: %d" % (result1, result2))
        if(result1>result2): return result1
        else: return result2

    def getXYZ(self, a0, b0, depth):
        return np.array([[a0*depth, b0*depth, depth]])

    def bbox_sub_callback(self, boundingBoxes):
        a, b, cnt = self.get_4points2d(boundingBoxes)
        XYZ = np.zeros((1,3))
        for i in range(cnt):
            #TODO:determine the r
            r = self.r_c
            depth = abs(self.newton_iter(a[i], b[i], r))
            if(XYZ[0][0]==0):
                XYZ = self.getXYZ(a[i][0], b[i][0], depth)
            else:
                XYZ = np.append(XYZ, self.getXYZ(a[i][0], b[i][0], depth), axis=1)
        self.XYZ_arr = Float64MultiArray(data=XYZ[0])
        # rospy.loginfo("XYZ_arr:{}".format(self.XYZ_arr))
        self.rPose_pub.publish(self.XYZ_arr)

    '''
    def bbox_sub_callback(self, boundingBoxes):
        Z0, Z1, Z2, Z3, Z4, A, B, C = sympy.symbols('Z0 Z1 Z2 Z3 Z4 A B C')  # 未知数
        eq1 = (a1*Z1-a0*Z0)**2+(b1*Z1-b0*Z0)**2+(Z1-Z0)**2-r**2
        eq2 = (a2*Z2-a0*Z0)**2+(b2*Z2-b0*Z0)**2+(Z2-Z0)**2-r**2
        eq3 = (a3*Z3-a0*Z0)**2+(b3*Z3-b0*Z0)**2+(Z3-Z0)**2-r**2
        eq4 = (a4*Z4-a4*Z0)**2+(b4*Z4-b0*Z0)**2+(Z4-Z0)**2-r**2
        eq5 = A*(a1*Z1-a0*Z0)+B*(b1*Z1-b0*Z0)+C*(Z1-Z0)
        eq6 = A*(a2*Z2-a0*Z0)+B*(b2*Z2-b0*Z0)+C*(Z2-Z0)
        eq7 = A*(a3*Z3-a0*Z0)+B*(b3*Z3-b0*Z0)+C*(Z3-Z0)
        eq8 = A*(a4*Z4-a0*Z0)+B*(b4*Z4-b0*Z0)+C*(Z4-Z0)
        sol = sympy.solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8),
            (Z0, Z1, Z2, Z3, Z4, A, B, C))  # 求解
        return sol
    '''

def main():
    rospy.init_node('relative_pose_pkg', anonymous=True)
    rPose_Dect = RPose_Dect()
    rospy.spin()


if __name__ == "__main__":
    main()