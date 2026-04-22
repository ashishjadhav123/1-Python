import argparse

# Command line Optional Arguments calling this file from Main2.py

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help="first number", type=int)
    parser.add_argument("--number2", help="second number", type=int)
    parser.add_argument("--operation", help="operation", type=str)

    args = parser.parse_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)

    if args.operation == "add":
        print(f"Addition: {args.number1 + args.number2}")
    elif args.operation == "sub":
        print(f"Subtraction: {args.number1 - args.number2}")
    elif args.operation == "mul":
        print(f"Multiplication: {args.number1 * args.number2}")
    elif args.operation == "div":
        print(f"Division: {args.number1 / args.number2}")
    else:
        print("Invalid operation")

