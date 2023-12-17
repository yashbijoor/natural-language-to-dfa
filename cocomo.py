import os
import io

def countlinesFrontend(start, lines=0, header=True, begin_start=None):
    if header:
        print('{:>10} |{:>10} | {:<20}'.format('ADDED', 'TOTAL', 'FILE'))
        print('{:->11}|{:->11}|{:->20}'.format('', '', ''))

    for thing in os.listdir(start):
        thing = os.path.join(start, thing)
        if os.path.isfile(thing):
            if thing.endswith('.js') or thing.endswith('.html') or thing.endswith('.css'):
                with io.open(thing, 'r') as f:
                    newlines = f.readlines()
                    newlines = len(newlines)
                    lines += newlines
 
                    if begin_start is not None:
                        reldir_of_thing = '.' + thing.replace(begin_start, '')
                    else:
                        reldir_of_thing = '.' + thing.replace(start, '')

                    print('{:>10} |{:>10} | {:<20}'.format(
                            newlines, lines, reldir_of_thing))


    # for thing in os.listdir(start):
    #     thing = os.path.join(start, thing)
    #     if os.path.isdir(thing):
    #         lines = countlinesPython(thing, lines, header=False, begin_start=start)

    return lines

def countlinesPython(start, lines=0, header=True, begin_start=None):
    if header:
        print('{:>10} |{:>10} | {:<20}'.format('ADDED', 'TOTAL', 'FILE'))
        print('{:->11}|{:->11}|{:->20}'.format('', '', ''))

    for thing in os.listdir(start):
        thing = os.path.join(start, thing)
        if os.path.isfile(thing):
            if thing.endswith('.py'):
                with io.open(thing, 'r') as f:
                    newlines = f.readlines()
                    newlines = len(newlines)
                    lines += newlines
 
                    if begin_start is not None:
                        reldir_of_thing = '.' + thing.replace(begin_start, '')
                    else:
                        reldir_of_thing = '.' + thing.replace(start, '')

                    print('{:>10} |{:>10} | {:<20}'.format(
                            newlines, lines, reldir_of_thing))


    # for thing in os.listdir(start):
    #     thing = os.path.join(start, thing)
    #     if os.path.isdir(thing):
    #         lines = countlinesPython(thing, lines, header=False, begin_start=start)

    return lines

l1 = countlinesPython('../project')
l2 = countlinesPython('nlq_to_re')
l3 = countlinesPython('re_to_dfa')
l4 = countlinesFrontend('templates')
l5 = countlinesFrontend('static/javascript')
l6 = countlinesFrontend('static/css')

print("\n\nTHE TOTAL LINES OF CODE IN THE PROJECT IS", l1+l2+l3+l4+l5+l6)