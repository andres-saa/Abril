from fastapi import FastAPI
app=FastAPI(title='asistente')

@app.get('/')
def hi():
    return {'msg':'asistente'}
