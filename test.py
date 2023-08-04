"""The built-in Python unit testing framework."""
import unittest
"""The Tkinter library, which provides tools for creating graphical user interfaces."""
import tkinter as tk
"""A module within Tkinter used for color selection."""
from tkinter import colorchooser
"""A decorator for temporarily modifying the behavior of functions."""
from unittest.mock import patch
from main import TextEditorApp


class TestTextEditorGUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = tk.Tk()
        cls.app = TextEditorApp(cls.root)

    @classmethod
    def tearDownClass(cls):
        cls.root.destroy()

    def test_change_color(self):
        with patch.object(colorchooser, 'askcolor', return_value=(None, "#FF0000")):
            self.app.change_color()
            self.assertEqual(self.app.text_area.cget("fg"), "#FF0000")

    def test_change_font(self):
        self.app.font_name.set("Arial")
        self.app.font_size.set("18")
        self.app.change_font()
        self.assertEqual(self.app.text_area.cget("font"), ("Arial", 18))

    def test_new_file(self):
        self.app.new_file()
        self.assertEqual(self.app.window.title(), "untitled")
        self.assertEqual(self.app.text_area.get("1.0", "end-1c"), "")


if __name__ == '__main__':
    unittest.main()
