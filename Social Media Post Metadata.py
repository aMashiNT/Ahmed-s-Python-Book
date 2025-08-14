#Social Media Post Metadata


def post_content(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

post_content(author="Ahmed", likes=120, shares=30, caption="Good vibes!")
