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

### Fine-tuning a model:
- In Amazon Bedrock, you can fine-tune a model by creating a custom model version. This involves providing your training data and specifying the base model you want to fine-tune. 
- The process is managed through the Bedrock API, and you can monitor the training progress and manage your custom models through the Bedrock console or API.
- Following models can be fine-tuned:
  - Amazon Titan
  - Cohere
  - Meta models
- Use VPC and private link to fine tune the model.
  - This is a potential security question in the model.

#### Low Rank Adaptation (LRA):

- LRA is a technique that reduces the number of parameters in a model by removing redundant information.
- It is used to reduce the size of a model by removing redundant information.
- We dont need to fine tune the entire model, but add some low-rank matrices to the attention weights.
- At inference time, we can use the low-rank matrices to generate the output, which is much faster than using the entire model.


### Retrieval Augmented Generation (RAG):

- RAG is a technique that combines the power of LLMs with the ability to retrieve and combine information from external sources.
- It allows you to generate responses based on a query and retrieve relevant information from a knowledge base.
- Can leverage semantic search via vector stores to find relevant information.