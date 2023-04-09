import random
import re
from itertools import product
from collections import defaultdict
from pprint import pprint

def process_listsStrapi(patterns, firm_list, search_target, search_term, location, language):
    
    
    #print("process_lists() : patterns")
    #print(patterns)
    #print("process_lists() : firm_list")
    #print(firm_list)
    #print("process_lists() : search_target")
    #print(search_target)
    #print("process_lists() : search_term")
    #print(search_term)
    #print("process_lists() : location")
    #print(location)

    result = []

    for str_pattern in patterns:
        #print("process_lists() : INSIDE FOR LOOP")
        lists_map = {
            '$SearchTarget': list(search_target), '$FirmName': list(firm_list), '$SearchTerm': list(search_term), '$Location': list(location),
            '$Language': list(language)#, '$exclusion': list(exclusions)
        }
        #print("process_lists() : print list_map variable")
        #print(lists_map) #works
        keys = []
        for key, val in lists_map.items():
            pattern = key.replace('$', '\$')
            pattern = r'{}\d*'.format(pattern)
            matches = re.findall(pattern, str_pattern)
            if matches:
                for match in matches:
                    #print("process_lists() : inside 2nd loop")
                    matched_key = ''
                    for l in match:
                        if not l.isdigit():
                            matched_key += l
                    # target_list = lists_map[matched_key]
                    keys.append((key, match))
                    #print("process_lists() : print KEYS")
                    #print(keys)
        perms_args = [lists_map[key] for key, match in keys]
        #print("process_lists() : perms_args")
        #print(perms_args)
        all_perms = product(*perms_args)
        #print("process_lists() : all_perms 1 after product")
        #print(all_perms)
        all_perms = list(all_perms)
        #print("process_lists() : all_perms 2")
        #print(all_perms) # this prints out all patterns
        all_perms = [val for val in all_perms if len(set(val[-3:])) == 3]
        #print("process_lists() : print all perms1?")
        #print(all_perms)
        perms = []
        excl_perms = None
        for perm in all_perms:
            #if not excl_perms:
            #    excl_perms = perm[-3:]
            #if excl_perms:
            #    if excl_perms != perm[-3:]:
            #        continue
            perms.append(perm)
        #print("process_lists() : print all perms2?")
        #print(perms)
        subresult = []
        while perms:
            new_pattern = str_pattern
            perm = list(perms.pop(0))
            for key, match in keys:
                repl_str = perm.pop(0)
                new_pattern = new_pattern.replace(match, repl_str, 1)
            subresult.append(new_pattern)
        result.append(subresult)

    #print("process_lists() : query")
    #print(result)
    return result