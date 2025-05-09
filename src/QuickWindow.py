from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QWidget, QPushButton, QLineEdit, QMainWindow
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont, QIntValidator
import shiboken2
import maya.OpenMayaUI as omui
import maya.cmds as cmds

def GetMayaMainWindow() -> QMainWindow:
    mainWindow = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(mainWindow), QMainWindow)

def DeleteWidgetWithName(name):
    for widget in GetMayaMainWindow().findChildren(QWidget, name):
        widget.deleteLater()

class MayaWindow(QWidget):
    def __init__(self):
        DeleteWidgetWithName(self.GetWidgetUniqueName())
        super().__init__(parent=GetMayaMainWindow())
        self.setWindowFlags(Qt.Window)
        self.setObjectName(self.GetWidgetUniqueName())
        self.setWindowTitle("Quick Window")
        self.setMinimumSize(320, 100)
        self.show()

    def GetWidgetUniqueName(self):
        return "ithtmphaifi"
    

class QuickWindowWidget(MayaWindow):
    def __init__(self):
        super().__init__()

        self.masterLayout = QVBoxLayout()      
        self.setLayout(self.masterLayout)

        graphEditorBtn = QPushButton("Graph Editor")
        graphEditorBtn.clicked.connect(self.GraphEditorBtnClicked)
        self.masterLayout.addWidget(graphEditorBtn)

        renderSettingsBtn = QPushButton("Render Settings")
        renderSettingsBtn.clicked.connect(self.RenderSettingsBtnClicked)
        self.masterLayout.addWidget(renderSettingsBtn)

        playblastSettingsBtn = QPushButton("Playblast Settings")
        playblastSettingsBtn.clicked.connect(self.PlayblastSettingsBtnClicked)
        self.masterLayout.addWidget(playblastSettingsBtn)

    def GraphEditorBtnClicked(self):
        for panel in cmds.getPanel(sty="graphEditor") or []:
            cmds.scriptedPanel(panel, e=True, to=True)

    def RenderSettingsBtnClicked(self):
        cmds.RenderGlobalsWindow()

    def PlayblastSettingsBtnClicked(self):
        cmds.playblast(options=True)


quickWindowWidget = QuickWindowWidget()
quickWindowWidget.show()

GetMayaMainWindow()