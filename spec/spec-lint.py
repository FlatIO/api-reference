#! /usr/bin/env python

import ruamel.yaml
from ruamel.yaml.scalarstring import PreservedScalarString, preserve_literal
from ruamel.yaml.compat import string_types

infname = "swagger.yaml"

def walk_tree(base):
	if isinstance(base, dict):
		for k in base:
			v = base[k]
			if isinstance(v, string_types) and '\n' in v:
				base[k] = preserve_literal(v)
			else:
				walk_tree(v)
	elif isinstance(base, list):
		for idx, elem in enumerate(base):
			if isinstance(elem, string_types) and '\n' in elem:
				base[idx] = preserve_literal(v)
			else:
				walk_tree(elem)


with open(infname, 'r') as fi:
	data = ruamel.yaml.round_trip_load(fi)

walk_tree(data)

with open(infname, 'w') as fo:
	ruamel.yaml.round_trip_dump(data, fo, width=10000)
