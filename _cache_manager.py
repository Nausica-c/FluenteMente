import os
import json
import hashlib

# =========================
# CACHE CONFIG
# =========================

CACHE_FILE = "_cache/cache.json"


# =========================
# INIT SAFETY
# =========================

def _ensure_dir():
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)


# =========================
# LOAD CACHE (SAFE MODE)
# =========================

def load_cache():
    """
    Safe load:
    - handles missing file
    - handles empty file
    - handles corrupted JSON
    - never crashes pipeline
    """

    _ensure_dir()

    if not os.path.exists(CACHE_FILE):
        return {}

    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            raw = f.read().strip()

            if raw == "":
                return {}

            return json.loads(raw)

    except Exception:
        # 🔥 auto recovery mode
        try:
            os.rename(CACHE_FILE, CACHE_FILE + ".broken")
        except:
            pass

        return {}


# =========================
# SAVE CACHE (ATOMIC WRITE)
# =========================

def save_cache(cache: dict):
    """
    Atomic write to avoid corruption in GitHub Actions.
    """

    _ensure_dir()

    tmp = CACHE_FILE + ".tmp"

    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

    os.replace(tmp, CACHE_FILE)


# =========================
# HASH UTIL
# =========================

def make_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# =========================
# CACHE OPERATIONS
# =========================

def get(cache: dict, key: str):
    return cache.get(key)


def set(cache: dict, key: str, value: str):
    cache[key] = value


def has_changed(cache: dict, key: str, new_value: str) -> bool:
    """
    True = needs update
    False = skip
    """
    return cache.get(key) != new_value
