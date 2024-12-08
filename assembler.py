import hack
import sys

parser = hack.Parser(sys.argv[1])
while parser.hasMoreLines():
    parser.advance()

    print("symbol: {}, dest: {}, comp: {}, jump: {}".format(
          parser.symbol(), parser.dest(), parser.comp(), parser.jump()))