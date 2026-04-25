import argparse
from datetime import timedelta

def main():
    parser = argparse.ArgumentParser(description='Pomodoro timer CLI with notifications')
    
    parser.add_argument('--work', type=int, default=25, help='Work time in minutes (default: 25)')
    parser.add_argument('--short-break', type=int, default=5, help='Short break time in minutes (default: 5)')
    parser.add_argument('--long-break', type=int, default=15, help='Long break time in minutes (default: 15)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--output', action='store_true', help='Write to output file')
    
    args = parser.parse_args()
    
    try:
        remaining_time = timedelta(minutes=args.work)
        
        while remaining_time > timedelta(seconds=0):
            print(f"Remaining time: {remaining_time}")
            
            if args.json:
                import json
                print(json.dumps({"time": str(remaining_time)}, indent=4))
            
            if args.output:
                with open("pomodoro.log", "a") as file:
                    file.write(f"{str(remaining_time)}\n")
            
            remaining_time -= timedelta(seconds=1)
            
            # Pause for the break time
            if remaining_time % (args.work + args.short_break) == 0:
                print("Long break time!")
                remaining_time = timedelta(minutes=args.long_break)
            elif remaining_time % (args.work + args.short_break) == args.short_break:
                print("Short break time!")
                remaining_time = timedelta(minutes=args.short_break)
            else:
                remaining_time -= timedelta(seconds=1)
        
        print("Pomodoro session completed!")
    except KeyboardInterrupt:
        print("Interrupted by user.")

if __name__ == "__main__":
    main()