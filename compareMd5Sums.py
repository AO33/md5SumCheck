
# Author: Aaron Odell 


import os
import commands
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-file1",help="md5Sum file1 to compare against file2",type=str)
parser.add_argument("-file2",help="md5Sum file2 to compare against file1",type=str)
args = parser.parse_args()


def compareMd5Sums(f1,f2):
    file1 = open(f1,'r')
    file2 = open(f2,'r')
    f1Dict,f2Dict = {},{}
    while True:
        l1 = file1.readline().strip('\r').strip('\n')
        if not l1:
            break
        cols1 = l1.split('\t')
        l2 = file2.readline().strip('\r').strip('\n')
        cols2 = l2.split('\t')
        f1Dict.update({cols1[0]:cols1[1]})
        f2Dict.update({cols2[0]:cols2[1]})
    #############
    file1.close()
    file2.close()
    print "CheckSums read into memory"
    print "Comparing fileNames and sums..."
    if len(f1Dict) != len(f2Dict):
        print "Error... Number of files in file1 does not match number of files in file2"
        return 
    ############################
    print "#######################"
    sameSums,sameFileNames = 0,0
    for fileName1,md5Sum1 in f1Dict.items():
        if fileName1 not in f2Dict:
            print "Error... File names are different between file1 and file2"
            print fileName1+" Not found in file2..."
            print "#######################"
        else:
            sameFileNames += 1
            if md5Sum1 != f2Dict[fileName1]:
                print "Error... md5Sums not the same"
                print fileName1+" md5Sum is different between file1 and file2"
                print "#######################"
            else:
                sameSums += 1
    ##############################################
    print "Total files in file1 "+str(len(f1Dict))
    print "Total files in file2 "+str(len(f2Dict))
    print "Total FileNames matching "+str(sameFileNames)
    print "Total md5Sums matching "+str(sameSums)
    print "Exiting..."
    

compareMd5Sums(args.file1,args.file2)

