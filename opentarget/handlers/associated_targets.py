from opentarget.core.base_handler import BaseHandler

class AssociatedTargetsHandler(BaseHandler):
    def get_url(self) -> str:
        query = """
        query associatedTargets($efoId: String!) {
          disease(efoId: $efoId) {
            id
            name
            associatedTargets {
              rows {
                target {
                  id
                  approvedSymbol
                }
                score
              }
            }
          }
        }
        """
        return {
            "url": "https://api.platform.opentargets.org/api/v4/graphql",
            "json": {
                "query": query,
                "variables": {"efoId": self.id}
            }
        }

    def parse(self, data: dict) -> tuple[list[list], list[str]]:
        try:
            rows = data["data"]["disease"]["associatedTargets"]["rows"]
            table_rows = [[r["target"]["approvedSymbol"], r["target"]["id"], round(r["score"], 3)] for r in rows]
            headers = ["Symbol", "Target ID", "Score"]
            return table_rows, headers
        except Exception as e:
            raise ValueError(f"Failed to parse response: {e}")