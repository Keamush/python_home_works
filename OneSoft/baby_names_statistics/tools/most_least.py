from typing import Dict, NamedTuple


class NameQty(NamedTuple):
    name: str
    qty: int


def make_statistics_by_years(names: Dict[str, str], gender: str):
    """Make statistics by year and gender"""
    gender_names = {}
    for year in names[gender]:
        top_name_qty = max(names[gender][year].values())
        top_name = [name for name, qty in names[gender][year].items() if qty == top_name_qty].pop()

        bottom_name_qty = min(names[gender][year].values())
        bottom_name = [name for name, qty in names[gender][year].items() if qty == bottom_name_qty].pop()

        gender_names[year] = {
            'top': NameQty(top_name, top_name_qty),
            'bottom': NameQty(bottom_name, bottom_name_qty)
        }
    return gender_names


def find_most_least_names(names: Dict[str, str]):
    """Find the mos and least common names by years"""
    girls_names = make_statistics_by_years(names, 'girls')
    boys_names = make_statistics_by_years(names, 'boys')
    return girls_names, boys_names

