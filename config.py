import logging
import sys
import constants as consts

LOG = logging.getLogger(__name__)


def setup_logging():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s %(message)s')
    LOG.info("Logging enabled!")
    LOG.info("%(prog)s version %(version)s",
             {'prog': sys.argv[0], 'version': consts.VERSION})