from array import array

vals= array('u',["a","e","i"])

for e in vals:
    print(e)
    
    
    
from array import array

vals= array('i',[5,9,8,4,2])

NuevoArr= array(vals.typecode, (a*a for a in vals))

for e in NuevoArr:
    print(e)