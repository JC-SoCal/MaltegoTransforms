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

import csv
import sys

def parseCSV(filepath):
	data = []
	header = None

	with open(filepath) as csvfile:
		filereader = csv.reader(csvfile, delimiter=',')
		for row in filereader:

			if header == None: 
				header = row #set header
				continue

			entry  = {}
			for i in range(len(header)):
				entry[header[i]] = row[i]

			data.append(entry)

	return data

def ItemsCounts(data, ColName):
	items = {}
	for entry in data:
		if entry[ColName] == '': continue # get rid of blank lines
		if entry[ColName] in items.keys():
			items[entry[ColName]] += 1
		else:
			items[entry[ColName]] = 1
	return items

def correlate(data, ColName, term):
	items = []
	for entry in data:
		if entry[ColName] == term:
			items.append(entry)
	return items

def fieldLookup(value):
	data = {
			'properties.fireampmd5detection':'MD5 (Detection)',
			'properties.fireampfilenameparent':'Filename (Parent)',
			'properties.fireampfilepath':'Filepath',
			'properties.fireampremoteip':'Remote IP',
			'properties.fireampinternalip':'IP',
			'properties.fireampfilename':'File Name',
			'properties.fireamphostname':'Hostname',
			'properties.fireampsha1parent':'SHA-1 (Parent)',
			'properties.fireampdetectionname':'Detection Name',
			'properties.fireampurl':'URL',
			'properties.fireampmd5parent':'MD5 (Parent)',
			'properties.fireampsha256detection':'SHA-256 (Detection)',
			'properties.fireampsha256parent':'SHA-256 (Parent)',
			'properties.fireamptime':'Time',
			'properties.fireampeventtype':'Event Type',
			'properties.fireampsha1detection':'SHA-1 (Detection)',
			'properties.fireampport':'Port'
	}
	return data[value]