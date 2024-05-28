import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    print("Current working directory:", os.getcwd())
    app.run(host='0.0.0.0', port=3000)
