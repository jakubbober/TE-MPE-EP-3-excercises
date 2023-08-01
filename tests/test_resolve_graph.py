import os
import unittest

from solutions.second import resolve_graph
from solutions.second import utils

VALID_JSON_FILENAME = os.path.join(os.path.dirname(__file__), 'test_data/valid_json.json')
VALID_REPR_FILENAME = os.path.join(os.path.dirname(__file__), 'test_data/valid_repr.json')


class TestResolveGraph(unittest.TestCase):
    def test_resolve_graph(self):
        expected = utils.read_json(VALID_REPR_FILENAME)
        # print(resolve_graph.resolve_graph(VALID_JSON_FILENAME).__repr__())
        self.assertDictEqual(expected, resolve_graph.resolve_graph(VALID_JSON_FILENAME).__repr__())
