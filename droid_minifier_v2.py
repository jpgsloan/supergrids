import random
import string
import os
import re

def splitLine(s):
    data = s.split('\n')[0]
    return data

def lineStartsWithComment(s):
    if s.startswith('#'):
        return s
    else:
        return None

def lineIsEmpty(s):
    if s == '\n' or s == '\r' or s == '\r\n' or s =='\n\r' or s == '    ' or s == '':
        return True
    else:
        return False

def generate_rndm(length=2):
    randomString = ''
    for index, value in enumerate(range(0,length)):
        if index == 0:
            digit_char = random.choices(string.ascii_uppercase, k=1)
        else:
            digit_char = random.choices(string.ascii_uppercase, k=1) + random.choices(string.digits, k=1)
            random.shuffle(digit_char)
        randomString += digit_char[0]
    return randomString

def generateNewVarName(varNameDictNewToOld):
    newVarNameFound = False
    while not newVarNameFound:
        newVarName = generate_rndm(2)
        if newVarName in varNameDictNewToOld:
            pass
        else:
            newVarNameFound = True
    return newVarName

def pr(*args):
    global DEBUG
    if DEBUG:
        s = ''
        for i in args:
            s += str(i) + ' '
        print(s)

def findVarName(line, varNameDictOldToNew, varNameDictNewToOld):
    newLine = ''
    if '_' in line:
        pr('line', line)
        stringsToReplaceList = []
        currentStartIndex = 0
        currentEndIndex = 0
        priorStartIndex = 0
        priorEndIndex = 0
        priorSearchResult = ''
        for m in re.finditer('_[A-Z0-9]{1,}', line):
            currentStartIndex = m.start()
            currentEndIndex = m.end()
            currentSearchResult = line[currentStartIndex:currentEndIndex]
            pr('>>', currentSearchResult, currentStartIndex, currentEndIndex, priorEndIndex)
            if currentStartIndex == priorEndIndex:
                priorSearchResult = stringsToReplaceList[-1:][0]
                updatedString = priorSearchResult + currentSearchResult
                pr('-+', priorSearchResult, updatedString)
                del(stringsToReplaceList[-1:])
                stringsToReplaceList.append(updatedString)
                pr('==', stringsToReplaceList)
                priorEndIndex = currentEndIndex
            else:
                stringsToReplaceList.append(currentSearchResult)
                priorEndIndex = currentEndIndex
                pr('++', stringsToReplaceList)

        splitLine = stringsToReplaceList
        pr('line+', line)
        pr('splitLine+', splitLine)

        for e in splitLine:
            if e.startswith('_'):
                originalVarName = e
                if originalVarName in varNameDictOldToNew:
                    newLine = line.replace(originalVarName, ('_'+ varNameDictOldToNew[originalVarName]), 1)
                    pr('oldLine1', line)
                    pr('newLine1', newLine)
                    line = newLine
                else:
                    newVarName = generateNewVarName(varNameDictNewToOld)
                    varNameDictOldToNew[originalVarName] = newVarName
                    varNameDictNewToOld[newVarName] = originalVarName
                    newLine = line.replace(originalVarName, ('_'+newVarName), 1)
                    pr('oldLine2', line)
                    pr('newLine2', newLine)
                    line = newLine
    return newLine

def stripWhiteSpace(s, linePadding = '    '):
    newLine = ''
    if s.startswith('    '):
        splitLine = s.split(' ')
        for i in splitLine:
            if not i == '':
                newLine += i
        newLine = linePadding + newLine
    return newLine

def stripCommentsOnLines(s):
    newLine = ''
    if '#' in s:
        index = s.rfind('#')
        newLine = s[0:index]
    return newLine

def main(scriptName, scriptBasePath, fileExtension='ini'):
    varNameDictOldToNew = {}
    varNameDictNewToOld = {}

    scriptPath = os.path.join(scriptBasePath, ('%s.%s' % (scriptName, fileExtension)))
    minifiedScriptPath = os.path.join(scriptBasePath, ('%s_mf.%s' % (scriptName, fileExtension)))

    pr(scriptPath)
    pr(minifiedScriptPath)

    LINE_PADDING = ' ' * 4 # if line padding isn't necessary for Droid parsing, or only 1 space indent is required, change accordingly

    newLines = []
    with open(scriptPath, 'r') as f:
        for line in f:
            addLine = True
            data = splitLine(line)

            if lineStartsWithComment(data): addLine = False
            if lineIsEmpty(data): addLine = False

            replaceVar = findVarName(data, varNameDictOldToNew, varNameDictNewToOld)
            if replaceVar: # line had an internal cable variable name in it (word started with '_')
                data = replaceVar

            strippedComments = stripCommentsOnLines(data)
            if strippedComments:
                data = strippedComments

            strippedSpace = stripWhiteSpace(data, LINE_PADDING)
            if strippedSpace:
                data = strippedSpace

            if addLine:
                newLines.append(data)

    with open(minifiedScriptPath, 'w') as f:
        for line in newLines:
            f.write(line + '\n')
            pr(line)

    pr(varNameDictOldToNew)
    pr(len(varNameDictOldToNew))

    pr(varNameDictNewToOld)
    pr(len(varNameDictNewToOld))

global DEBUG
DEBUG = False
if __name__ == "__main__":
    scriptName = 'SuperGrids' # script name without file extension
    scriptBasePath = '.' # folder containing script.ini file
    main(scriptName, scriptBasePath)
