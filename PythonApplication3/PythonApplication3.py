from math import cos,radians

# Create a string with spaces proportional to a cosine of x in degrees 
def make_dot_string(x):
    rad =radians(x)
    numspaces =int(20*cos(radians(x))+20)
    st =' '*numspaces+'o'
    return st
#what's your problem
def main():
    for i in range(0,1800,12):
        s=make_dot_string(i)
        print(s)

main()