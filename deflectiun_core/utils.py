from pprint import pprint

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

def dict_to_class(_dict):
    ''' Works only on a one nested level dict '''

    for i in _dict:
        if type(_dict[i]) == dict:
            _dict[i] = dotdict(_dict[i])
    
    return dotdict(_dict)

def round_to_nearest(num, nearest):
    return round(num/nearest) * nearest