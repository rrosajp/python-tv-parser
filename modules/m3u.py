#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import os

class M3UParser():

    def __init__(self, extensionDefiner):
        extensionDefiner(self, [".m3u8", ".m3u"])


    def parse(self, pathToFile, content = None):
        if content:
            fileContent = content
        else:
            if os.path.isfile(pathToFile):
                fileContent = open(pathToFile, "r")
            else:
                return {}

        lines = fileContent.split('\n')
        if "#EXTM3U" in lines[0]:
            return self.parse_ext(lines)
        return self.parse_normal(lines)

    def parse_normal(self, lines):
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


    def parse_ext(self, lines):
        m3u8Content = {}

        m3u8Object = None
        for line in lines:
            if m3u8Object is None:
                if 'EXTINF' in line.split(':')[0]:
                    m3u8Object = {}
                    self.EXTM3U_ParseLine(m3u8Object, line)
                else:
                    continue
            else:
                if 'EXTINF' in line.split(':')[0]:
                    m3u8Object['url'] = ""
                    self.EXTM3U_AppendObject(m3u8Object, m3u8Content)
                    m3u8Object = {}
                    self.EXTM3U_ParseLine(m3u8Object, line)

                else:
                    line = line.strip()
                    if line:
                        m3u8Object['url'] = line
                    else:
                        continue
                    self.EXTM3U_AppendObject(m3u8Object, m3u8Content)
                    m3u8Object = None
        return m3u8Content

    def EXTM3U_AppendObject(self, m3u8Object, m3u8Content):
        group = (m3u8Object['group'] + "")
        if not group in m3u8Content:
            m3u8Content[group] = []

        m3u8Object.pop('group', None)
        m3u8Content[group].append(m3u8Object)

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

    def EXTM3U_ParseLine(self, m3u8Object, line):
        pattern = re.compile(r'([\w-]+)="((?![^"])|[^"]+)"')

        dict = {}
        for match in pattern.finditer(line):
            dict[match.group(1)] = match.group(2)

        m3u8Object['id'] = self.EXTM3U_GetGroup(dict)
        m3u8Object['title'] = self.EXTM3U_GetTitle(dict, line)
        m3u8Object['icon'] = self.EXTM3U_GetLogo(dict)
        m3u8Object['group'] = self.EXTM3U_GetGroup(dict)
