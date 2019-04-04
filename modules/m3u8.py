#!/usr/bin/python
# -*- coding: utf-8 -*-
#

class M3U8Parser(Parser):

    def __init__(self, extensionDefiner):
        extensionDefiner(self, [".m3u8"])

    def parse(self, pathToFile):
        fileContent = open(pathToFile, "r")
        lines = fileContent.split('\n')

        headerFound = False
        m3u8Content = {}

        m3u8Object = None
        for line in lines:

            if not headerFound:
                if "#EXTM3U" in line:
                    headerFound = True
                    continue

            if m3u8Object is None:
                if 'EXTINF' in line.split(':')[0]:
                    m3u8Object = {}
                    self.EXTM3U8_ParseLine(m3u8Object, line)
                else:
                    continue
            else:
                if 'EXTINF' in line.split(':')[0]:
                    m3u8Object['url'] = ""
                    self.EXTM3U8_AppendObject(m3u8Object, m3u8Content)
                    m3u8Object = {}
                    self.EXTM3U8_ParseLine(m3u8Object, line)

                else:
                    line = line.strip()
                    if line:
                        m3u8Object['url'] = line
                    else:
                        continue
                    self.EXTM3U8_AppendObject(m3u8Object, m3u8Content)
                    m3u8Object = None
        return m3u8Content

    def EXTM3U8_AppendObject(self, m3u8Object, m3u8Content):
        group = (m3u8Object['group'] . "")
        if not group in m3u8Content:
            m3u8Content[group] = []

        m3u8Object.pop('group', None)
        m3u8Content[group].append(m3u8Object)

    def EXTM3U8_GetTitle(self, dict, line):

        if 'tvg-name' in dict:
            if len(dict['tvg-name']) > 0:
                return dict['tvg-name']

        splitty = line.split(',')
        if splitty and len(splitty) > 0:
            return splitty[-1]

        return "Unknown"

    def EXTM3U8_GetLogo(self, dict):

        if 'tvg-logo' in dict:
            if len(dict['tvg-logo']) > 0:
                return dict['tvg-logo']

        return ''

    def EXTM3U8_GetGroup(self, dict):

        if 'group-title' in dict:
            if len(dict['group-title']) > 0:
                return dict['group-title']

        return 'Unknown'

    def EXTM3U8_ParseLine(self, m3u8Object, line):
        pattern = re.compile(r'([\w-]+)="((?![^"])|[^"]+)"')

        dict = {}
        for match in pattern.finditer(line):
            dict[match.group(1)] = match.group(2)

        m3u8Object['title'] = self.EXTM3U8_GetTitle(dict, line)
        m3u8Object['icon'] = self.EXTM3U8_GetLogo(dict)
        m3u8Object['group'] = self.EXTM3U8_GetGroup(dict)
