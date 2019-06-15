# Original source: https://gist.github.com/xesscorp/8a2ed1b8923f04ae6366
# Edit by Jarek Paral <paral@robotikabrno.cz>

#
# KiCad outputs Gerber files with extensions that aren't recognized by the most commonly used 
# PCB manufacturers. This Python script renames the files to what want manufactory Gatema for
# (company in Czech Republic which produce PCB - http://www.gatema.cz) Pool servis - prototype PCB
# (http://pcb.gatema.cz/kriteria-dat-pro-pool-servis/).
# Just execute this script in your KiCad project directory and the Gerber files will be renamed.
#
# Last update: 2019-06-15

import glob
import os

# Make a list of .gbr and .drl files in the current directory.
gerbers = glob.glob('*.gbr')
gerbers.extend(glob.glob('*.drl'))

# File renaming rules.
gerber_types = [
    {'from': '-B_SilkS.gbr',   'to': '-B_SilkS.gbr.plb'},
    {'from': '-B_Mask.gbr',    'to': '-B_Mask.gbr.smb'},
    {'from': '-B_Cu.gbr',      'to': '-B_Cu.gbr.bot'},
    {'from': '-Inner1_Cu.gbr', 'to': '.G2L'},
    {'from': '-Inner2_Cu.gbr', 'to': '.G3L'},
    {'from': '-F_Cu.gbr',      'to': '-F_Cu.gbr.top'},
    {'from': '-F_Mask.gbr',    'to': '-F_Mask.gbr.smt'},
    {'from': '-F_SilkS.gbr',   'to': '-F_SilkS.gbr.plt'},
    {'from': '-Edge_Cuts.gbr', 'to': '-Edge_Cuts.gbr.dim'},
    {'from': '-NPTH.drl',      'to': '-NPTH.drl.mil'},
    {'from': '.drl',           'to': '.drl.pth'},
]

if len(gerbers) == 0:
    print "No files found with this extensions: "
    for type in gerber_types:
        print "\t" + type['from'] + ""
    print "\nEND of script."
else:
    print "Load files:"
    for g in gerbers:
        print g
    print "\n",
    
    print "Start renaming:"
    # Rename files depending upon their names.
    for g in gerbers:
        for t in gerber_types:
            if g.endswith(t['from']):
                # Strip the 'from' string from the old name and append the 'to' string to make the new name.
                new_g = g[:-len(t['from'])] + t['to']
                # Remove any existing file having the new name.
                print "\t" + g + " -> " + new_g
                try:
                    os.remove(new_g)
                except:
                    # An exception occurred because the file we tried to remove probably didn't exist.
                    pass
                # Rename the old file with the new name.
                os.rename(g, new_g)
                break

raw_input('Press Enter to exit.')
