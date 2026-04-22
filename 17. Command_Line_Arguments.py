import argparse

# Command line Arguments Calling this file from Main.py

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", type=int, help="first number")
    parser.add_argument("number2", type=int, help="second number")
    parser.add_argument("operation", type=str, help="operation")

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

