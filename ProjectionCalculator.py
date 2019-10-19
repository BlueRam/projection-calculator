# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:04:11 2019

@author: stany
"""
import numpy as np  

class ProjectionCalculator: 
    ''' 
    Calculates the project of matrix A onto vector b.
    '''
    
    def __init__(self,A,b): 
        self.A = A 
        self.b = b 
        self.A_transpose = np.transpose(A)
        
    def calculate_projection(self): 
        A = self.A 
        b = self.b
        A_transpose = self.A_transpose
        left_side = np.matmul(A_transpose, A)
        right_side = np.matmul(A_transpose, b)
        left_side_inverse = np.linalg.inv(left_side) 
        projection_x = np.matmul(left_side_inverse, right_side)
        return(projection_x)
        
    def double_check(self):  
        A = self.A
        b = self.b
        A_transpose = self.A_transpose 
        projection_x = self.calculate_projection()
        AT_A = np.matmul(A_transpose, A)  
        left_side = np.matmul(AT_A, projection_x)
        #print("Left Side: \n", left_side)
        right_side = np.matmul(A_transpose, b)
        #print("Right Side: \n", right_side)
        if left_side.any() == right_side.any():
            print("Calculation is correct.")  
            return(True)
        else: 
            print("Calculation is incorrect.  Double check input matrices.") 
            return(False)    
            
    def calculate_error(self): 
        A = self.A
        b = self.b
        projection_x = self.calculate_projection()
        b_estimate = np.matmul(A, projection_x)
        error = b - b_estimate 
        return(error) 
            
    def print_function(self): 
        if self.double_check() == True:
            projection_x = self.calculate_projection()
            error = self.calculate_error()
        print("Projection vector: \n", projection_x)
        print("Error: \n", error)
        return(projection_x)
        
        
A = np.matrix([[1,1],
               [1,2],
               [1,3],
               [1,4]])

b = np.matrix([[163],[186],[195],[198]])    

PC = ProjectionCalculator(A, b)

PC.print_function()
        