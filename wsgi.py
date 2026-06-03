import sys
import os

# Identify the project path (handles multiple common naming conventions)
path = os.path.expanduser('~/Event-management-main/Event-management-main')
if not os.path.exists(path):
    path = os.path.expanduser('~/Event-management/Event-management-main')
if not os.path.exists(path):
    path = os.path.expanduser('~/Event-management-main')
if not os.path.exists(path):
    path = os.path.expanduser('~/Event-management')

if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variables for production
# On PythonAnywhere, you can also set these in the WSGI config file itself
# os.environ['DATABASE_URL'] = 'your-neon-url'
# os.environ['SECRET_KEY'] = 'your-secret-key'

from app import app as application
