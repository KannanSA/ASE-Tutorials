# ASE-Tutorials

Examples of using the Atomic Simulation Environment for making research easier.  See their installation [guide](https://wiki.fysik.dtu.dk/ase/download.html). Installation on OS X should now be as simple as:
```
brew install pygtk
pip install ase
```

### spacegroup

Requires [spglib](http://spglib.sourceforge.net/python-spglib.html#python-spglib) to be installed.
```
pip install spglib
```
To run:
```
python3 get_spg.py -f CONTCAR.zincblende
```

### convert-structures

```
pythonn3 convert_structure.py -f 958456.cif
```

### compare-structures
```
python3 compare_structures.py
````

### ase-db (database)

```
juypter notebook ase-db.ipynb
```

### LAMMPS-forcefield
```
juypter notebook ForceFields.ipynb
```

### VASP-bandstructures
```
juypter notebook SiBandsASE.ipynb
```

