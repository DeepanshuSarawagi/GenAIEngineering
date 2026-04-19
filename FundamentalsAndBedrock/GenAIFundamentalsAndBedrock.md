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

### Chunking with Bedrock:
- Chunking is the process of breaking down large documents into smaller, manageable pieces (chunks) that can be processed by the LLM.
- This is important because LLMs have a context window limit, which is the maximum amount of text they can process at once.
- By chunking documents, we can ensure that the LLM can effectively process the information without exceeding its context window limit.

#### Standard Chunking:

- In **Fixed Size**, you specify the tokens per chunk and overlap percentage.
- Default is 300 tokens per chunk with 20% overlap.
- No chunking:
  - Every document is a chunk, regardless of size.

#### Hierarchical Chunking:
- In **Hierarchical**, you specify the chunking levels and the tokens per chunk for each level.
- Nested parent/child chunk.
- Initial search hits the child chunks, then the parent chunk is hit to get more context when appropriate.
- The idea is get better precision in retrieval by having smaller chunks, but also get better recall by having parent chunks that can provide more context.

#### Semantic Chunking:
- In **Semantic**, hits a foundation model to break up chunks based on the meaning of the text and just things like sentences or
  fixed chunk size.
- This is more expensive than the other two chunking methods, but it can provide better results.
- Buffer size:
  - Number of surrounding sentences per sentence to consider when embedding i.e., if buffer size of 1 results in 3 sentences per chunk (the sentence itself and one sentence on either side).
  - Too large = introducing noise, too small = missing out on important context.

### Optimizing your embeddings:

- Use a smaller vector is a good way to cost efficiency.
- Smaller vector means fewer dimensions per chunk which means less cost.

### Measuring your RAG system:
- Bedrock includes RAG evaluation jobs that can measure:
  - Correctness
  - Completeness
  - Helpfulness
  - Logical coherence
  - Faithfulness
  - Citation precision
  - Coverage
  - Harmfulness
  - Stereotyping
  - Bias
  - Refusal
- 