# I/O async/await, concurrency operator
import asyncio 
from datetime import datetime
import time 
import logging 


def test(n:int = None)-> int:
    if n%2 != 0:
        return n **2

async def test2(n:int = None, when: float=0.1)-> int:
    if n in range(100000) and n<90000:
        await asyncio.sleep(when)
        logger.info('SLEEP {} for {}'.format(datetime.now(), n)) 
        return test(n)

async def testAdd(a, b,c, when):
    start = time.time() 
    await asyncio.wait([
            test2(a, when),
            test2(b, when), 
            test2(c, when),
            ])
    end = time.time()  
    logger.info("Total time: {}".format(end - start))



if __name__=='__main__':
    logging.basicConfig(format= '%(asctime)s - %(message)s', datefmt='[%H:%M:%S]')
    logger= logging.getLogger()
    logger.setLevel(logging.INFO) 
    
    loop= asyncio.get_event_loop() 
    # loop.set_debug(True) 
    try:
        loop.run_until_complete(testAdd(999, 9999, 89999, 0.01))
    finally:
        loop.close() 