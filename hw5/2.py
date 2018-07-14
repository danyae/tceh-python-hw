class Printer:
    def log(self, *values):
        for item in values:
            print(item)


class FormattedPrinter(Printer):
    def log(self, *values):
        for item in values:
            print('\n' + '*' * 20)
            print(item)
            print('*' * 20)


line1 = 'line1'
line2 = 'line2'
line3 = 'line3'
printer = Printer()
formatterprinter = FormattedPrinter()
printer.log(line1, line2, line3)
formatterprinter.log(line1, line2, line3)
