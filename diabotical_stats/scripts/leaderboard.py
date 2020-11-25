#!/usr/bin/env python3
from diabotical_stats.cli import parser
from diabotical_stats.diabotical_stats import get_stats


def main():
    args = parser().parse_args()
    result = get_stats(args.mode, args.count, args.user_id, args.country)
    print(result)


if __name__ == '__main__':
    main()
