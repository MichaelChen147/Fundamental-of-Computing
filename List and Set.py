Set:

# Example1
# set immutable in loop
instructors = set(['Rixner', 'Warren', 'Greiner', 'Wong'])
print instructors

def get_rid_of(inst_set, starting_letter):
    remove_set = set([])
    for inst in inst_set:
        if inst[0] == starting_letter:
            remove_set.add(inst)
    inst_set.difference_update(remove_set)

get_rid_of(instructors, 'W')
print instructors

# Example2
# use list() to avoid the situation where set is immutable in loop
rs = set([])
for s in myset:
    rs.add(s)
myset.d_u(rs)

or 

for s in list(myset):
    myset.remove(s)
    
#Example3
# cell[row][col]
cells = [ [... for dummy_col in range(grid_width)] for dummy_row in range(grid_height)]

