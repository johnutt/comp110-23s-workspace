"""Practice with dictionaries"""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

ice_cream["mint"] = 3
print(f"After adding mint: {ice_cream}")

ice_cream.pop("mint")
print(f"After removing mint: {ice_cream}")

print(f"Number of vanilla: {ice_cream['vanilla']}")

ice_cream["vanilla"] += 1

print(f"After adding 1 vanilla: {ice_cream['vanilla']}")

print("mint" in ice_cream)
print("chocolate" in ice_cream)

