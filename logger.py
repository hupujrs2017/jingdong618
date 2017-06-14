__author__ = 'yangyz'


import logging
logger = logging.getLogger( 'weibo' )
logger.setLevel( logging.DEBUG )

# log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# console log
ch = logging.StreamHandler()
ch.setLevel( logging.DEBUG )
ch.setFormatter( formatter )
logger.addHandler(ch)