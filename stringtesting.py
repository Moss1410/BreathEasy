test1 = "1234"
test2 = "1f234d"

def testforletters():
    try:
        int(test1)
    except:
        return
    print(test1)
        
testforletters()