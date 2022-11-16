from test_module import test

def ContentGC(dnaString):
    amount = 0
    for char in dnaString:
        if(char == "G" or char == "C"):
            amount +=1

    return round((amount/len(dnaString))*100,2)
    

# –- Unit tests –-
if __name__== '__main__':
      
    test(ContentGC('GCGC') == 100.0)
    test(ContentGC('CGCG') == 100.0)
    test(ContentGC('GACGAC') == 66.67)
    test(ContentGC('TACGTACGTAT') == 36.36)
    test(ContentGC('CAGTACTACCTCAGACGT') == 50.0)
    test(ContentGC('GATCGATCGATGCTAGCTAGCGCATC') == 53.85)
