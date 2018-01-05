from unittest import TestCase
from exchanges import bitflyer
from exchanges.base.initializer import NewExchange
from exchanges.base.exchange import EXCHANGES
import os,json,logging

KEYS_GLOBAL = './keys.json'
KEYS_LOCAL = './keys.local.json'
KEYS_FILE = KEYS_LOCAL if os.path.exists(KEYS_LOCAL) else KEYS_GLOBAL

class TestExchanges(TestCase):
    @classmethod
    def setUpClass(cls):
        with open(KEYS_FILE) as file:
            cls.config = json.load(file)
        cls.gen_exchange(cls)

    def gen_exchange(self):
        self.exchanges = [NewExchange(e,self.config[e]["apikey"],self.config[e]["secretkey"]) for e in EXCHANGES]

    def test_ticker(self):
        for ex in self.exchanges:
            markets = ex.markets()
            self.assertEqual(type(markets), tuple)
            for m in markets:
                self.assertEqual(len(ex.ticker(m)), 7)

    def test_board(self):
        for ex in self.exchanges:
            board = ex.board()
            

if __name__ == "__main__":
    unittest.main()