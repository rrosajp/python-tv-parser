#!/usr/bin/python
# -*- coding: utf-8 -*-
#

class M3UParser(Parser):

    def __init__(self, extensionDefiner):
        extensionDefiner(self, [".m3u8"])

    def parse(self, pathToFile, addElement):
        fileContent = open(pathToFile, "r")
        lines = fileContent.split('\n')

        m3uContent = {}

        m3uObject = None
        for line in lines:
            if m3uObject is None:
                if 'EXTINF' in line.split(':')[0]:
                    m3uObject = {}
                    self.EXTM3U_ParseLine(m3uObject, line)
                else:
                    continue
            else:
                if 'EXTINF' in line.split(':')[0]:
                    m3uObject['video'] = ""
                    self.EXTM3U_AppendObject(m3uObject, m3uContent)
                    m3uObject = {}
                    self.EXTM3U_ParseLine(m3uObject, line)

                else:
                    line = line.strip()
                    if line:
                        m3uObject['video'] = line
                    else:
                        continue
                    self.EXTM3U_AppendObject(m3uObject, m3uContent)
                    m3uObject = None
        return m3uContent

    def EXTM3U_AppendObject(self, m3uObject, m3uContent):
        group = (m3uObject['group'] . "")
        if not group in m3uContent:
            m3uContent[group] = []

        m3uObject.pop('group', None)
        m3uContent[group].append(m3uObject)

    def EXTM3U_GetTitle(self, dict, line):

        if 'tvg-name' in dict:
            if len(dict['tvg-name']) > 0:
                return dict['tvg-name']

        splitty = line.split(',')
        if splitty and len(splitty) > 0:
            return splitty[-1]

        return "Unknown"

    def EXTM3U_GetLogo(self, dict):

        if 'tvg-logo' in dict:
            if len(dict['tvg-logo']) > 0:
                return dict['tvg-logo']

        return ''

    def EXTM3U_GetGroup(self, dict):

        if 'group-title' in dict:
            if len(dict['group-title']) > 0:
                return dict['group-title']

        return 'Unknown'

    def EXTM3U_ParseLine(self, m3uObject, line):
        pattern = re.compile(r'([\w-]+)="((?![^"])|[^"]+)"')

        dict = {}
        for match in pattern.finditer(line):
            dict[match.group(1)] = match.group(2)

        m3uObject['title'] = self.EXTM3U_GetTitle(dict, line)
        m3uObject['icon'] = self.EXTM3U_GetLogo(dict)
        m3uObject['group'] = self.EXTM3U_GetGroup(dict)
