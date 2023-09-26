import numpy as np

def nominal_resolution():
    for i in range(1,7):
        max_horizon = 0
        with open(f"figure{i}.txt", 'r') as file:
            size = float(file.readline())
            file.readline()
            for line in file:
                elements=np.array(line.split())
                if any(elements[elements=='1']):
                    len_line = sum(map(int, line.split()))
                    if (len_line > max_horizon):
                        max_horizon = len_line
        if (max_horizon >0):
            print(f"The nominal resolution for figure{i} is:", size/max_horizon)
        else:
            print("There is no image")

def work_with_file(filename):
    offset=[0,0]
    y=0
    x=0
    with open(filename, 'r') as file:
        for line in file:
            if line =="30\n" or line=="#\n":
                continue
            elements=np.array(line.split())
            if any(elements[elements=='1']):
                for num in elements:
                    if num =='0':
                        x+=1
                    else:
                        x+=1
                        offset[0]=x
                        break
                y+=1
                offset[1]=y
                break
            else:
                y+=1
    return offset
            

files=["img1.txt","img2.txt"]

offsetimg1 = work_with_file(files[0])
offsetimg2 = work_with_file(files[1])

print(f"Offset of the first relative to the second(y, x): {offsetimg1[1]-offsetimg2[1],offsetimg2[0]-offsetimg1[0]}", end='\n\n\n')

nominal_resolution()