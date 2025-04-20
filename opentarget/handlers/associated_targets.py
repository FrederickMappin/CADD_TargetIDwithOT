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
            # Add ANSI escape codes for green headers
            headers = ["\033[92mSymbol\033[0m", "\033[92mTarget ID\033[0m", "\033[92mScore\033[0m"]
            return table_rows, headers
        except Exception as e:
            raise ValueError(f"Failed to parse response: {e}")