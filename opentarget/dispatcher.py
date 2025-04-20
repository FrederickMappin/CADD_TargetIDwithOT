from opentarget.handlers.associated_targets import AssociatedTargetsHandler
from opentarget.handlers.associated_diseases import AssociatedDiseasesHandler
from opentarget.handlers.target_disease_evidence import TargetDiseaseEvidenceHandler

HANDLERS = {
    "associated_targets": AssociatedTargetsHandler,
    "associated_diseases": AssociatedDiseasesHandler,
    "target_disease_evidence": TargetDiseaseEvidenceHandler,
}

def handler_factory(request_type: str, id: str):
    """Returns the appropriate handler class based on request_type."""
    try:
        return HANDLERS[request_type](id)
    except KeyError:
        raise ValueError(f"Unsupported request type: {request_type}")