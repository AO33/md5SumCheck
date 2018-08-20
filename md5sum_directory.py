
# Author: Aaron Odell #
# Written for mac OSX. Untested on other operating systems...


import os
import commands
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-directory",help="Top level directory to obtain md5sums for. -directory /myDirectory ",type=str)
parser.add_argument("-outFile",help="OutFile to write sums to. Full file path is a good idea",type=str)
parser.add_argument("-excludeHidden",help="Look for hidden directories and files. Valid inputs = True,False. Default = False",type=str)
args = parser.parse_args()


def recurse_md5Sum(directory,fileList,excludeHidden="True"):
    directoryList = os.listdir(directory)
    for item in directoryList:
        ### Exclude hidden files ###
        if excludeHidden == "True":
            if item[0] == ".":
                continue
        #####################################
        if os.path.isdir(directory+'/'+item):
            fileList = recurse_md5Sum(directory+'/'+item,fileList)
        else:
            md5sum = commands.getoutput('md5 -r '+directory+'/'+item+' | cut -d " " -f1')
            fileList.append([directory+'/'+item,md5sum])
    ###############
    return fileList


def writeSumsToFile(directory,outFile,excludeHidden="True"):
    md5sums = recurse_md5Sum(directory,[],excludeHidden=excludeHidden)
    md5sums = sorted(md5sums,key=lambda x: x[0])
    #######################################################################
    print "All md5sums for file in directory "+str(directory)+" calculated"
    print "Number of files found "+str(len(md5sums))
    print "Writing sums to file "+str(outFile)+" ..."
    ###########################
    outFile = open(outFile,'w')
    for fileSum in md5sums:
        outFile.write(fileSum[0]+'\t'+fileSum[1]+'\n')
    ###############
    outFile.close()


writeSumsToFile(args.directory,args.outFile,args.excludeHidden)

