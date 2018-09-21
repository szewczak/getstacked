import itertools
#import yourmom (she's aready here)

#explicit question:
#what is the closed form solution for calculating the n permutations out of a FILO stack of size m
#push pop strict rules apply


def checklist( item1, item2, calledsofar ):
# This function will search through arbitrary portions of a list and check to see that all the intermediate elements were called
#   It is assumed that the bigger item always goes in item2 and the smaller in item 1
    itemstocheck = list(range( item1 + 1, item2 ))
    # Bail out early if there was nothing to check, since the items were right next to each other   
    if( len(itemstocheck) == 0):
        return True

    for item in itemstocheck:
        if( item not in calledsofar ):
            return False
    
    return True

def tableout(n):
    ITEMLIST = list(range( 1, n ))

    # Create giant-ass list of all permutations possible for these items
    final_list = list(itertools.permutations( ITEMLIST, len(ITEMLIST) ))
    bad_list = []
    good_list = []
    #print(final_list)

    # Loop through the different permutations of items
    for combo in final_list:
        result = True

        # loop through each couplet of cells in the list
        for i in list(range( 1, len(ITEMLIST) )):
            if( combo[i] < combo[i-1] ):
                result &= checklist( combo[i], combo[i-1], combo[:(i-1)] )

        # if one of the couplets failed the test, add them to the bad list, otherwise pass them to the good list
        if( result == False ):
            bad_list.append( combo )
        else:
            good_list.append( combo )

    print(good_list, end='\n\n')

    # Start printing our pretty header
    print( "Num\\Col", end='\t' )
    for i in ITEMLIST:
        print( i, end='\t' )

    print( '\n', end='' )

    for value in ITEMLIST:
        print( value, end='\t' )
        for position in list(range( len(ITEMLIST) )):
            count = 0
            for combo in good_list:
                if( combo[position] == value ):
                    count += 1
            print("%.4f"  % (count/len(good_list)), end='\t' )
        print( '\n', end='' )

tableout(3)
tableout(4)
tableout(5)
tableout(6)