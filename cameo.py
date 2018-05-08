import cv2
from Opencv_test.managers import WindowManager, CaptureManager


class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Camo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)

    def run(self):
        """运行main"""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):
        """设置按键
        空格  ->  截图
        tab   ->  开始/暂停视频截取
        esc -> 退出窗口
        """

        if keycode == 32:  # 空格
            self._captureManager.writeImage('F:\python\data\photos\screenshot.png')
        elif keycode == 9:  # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('F:\python\data\photos\screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27:  # esc
            self._windowManager.destroyWindow()


if __name__ == "__main__":
    Cameo().run()