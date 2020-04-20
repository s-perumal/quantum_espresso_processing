# Program to extract lattice constants from espresso relaxation calculations
#Sathya S R R Perumal Phd
# 2020 March
#espresso_read.py espresso_output_file

import re
import sys
import numpy as np


def sanitize(matrix_row):
    matrix_row = [t for t in matrix_row if t]
    return matrix_row

espresso_out = open(sys.argv[1],mode="r+")

content = espresso_out.read()

content_print = re.findall(r'Begin final coordinates(.*?)End final coordinates',content,re.DOTALL)
#print(" ".join(content_print))
content_print_1 = "".join(content_print)
#print(content_print_1)
#print(content_print_1)
#content_print_2 = tuple(content_print('\n')[:-1])
content_print_2 = content_print_1.split('\n')

print(content_print_2[1])

volume = sanitize(content_print_2[1].split(" "))
#print("Volume ", volume[4], volume[5], volume[6])

print(content_print_2[2])

#print(content_print_2[5])

#print("before alat",content_print_2[4])


matrix_row_1 = content_print_2[5].split(" ")
matrix_row_2 = content_print_2[6].split(" ")
matrix_row_3 = content_print_2[7].split(" ")
#print(matrix_row_1)



alat = re.findall(r'\d*\.\d*',content_print_2[4])

#alat = re.match(r'\d*\.\d*',content_print_2[4])


matrix_row_1 = sanitize(matrix_row_1)
matrix_row_2 = sanitize(matrix_row_2)
matrix_row_3 = sanitize(matrix_row_3)
alat = sanitize(alat)


#print(matrix_row_1)
#print(matrix_row_2)
#print(matrix_row_3)

def real_numbers(matrix_row):
    matrix_row = list(np.float_(matrix_row))
    return matrix_row


#cell_matrix = np.array([ real_numbers(matrix_row_1), real_numbers(matrix_row_2), real_numbers(matrix_row_3) ])

cell_matrix = np.array([matrix_row_1, matrix_row_2, matrix_row_3])


cell_matrix = np.array(real_numbers(cell_matrix))

alat = real_numbers(alat)

#print(alat)

bohr_radius_angs = [ 0.52917720859 ]

bohr_radius_angs = real_numbers(bohr_radius_angs)

#print(type(bohr_radius_angs),type(alat))

coeff = alat[0] * bohr_radius_angs[0]

cell_matrix = coeff * np.array(cell_matrix)

matrix_row_1 = real_numbers(matrix_row_1)
matrix_row_2 = real_numbers(matrix_row_2)
matrix_row_3 = real_numbers(matrix_row_3)

#print(matrix_row_1)

norm1 = matrix_row_1[0]*matrix_row_1[0] + matrix_row_1[1]*matrix_row_1[1] + matrix_row_1[2]*matrix_row_1[2]
norm2 = matrix_row_2[0]*matrix_row_2[0] + matrix_row_2[1]*matrix_row_2[1] + matrix_row_2[2]*matrix_row_2[2]
norm3 = matrix_row_3[0]*matrix_row_3[0] + matrix_row_3[1]*matrix_row_3[1] + matrix_row_3[2]*matrix_row_3[2]

print("a:",norm1*coeff,"b:",norm2*coeff,"c:",norm3*coeff)

#gamma = sum([x*y in x,y in zip(matrix_row_1,matrix_row_2)])
gamma = np.dot(matrix_row_1,matrix_row_2)/( norm1 * norm2 )
beta  = np.dot(matrix_row_1,matrix_row_3)/( norm1 * norm3 )
alpha = np.dot(matrix_row_2,matrix_row_3)/( norm2 * norm3 )

deg = 180.0/np.pi

print("alpha:",np.arccos(alpha)*deg,"beta:",np.arccos(beta)*deg,"gamma:",np.arccos(gamma)*deg)

#print(cell_matrix)
#map(float,cell_matrix)

#print(cell_matrix)



#list(np.float_(cell_matrix))

#x = np.array([[1.5,2.3],[3.4,4.5]])
#y = np.linalg.inv(x)
#print(y)
#print(str(cell_matrix))

#print(np.linalg.inv(cell_matrix),)

#print(type(cell_matrix)) numpy.ndarray

#print(np.multiply(cell_matrix*cell_matrix))
#print(numpy.sqrt(cell_matrix))
#print(np.linalg.inv(cell_matrix))

#print(cell_matrix)
#matrix_row_1 = [ t for t in matrix_row_1 if t]

#print((matrix_row_3)
#print(matrix_row_1)
#print(matrix_row_2)

espresso_out.close()

#items = re.findall(r'new.*$',content_print,re.DOTALL)
#print(items)

#print(content_print.split())
#t1 = content_print.
#print(t1)

#for line in content_print:
#    if "new unit-cell" in line:
#        print(line)
#volume = re.findall(r'new unit-cell volume(.*?)density',content,re.DOTALL)
#print(volume)

#for line in content_print:
    #if 'density' in line:
     # print(line)


   # volume = re.findall(r'new unit-cell volume',line,re.DOTALL)





