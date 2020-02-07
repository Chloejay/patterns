# I/O async/await, concurrency operator
import asyncio 
from datetime import datetime
import time 
import logging 


async def test(n:int = None)-> int:
    if n%2 != 0:
        logger.info('SLEEP {}'.format(datetime.now()))
        await asyncio.sleep(1)
        return n **2

async def test2(n:int = None)-> int:
    if n in range(100) and n<50:
        return await test(n) + n**3

async def testAdd(m:int,n:int)-> int:
    x = await test(m)
    y = await test2(n) 
    return (x,y)
    # return f'add result is {x+y}'


if __name__=='__main__':
    logging.basicConfig(format= '%(asctime)s - %(message)s', datefmt='[%H:%M:%S]')
    logger= logging.getLogger()
    logger.setLevel(logging.INFO) 
    start = time.time()

    #create loop 
    loop= asyncio.get_event_loop() 
    try:
        a,b =loop.run_until_complete(testAdd(9,21))
        print(a,b)
    finally:
        loop.close() 

    end = time.time()  
    logger.info("Total time: {}".format(end - start))