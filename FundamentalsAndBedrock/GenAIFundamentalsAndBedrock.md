# FundamentalsAndBedrock

## Bedrock basics:

- An API to interact with the genAI foundation models, completely serverless.
  - has built-in support for RAG and LLM Agents
- Can integrate with Sagemaker Canvas.

### Bedrock API endpoints:

- **bedrock:** Manage, deploy, and train models.
- **bedrock-runtime:** Perform inference on models. (execute prompts, generate embeddings)
- **bedrock-agent:** Manage, deploy, and train LLM agents.
- **bedrock-agent-runtime:** Perform inference on LLM agents and knowledge bases.

### Bedrock IAM permissions:

- Must use with an IAM user and not root user.
- Requires specific permissions for each API endpoint.
