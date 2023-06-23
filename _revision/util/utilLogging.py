import logging


class LoggerPrint:
    logging.basicConfig(format='%(asctime)s [PY-SNAP] - %(message)s',
                        filemode='w')
    LOGGER = logging.getLogger()
    MAGENTA = "\u001B[35m"
    BLUE = "\u001B[34m"
    YELLOW = "\u001B[33m"
    GREEN = "\u001B[32m"
    RED = "\u001B[31m"
    RESET = "\u001B[0m"
    LOGGER.setLevel(logging.DEBUG)

    def logInfoHeader(self, logging):
        self.LOGGER.info(f"{self.YELLOW}{logging}{self.RESET}")

    def logInfoBody(self, logging):
        self.LOGGER.info(f"{self.BLUE}{logging}{self.RESET}")

    def logInfoResponse(self, logging):
        self.LOGGER.info(f"{self.MAGENTA}{logging}{self.RESET}")

    def logInfo(self, logging):
        self.LOGGER.info(f"{self.GREEN}{logging}{self.RESET}")

    def logError(self, logging):
        self.LOGGER.error(f"{self.RED}{logging}{self.RESET}")

# log = LoggerPrint()
# log.logInfo("HANTU KESOREAN")