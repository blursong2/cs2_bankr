import os
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
)

os.getcwd()
class MainWindow(QMainWindow):

  def __init__(self):
    super().__init__()
    self.setWindowTitle("CS2 한섭차단 툴")
    self.setGeometry(200, 200, 300, 150)

    central_widget = QWidget()
    self.setCentralWidget(central_widget)

    layout = QVBoxLayout(central_widget)

    btn_block = QPushButton("차단")
    btn_unblock = QPushButton("차단 해제")

    layout.addWidget(btn_block)
    layout.addWidget(btn_unblock)

    btn_block.clicked.connect(self.block_server)
    btn_unblock.clicked.connect(self.unblock_server)

  def block_server(self):
    if sys.platform == "win32":
      os.system("route add 146.66.152.0 mask 255.255.255.0 0.0.0.0 metric 1")
    elif sys.platform.startswith("linux"):
      os.system("sudo ip route add unreachable 146.66.152.0/24")

  def unblock_server(self):
    if sys.platform == "win32":
      os.system("route delete 146.66.152.0")
    elif sys.platform.startswith("linux"):
      os.system("sudo ip route del unreachable 146.66.152.0/24")


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())
