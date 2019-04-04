#!/usr/bin/python
# -*- coding: utf-8 -*-
#

class M3UParser(Parser):

    def __init__(self, extensionDefiner):
        extensionDefiner(self, [".m3u"])

    def parse(self, pathToFile):
        fileContent = open(pathToFile, "r")
        lines = fileContent.split('\n')

        m3uContent = {}

        for line in lines:
            m3uObject = {}

            title = line
            titleFound = False
            if titleFound and '\\' in title:
                title = title.split('\\')[-1]
                titleFound = True

            if titleFound and '/' in title:
                title = title.split('/')[-1]
                titleFound = True

            m3uObject["title"] = title
            m3uObject["url"] = line

            m3uContent["Unknown"].append(m3uObject)
