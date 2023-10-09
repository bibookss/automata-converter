import unittest
from tests.tests import TestDFA, TestNFA, TestENFA
import argparse

def run_tests(test_classes):
    suite = unittest.TestSuite()

    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suite.addTests(tests)

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', '-t', action='store_true', help='Run tests')
    args = parser.parse_args()

    if args.test:
        print('Running tests...')
        test_classes = [TestDFA, TestNFA, TestENFA]
        run_tests(test_classes)

        exit(0)


        