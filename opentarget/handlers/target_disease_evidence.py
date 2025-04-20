from opentarget.core.base_handler import BaseHandler
from opentarget.handlers.associated_targets import AssociatedTargetsHandler
from opentarget.handlers.associated_diseases import AssociatedDiseasesHandler

class TargetDiseaseEvidenceHandler(BaseHandler):
    def get_url(self) -> str:
        query = """
        query targetDiseaseEvidence($efoId: String!, $ensemblId: String!, $datasourceIds: [String!]) {
          disease(efoId: $efoId) {
            id
            name
            evidences(datasourceIds: $datasourceIds, ensemblIds: [$ensemblId]) {
              count
              rows {
                disease {
                  id
                  name
                }
                diseaseFromSource
                target {
                  id
                  approvedSymbol
                }
                mutatedSamples {
                  functionalConsequence {
                    id
                    label
                  }
                  numberSamplesTested
                  numberMutatedSamples
                }
                resourceScore
                significantDriverMethods
                cohortId
                cohortShortName
                cohortDescription
              }
            }
          }
        }
        """
        return {
            "url": "https://api.platform.opentargets.org/api/v4/graphql",
            "json": {
                "query": query,
                "variables": {
                    "efoId": self.id,
                    "ensemblId": "ENSG00000172936",
                    "datasourceIds": ["intogen"]
                }
            }
        }

    def parse(self, data: dict) -> tuple[list[list], list[str]]:
        try:
            rows = data["data"]["disease"]["evidences"]["rows"]
            table_rows = []
            for row in rows:
                disease_id = row["disease"]["id"]
                disease_name = row["disease"]["name"]
                disease_from_source = row.get("diseaseFromSource", "N/A")
                target_symbol = row["target"]["approvedSymbol"]
                resource_score = round(row["resourceScore"], 3) if row.get("resourceScore") else "N/A"
                cohort_short_name = row.get("cohortShortName", "N/A")
                mutated_samples = ", ".join(
                    f"{sample['functionalConsequence']['label']} ({sample['numberMutatedSamples']}/{sample['numberSamplesTested']})"
                    for sample in row.get("mutatedSamples", [])
                )
                table_rows.append([
                    disease_id,
                    disease_name,
                    disease_from_source,
                    target_symbol,
                    resource_score,
                    cohort_short_name,
                    mutated_samples
                ])
            
            headers = [
                "\033[92mDisease ID\033[0m",
                "\033[92mDisease Name\033[0m",
                "\033[92mDisease From Source\033[0m",
                "\033[92mTarget Symbol\033[0m",
                "\033[92mResource Score\033[0m",
                "\033[92mCohort Short Name\033[0m",
                "\033[92mMutated Samples\033[0m"
            ]
            return table_rows, headers
        except Exception as e:
            raise ValueError(f"Failed to parse response: {e}")

HANDLERS = {
    "associated_targets": AssociatedTargetsHandler,
    "associated_diseases": AssociatedDiseasesHandler,
    "target_disease_evidence": TargetDiseaseEvidenceHandler,
}