import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s", datefmt="%H:%M:%S")
