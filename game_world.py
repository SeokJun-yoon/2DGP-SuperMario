
# layer 0: Background Objects
# layer 1: Foreground Objects
testob = [[], []]


def add_object(o, layer):
    testob[layer].append(o)


def add_objects(l, layer):
    testob[layer] += l


def remove_object(o):
    for i in range(len(testob)):
        if o in testob[i]:
            testob[i].remove(o)
            del o
            break




def clear():
    for o in all_objects():
        del o
    for l in testob:
        l.clear()

def destroy():
    clear()
    testob.clear()


def all_objects():
    for i in range(len(testob)):
        for o in testob[i]:
            yield o

