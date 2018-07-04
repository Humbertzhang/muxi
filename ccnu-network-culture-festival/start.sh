#! /bin/bash
gunicorn --name festival --timeout "120" --log-level debug -b 0.0.0.0:8085 -w 4 wsgi:app
