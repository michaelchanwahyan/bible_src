#!/usr/bin/python3
import os
import sys
import re


def readText(infilename):
    if not os.path.exists(infilename):
        print(f"file {infilename} not found !")
        return ''
    else:
        with open(infilename, "r") as fp:
            texts = fp.readlines()
        fp.close()
    return texts


def u200bRemoval(inTextLines):
    outTextLines = [ line.replace("\u200b", "") for line in inTextLines ]
    return outTextLines


def checkInArgCnt():
    inArgCnt = len(sys.argv)
    return inArgCnt


def topicalPhraseRemoval(inTextLines):
    outTextLines = "" # string variable to host the desired output results
    # verse number enumerating
    # by checking if new chapter wordings are detected
    cn = 0 # chapter number
    vn = 0 # verse number
    isFirstVerse = True
    multiVerse_extraLineRowCnt = 0 # for handling multi verse in same line
    for textline in textlines:
        textline = textline.strip().replace("\t", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ")
        if "第" in textline and ("章" in textline or "篇" in textline):
            cn += 1
            vn = 0
            continue
        else:
            res = re.search(r"[0-9]", textline)
            if res is None: # check if textline is not initiated by verse number
                print(f"likely topical wordings found    :    {textline}")
                pass
            elif res.start() == 0: # case if textline is initiated by verse number
                vn += 1
                # print(f"{cn}:{vn} {textline}")
                textSplitRes = textline.split(" ", 1)
                vn_in_line = textSplitRes[0]
                try:
                    vn_in_line = int(vn_in_line)
                except:
                    if "-" in vn_in_line: # if there contains multi-verse in same line
                        vn_curr = int(vn_in_line.split("-")[0])
                        vn_next = int(vn_in_line.split("-")[1])
                        multiVerse_extraLineRowCnt = vn_next - vn_curr
                        vn_in_line = vn_curr
                    pass
                if vn != vn_in_line: # check verse number consistence
                    print("verse no. mismatch ! ", textline)
                    break
                else: # if consistent, remove the verse number built in from input text, anchored by first white-space occurance
                    textline = textSplitRes[1]
                if isFirstVerse: # next line character control
                    isFirstVerse = False
                    pass
                else:
                    outTextLines += "\n"
                outTextLines += f"{cn}.{vn} {textline}"
                pass
            # END OF if re.search(r"[0-9]", textline) is None: # check if textline is not initiated by verse number
            if multiVerse_extraLineRowCnt > 0:
                for cnt in range(multiVerse_extraLineRowCnt):
                    outTextLines += "\n"
                    vn += 1
                multiVerse_extraLineRowCnt = 0
            pass
        # END OF if "第" in textline and ("章" in textline or "篇" in textline):
    # END OF for textline in textlines:
    return outTextLines


def writeText(outfilename, outtext):
    if os.path.exists(outfilename):
        print(f"file {outfilename} already exists ! stop operation")
        return
    with open(outfilename, "w") as fp:
        fp.write(outtext)
    fp.close()
    return



if __name__ == "__main__":


    # check program input arguments
    inArgCnt = checkInArgCnt()
    if inArgCnt == 1:
        print("no input argument provided !")
        exit()
    elif inArgCnt == 2:
        infname = sys.argv[1]
        print(f"input file name: {infname}")
        pass


    # read in text contents
    textlines = readText(infname)
    
    
    # special char removal
    textlines = u200bRemoval(textlines)


    # convert to required text source format
    cleansedText = topicalPhraseRemoval(textlines)
    # print(textlines)


    # write text contents
    outfname = infname.replace("_raw", "")
    writeText(outfname, cleansedText)

    exit()
