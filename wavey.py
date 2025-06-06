# -*- coding: utf-8 -*-
"""Wavey

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IbBP2k_z0EKiPRyFAo186TPD70KyKeya
"""

import os
import pandas as pd
import numpy as np
def sig_wave_height(wave_heights):
  sorted_waves = np.sort(wave_heights)[::-1]
  top_third = sorted_waves[:len(sorted_waves) // 3]
  height = np.mean(top_third)
  return height

def damping_displacement(time, amp, dp):
  displacement = amp * np.exp(-dp * time) * np.cos(2 * np.pi * time)
  return displacement

def do_i(cool):
  wow = float(2*cool)
  return wow

def calc_incoming_power(H_s, T_p):
  incoming_power = 0.5 * (H_s ** 2) * T_p
  return incoming_power

def find_monthly_data(AOI, month, MOI):
  return np.array(AOI)[np.array(month) == MOI]

def max_avg_hgt_pwr_period(monthly_height, monthly_power, monthly_period):
  max_height = np.max(monthly_height)
  mean_height = np.mean(monthly_height)
  max_power = np.max(monthly_power)
  mean_power = np.mean(monthly_power)
  max_period = np.max(monthly_period)
  mean_period = np.mean(monthly_period)

  return max_height, mean_height, max_power, mean_power, max_period, mean_period

def wec_power(avg_power, array_found):
  temp_data1 = []
  temp_data2 = []
  for x in range(len(avg_power)):
    wec = avg_power[x]*20
    temp_data1.append(wec)
    temp_data2.append(array_found[x] / wec*100)

  return temp_data1, temp_data2
