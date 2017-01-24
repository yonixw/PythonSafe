# Server config
# =====================================================
SERVER_PORT = 8000
GUI_SEPERATOR = '\\'

# Strings
# =====================================================
HELP_MESSAGE = """
<pre>
This site is part of the Python Safe (R-Pi).\r\n
Usage, POST json:\r\n
    \t{ "action" : "trycomplete" , "path" : path } for autocomplete paths\r\n
    \t{ "action" : "lock" , "path" : path } to lock a file/folder\r\n
    \t{ "action" : "unlock" , "path" : path } to unlock a file/folder\r\n
</pre>
"""

# Script config
# =====================================================
DETAILED_ERRORS = True # Set false if security is an issue
STACK_TRACE_LIMIT = 100
