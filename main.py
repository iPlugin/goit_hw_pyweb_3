from threading import Thread
import logging as logger

def worker(param):
    logger.debug(param)


if __name__ == "__main__":
    
    for i in range(1,6):
        logger.basicConfig(
            filename="logger.log",
            level=logger.DEBUG,
            format='%(asctime)s | %(levelname)8s = %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')
        th = Thread(target=worker, args=(f"Worker #{i} is working",))
        th.start()
                    