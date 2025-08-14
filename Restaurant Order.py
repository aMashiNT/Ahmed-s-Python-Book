#Restaurant Order


def place_order(*args, **kwargs):
    print("Dishes:", args)
    print("Special Requests:", kwargs)

place_order("Pizza", "Pasta", drink="Coke", extra_cheese=True)
