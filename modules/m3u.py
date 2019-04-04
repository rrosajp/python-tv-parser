#!/usr/bin/python
# -*- coding: utf-8 -*-
#

class M3UParser(Parser):

    def __init__(self, extensionDefiner):
        extensionDefiner(self, [".m3u", ".m3u8"])

    def parse(pathToFile, addElement):
        pass
