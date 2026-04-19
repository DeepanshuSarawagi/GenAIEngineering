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
  - It uses embeddings which kind of encode the underlying meaning of the information.
  - And therefore performs a search based on the semantic meaning of the query/prompt.

#### Embeddings:
- Embeddings are a way to represent the meaning of an information piece.
  - They are a vector representation of the information.
  - Embeddings are computed such that items that are similar to each other are close to each other in the vector space.
  - Finding items that are similar to each other is performed using cosine similarity.
- They are used to encode the underlying meaning of the information.
- They are used to perform semantic search.
- We can use embedding base models like Amazon Titan to compute embeddings.

#### RAG Flow:
1. User provides a query or prompt.
2. The system computes the embedding of the query using an embedding model.
3. The system performs a semantic search in the vector store to find relevant information based on the computed embedding.
4. The retrieved information is then combined with the original query and passed to the LLM to generate a response.
5. The LLM generates a response based on the combined input of the original query and the retrieved information.
