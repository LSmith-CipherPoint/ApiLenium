# coding=utf-8
"""
ApiLenium.__main__ Tests
"""
from __future__ import print_function

from random import randrange

from nose.tools import assert_false

from ApiLenium.__main__ import main

argv0 = 'apilenium'


def fuzz():
    return [argv0] + ["".join([chr(randrange(256))
                      for _ in range(randrange(16))])
                      for _ in range(randrange(16))]


class TestApiLenium(object):
    """Tests the main call method and argument/options parser.

    """
    def test_it_runs(self):
        raised = False
        try:
            main()
            main([argv0])
            main([argv0, '-h'])
        except:
            raised = True
        assert_false(raised, "Should Always run")

    def test_main_inputs_fuzz(self):
        for _ in range(5000):
            raised = False
            inputs = fuzz()
            try:
                main(inputs)
            except:
                raised = True
            assert_false(raised,
                         "Input should not raise errors: " + " ".join(inputs))
