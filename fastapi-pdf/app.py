from fastapi import FastAPI
import sys
import os

debug = os.environ.get('DEBUG', False)

app = FastAPI(debug=debug)


@app.get('/')
async def version():
    return {'version': sys.version}
