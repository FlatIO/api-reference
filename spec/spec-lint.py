#! /usr/bin/env python
'''
Copyright (c) 2022, Tutteo Limited. All rights reserved.
'''

import ruamel.yaml
from ruamel.yaml.scalarstring import PreservedScalarString, preserve_literal

infname = "openapi.yaml"

def walk_tree(base):
	if isinstance(base, dict):
		for k in base:
			v = base[k]
			if isinstance(v, str) and '\n' in v:
				base[k] = preserve_literal(v)
			else:
				walk_tree(v)
	elif isinstance(base, list):
		for idx, elem in enumerate(base):
			if isinstance(elem, str) and '\n' in elem:
				base[idx] = preserve_literal(v)
			else:
				walk_tree(elem)


with open(infname, 'r') as fi:
	data = ruamel.yaml.round_trip_load(fi)

walk_tree(data)

with open(infname, 'w') as fo:
	ruamel.yaml.round_trip_dump(data, fo, width=10000)
