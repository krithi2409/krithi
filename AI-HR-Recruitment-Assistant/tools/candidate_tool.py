from database import get_candidates

def search_candidates(keyword):
    keyword = keyword.lower()
    return [c for c in get_candidates()
            if keyword in " ".join(map(str, c)).lower()]
