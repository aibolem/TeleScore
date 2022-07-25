"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import sys
import os

from unittest.mock import PropertyMock, patch
from PyQt6.QtWidgets import QApplication, QWidgetItem, QPushButton
from PyQt6.QtCore import QSize
import unittest 
import requests


PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

import gm_resources
from layout.abstract_layout.freelayout import FreeLayout
from component.basiccomp.buttoncomp import ButtonComp

# Note, these tests might be seperated into different classes in the future.

class gm_resourcetest(unittest.TestCase):
    '''@classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass'''

    def test_retrieveFile(self):
        '''with patch("gm_resources.requests.get") as mocked_get:
            rtn = requests.Response()
            rtn.status_code = 200
            type(rtn).content = "Hello World"
            type(rtn).text = "Hello World"
            type(rtn).ok = True
            mocked_get.return_value = rtn
            print(mocked_get.return_value)
            rtnVal = gm_resources.retrieveFile("https://www.example.com", "Hello")
            #print(rtnVal)
            #self.assertEqual(rtnVal, "Hello World")'''
        pass

class freelayout_test(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.layoutInst = FreeLayout(None)

    def tearDown(self):
        pass

    def test_count(self):
        self.assertEqual(self.layoutInst.count(), 0)
        widgetInst = QPushButton()
        itemInst = QWidgetItem(widgetInst)
        self.layoutInst.addItem(itemInst)

        self.assertEqual(self.layoutInst.count(), 1)

    def test_addItem(self):
        widgetInst = QPushButton()
        itemInst = QWidgetItem(widgetInst)
        self.layoutInst.addItem(itemInst)

        self.assertEqual(self.layoutInst.itemAt(0), itemInst)

    def test_indexOf(self):
        widgetInst = QPushButton()
        itemInst = QWidgetItem(widgetInst)
        self.layoutInst.addItem(itemInst)

        widgetInst1 = QPushButton()
        itemInst1 = QWidgetItem(widgetInst1)
        self.layoutInst.addItem(itemInst1)

        self.assertEqual(self.layoutInst.indexOf(itemInst), 0)
        self.assertEqual(self.layoutInst.indexOf(itemInst1), 1)

    def test_itemAt(self):
        widgetInst = QPushButton()
        itemInst = QWidgetItem(widgetInst)
        self.layoutInst.addItem(itemInst)

        widgetInst1 = QPushButton()
        itemInst1 = QWidgetItem(widgetInst1)
        self.layoutInst.addItem(itemInst1)

        self.assertEqual(self.layoutInst.itemAt(0), itemInst)
        self.assertEqual(self.layoutInst.itemAt(1), itemInst1) 

    def test_spacing(self):
        self.assertEqual(self.layoutInst.spacing(), -1)

    def test_setSpacing(self):
        self.assertEqual(self.layoutInst.spacing(), -1)
        self.layoutInst.setSpacing(2)
        self.assertEqual(self.layoutInst.spacing(), 2)

    def test_takeAt(self):
        widgetInst = ButtonComp("test")
        self.layoutInst.addComponent(widgetInst, QSize(700, 600))

        self.assertEqual(self.layoutInst.count(), 1)

        self.layoutInst.takeAt(0)

        self.assertEqual(self.layoutInst.count(), 0)
        


if __name__ == '__main__':
    unittest.main()
