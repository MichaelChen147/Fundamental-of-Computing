Set:

# Example1

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

rs = set([])
for s in myset:
    rs.add(s)
myset.d_u(rs)

or 

for s in list(myset):
    myset.remove(s)

