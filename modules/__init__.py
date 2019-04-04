#!/usr/bin/python
# -*- coding: utf-8 -*-
#
ParserCollection = {}

# M3U, M3U8
import m3u
M3UParser = m3u.M3UParser(defineExtensions)

#...

#...

def defineExtensions(parser, extensionArray):
    global ParserCollection
    for extension in extensionArray:
        ParserCollection[extension] = parser
