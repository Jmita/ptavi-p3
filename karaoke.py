

#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import os
import sys


class KaraokeLocal(smallsmilhandler.SmallSMILHandler):

    def __init__(self):
        parser = make_parser()
        SSHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(SSHandler)
        parser.parse(open(sys.argv[1]))
        self.data = SSHandler.get_tags()
