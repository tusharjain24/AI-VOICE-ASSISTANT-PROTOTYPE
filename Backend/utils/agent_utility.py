from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero
import random
from data import QUESTION_POOL
import asyncio

async def quiz(ctx: JobContext, assistant: VoiceAssistant):
    questions = random.sample(QUESTION_POOL, 5)
    correct_answers = 0

    for i, question in enumerate(questions, start=1):
        await assistant.say(f"Question {i}: {question['question']}")
        try:
            response = await asyncio.wait_for(get_user_response(ctx), timeout=20)
            if response and any(answer.lower() == response.lower() for answer in question["answers"]):
                correct_answers += 1
                await assistant.say("Correct!")
            else:
                await assistant.say("That was incorrect.")
        except asyncio.TimeoutError:
            await assistant.say("Time’s up for this question.")

    await assistant.say(f"You got {correct_answers} out of 5 correct.")
    if correct_answers >= 3:
        await assistant.say("Congratulations, you passed the quiz!")
    else:
        await assistant.say("Unfortunately, you did not pass the quiz this time.")

async def get_user_response(ctx: JobContext) -> str:
    # Assuming ctx.room allows listening to specific types of participant events.
    response_future = asyncio.Future()

    def on_participant_message(participant, message):
        if not response_future.done():
            response_future.set_result(message)

    ctx.room.on("participant_message_received", on_participant_message)

    try:
        return await response_future
    finally:
        ctx.room.off("participant_message_received", on_participant_message)
