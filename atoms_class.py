import math
import copy


from class_data import Data

class Atoms(object):
    # считывает атомы из заданного файла
    # сколько их, смотрит в файле
    # параметры ячейки тоже знает
    def __init__(self, filename):
        f = open(filename, 'r')

        atoms_start = 0 # first line with info about atoms
        atomsnumber = 0
        str_counter = 0
        atomscounter = 0

        self.atoms = [[]]

        for line in f:
            str_counter += 1

            if line.endswith(" xlo xhi\n"):
                line_splitted = line.split()
                self.xlo = float(line_splitted[0])
                self.xhi = float(line_splitted[1])

            if line.endswith(" ylo yhi\n"):
                line_splitted = line.split()
                self.ylo = float(line_splitted[0])
                self.yhi = float(line_splitted[1])

            if line.endswith(" zlo zhi\n"):
                line_splitted = line.split()
                self.zlo = float(line_splitted[0])
                self.zhi = float(line_splitted[1])

            if line.endswith("atoms\n"):
                line_splitted = line.split()
                atomsnumber = int(line_splitted[0])
                for i in range(atomsnumber):
                    self.atoms.append([0, 0, 0, 0])

            if line.startswith("Atoms"):
                line_splitted = line.split()
                atoms_start = str_counter + 2

            if (atomsnumber and
            atoms_start and
            str_counter >= atoms_start and
            atomscounter < atomsnumber):
                atomscounter += 1
                line_splitted = line.split()
                self.atoms[int(line_splitted[0])][0] = int(line_splitted[2]) # type 
                self.atoms[int(line_splitted[0])][1] = float(line_splitted[4]) # x
                self.atoms[int(line_splitted[0])][2] = float(line_splitted[5]) # y
                self.atoms[int(line_splitted[0])][3] = float(line_splitted[6]) # z

        f.close()

