# test_pancakeswap.py
"""
Tests for PancakeSwap module.
"""

import unittest
from pancakeswap import PancakeSwap

class TestPancakeSwap(unittest.TestCase):
    """Test cases for PancakeSwap class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PancakeSwap()
        self.assertIsInstance(instance, PancakeSwap)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PancakeSwap()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
