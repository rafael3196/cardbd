#!/usr/bin/env python2

import sqlite3

bancoconect = sqlite3.connect('cartao.db')
command = bancoconect.cursor()
