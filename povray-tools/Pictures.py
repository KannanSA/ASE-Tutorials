#!/usr/bin/env python
from ase import Atoms
from ase.io import read, write
from ase.visualize import view
from ase_povray import povray_parameter
import numpy as np

B=read('/Users/kannansekarannuradha/Documents/Projects/ASE-Tutorials/compare-structures/0.POSCAR')
A=B.repeat((2,2,1))
view(A)

#Set atomic radii, colors and textures for all atoms
PovRay=povray_parameter(A,atoms_radii={'Zn':1.2,'O':0.74,'H':0.4,'C':0.68, 'N':0.65})

PovRay.set_colors({'Zn':(0.87,0.87,0.9),
                               'O':(1.,0.,0.),
                               'H':(1.000,1.0,1.0),
                               'N':(0.188,0.314,0.973),
                               'C':(0.25,0.25,0.25)})
PovRay.set_textures({'Zn':'jmol' ,
                               'O':'jmol',
                               'H':'jmol',
                               'C':'jmol',
                               'N':'jmol'})

#Rotate structure
PovRay.kwargs['rotation']='0x,0y,0z'

#Set bounding box and resolution
PovRay.kwargs['bbox']=(15, 12, 32, 27) #+2y
PovRay.kwargs['canvas_width']=200


at=[]
at_color=[]
at_text=[]

#Set different colors for specific atoms different colors
#at.append(568)
#at.append(569)
#at_color.append((1.0,0.5,0.0))
#at_color.append((0.5,0.2,0.05))
#PovRay.set_specific_colors(at,at_color)
#PovRay.set_specific_textures(at,at_text)

# Remove deprecated or unsupported keywords for ASE's write_pov
povray_kwargs = PovRay.kwargs.copy()
povray_kwargs.pop('run_povray', None)
povray_kwargs.pop('display', None)
povray_kwargs.pop('pause', None)
povray_kwargs.pop('transparent', None)
povray_kwargs.pop('canvas_width', None)
povray_kwargs.pop('canvas_height', None)
write('POSCAR.pov', A, format='pov', **povray_kwargs)

