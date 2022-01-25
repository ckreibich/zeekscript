#! /usr/bin/env python
import io
import os
import unittest

import zeekscript

TESTS = os.path.dirname(os.path.realpath(__file__))

class TestFormatting(unittest.TestCase):

    def test_file_formatting(self):
        script = zeekscript.Script(os.path.join(TESTS, 'data', 'test1.zeek'))
        script.parse()

        buf = io.BytesIO()
        script.format(buf)

        with open(os.path.join(TESTS, 'data', 'test1.zeek.out'), 'rb') as hdl:
            result_wanted = hdl.read()
        result_is = buf.getvalue()

        self.assertEqual(result_wanted, result_is)

    def test_parse_error(self):
        script = zeekscript.Script(os.path.join(TESTS, 'data', 'test2.zeek'))
        with self.assertRaises(zeekscript.ParserError) as cmgr:
            script.parse()
        self.assertEqual(str(cmgr.exception), 'cannot parse line 2, col 4: ")"')

if __name__ == '__main__':
    unittest.main(verbosity=0)
