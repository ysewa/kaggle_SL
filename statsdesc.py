import pandas as pd 
import numpy as np
from statsdesc_source import *

data_path='../data/'

print 'Loading the data: \n'
data_train=pd.read_csv(data_path+'train.csv', sep=',', header=0)


print 'Head of the dataset:	'
print data_train.head()
print '\n'

print 'Short summary info of the dataset:'
print data_train.info()
print '\n'

dict_table=get_info_type_of_variables(data_train)

print 'Type of variables in the dataset:'
print np.unique(dict_table.values()).tolist()
print '\n'

dict_type, dict_nb_type = get_variables_with_type(data_train)

print 'Number of variables of each type:'
print dict_nb_type
print '\n'

#new_dataset=conv_bool_to_int(data_train, dict_type['bool'])
#{'bool': 13, 'float64': 28, 'int64': 1862, 'object': 31}
new_dataset=factorize_categories(data_train, dict_type['object'])

print new_dataset['VAR_0010']
print new_dataset['VAR_0466']

dict_fill_rate={}
n=len(data_train)
for  col in data_train.columns:
	dict_fill_rate[col]=float(len(data_train[col][np.isnan(data_train[col])]))/n*100





