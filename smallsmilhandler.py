from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.lista = []

    def startElement(self, name, attrs):
        if name == "root-layout":
            self.root_layout = {}
            self.root_layout['width'] = attrs.get('width', "")
            self.root_layout['height'] = attrs.get('height', "")
            self.root_layout['background_color'] =(attrs.get('background-color', ""))
            self.lista.append([name, self.root_layout])

        elif name == "region":
            self.region = {}
            self.region['id'] = attrs.get('id', "")
            self.region['top'] = attrs.get('top', "")
            self.region['bottom'] = attrs.get('bottom', "")
            self.region['left'] = attrs.get('left', "")
            self.region['right'] = attrs.get('right', "")
            self.lista.append([name, self.region])

        elif name == "img":
            self.img = {}
            self.img['src'] = attrs.get('src', "")
            self.img['region'] = attrs.get('region', "")
            self.img['begin'] = attrs.get('begin', "")
            self.img['dur'] = attrs.get('dur', "")
            self.lista.append([name, self.img])

        elif name == "audio":
            self.audio = {}
            self.audio['src'] = attrs.get('src', "")
            self.audio['begin'] = attrs.get('begin', "")
            self.audio['dur'] = attrs.get('dur', "")
            self.lista.append([name, self.audio])

        elif name == "textstream":
            self.textstream = {}
            self.textstream['src'] = attrs.get('src', "")
            self.textstream['region'] = attrs.get('region', "")
            self.lista.append([name, self.textstream])

    def get_tags(self):

        return self.lista


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    SSHandler = SmallSMILHandler()
    parser.setContentHandler(SSHandler)
    parser.parse(open('karaoke.smil'))
    data = SSHandler.get_tags()
    print data
