#!/usr/bin/python 
######################################################################
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Written by JC (https://twitter.com/jc_socal)
# Copyright 2015
######################################################################

import sys
from MaltegoTransform import * 
import fa_parser as fa

value = sys.argv[1]

MT = MaltegoTransform()
MT.parseArguments(sys.argv)

#########################################
## lookup fieldname of sending request ##
#########################################
field = None
filepath = None
for x in MT.values:

	if x == 'properties.fireampbaseentity': continue
	if x.startswith('properties.'):
		field = fa.fieldLookup(x)
	if x.startswith('CSV File'):
		filepath = MT.values[x].replace("\\\\", "\\")

#############################
## Get the correlated data ##
#############################
data = fa.parseCSV(filepath)
query = fa.correlate(data, field, value)
result = fa.ItemsCounts(query, 'Port') ## Edit Here

####################
## Submit Results ##
####################
for entry in result:
	e = MT.addEntity("FireAMP.FireAMPPort",entry); ## Edit HEre
	e.addAdditionalFields("CSV File",filepath,True,filepath)
MT.returnOutput()