REVIEW_PROMPT = """You are an expert DevOps engineer. Review the following code and give suggestions or best practices.

Code:
{code}
"""

ANALYZE_PROMPT = """You are a cloud engineer analyzing a DevOps IaC configuration. Analyze the following code and return only observations or potential issues.

Code:
{code}
"""

CRITIC_PROMPT = """You're acting as a senior SRE reviewer. Critique the following code, suggesting improvements in security, reliability, or cost-efficiency.

Code:
{code}
"""
