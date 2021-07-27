# Transportation System using Jetson Nano


Vehicle and License Plate detection in real-time at ~40 FPS
-----------------
Install the libraries:

```
pip3 install -r requirements.txt
```

Move to the main folder:

```
cd vehicledetectionjsnn
```


License Plate Detection:
-----------------
Run the License Plate detection with the webcam at:

```
python3 detectnet-cameraLP.py --model=./networks/plate/plate.onnx --class_labels=./networks/plate/labels.txt --input_blob=input_0 --output_cvg=scores --output_bbox=boxes --camera=/dev/video0 --width=640  --height=480
```
Or, run the License Plate detection with the "clip3.mp4" video at:

```
python3 detectnet-cameraLP.py --model=./networks/plate/plate.onnx --class_labels=./networks/plate/labels.txt --input_blob=input_0 --output_cvg=scores --output_bbox=boxes clip3.mp4
```
Or, run the License Plate detection with the "pic5.PNG" image ("testpic5.PNG" is the new output, includes the input and detection boxes, PNG or JPG are also accepted) at:

```
python3 detectnet-cameraLP.py --model=./networks/plate/plate.onnx --class_labels=./networks/plate/labels.txt --input_blob=input_0 --output_cvg=scores --output_bbox=boxes pic5.PNG testpic5.PNG
```


Vehicle Detection:
-----------------
Run the Vehicle detection with the webcam at:

```
python3 detectnet-cameraVH.py --model=./networks/vehicle/vehicle.onnx --class_labels=./networks/vehicle/labels.txt --input_blob=input_0 --output_cvg=scores --output_bbox=boxes --camera=/dev/video0 --width=640  --height=480
```

Or, run the Vehicle detection with the "clip1.mp4" video at:

```
python3 detectnet-cameraVH.py --model=./networks/vehicle/vehicle.onnx --class_labels=./networks/vehicle/labels.txt --input_blob=input_0 --output_cvg=scores --output_bbox=boxes clip1.mp4	
```
Or, run the Licens Plate detection with the "pic1.jpg" image ("testpic1.PNG" is the new output, includes the input and detection boxes, PNG or JPG are also accepted) at:

```
python3 detectnet-cameraVH.py --model=./networks/vehicle/vehicle.onnx --class_labels=./networks/vehicle/labels.txt --input_blob=input_0 --output_cvg=scores --output_bbox=boxes pic1.jpg testpic1.PNG	
```

Finally, Enjoy it! 
Any concerns, please e-mail me at hieutran6698@gmail.com


References:
-----------------
```
[1] Liu, Wei, et al. "Ssd: Single shot multibox detector." European conference on computer vision. Springer, Cham, 2016.
[2] Howard, Andrew G., et al. "Mobilenets: Efficient convolutional neural networks for mobile vision applications." arXiv preprint arXiv:1704.04861 (2017).
[3] https://github.com/dusty-nv/jetson-inference
[3] https://github.com/winter2897/Real-time-Auto-License-Plate-Recognition-with-Jetson-Nano
```
