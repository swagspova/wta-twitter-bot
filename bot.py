from api.tennis_api import get_live_matches
from api.match_parser import parse_matches

data = get_live_matches()

parse_matches(data)