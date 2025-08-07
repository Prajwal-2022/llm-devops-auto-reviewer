from graph_builder import build_graph

print("🚀 Sending code to the DevOps Auto-Reviewer Agent...\n")

graph = build_graph()

sample_code = """
resource "aws_s3_bucket" "example" {
  bucket = "example-bucket"
  acl    = "private"
}
"""

result = graph.invoke({"code": sample_code})

print("🧠 LLM DevOps Review:\n", result["review"])
print("\n⏱️ Done!")
