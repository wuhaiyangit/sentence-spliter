#!/usr/bin/env python 

"""
A sentence splitter is a program capable of splitting a text into sentences. The standard set of heuristics for sentence splitting includes (but isn't limited to) the following rules:

Sentence boundaries occur at one of "." (periods), "?" or "!", except that

    Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
        Periods followed by a digit with no intervening whitespace are not sentence boundaries.
	    Periods followed by whitespace and then an upper case letter, but preceded by any of a short list of titles are not sentence boundaries. Sample titles include Mr., Mrs., Dr., and so on.
	        Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries (for example, www.aptex.com, or e.g).
		    Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not sentence boundaries.

		    Your task here is to write a program that given the name of a text file is able to write its content with each sentence on a separate line. Test your program with the following short text: Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't. The result should be:

		    Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
		    Did he mind?
		    Adam Jones Jr. thinks he didn't.
		    In any case, this isn't true...
		    Well, with a probability of .9 it isn't.

"""

import sys, re 




def find_position(line):
    
    if re.search(r"[.?!]+", line):
        pun = re.search(r"[.?!]+", line).group()
        pos = line.find(pun)
        pos = pos+len(pun)-1
    else:
        pos = -1
    return pos




def sentence_splitter(filename):

    f = open(filename, "r")

    for line in f:
        line = line.strip()
        while line:
            pos  =  find_position(line)
            if pos != -1:
                line2 = line[ : pos+1].split(" ")
                length = len(line2)
                last_word = line2[length -1]
        
	        try:
                    if re.search(r"[A-Z]+.*", last_word) or  line[pos+1] != " " or line[pos+2].islower() :
	                print line[:pos+1],
	                line = line[pos+1:]
	            
	            else:
		        print line[ : pos+1]
	                line = line[pos+1 :]

        
                except :
                    print line 
                    line = ""
            else :
                print line
                line = ""
    
    f.close() 
    print        
    return " bye bye"


    
    
    
if __name__=="__main__": 
    #print len(sys.argv)
    if len(sys.argv) < 2:
        print 
        print " Please try it as python sentence_splitter.py \"filename\""
        print 
        sys.exit(1)
    else: 
        print sentence_splitter(sys.argv[1])
    

  
    
     
