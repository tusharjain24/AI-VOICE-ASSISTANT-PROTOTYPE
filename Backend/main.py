import asyncio
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero
from data import QUESTION_POOL
from utils import AssistantFnc, get_user_response, quiz
load_dotenv()

async def entrypoint(ctx: JobContext):
    initial_ctx = llm.ChatContext().append(
        role="system",
        text=(
            "You are a knowledgeable assistant about 'Cosmos: A Personal Voyage' by Carl Sagan. "
            "Please answer questions only about this series. If the question is unrelated, remind the user that "
            "you can only discuss 'Cosmos: A Personal Voyage'."
        ),
    )
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    fnc_ctx = AssistantFnc()

    assistant = VoiceAssistant(
        vad=silero.VAD.load(),
        stt=openai.STT(),
        llm=openai.LLM(model="gpt-4o-mini"),
        tts=openai.TTS(),
        chat_ctx=initial_ctx,
        fnc_ctx=fnc_ctx,
    )
    assistant.start(ctx.room)

    await asyncio.sleep(1)
    await assistant.say("Hello! Do you want information about Cosmos, or would you like to take a quiz?")
    
    try:
        response = await asyncio.wait_for(get_user_response(ctx), timeout=20)
        if "quiz" in response.lower():
            await quiz(ctx, assistant)
        else:
            await assistant.say("Okay, feel free to ask about 'Cosmos: A Personal Voyage.'")
    except asyncio.TimeoutError:
        await assistant.say("No response detected. I'm here whenever you need help.")

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
