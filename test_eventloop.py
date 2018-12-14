
# https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/

import os
import time
import asyncio, time, random
""" from library import text_to_speech
from library import speech_out
from library import test_async """

#############################   help functions      #####################
""" def text_from_book2():
    f = open("book2/async_test.txt", "r", encoding="utf-8")
    #holmes = f.read(50)
    holmes = f.read()
    # each paragraph in holmes - no empy paragraphs
    paragraph = holmes.split("\n\n")
    f.close()
    return paragraph """
    #text_to_speech.save_input_as_audio(paragraph[0], 1)
######################################################################

# Install python 3.7. Skriv i komandline: conda install python=3.7
# Luk terminalen og vs code og åben igen.
# Slet ikke ovenstående linjer før de er skrevet i readme filen.

#https://docs.python.org/3/library/asyncio-queue.html

async def stupid_sum():
    time_int = 0
    global global_time
    while time_int < 1000:
        await asyncio.sleep(1)
        time_int += 1
        global_time = time_int
        print(time_int)

async def firstWorker():
    while True:
        await asyncio.sleep(3)
        print("First Worker Executed " + str(global_time))


async def secondWorker():
    while True:
        await asyncio.sleep(1)
        print("Second Worker Executed")

# Async med asyncio.run. Event loopet behøves ikke. Er en del af asyncio.run.
""" async def main():
    global_time = 0

    stupid_sum_task = asyncio.create_task(
        stupid_sum()
    )

    firstWorker_task = asyncio.create_task(
        firstWorker()
    )

    secondWorker_task = asyncio.create_task(
        secondWorker()
    )

    await stupid_sum_task
    await firstWorker_task
    await secondWorker_task

asyncio.run(main()) """

# Eksempel med kø
async def stupid_sum(queue):
    time_int = 0
    global global_time
    while time_int < 10:
        await asyncio.sleep(1)
        time_int += 1
        global_time = time_int
        stupid = print(time_int)
        await queue.put(stupid)

        if time_int == 2:
            await queue.put(firstWorker(queue)) 
        elif time_int == 4:
            await queue.put(secondWorker(queue))
            
        

async def firstWorker(queue):
    time_int = 0
    while time_int < 1:
        await asyncio.sleep(1)
        time = print("First Worker Executed " + str(global_time))
        await queue.put(time)
        break

async def secondWorker(queue):
    while True:
        await asyncio.sleep(1)
        sec = print("Second Worker Executed")
        await queue.put(sec)
        break

async def consumer(queue):
    while True:
        from_queue = await queue.get()
        queue.task_done()
        print(f'consumed {from_queue}')

async def main():
    num_producers = 1
    num_consumers = 1
    print('Make queue')
    queue = asyncio.Queue()

    # fire up the both producers and consumers
    producers = [asyncio.create_task(stupid_sum(queue))
                 for i in range(num_producers)]
    consumers = [asyncio.create_task(consumer(queue))
                 for i in range(num_consumers)]

    # with both producers and consumers running, wait for
    # the producers to finish
    await asyncio.wait(consumers)
    #await asyncio.gather(*producers)
    #print('---- done producing')

    # wait for the remaining tasks to be processed
    #await queue.join()

    # cancel the consumers, which are now idle
    #for c in consumers:
    #    c.cancel()

asyncio.run(main())


# Eksempel med kø
""" async def rnd_sleep(t):
    # sleep for T seconds on average
    await asyncio.sleep(t * random.random() * 2)

async def producer(queue):
    while True:
        token = random.random()
        print(f'produced {token}')
        if token < .05:
            break
        await queue.put(token)
        await rnd_sleep(.1)

async def consumer(queue):
    while True:
        token = await queue.get()
        await rnd_sleep(.3)
        queue.task_done()
        print(f'consumed {token}')

async def main():
    queue = asyncio.Queue()

    # fire up the both producers and consumers
    producers = [asyncio.create_task(producer(queue))
                 for _ in range(3)]
    consumers = [asyncio.create_task(consumer(queue))
                 for _ in range(10)]

    # with both producers and consumers running, wait for
    # the producers to finish
    await asyncio.gather(*producers)
    print('---- done producing')

    # wait for the remaining tasks to be processed
    await queue.join()

    # cancel the consumers, which are now idle
    for c in consumers:
        c.cancel()

asyncio.run(main()) """



""" 
#############################   help functions      #####################
def text_from_book2():
    f = open("book2/async_test.txt", "r", encoding="utf-8")
    #holmes = f.read(50)
    holmes = f.read()
    # each paragraph in holmes - no empy paragraphs
    paragraph = holmes.split("\n\n")
    f.close()
    return paragraph
    #text_to_speech.save_input_as_audio(paragraph[0], 1)
######################################################################

async def stupid_sum():
    time_int = 0
    global global_time
    while time_int < 1000:
        await asyncio.sleep(1)
        time_int += 1
        global_time = time_int
        print(time_int)

async def firstWorker():
    while True:
        await asyncio.sleep(3)
        print("First Worker Executed " + str(global_time))


async def secondWorker():
    while True:
        await asyncio.sleep(1)
        print("Second Worker Executed")

paragraph_list = text_from_book2()

global_time = 0
loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(firstWorker())
    asyncio.ensure_future(secondWorker())
    asyncio.ensure_future(stupid_sum())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()
 """
