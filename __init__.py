#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import os, sys, json
import modules as ParserModules

ExtensionParser = ParserModules.ParserCollection

def ConvertDirectory(pathToDir, arrayName = "Collection"):
    collection = {}
    if os.path.isdir(pathToDir):
        for item in os.listdir(pathToDir):
            itemPath = os.path.join(pathToDir, item)
            if os.path.isfile(itemPath):
                content = ConvertFile(itemPath)
                if len(content) > 0:
                    name = _ResolveFileName(itemPath)
                    collection[name] = content

    return collection

def ConvertFile(pathToFile):
    if os.path.isfile(pathToFile):
        extension = _ResolveFileType(pathToFile).lower()
        if extension in ExtensionParser:
            return ExtensionParser[extension].parse(pathToFile, _addElement)
    return {}

def _addElement(arrayToAdd, title, group = "unknown"):
    if not group in arrayToAdd:
        arrayToAdd[group] = []
    arrayToAdd[group].append({
        "title": title
    })

def _ResolveFileType(pathToFile):
    filename, extension = os.path.splitext(pathToFile)
    return extension

def _ResolveFileName(pathToFile):
    filename, extension = os.path.splitext(pathToFile)
    return filename
