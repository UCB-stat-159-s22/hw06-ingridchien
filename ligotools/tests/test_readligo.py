from ligotools import readligo
import numpy as np
import json

def test_hdf5_structure():
    H1 = readligo.read_hdf5('data/H-H1_LOSC_4_V2-1126259446-32.hdf5')
    
    assert len(H1) == 7
    assert type(H1[0]) == np.ndarray
    assert type(H1[1]) == np.int64
    assert type(H1[2]) == np.float64
    assert type(H1[3]) == np.ndarray
    assert type(H1[4]) == list
    assert type(H1[5]) == np.ndarray
    assert type(H1[6]) == list

def test_hdf5_shape():
    H1 = readligo.read_hdf5('data/H-H1_LOSC_4_V2-1126259446-32.hdf5')
    
    assert H1[0].shape == (131072, )
    assert H1[3].shape == (32, )
    assert H1[5].shape == (32, )

eventname = 'GW150914' 
fnjson = "data/BBH_events_v3.json"
events = json.load(open(fnjson,"r"))
event = events[eventname]
fn_H1 = 'data/'+event['fn_H1']
fn_L1 = 'data/'+event['fn_L1']

def test_loaddata_H1():
    strain_H1, time_H1, chan_dict_H1 = readligo.loaddata(fn_H1, 'H1')
    
    assert strain_H1.shape == (131072, ) and time_H1.shape == (131072, )
    assert type(chan_dict_H1) == dict 
    
def test_loaddata_H1H2():
    strain_H1, time_H1, chan_dict_H1 = readligo.loaddata(fn_H1, 'H1')
    strain_L1, time_L1, chan_dict_L1 = readligo.loaddata(fn_L1, 'L1')
    
    assert strain_H1.shape == strain_L1.shape 
    assert time_H1.shape == time_L1.shape
    assert len(chan_dict_H1) == len(chan_dict_L1) == 13 
    assert chan_dict_H1.keys() == chan_dict_L1.keys()
    


