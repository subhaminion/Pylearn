import os
import json
parsed = os.environ
print json.dumps(parsed, indent=4, sort_keys=True)

# postgres 9.6
# latest rabit
# latest redis