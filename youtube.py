#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 13:36:16 2020

@author: jin
"""

from pytube import YouTube

url = "https://www.youtube.com/watch?v=P99qJGrPNLs&ab_channel=Cyberpunk2077"    

YouTube(url).steams.all()
#YouTube(url).streams.filter(res="1440p")[0].download(output_path = "/Users/jin/Desktop/")
