#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import os, sys, json
import modules as ParserModules

ExtensionParser = ParserModules.ParserCollection

def ConvertDirectory(pathToDir, badCharacter = ""):
    collection = {}
    if os.path.isdir(pathToDir):
        for item in os.listdir(pathToDir):
            itemPath = os.path.join(pathToDir, item)
            if os.path.isfile(itemPath):
                content = ConvertFile(itemPath, badCharacter)
                if len(content) > 0:
                    name = _ResolveFileName(itemPath)
                    collection[name] = content

    return collection

def ConvertContent(content, extension, badCharacter = ""):
    extension = extension.lower()
    if not "." in extension:
        extension = "." + extension
    if extension in ExtensionParser:
        return ExtensionParser[extension].parse(None, content, badCharacter)
    return {}

def ConvertFile(pathToFile, badCharacter = ""):
    if os.path.isfile(pathToFile):
        extension = _ResolveFileType(pathToFile)
        if extension in ExtensionParser:
            return ExtensionParser[extension].parse(pathToFile, None, badCharacter)
    return {}

def _ResolveFileType(pathToFile):
    filename, extension = os.path.splitext(pathToFile)
    return extension.lower()

def _ResolveFileName(pathToFile):
    filename, extension = os.path.splitext(pathToFile)
    return filename
