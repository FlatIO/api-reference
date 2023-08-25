#! /usr/bin/env python3
'''
Copyright (c) 2022-2023, Tutteo Limited.
'''

from copy import deepcopy
import ruamel.yaml
from ruamel.yaml.scalarstring import PreservedScalarString, preserve_literal

infname = 'openapi.yaml'
outfname = 'openapi-flatten.yaml'

models_flatten = []
models_used_as_ref = []

def walk_tree(base, in_inheritance=False):
	if isinstance(base, dict):
		for k in base.keys():
			v = base[k]
			if not in_inheritance and k == '$ref':
				schema_key = v.split('/').pop()
				models_used_as_ref.append(schema_key)
			if isinstance(v, str) and '\n' in v:
				base[k] = preserve_literal(v)
			else:
				# flatten allOf for code generator
				if k == 'allOf' or k == 'oneOf':
					children_props = {}
					required = []
					for children_set in base[k]:
						# $ref to another schema
						if '$ref' in children_set:
							schema_key = children_set['$ref'].split('/').pop()
							models_flatten.append(schema_key)
							children_ref = walk_tree(data['components']['schemas'][schema_key], in_inheritance=True)

							if children_ref != 'remove':
								# Properties from children
								children_props.update(deepcopy(walk_tree(children_ref['properties'])))
								# Combine required arrays
								if 'required' in children_ref and children_ref['required'] is not None:
									required.extend(children_ref['required'])

						# direct children props
						else:
							children_props.update(deepcopy(walk_tree(children_set['properties'])))

					result = {
						'type': 'object',
						'properties': children_props,
					}
					if len(required) > 0:
						required.sort()
						result['required'] = required
					return result

				# walk childrens
				result = walk_tree(v)
				if result == 'remove':
					del base[k]
				elif result is not None:
					base[k] = result
		if len(base.keys()) == 0:
			return 'remove'
	elif isinstance(base, list):
		for idx, elem in reversed(list(enumerate(base))):
			if isinstance(elem, str) and '\n' in elem:
				base[idx] = preserve_literal(v)
			else:
				result = walk_tree(elem)
				if result == 'remove':
					del base[idx]
				elif result is not None:
					base[idx] = result
	return base

with open(infname, 'r') as fi:
	data = ruamel.yaml.round_trip_load(fi)

walk_tree(data)

# Remove unused models left after flattening allOf/oneOf
unused_models = list(set(models_flatten) - set(models_used_as_ref))
print(unused_models)
for model in unused_models:
	if model in data['components']['schemas']:
		del data['components']['schemas'][model]

with open(outfname, 'w') as fo:
	ruamel.yaml.round_trip_dump(data, fo, width=10000)
