# I/O async/await, concurrency operator
import asyncio 
from datetime import datetime
import time 
import logging 


def test(n:int = None)-> int:
    if n%2 != 0:
        return n **2

async def test2(n:int = None)-> int:
    if n in range(100000) and n<90000:
        await asyncio.sleep(0.1)
        logger.info('SLEEP {} for {}'.format(datetime.now(), n)) 
        return test(n)

async def testAdd(a, b,c):
    start = time.time() 
    await asyncio.wait([
            test2(a),
            test2(b), 
            test2(c),
            ])
    end = time.time()  
    logger.info("Total time: {}".format(end - start))



if __name__=='__main__':
    logging.basicConfig(format= '%(asctime)s - %(message)s', datefmt='[%H:%M:%S]')
    logger= logging.getLogger()
    logger.setLevel(logging.INFO) 
    #create loop 
    loop= asyncio.get_event_loop() 
    try:
        loop.run_until_complete(testAdd(999, 9999, 89999))
    finally:
        loop.close() 