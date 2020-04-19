#!/usr/bin/env python

# WS server example
import asyncio
import websockets
from Marcus import StartLesson, CheckAnswer

current_phrase = ""

def process_Answer(user_answer):
	global current_phrase
	#Do something with user answer
	current_phrase = "Server Answer2"
	return current_phrase
	


async def Marcus(websocket, path):
	global current_phrase
	#Here we start MarcusCode and we update current answer
	current_phrase = StartLesson()	
	await websocket.send(current_phrase)		
	while True:
		user_answer = await websocket.recv()
		#Do something with user answer
		current_phrase = CheckAnswer(user_answer)
		await websocket.send(current_phrase)




start_server = websockets.serve(Marcus, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()