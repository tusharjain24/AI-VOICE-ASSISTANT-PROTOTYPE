# Cosmos Voice Assistant

A conversational AI voice assistant focused on answering questions exclusively about _Cosmos: A Personal Voyage_ by Carl Sagan. This assistant, built with LiveKit and OpenAI's APIs, includes a unique quiz feature, prompting users with questions on the same topic.

## Features

- **Knowledge-Based Conversations**: The assistant answers questions only related to _Cosmos: A Personal Voyage_. For unrelated topics, it politely reminds the user to stay on topic.
- **Interactive Quiz**: Users can take a 5-question quiz related to _Cosmos_. The assistant tracks previous questions and avoids repeats if the user retakes the quiz.
- **Audio-Only Mode**: Uses LiveKit to interact with users over voice, featuring speech recognition (STT), language processing (LLM), and text-to-speech (TTS).

## Technologies Used

- **LiveKit**: For real-time voice interaction.
- **OpenAI API**: Powers the assistant's STT, LLM, and TTS.
- **Silero**: Voice Activity Detection (VAD) to detect when the user is speaking.

## Project Structure

- `agent.py`: Main file to initialize and run the voice assistant.
- `.env`: Stores API keys and configuration settings (add your OpenAI API key here).

## Setup and Installation

### Prerequisites

- Python 3.8+
- [OpenAI API Key](https://platform.openai.com/) (add to `.env` file)
- [LiveKit Server](https://docs.livekit.io) for handling voice interactions.

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd Backend
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables**

   - Create a `.env` file in the project root with the following variables:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   LIVEKIT_API_KEY=your_livekit_api_key
   LIVEKIT_API_SECRET=your_livekit_api_secret
   LIVEKIT_URL=your_livekit_url
   ```

### Running the Application

1. Start the voice assistant:

   ```bash
   python agent.py start
   ```

2. Follow prompts for questions on _Cosmos_ or initiate the quiz by requesting it.

## Usage

- **Ask Questions**: Engage with the assistant by asking questions related to _Cosmos_. If you ask unrelated questions, the assistant will remind you of its limited scope.
- **Take a Quiz**: To test your knowledge, say "I'd like to take a quiz." The assistant will ask five questions from the _Cosmos_ quiz pool. Each question includes multiple-choice options by default.

## Examples

**Question**: Tell me about the universe in Cosmos.

- **Response**: Provides information directly from the series.

**Unrelated Question**: "What is machine learning?"

- **Response**: "I can only discuss _Cosmos: A Personal Voyage_. Please ask questions on this topic."

**Quiz Interaction**:

1. Do you want information about Cosmos, or would you like to take a quiz?
2. If "quiz" is selected, a 5-question quiz begins, with answers validated and scored out of 5.
