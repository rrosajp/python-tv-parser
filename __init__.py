#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import os, sys, json

sys.path.insert(0, './modules')
import m3u
M3UParser = m3u.M3UParser(defineExtensions)

ExtensionParser = {}

def ConvertDirectory(pathToDir, arrayName = "Collection"):
    collection = {}
    if os.path.isdir(pathToDir):
        for item in os.listdir(pathToDir):
            itemPath = os.path.join(pathToDir, item)
            if os.path.isfile(itemPath):
                content = ConvertFile(itemPath)
                if len(content) > 0:
                    name = ResolveFileName(itemPath)
                    collection[name] = content

    return collection

def ConvertFile(pathToFile): #return a Dict of all Groups (created with the addElement function)
    if os.path.isfile(pathToFile):
        extension = ResolveFileType(pathToFile)
        if extension in ExtensionParser:
            return ExtensionParser[extension].parse(pathToFile, addElement)
    return {}

def defineExtensions(parser, extensionArray):
    global ExtensionParser
    for extension in extensionArray:
        ExtensionParser[extension] = parser

def addElement(arrayToAdd, title, group = "unknown"):
    if not group in arrayToAdd:
        arrayToAdd[group] = []
    arrayToAdd[group].append({
        "title": title
    })

def ResolveFileType(pathToFile):
    filename, extension = os.path.splitext(pathToFile)
    return extension

def ResolveFileName(pathToFile):
    filename, extension = os.path.splitext(pathToFile)
    return filename
