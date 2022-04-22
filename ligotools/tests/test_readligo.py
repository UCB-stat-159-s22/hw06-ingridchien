from ligotools import readligo
from ligotools import utils
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.mlab as mlab
from scipy.io import wavfile
import json
import os

#readligo tests
H1 = readligo.read_hdf5('data/H-H1_LOSC_4_V2-1126259446-32.hdf5')

def test_hdf5_structure():
    assert len(H1) == 7
    assert type(H1[0]) == np.ndarray
    assert type(H1[1]) == np.int64
    assert type(H1[2]) == np.float64
    assert type(H1[3]) == np.ndarray
    assert type(H1[4]) == list
    assert type(H1[5]) == np.ndarray
    assert type(H1[6]) == list

def test_hdf5_shape():
    assert H1[0].shape == (131072, )
    assert H1[3].shape == (32, )
    assert H1[5].shape == (32, )

eventname = 'GW150914' 
fnjson = "data/BBH_events_v3.json"
events = json.load(open(fnjson,"r"))
event = events[eventname]
fn_H1 = 'data/'+event['fn_H1']
fn_L1 = 'data/'+event['fn_L1']

strain_H1, time_H1, chan_dict_H1 = readligo.loaddata(fn_H1, 'H1')
strain_L1, time_L1, chan_dict_L1 = readligo.loaddata(fn_L1, 'L1')

def test_loaddata_H1():
    assert strain_H1.shape == (131072, ) and time_H1.shape == (131072, )
    assert type(chan_dict_H1) == dict 
    
def test_loaddata_H1H2(): 
    assert strain_H1.shape == strain_L1.shape 
    assert time_H1.shape == time_L1.shape
    assert len(chan_dict_H1) == len(chan_dict_L1) == 13 
    assert chan_dict_H1.keys() == chan_dict_L1.keys()
    
#utils tests

time = time_H1
dt = time[1] - time[0]
fs = event['fs'] 
NFFT = 4*fs
Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
Pxx_L1, freqs = mlab.psd(strain_L1, Fs = fs, NFFT = NFFT)
psd_H1 = interp1d(freqs, Pxx_H1)
psd_L1 = interp1d(freqs, Pxx_L1)

def test_whiten():
    WH = utils.whiten(strain_H1,psd_H1,dt)
    assert WH.max() == 734.9858519096138
    assert WH.min() == -688.2602995919118
    assert WH.shape == (131072, )

def test_write_wavfile():
    WH = utils.whiten(strain_H1,psd_H1,dt)
    utils.write_wavfile(eventname, 4096, WH)
    wav = wavfile.read(eventname)
    assert len(wav) == 2
    assert wav[0] == 4096
    assert type(wav[1]) == np.ndarray
    os.remove(eventname)

def test_reqshift():
    WL = utils.whiten(strain_L1, psd_L1, dt)
    strain_L1_shift = utils.reqshift(WL, 400., 4096)
    assert strain_L1_shift.max() == 91.63543337076183
    assert strain_L1_shift.min() == -88.35025813837271
    assert len(strain_L1_shift) == 131072