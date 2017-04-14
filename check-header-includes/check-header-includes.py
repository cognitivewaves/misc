#-------------------------------------------------------------------------------
# Name:      check-header-includes.py
# Purpose:   It checks the include file for each source (.cpp,.h,etc) of the given
#            project and removes the dependency(include file),if it is not required.
# Copyright: (c) 2017
# License:   This program is free software: you can redistribute it and/or modify
#            it under the terms of the GNU General Public License as published by
#            the Free Software Foundation, either version 3 of the License, or
#            (at your option) any later version.
#
#            This program is distributed in the hope that it will be useful,
#            but WITHOUT ANY WARRANTY; without even the implied warranty of
#            MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#            GNU General Public License for more details.
#            GPL-3.0+ <https://www.gnu.org/licenses/gpl.txt>
#-------------------------------------------------------------------------------

#---------------------------Imports-----------------------------#
import os
import re
import sys
#---------------------------------------------------------------#

#---------------------------Editable----------------------------#
# Change according to your directory structure                  #
ProjectRootDir = "D:/project/root/dir/"
SourceDir      = ProjectRootDir + "src/"
ProjectDir     = ProjectRootDir + "_build/"
ProjectName    = "test"                                # The Project You work on
WorkingDir     = "D:/tmp/header/"                      # Path to this python and batch script
ExcludeList    = ["StdAfx.h","stdafx.h","windows.h"]   # Header files to be excluded from checking
BuildLogFile   = WorkingDir + "build.log"              # Build log to fetch results and take decision
FileExt        = "cpp"                                 # Source file extension e.g. "h", "cpp", "cxx" etc.
StartIndex     = 0                                     # Skip files if needed
BuildScript    = WorkingDir + "build.bat"              # Script that executes the build
#---------------------------------------------------------------#

def DebugPrint(str):
    str = ""
    #print str

def GetBuildParams():
    return ProjectDir + " " + ProjectName + " " + BuildLogFile.replace('/', '\\')

def Build(path):
    buildParams = GetBuildParams()
    ret = os.system(BuildScript + " " + "build" + " " +  buildParams)

def Rebuild(path):
    print ("Rebuilding "+ path +"...... ", end=" ")
    buildParams = GetBuildParams()
    ret = os.system(BuildScript + " rebuild" + " " +  buildParams)
    print ("Done")

def CheckBuildLog():
    f = open(BuildLogFile,'r')
    log_lines = f.readlines()
    f.close()
 
    for line in log_lines:
        regex = re.compile("error\(s\); stopping compilation")
        found = regex.search(line)
        if found:
            return False

        regex = re.compile("1 failed")
        found = regex.search(line)
        if found:
            return False
        
        regex = re.compile("1 succeeded")
        found = regex.search(line)
        if found:
            return True

        regex = re.compile("1 up-to-date")
        found = regex.search(line)
        if found:
            return True

    print ("\nUnknown build outcome - reached build log end of file... stopping")
    exit()

def InExcludeFileList(line):
    for excludeFile in ExcludeList:
        if line.find(excludeFile) > 0:
            return True
    return False

def Overwrite(filename, lineNum, line):
    fp = open(filename,'r+', newline='')
    
    i=0
    while i < lineNum:
        fp.readline()
        i = i + 1

    fp.seek(fp.tell())
    fp.write(line)

    fp.close()
    
def TestFile(filename):
    fp = open(filename,'r+', newline='')
    lines = fp.readlines()  # Read all the lines
    fp.close()

    lineNum = 0
    for line in lines:
        if line.startswith('#include'):
            if InExcludeFileList(line) == False:
                tmpstr = line
                print ("    Testing: " + tmpstr.rstrip("\n"), end=" ")
                fp = Overwrite(filename, lineNum, re.sub(r'#include','//nclude',line))
                
                Build(filename)
                ok1 = CheckBuildLog()

                if ok1 == False:   # header is required
                    print ("")
                    fp = Overwrite(filename, lineNum, re.sub(r'//nclude','#include',line))
                    
                    Build(filename)
                    ok2 = CheckBuildLog()
                    
                    if ok2 == False:
                        print ("Uncomment and build failed")
                        exit()
                else:
                    print ("[unused]")
                
        lineNum = lineNum + 1 

def main():
    print ("---------------START----------")

    command_arg_list = sys.argv
    fileExt = FileExt
    startIndex = StartIndex
    try:
        arg1 = command_arg_list[1]
        arg2 = command_arg_list[2]
    except:
        print ("No command line args")

    print ("Checking "+"."+ fileExt +" files")
    print ("Project: " + ProjectDir + ProjectName)

    Rebuild(ProjectDir) # Compile/Rebuild Project for the first time
    #Build(ProjectDir)   # Compile/Build Project for the first time
    ok = CheckBuildLog()
    if ok == False:
        print ("First build failed - cannot proceed")
        exit()
    
    i = 0
    for root,subfolders,files in os.walk(SourceDir):
        for file in files:
            path = os.path.join(root,file)
            if path.endswith("." + fileExt):
                if i >= startIndex:
                    print ("-------------------------------------------------------------")
                    print (str(i) + " " + path)
                    TestFile(path) 
                i = i + 1

    print ("-------------------------------------------------------------")
    print ("Project completed")
    print ("--------------END-------------")

if __name__ == '__main__':
    main()

