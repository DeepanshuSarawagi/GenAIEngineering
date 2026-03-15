# AI Concepts

## Cognitive Computing

- Provides enhanced functionality, Adaptability, and Intelligence.
- Tech to mimic human cognitive processes.

### Core elements of Cognitive Computing:
- Perception
  - Interprets the environment
  - Gathers structured and unstructured information
- Learning
  - Use ML algorithms to analyze data and learn from it
- Reasoning
  - Making accurate decisions and predictions based on data analysis.

## AI Terminologies:

### Deep Learning:

- Uses layered neural networks to analyze and learn from data.
- Labels and categorize data.
- Identifies patterns and relationships.
- Determines the correctness of predictions.
- Enabled natural language understanding.
- Deep learning applications:
  - Image captioning
  - Voice transcription and recognition
  - Facial recognition
  - Object detection and tracking
  - Speech recognition
  - Recommendation systems
  - Natural language processing
  - Computer vision
  - Robotics
  - Medical imaging
  - Autonomous driving
  - Personalized content and advertising

### Neural Networks:
- Input layer: Receives data.
- Hidden layers: Process data and extract features.
- Output layer: Produces the final result.
- **Neural network architecture:**
  - **Neural network layers:**
    - Neurons: Basic processing units that receive input, apply weights, and produce output.
    - Activation functions: Determine whether a neuron should be activated based on the input it receives.
    - Weights: Parameters that determine the strength of the connection between neurons.
    - Biases: Additional parameters that allow the model to fit the data better by shifting the activation function.
- **Training techniques:**
  - **Forward Propagation:**
    - Data flows through the network from input to output.
    - Each layer processes the data and passes it to the next layer.
    - Network computes an output.
  - **Backpropagation:**
    - After forward propagation, the network calculates the error by comparing the predicted output to the actual output.
    - The error is then propagated backward through the network to update the weights and biases.
    - This process helps the network learn and improve its predictions over time.
- **Types of Neural Networks:**
  - Convolutional Neural Networks (CNNs): Primarily used for image and video recognition tasks.
  - Recurrent Neural Networks (RNNs): Designed for sequential data, such as time series or natural language processing.
  - Generative Adversarial Networks (GANs): Consist of two or more neural networks that compete against each other to generate realistic data.

### Machine Learning:
- Algorithms that enable computers to learn from data.
- Supervised learning: Uses labeled data to make predictions.
- Unsupervised learning: Finds patterns and relationships in unlabeled data.
  - Clustering: Groups similar data points together.
- Reinforcement learning: Learns through trial and error.
  - Define state, desired goal, allowed actions, and constraints to guide learning.

#### Machine Learning Techniques and Training:
- **Supervised Learning:**
  - Employs data sets with predefined class labels.
  - Trains models to predict or classify new data points.
- **Unsupervised Learning:**
  - Utilizes data sets without predefined labels.
  - Identifies patterns, relationships, or clusters within the data.
- **Reinforcement Learning:**
  - Involves an agent learning to make decisions by interacting with an environment.
  - The agent receives feedback in the form of rewards or penalties based on its actions, allowing it to learn optimal strategies over time.

#### Types of supervised learning:
- **Regression:**
    - Predicts continuous values based on input data.
    - Example: Predicting house prices based on features like size, location, and number of bedrooms.
- **Classification:**
    - Assigns input data to predefined categories or classes.
    - Example: Classifying emails as spam or not spam based on their content and metadata.
    - Forms of classification:
        - Decision trees
        - Logistic regression
        - Random forests
        - Support vector machines

### Machine Learning vs Deep Learning vs Foundation Models:
- **Machine Learning:**
  - We define inputs to the data and assign weights to each input marking its importance.
  - Larger weights make a single input contribution to the output more significant compared to others.
- **Deep Learning:**
  - Neural networks are trained to learn patterns and relationships in data.
  - Each neuron in the network is connected to other neurons in the network.
  - The more connections between neurons, the more complex the patterns and relationships that can be learned.
  - Doesn't really require any labeled datasets.
- **Foundation Models:**
  - These are large-scale neural networks trained on vast amounts of data, often using unsupervised learning techniques.
  
## Generative AI models:

### Variational Autoencoders (VAEs):
- Works by transforming input data by encoding and decoding.
- They have three main components:
  - Encoder: Compresses the input data into a lower-dimensional representation.
  - Latent space: A continuous space where the key features of the data is captured.
  - Decoder: Reconstructs the original data from the compressed representation from latent space.
- VAEs are used in image generation, text generation, and other applications where generating new data is desired.

### Generative Adversarial Networks (GANs):
- A type of generative model that combines two neural networks:
  - Generator: Generates new data samples.
  - Discriminator: Evaluates the authenticity of the generated samples.
- The generator and discriminator are trained together in a competitive process, 
  where the generator tries to produce realistic data to fool the discriminator, while the discriminator tries to distinguish between real and generated data.
- Used for image synthesis, Style transfer, and data augmentation.

### Autoregressive models:
- A type of generative model creates data sequentially based on previous data.
- These models predict the next value in a sequence based on the previous values.
- WaveNets are a popular example of autoregressive models.
- Autoregressive models are particularly useful in time series analysis and forecasting.

### Transformers:
- Transformers are particularly useful in natural language processing and machine translation.
- They consist of encoder and decoder layers enabling the model to generate text sequences or perform cross language translations.
- OpenAI's GPT-5 (Generative Pretrained Transformer) is a transformer-based language model.
- Categories of transformers:
  - Unimodal:
    - Processes a single type of data, such as text or images. E.g., GPT-3.
  - Multimodal:
    - Capable of processing and generating multiple types of data, such as text and images together. E.g., DALL-E.

## Large Language Models (LLMs):
- Large language models are capable of generating human-like text based on a large amount of data.
- They are trained on large datasets of text and are able to generate new text based on the input.
- They are part of different class of models called foundation models.
- They are trained on huge amounts of data that are unstructured and unlabeled in unsupervised manner.
  - If we introduce small amounts of labeled data, to the equation, the model will be tuned to perform traditional NLP tasks.
  - This is called fine-tuning.
  - If you don't have enough data, or have only few data points, they can still work with low label data domains in a 
    process called prompting.