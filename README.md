# PyPOS

A POS (Point of Sale) system I'm building for my mother's store as a personal project.

## About

I wanted to solve a real problem instead of building something fictional. The current focus is on the backend API. A desktop interface with PyQt6 is planned for a future phase.

## What it does so far

- Creates the database tables on startup (`shop_owner`, `product`, `sale`)
- Registers accounts with bcrypt password hashing
- Validates email uniqueness
- REST API with FastAPI deployed on Render

## Tech Stack

- Python / FastAPI
- PostgreSQL (Supabase)
- Render
- bcrypt

## Running Locally

1. Clone the repository

2. Install dependencies:
      pip install -r requirements.txt

3. Set the environment variable:
      URL_DATABASE=your_supabase_connection_string

4. Run:
      uvicorn main:app --reload