# -*- coding: utf-8 -*-
import pymel.core as pm
import function_base as base
import function_link as link


def _____():
    pass


def create():
    winName = 'test_win'
    if pm.window(winName, exists = 1):
        pm.deleteUI(winName, wnd = 1)
    pm.window(winName, title = u'模板窗口')
    pm.window(winName, e = 1, w = 255, h = 1)

    with pm.columnLayout(adj = 1):
        pm.button()
        pm.button()
        pm.button()
        pm.button()

    pm.showWindow(winName)