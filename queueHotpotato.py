from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    
    print('After Pushing: ')
    simqueue.peek()
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        print('After lol: ')
        simqueue.peek()
        simqueue.dequeue()

    return simqueue.dequeue()

hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7)
