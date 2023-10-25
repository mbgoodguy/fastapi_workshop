import uvicorn

uvicorn.run(
    'workshop.app:app',
    reload=True,
    port=8000
)
