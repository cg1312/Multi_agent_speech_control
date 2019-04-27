# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:29:45 2019

@author: gupte
"""
import setup_path 
import airsim

import time
import os
import numpy as np


def applyBrake(client, car_controls, carNumber):
    car_controls.brake = 1
    client.setCarControls(car_controls, "Car" + str(carNumber))
    time.sleep(3)   # let car drive a bit
    #car_controls.brake = 0 #remove brake

def goForward(client, car_controls, carNumber):
    car_controls.brake = 0
    car_controls.throttle = 1
    car_controls.steering = 0
    client.setCarControls(car_controls, "Car" + str(carNumber))
    time.sleep(5)
    applyBrake(client, car_controls, carNumber)
    
def goReverse(client, car_controls, carNumber):
    car_controls.brake = 0
    car_controls.throttle = -1
    car_controls.is_manual_gear = True;
    car_controls.manual_gear = -1
    car_controls.steering = 0
    client.setCarControls(car_controls, "Car" + str(carNumber))
    time.sleep(5)   # let car drive a bit
    applyBrake(client, car_controls, carNumber)
   
    car_controls.is_manual_gear = False; # change back gear to auto
    car_controls.manual_gear = 0 
    
def goRight(client, car_controls, carNumber):
    car_controls.brake = 0
    car_controls.throttle = 1
    car_controls.steering = 0.5
    client.setCarControls(car_controls, "Car" + str(carNumber))
    time.sleep(1)
    car_controls.throttle = 1
    time.sleep(5)
    applyBrake(client, car_controls, carNumber)

def goLeft(client, car_controls, carNumber):
    car_controls.brake = 0
    car_controls.throttle = 1
    car_controls.steering = -0.5
    client.setCarControls(car_controls, "Car" + str(carNumber))
    time.sleep(1)
    car_controls.throttle = 1
    time.sleep(5)
    applyBrake(client, car_controls, carNumber)
    
def execute(client, carNumber, command, command_dict, car_controls_dict):
    
    command_dict[command](client, car_controls_dict[carNumber], carNumber)

    

    
                