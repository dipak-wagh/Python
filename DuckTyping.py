# Duck typing : It is a concept where type of an object is determined by its behaviour
#               not by its class

class InkjetPrinter:
    def printdocument(self,document):
        print("Inkjet printer printing : ",document)

class LaserPrinter:
    def printdocument(self,document):
        print("Laser printer printing : ",document)

class PDFwriter:
    def printdocument(self,document):
        print(f"Saving {document} as PDF",document)

def startPrinting(Device):
    Device.printdocument("Marvellous Notes")

def main():
    startPrinting(InkjetPrinter())
    startPrinting(LaserPrinter())
    startPrinting(PDFwriter())

main()


