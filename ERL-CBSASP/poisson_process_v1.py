import time
import numpy as np

def poisson_process (time_in_sec):

###########################
# random primary user time
###########################

	time_in_sec = int(np.random.poisson(time_in_sec,1))

################################
# return the value
################################

	return (time_in_sec)	

