
#  conda install -c conda-forge trio
#  https://trio.readthedocs.io/en/latest/reference-core.html#synchronizing-and-communicating-between-tasks
#  https://trio.readthedocs.io/en/latest/reference-core.html#buffering-in-channels

import trio
import math

async def main():
    async with trio.open_nursery() as nursery:
        send_channel, receive_channel = trio.open_memory_channel(30)
        nursery.start_soon(producer, send_channel)
        nursery.start_soon(consumer, receive_channel)

async def producer(send_channel):
    async with send_channel:
        for i in range(50):
            print(i)
            await send_channel.send(i)

async def consumer(receive_channel):
    async with receive_channel:
        async for value in receive_channel:
            result = math.factorial(value)
            await trio.sleep(1)
            print("number: " + str(value) + " got value {!r}".format(result))

trio.run(main)







# eksempel - kan se at koen virker
'''
#  conda install -c conda-forge trio
#  https://trio.readthedocs.io/en/latest/reference-core.html#synchronizing-and-communicating-between-tasks
#  https://trio.readthedocs.io/en/latest/reference-core.html#buffering-in-channels

import trio
import math

async def main():
    async with trio.open_nursery() as nursery:
        send_channel, receive_channel = trio.open_memory_channel(30)
        nursery.start_soon(producer, send_channel)
        nursery.start_soon(consumer, receive_channel)

async def producer(send_channel):
    async with send_channel:
        for i in range(50):
            print(i)
            await send_channel.send(i)

async def consumer(receive_channel):
    async with receive_channel:
        async for value in receive_channel:
            result = math.factorial(value)
            await trio.sleep(1)
            print("number: " + str(value) + " got value {!r}".format(result))

trio.run(main)

'''




# godt channel eksempel.
'''
import trio
import math

async def main():
    async with trio.open_nursery() as nursery:
        send_channel, receive_channel = trio.open_memory_channel(10)
        nursery.start_soon(producer, send_channel)
        nursery.start_soon(consumer, receive_channel)

async def producer(send_channel):
    async with send_channel:
        for i in range(5):
            await send_channel.send("message {}".format(i))

async def consumer(receive_channel):
    async with receive_channel:
        async for value in receive_channel:
            #result = math.factorial(5)
            print("got value {!r}".format(value))

trio.run(main)
'''



#end