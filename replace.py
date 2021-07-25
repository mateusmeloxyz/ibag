#!/usr/bin/env python3
from os import listdir

headerPath = "./header.html"
footerPath = "./footer.html"
source = "./source"
output = "./output"
files = listdir(source)

headerData = ""
with open(headerPath) as headerFile:
    for line in headerFile:
        headerData += line
footerData = ""
with open(footerPath) as footerFile:
    for line in footerFile:
        footerData += line

for inputPath in files:
    newInputPath = source + "/" + inputPath
    with open(newInputPath) as inputFile:
        outputPath = output + "/" + inputPath
        with open(outputPath, "wt") as outputFile:
            for line in inputFile:
                if '<!--HEAD-->' in line:
                    outputFile.write(line.replace('<!--HEAD-->', headerData))
                elif '<!--HEADER-->' in line:
                    outputFile.write(line.replace('<!--HEADER-->', headerData))
                elif '<!--FOOTER-->' in line:
                    outputFile.write(line.replace('<!--FOOTER-->', footerData))
                else:
                    outputFile.write(line)
