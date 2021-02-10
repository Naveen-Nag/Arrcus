import argparse
    
def missingNumber(in_list,max_r,min_r):

    mis_list = []
    for dig in range(min_r,max_r+1):
        if dig in in_list:
            in_list.remove(dig)
        else:
            mis_list.append(dig)
        
        
    print('\nExtra numbers == {} \nMissing numbers are : {}'.format(in_list,mis_list))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='''This function will input a list of numbers, min ,max range and returns extra number list and missing number list''')
    parser.add_argument('-in_list', '--inlist', nargs="*",type=int,required=True,metavar='',help='Enter the list of elements')
    parser.add_argument('-max_r', '--max_range', type=int,required=True,metavar='',help='Enter the max range')
    parser.add_argument('-min_r', '--min_range', type=int,required=True,metavar='',help='Enter the min range')
    args = parser.parse_args()
    missingNumber(args.inlist,args.max_range,args.min_range)







