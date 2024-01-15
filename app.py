from companyblog import app
from flask import Flask
import os 
#port = int(os.environ.get('PORT', 33507))


if __name__ == '__main__':
    app.run(debug=True)