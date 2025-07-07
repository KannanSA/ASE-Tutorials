#!/usr/bin/env python

import ase.io.vasp as io
import spglib
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file",
                  action="store", type="string", dest="file", default="POSCAR",
                  help="Path to input file [default: ./POSCAR]")
parser.add_option("-p", "--prec",
                  action="store", type="float", dest="prec", default=0.001,
                  help="Precision for symmetry test [default: 0.001]")
(options, args) = parser.parse_args()


# Read POSCAR/CONTCAR using ASE and convert to spglib input
bulk = io.read_vasp(options.file)
# spglib expects a tuple: (lattice, positions, numbers)
lattice = bulk.get_cell()
positions = bulk.get_scaled_positions()
numbers = bulk.get_atomic_numbers()
cell = (lattice, positions, numbers)
spacegroup = spglib.get_spacegroup(cell, symprec=options.prec)

print("Spacegroup information.")
print("-----------------------")
print(spacegroup)
print("-----------------------")
