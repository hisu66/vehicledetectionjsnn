#!/usr/bin/python3
#
# Copyright (c) 2020, NVIDIA CORPORATION. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#
import time
import csv
import jetson.inference
import jetson.utils

import argparse
import sys

# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.", 
                                 formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage() +
                                 jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())

parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v1", help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use") 

is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]

try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)

# load the object detection network
net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)

# create video sources & outputs
input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)
output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv+is_headless)
with open('CSV/checkLP.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Local Time','Total LP'])

# process frames until the user exits
        while True:
	# capture the next image
            img = input.Capture()
            localtime = time.asctime(time.localtime(time.time())) #To show in CSV - Full date time form
            
            second1 = int(time.time()) #To list the row for second unit
            
            ms1 = int(time.time()*1000.0) #Check milisecond before detection for FPS Checking
	# detect objects in the image (with overlay)
            detections = net.Detect(img, overlay=opt.overlay)
            ms2 = int(time.time()*1000.0) #Check milisecond after detection for FPS Checking
            FPS = 1000/(ms2-ms1) #FPS Checking by ms2 and ms1
            
	# print the detections
            print("Detected {:d} objects in image".format(len(detections)))
#Command for condition of object detected

            allobject=len(detections) 
            
# 		print("OK")
			#h1=h1+1
            #condition = (h1/(allobject+0.0000001))*100 #To prevent number 0 in the beginning
	#Check condition for object detected
            if len(detections)>=4: notice = 'Stuck'
            else: notice = 'Normal'
            
            second2 = int(time.time()) #To list the row for second unit
            #local = second2 - second1 #To list the row for second unit
            writer.writerow([localtime,allobject])
           # if ((second2 - second1) == 1): writer.writerow([localtime,allobject,h1,h2,h3,notice]) #Add 'FPS' to show the FPS in CSV
            

	# render the image
            output.Render(img)

	# update the title bar
            output.SetStatus("Senior 2020 | FPS: {:.0f}".format(net.GetNetworkFPS())) #Using 'FPS' instead of 'GetNetworkFPS' to show the real FPS

	# print out performance info
            net.PrintProfilerTimes()

	# exit on input/output EOS
            if not input.IsStreaming() or not output.IsStreaming():
                break


