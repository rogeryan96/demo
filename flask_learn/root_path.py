import sys
import os

import_name = __name__

print import_name

mod = sys.modules.get(import_name)
print mod.__file__, os.path.abspath(mod.__file__) , os.path.dirname(os.path.abspath(mod.__file__))