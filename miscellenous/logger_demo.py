import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')





def testFunctionTologData(val):
     logging.info(f"function invoked with value: {val}")


if __name__== "__main__":
     logging.info("Script started")
testFunctionTologData("hello world")
logging.info("Script ended")