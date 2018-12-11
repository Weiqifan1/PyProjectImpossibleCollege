
# https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/

import os
import time
import asyncio
from library import text_to_speech
from library import speech_out
from library import test_async

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
