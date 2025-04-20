import sys
from opentarget.dispatcher import handler_factory
from opentarget.core.fetcher import fetch_or_load

def main():
    if len(sys.argv) != 3:
        print("Usage: python -m opentarget <ID> <request_type>")
        sys.exit(1)

    id = sys.argv[1]
    request_type = sys.argv[2]
    
    handler = handler_factory(request_type, id)  # Dispatch correct handler
    data = fetch_or_load(handler)                # Load from cache or fetch from API
    rows, headers = handler.parse(data)          # Parse response
    
    # Pretty print table output
    from tabulate import tabulate
    print(tabulate(rows, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    main()

