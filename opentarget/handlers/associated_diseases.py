from opentarget.core.base_handler import BaseHandler

class AssociatedDiseasesHandler(BaseHandler):
    def get_url(self) -> str:
        query = """
        query associatedDiseases($ensemblId: String!) {
          target(ensemblId: $ensemblId) {
            id
            approvedSymbol
            associatedDiseases {
              count
              rows {
                disease {
                  id
                  name
                }
                datasourceScores {
                  id
                  score
                }
              }
            }
          }
        }
        """
        return {
            "url": "https://api.platform.opentargets.org/api/v4/graphql",
            "json": {
                "query": query,
                "variables": {"ensemblId": self.id}
            }
        }

    def parse(self, data: dict) -> tuple[list[list], list[str]]:
        try:
            rows = data["data"]["target"]["associatedDiseases"]["rows"]
            table_rows = []
            for row in rows:
                disease_id = row["disease"]["id"]
                disease_name = row["disease"]["name"]
                scores = ", ".join(
                    f"{score['id']}: {round(score['score'], 3)}"
                    for score in row["datasourceScores"]
                )
                table_rows.append([disease_id, disease_name, scores])
            
            headers = ["\033[92mDisease ID\033[0m", "\033[92mDisease Name\033[0m", "\033[92mDatasource Scores\033[0m"]
            return table_rows, headers
        except Exception as e:
            raise ValueError(f"Failed to parse response: {e}")