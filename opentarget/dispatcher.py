from opentarget.handlers.associated_targets import AssociatedTargetsHandler

def handler_factory(request_type: str, id: str):
    """Returns the appropriate handler class based on request_type."""
    handlers = {
        "associated_targets": AssociatedTargetsHandler,
        # Future request types can be added here
        # "disease": DiseaseHandler,
        # "target": TargetHandler,
    }

    try:
        return handlers[request_type](id)
    except KeyError:
        raise ValueError(f"Unsupported request type: {request_type}")