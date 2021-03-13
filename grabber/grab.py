# this module will allows us to grab data from different source :
# S0, S1, S2, ..., SN 
# type of source : database, file, api 

import os 
import zmq  # socket programming 
import time 


import numpy as np 
import pandas as pd 
import requests as req 

import operator as op 
import itertools as it, functools as ft 

from glob import glob 
from os import path 
from multiprocessing import Process, Event, Queue 


def grab_from_database():  #mysql 
	pass 

def grab_from_filesystem(location, extension="*"):
	files_paths = sorted(glob(path.join(location, extension)))
	acc = []
	for f_path in files_paths:
		df = pd.read_csv(f_path, sep=';')
		acc.append(df)
	res = pd.concat(acc)
	return res 


def grab_from_api(url_api, api_key):
	data = req.post(
		url=url_api, 
		data={
			'date': '', 
			'': ''
		}
	)
	return data 


def main_grabber():
	try:
		keep_grabbing = True 
		timer = time.time()
		while keep_grabbing:
			print('main grabber is on...!')
			if time.time() - timer > 10: 
				timer = time.time()  # update timer 
				res = grab_from_filesystem('source/filesystem')
				print(res)
			time.sleep(0.001)
		# end LOOP 

	except KeyboardInterrupt as e: 
		pass 

if __name__ == '__main__':
	print(' ... api-data-ETL... ')
	#grab_from_filesystem('source/filesystem')
	main_grabber()
