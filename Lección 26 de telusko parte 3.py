from array import array
vals= array('i',[5,9,8,4,2])
NuevoArr= array(vals.typecode, (a*a for a in vals))


i=0
while i <len(NuevoArr):
    print(NuevoArr(i))
    i+=1
    
    
    