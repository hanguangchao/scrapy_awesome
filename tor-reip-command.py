# -*- coding: utf-8 -*-
import os

os.system("""(echo authenticate '"mypassword"'; echo signal newnym; echo quit) | nc localhost 9051""")
