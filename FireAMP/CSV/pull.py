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

column = sys.argv[1]
filepath = sys.argv[2]

MT = MaltegoTransform()
data = fa.parseCSV(filepath)


##########################################################################
if column == 'MD5 (Detection)':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("FireAMP.FireAMPMD5Detection",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'Filename (Parent)':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("FireAMP.FireAMPFilenameParent",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'Filepath':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("FireAMP.FireAMPFilepath",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'Remote IP':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("FireAMP.FireAMPRemoteIP",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'IP':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("FireAMP.FireAMPInternalIP",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'File Name':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("FireAMP.FireAMPFilename",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'Hostname':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("FireAMP.FireAMPHostname",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'SHA-1 (Parent)':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("FireAMP.FireAMPSHA1Parent",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'Detection Name':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("FireAMP.FireAMPDetectionName",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'URL':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("FireAMP.FireAMPURL",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'MD5 (Parent)':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("FireAMP.FireAMPMD5Parent",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'SHA-256 (Detection)':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("FireAMP.FireAMPSHA256Detection",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'SHA-256 (Parent)':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("FireAMP.FireAMPSHA256Parent",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'Time':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("FireAMP.FireAMPTime",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'Event Type':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("FireAMP.FireAMPEventType",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'SHA-1 (Detection)':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("FireAMP.FireAMPSHA1Detection",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'Port':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("FireAMP.FireAMPPort",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################

MT.returnOutput()
