# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fieldfitterwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QWidget)

from cmlibs.widgets.sceneviewerwidget import SceneviewerWidget

class Ui_FieldFitterWidget(object):
    def setupUi(self, FieldFitterWidget):
        if not FieldFitterWidget.objectName():
            FieldFitterWidget.setObjectName(u"FieldFitterWidget")
        FieldFitterWidget.resize(1702, 1134)
        self.sceneviewerwidget = SceneviewerWidget(FieldFitterWidget)
        self.sceneviewerwidget.setObjectName(u"sceneviewerwidget")
        FieldFitterWidget.setCentralWidget(self.sceneviewerwidget)

        self.retranslateUi(FieldFitterWidget)

        QMetaObject.connectSlotsByName(FieldFitterWidget)
    # setupUi

    def retranslateUi(self, FieldFitterWidget):
        FieldFitterWidget.setWindowTitle(QCoreApplication.translate("FieldFitterWidget", u"Field Fitter", None))
    # retranslateUi

