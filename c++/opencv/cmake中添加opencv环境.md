### opencv cmake路径添加
在编译好opencv之后，如果系统路径存在问题，可以直接指定编译路径

```
set( OpenCV_DIR "/home/opencv-4.4.0/build")
find_package(OpenCV 4 REQUIRED)
```