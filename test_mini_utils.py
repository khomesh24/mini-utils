import unittest
import os
import argparse
from mini_ls import mini_ls
from mini_grep import mini_grep
from mini_df import mini_df


class MyTestCase(unittest.TestCase):
    def test_mini_ls_1(self):
        path = os.path.abspath(os.curdir)
        recursive = False
        result = mini_ls(path, recursive)
        self.assertEqual(result, 0)

    def test_mini_ls_2(self):
        path = os.path.abspath(os.curdir)
        recursive = True
        result = mini_ls(path, recursive)
        self.assertEqual(result, 0)

    def test_mini_ls_3(self):
        path = '/etcsad/adwawd'
        recursive = True
        self.assertEqual(mini_ls(path, recursive), 2)

    def test_mini_grep_1(self):
        args = argparse.Namespace(e='mini', q=False, File=['mini_grep.py'])
        self.assertEqual(mini_grep(args), 0)

    def test_mini_grep_2(self):
        args = argparse.Namespace(e='print', q=True, File=['mini_grep.py', 'mini_ls.py', 'mini_df.py'])
        self.assertEqual(mini_grep(args), 0)

    def test_mini_grep_3(self):
        args = argparse.Namespace(e='mini', q=False, File=['mini_grep.py', 'mini_random.py'])
        self.assertEqual(mini_grep(args), 0)

    def test_mini_df_1(self):
        args = argparse.Namespace(H=False, Path=['/home/khomesh/PycharmProjects/mini-utils'])
        self.assertEqual(mini_df(args), 0)

    def test_mini_df_2(self):
        args = argparse.Namespace(H=True, Path=['/home/khomesh/PycharmProjects/mini-utils', '/etc'])
        self.assertEqual(mini_df(args), 0)


if __name__ == '__main__':
    unittest.main()
