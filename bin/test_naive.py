#!/usr/bin/env python

# standard library imports
import sys

# third party related imports

# local library imports
from Thor.pdf.page import PDFPage
from Thor.preprocess.naive import NaivePreprocessor


def main(argv):

    if len(argv) != 3:
        print 'usage: python %s <PDF-File> <page-num>' % argv[0]
        exit(1)

    filename = argv[1]
    page_num = int(argv[2])

    page = PDFPage.extract_texts(filename, [page_num])[0]
    for ix, w in enumerate(page.words):
        out = '%02d: %s' % (ix + 1, w.t)
        print out.encode('utf8')

    print '-----------------------------------------------------------'

    preprocessor = NaivePreprocessor(filename, page)
    page = preprocessor.run()
    print '-----------------------------------------------------------'
    for ix, w in enumerate(page.words):
        out = '%02d: %s' % (ix + 1, w.t)
        print out.encode('utf8')


if __name__ == '__main__':
    main(sys.argv)
