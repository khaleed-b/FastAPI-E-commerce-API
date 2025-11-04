from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import Base
from app.routes import auth, users, products, orders

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce API",
    description="A production-ready e-commerce backend API",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[ "http://localhost",
    "http://localhost:5173",  # local dev
    "https://69095a66c3abc9af3e929366--aesthetic-rolypoly-bf1dbc.netlify.app",  # your Netlify preview
    "https://aesthetic-rolypoly-bf1dbc.netlify.app",  # final Netlify URL (future)
]],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)


@app.get("/")
def read_root():
    return {"message": "E-Commerce API is running!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
