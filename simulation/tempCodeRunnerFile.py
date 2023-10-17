# allocate molecules to move; set destination to benzine
for i in range(len(mol_array)):
    objects[i].dest['x'] = mol_array[i][0]
    objects[i].dest['y'] = mol_array[i][1]
    objects[i].active = True
# objects[37].dest = {'x': mol_array[2][0], 'y': mol_array[2][1]}
# objects[37].active = True
# objects[12].dest = {'x': mol_array[4][0], 'y': mol_array[4][1]}
# objects[12].active = True
# objects[43].dest = {'x': mol_array[3][0], 'y': mol_array[3][1]}
# objects[43].active = True
# objects[18].dest = {'x': mol_array[5][0], 'y': mol_array[5][1]}
# objects[18].active = True
# objects[0].dest = {'x': mol_array[0][0], 'y': mol_array[0][1]}
# objects[0].active = True
# objects[1].dest = {'x': mol_array[1][0], 'y': mol_array[1][1]}
# objects[1].active = True
