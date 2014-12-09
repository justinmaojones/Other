

def formatfloats(x):
    return '%0.8E' % x


def printlog(Log,Method):
    if Method == 1:
        n = 3
    else:
        n = 4
    adj0 = 3
    adj1 = 8
    adj2 = 8
    sep = "-"*(adj0 +6*(adj1+1)+6)
    
    
    
    
    print sep
    for line in Log:
        k,x,f,g,alpha,B,skipped,alphareset = line
        
        print "Iteration",
        print repr(k).rjust(adj0),
        print "        ",
        print "f = ",formatfloats(f).rjust(adj1),
        print "  ",
        print "||g|| =",formatfloats(g).rjust(adj1),
        print "  ",
        print "alpha =",formatfloats(alpha).rjust(adj1)
        
        m = B.shape[0]
        n = B.shape[1]
        
        L = []
        for i in range(m):
            val = formatfloats(float(x[i])).rjust(adj2)
            l = [val]
            for j in range(n):
                val = formatfloats(float(B[i,j])).rjust(adj2)
                l.append(val)
            L.append(l)
        
        extra = 3
        
        print "\n",
        print "x =",
        print L[0][0],
        '''        
        print " "*extra,
        print "B =",
        for j in range(n):
            print L[0][j+1],
        print "\n",
        '''
        
        for i in range(1,m):
            print " "*extra,
            print L[i][0].rjust(extra),
            print " "*(extra+4),
            #for j in range(1,n+1):
            #    print L[i][j].rjust(extra),
            print "\n",
        
        '''
        if skipped == True:
            
            print "Update to B was skipped",
            print "\n",
        if alphareset == True:
            print "Backtracking FAILED, alpha reset to 1",
            print "\n",
        '''
        print sep