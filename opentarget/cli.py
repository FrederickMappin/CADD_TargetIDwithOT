import sys
from opentarget.dispatcher import HANDLERS

def main():
    if len(sys.argv) != 3:
        print("Usage: python -m opentarget <ID> <request_type>")
        print(f"Valid request types: {', '.join(HANDLERS.keys())}")
        sys.exit(1)

    entity_id = sys.argv[1]
    request_type = sys.argv[2]

    if request_type not in HANDLERS:
        print(f"Invalid request type: {request_type}")
        print(f"Valid request types: {', '.join(HANDLERS.keys())}")
        sys.exit(1)

    handler_class = HANDLERS[request_type]
    handler = handler_class(entity_id)
    data = handler.fetch_or_load()
    table_rows, headers = handler.parse(data)

    from tabulate import tabulate
    print(tabulate(table_rows, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    main()

