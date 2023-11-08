class Molecule:
    _mcule = ""
    _coordinates = {}

    def __init__(self, mcule):
        self.mcule = mcule
        #creates dictionary of molecule destinations, and type of molecule
        if mcule == "NITRIC_ACID":
            self.coordinates = {'O': [(5, 5), (5, 7), (7, 6)], 'N': [(6, 6)], 'H': [(8, 6)]}
        elif mcule == "SULFURIC_ACID":
            self.coordinates = {'O': [(7, 3), (5, 5), (9, 5), (7, 7)], 'S': [(7, 5)], 'H': [(3, 5) (7, 9)]}
        elif mcule == "ACETIC_ACID":
            self.coordinates = {'H': [(3, 6), (4, 5), (4, 7)], 'C': [(4, 6), (5, 6)],'O': [(6, 5), (6, 7)]}
        elif mcule == "AMMONIUM":
            self.coordinates = {'N': [(6, 6)], 'H': [()]}
    #gets coordinates
    def getCoords(self):
        return self.coordinates

    #get molecule type
    def getMolecule(self):
        return self.mcule
    
    #maybe returns another dictionary of the colors?
    #how to do colors - rbg values? idk, however controls wants them.
    #assign colors to coordinates; or maybe just change the key value?
    #or maybe assign colors to sphero IDs; probably better
    def getColor(self, mcule):
        color = {}
        for key in self.coordinates:
            if key == 'O':
