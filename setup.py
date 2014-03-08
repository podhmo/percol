#/usr/bin/env python

from setuptools import setup

import percol
tests_require = [
    'nose'
]

setup(name             = "percol",
      version          = percol.__version__,
      author           = "mooz",
      author_email     = "stillpedant@gmail.com",
      url              = "https://github.com/mooz/percol",
      description      = "Adds flavor of interactive filtering to the traditional pipe concept of shell",
      long_description = percol.__doc__,
      packages         = ["percol"],
      scripts          = ["bin/percol"],
      classifiers      = ["Environment :: Console :: Curses",
                          "License :: OSI Approved :: MIT License",
                          "Operating System :: POSIX",
                          "Programming Language :: Python",
                          "Topic :: Text Processing :: Filters",
                          "Topic :: Text Editors :: Emacs",
                          "Topic :: Utilities",
                          "Programming Language :: Python",
                          "Programming Language :: Python :: 3"],
      keywords         = "anything.el unite.vim dmenu shell pipe filter curses",
      license          = "MIT",
      extras_require = {
          "testing": tests_require
      }, 
      test_suite="percol.tests"
  )
