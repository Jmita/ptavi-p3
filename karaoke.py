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

    def print_list(self):

        for lista in self.data:
            elemento = lista[0]
            dicc = lista[1]
            print
            print elemento, "\t",
            for key in dicc:
                if dicc[key] != "":
                    print key + "=" + dicc[key] + "\t",

    def do_local(self):
        for lista in self.data:
            elemento = lista[0]
            dicc = lista[1]
            for key in dicc:
                if key == "src":
                    source = dicc[key]
                    os.system("wget -nv " + dicc[key])
                    data = source.split('/')
                    data = data[-1]
                    dicc[key] = data

if __name__ == "__main__":
    KL = KaraokeLocal()
    KL.print_list()
    KL.do_local()
    KL.print_list()
    print
