import argparse

# accept and parse args
def main():
    parser = argparse.ArgumentParser(description="All-In-One Productivity Suite in your Terminal")

    parser.add_argument('-p', action='store_true', help="Starts Pomodoro Timer")

    args = parser.parse_args()

    print(args.p)


if __name__ == "__main__":
    main()