from time import ctime,localtime
from layout import box_h, box_w
import os

def export_red_collisions(collisions):
    cutime=localtime()
    filename="_".join([str(x) for x in cutime[:5]])
    make_directory_if_not_exists("results/")
    file=open("results/"+filename+".txt", "w+") #export dir shall be included in .gitignore
    file.write("Atom box simulation results from "+ctime()+"\n")
    file.write("box_w "+str(box_w)+"\n")
    file.write("box_h "+str(box_h)+"\n")
    for i in collisions:
        file.write(str(i)+"\n")
    export_distances(file,collisions)

def export_distances(file, collisions):
    file.write("Distances\n")
    distances=[]
    for i in range(len(collisions)-1):
        distances.append(calculate_distance(collisions[i], collisions[i+1]))
        file.write(str(distances[i])+"\n")
    file.write("Average\n")
    avg=sum(distances)/max(collisions)[0]
    file.write(str(avg)+"\n")

def make_directory_if_not_exists(path):
    if not os.path.isdir(path):
        os.makedirs(path)

def calculate_distance(first, second): 
    """
    generic function to calculate distances
    takes three element tuples and ignores the first element
    """
    a, firstx, firsty=first
    a, secondx, secondy=second
    distance=((firstx-secondx)**2+(firsty-secondy)**2)**0.5
    return(distance)