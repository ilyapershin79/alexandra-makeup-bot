import os

# =========================
# TELEGRAM BOT
# =========================

BOT_TOKEN = os.getenv(
    "BOT_TOKEN",
    "8538814149:AAFh7ygU2wMe9pkBSIKYFfebGr4-SiSQAhU"
)

# =========================
# BACKEND
# =========================

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000"
)

# =========================
# DATABASE (SUPABASE)
# =========================

SUPABASE_URL = os.getenv(
    "SUPABASE_URL",
    "ВСТАВЬ_SUPABASE_URL"
)

SUPABASE_KEY = os.getenv(
    "SUPABASE_KEY",
    "ВСТАВЬ_SUPABASE_ANON_KEY"
)
