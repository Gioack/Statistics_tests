import numpy as np

def calculate(list):
    try:
        calculations = dict()
        array = np.array(list)
        array = array.reshape(3,3)
        
        axis1_mean = array.mean(axis = 0)
        axis2_mean = array.mean(axis = 1)
        flattened_mean = array.mean()
        calculations["mean"] = [axis1_mean.tolist(),axis2_mean.tolist(), flattened_mean.tolist()]
        print(calculations)
        
        axis1_variance = array.var(axis = 0)
        axis2_variance = array.var(axis = 1)
        flattened_variance = array.var()
        calculations["variance"] = [axis1_variance.tolist(),axis2_variance.tolist(), flattened_variance.tolist()]
        
        axis1_deviation = array.std(axis = 0)
        axis2_deviation = array.std(axis = 1)
        flattened_deviation = array.std()
        calculations["standard deviation"] = [axis1_deviation.tolist(),axis2_deviation.tolist(), flattened_deviation.tolist()]
        
        axis1_max = array.max(axis = 0)
        axis2_max = array.max(axis = 1)
        flattened_max = array.max()
        calculations["max"] = [axis1_max.tolist(),axis2_max.tolist(), flattened_max.tolist()]
        
        axis1_min = array.min(axis = 0)
        axis2_min = array.min(axis = 1)
        flattened_min = array.min()
        calculations["min"] = [axis1_min.tolist(),axis2_min.tolist(), flattened_min.tolist()]
        
        axis1_sum = array.sum(axis=0)
        axis2_sum = array.sum(axis=1)
        flattened_sum = array.sum()
        calculations["sum"] = [axis1_sum.tolist(),axis2_sum.tolist(), flattened_sum.tolist()]
        return calculations
    except ValueError:
        raise ValueError("List must contain nine numbers.")
print(calculate([2,6,2,8,4,0,1,]))
