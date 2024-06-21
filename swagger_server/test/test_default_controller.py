# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_api_market_asks_get(self):
        """Test case for api_market_asks_get

        Get Market Ask Orders
        """
        response = self.client.open(
            '/api/market/asks',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_market_bids_get(self):
        """Test case for api_market_bids_get

        Get Market Bid Orders
        """
        response = self.client.open(
            '/api/market/bids',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_market_books_get(self):
        """Test case for api_market_books_get

        Get Market Order Book
        """
        response = self.client.open(
            '/api/market/books',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_market_depth_get(self):
        """Test case for api_market_depth_get

        Get Market Order Depth
        """
        response = self.client.open(
            '/api/market/depth',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_market_symbols_get(self):
        """Test case for api_market_symbols_get

        Get Available Market Symbols
        """
        response = self.client.open(
            '/api/market/symbols',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_market_ticker_get(self):
        """Test case for api_market_ticker_get

        Get Market Ticker Information
        """
        response = self.client.open(
            '/api/market/ticker',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_market_trades_get(self):
        """Test case for api_market_trades_get

        Get Recent Market Trades
        """
        response = self.client.open(
            '/api/market/trades',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servertime_get(self):
        """Test case for api_servertime_get

        Get Server Time
        """
        response = self.client.open(
            '/api/servertime',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_status_get(self):
        """Test case for api_status_get

        Get API Status
        """
        response = self.client.open(
            '/api/status',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v3_servertime_get(self):
        """Test case for api_v3_servertime_get

        Get Server Time (v3)
        """
        response = self.client.open(
            '/api/v3/servertime',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_tradingview_history_get(self):
        """Test case for tradingview_history_get

        Get TradingView Historical Data (Deprecated)
        """
        response = self.client.open(
            '/tradingview/history',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
