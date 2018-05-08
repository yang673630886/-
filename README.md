# -
Python+OpenCV
项目功能：调取电脑摄像头，并使用键盘进行截图和录制视频
系统：window 8.1
Python 3.6 + Opencv 3

设计方法：
  在 managers.py 的文件中，包含CaptureManager类、enterFrame()和exitFrame()函数、WindowManager类。
  其中CaptureManager类和WindowManager类作为高级的I/O流接口都具有可扩展性。
  Cameo类中提供了两种启动应用程序：run()和onkeypress()。
  CaptureManager类会使用摄像头和WindowManager类。
  按空格键截图，tab键启动/停止录像，Esc退出程序。  
