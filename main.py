#!/usr/bin/env python3
"""Worth Invading — entry for One Star, Five Stars for the Food on make.fun.

Prints exactly one sentence (at most 200 characters) in the voice of an
alien tourist giving Earth a one-star review while praising the food.
"""

LINE = "One star: gravity is exhausting, the locals charge for water, and the sun is unshielded, but the noodle soups alone nearly justify the invasion."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 200
    print(LINE)


if __name__ == "__main__":
    main()
