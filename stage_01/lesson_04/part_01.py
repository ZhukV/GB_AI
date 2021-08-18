import argparse


def initialize_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--rate',
        help='The salary rate per one hour.',
        required=True
    )

    parser.add_argument(
        '--hours',
        help='Total worked hours.',
        required=True
    )

    parser.add_argument(
        '--bonus',
        help='The bonus for employee.',
        required=False,
        default='0'
    )

    return parser


def main() -> None:
    parser = initialize_argument_parser()

    args = parser.parse_args()

    if not str(args.rate).isdigit() or int(args.rate) < 0:
        print('The --rate is invalid. Only positive digits allowed.')
        exit(1)

    if not str(args.hours).isdigit() or int(args.hours) < 0:
        print('The --hours is invalid. Only positive digits allowed.')
        exit(1)

    if not str(args.bonus).isdigit() or int(args.bonus) < 0:
        print('The --bonus is invalid. Only positive digits allowed.')
        exit(1)

    total_salary = int(args.rate) * int(args.hours) + int(args.bonus)

    print(f'Total salary for employee is {total_salary}.')


if __name__ == '__main__':
    main()
