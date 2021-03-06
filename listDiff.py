import argparse
    
def listDiff(inlistA,inlistB):
    common_list = []
    removed_list = []
                
    for num in inlistA:
        if num in inlistB:
            common_list.append(num)
            inlistB.remove(num)
        else:
            removed_list.append(num)

    print ('Common = {} \nRemoved = {}\nAdded = {}'.format(common_list,removed_list,inlistB))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='''This function will input 2 lists of numbers and returns 3 lists - Common, removed and added list''')
    parser.add_argument('-lA', '--inlistA', nargs="*",type=int,required=True,metavar='',help='Enter the list of elements to be added to List A')
    parser.add_argument('-lB', '--inlistB', nargs="*",type=int,required=True,metavar='',help='Enter the list of elements to be added to List B')
    args = parser.parse_args()
    listDiff(args.inlistA,args.inlistB)
   




