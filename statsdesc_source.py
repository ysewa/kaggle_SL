import numpy as np
import pandas as pd

def get_info_type_of_variables(dataset):
	"""
	input: dataset
	output: a dictionary
	Give a dictionay of all the variables with their type. 
	"""
	dict_table={}
	for var in [dataset[col] for col in dataset.columns]:
		dict_table[var.name]=var.dtype
	return dict_table

def get_variables_with_type(dataset):
	"""
	return a dictionary with all the type and the list of varaibles of this type
	and the dictionary of the different types and the number of variables of this type
	"""
	dict_table=get_info_type_of_variables(dataset)
	dict_type={}
	dict_nb_type={}
	for typ in np.unique(dict_table.values()).tolist():
		key_list=[]
		count=0
		for key,val in dict_table.items():
			if val==typ:
				count+=1
				key_list.append(key)
			dict_type[str(typ)]=key_list
			dict_nb_type[str(typ)]=count
	return dict_type, dict_nb_type

def conv_bool_to_int(dataset, list_of_bool):
	"""
	convert boolean variables into binary variables
	"""
	for var in list_of_bool:
		dataset[var]=dataset[var].astype(int)
	return dataset

def factorize_categories(dataset, list_of_cat):
	"""
	factorize categorical variables into factors.
	"""
	for var in list_of_cat:
		dataset[var]=pd.Categorical.from_array(dataset[var]).labels
	return dataset
	
