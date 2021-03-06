# -*- coding: utf-8 -*-

import json
import urllib
import urllib
from telebot import types

from data import botSendMessage, authors, Author, VARIANTS_INDEXES
import texts
from bot_log import log

AUTHORS_URL = 'https://api.fantlab.ru/search-autors.json?q='
JSON_AUTHOR_URL = 'https://api.fantlab.ru/autor/'
HTML_AUTHOR_URL = 'https://fantlab.ru/autor'
ANSWER_PER_REQUEST = 25 #value from Fantlab API
ANSWERS_COUNT = 5

def show_authors_invite(message):
	message_chat_id = message.chat.id
	authors[message_chat_id] = Author(True, "", 0, 0, {})
	botSendMessage(message_chat_id, texts.AUTHORSREQUESTTEXT)

def get_json_request(url):
	result = urllib.request.urlopen(url).read()
	return json.loads(result)

def show_authors_result(message):
	url = AUTHORS_URL + urllib.quote(message.text.encode('utf-8'))
	data = get_json_request(url)
	authors[message.chat.id] = Author(False, url, 0, 1, data)
	form_author_response(message.chat.id, authors[message.chat.id])

def stop_authors_request(message_chat_id):
	authors[message_chat_id] = Author(False, "", 0, 0, {})

def form_author_response(message_chat_id, author):
	if not message_chat_id in VARIANTS_INDEXES:
		VARIANTS_INDEXES[message_chat_id] = 0
	keyboard = types.InlineKeyboardMarkup()
	flag = False
	if author.offset >= len(author.data['matches']):
		keyboard.add(types.InlineKeyboardButton(text=texts.TRY_AGAIN_AUTHORS, callback_data="author_again"))
		keyboard.add(types.InlineKeyboardButton(text=texts.NO_THANKS, callback_data="main_menu"))
		botSendMessage(message_chat_id, texts.NO_AUTHORS, reply_markup=keyboard)
		return
	for k in range(ANSWERS_COUNT):
		index = k + author.offset
		if index >= len(author.data['matches']):
			flag = True
			break
		keyboard.add(types.InlineKeyboardButton(text=author.data['matches'][index]['rusname'],
			callback_data="author_show\n" + str(author.data['matches'][index]['autor_id'])))
	if not flag:
		keyboard.add(types.InlineKeyboardButton(text=texts.AUTHORS_OTHER, callback_data="author_other\n"))
	keyboard.add(types.InlineKeyboardButton(text=texts.AUTHORS_ANOTHER_REQUEST, callback_data="author_again"))
	keyboard.add(types.InlineKeyboardButton(text=texts.MAIN_MENU, callback_data="main_menu"))
	VARIANTS_INDEXES[message_chat_id] += 1
	if VARIANTS_INDEXES[message_chat_id] >= len(texts.AUTHORS_VARIANTS):
		VARIANTS_INDEXES[message_chat_id] = 0
	botSendMessage(message_chat_id, texts.AUTHORS_VARIANTS[VARIANTS_INDEXES[message_chat_id]], reply_markup=keyboard)

def next_author_response(message_chat_id):
	authors[message_chat_id].offset += ANSWERS_COUNT
	if authors[message_chat_id].offset == ANSWER_PER_REQUEST:
		authors[message_chat_id].step += 1
		authors[message_chat_id].offset = 0
		authors[message_chat_id].data = get_json_request(authors[message_chat_id].request + "&page=" + str(authors[message_chat_id].step))
	form_author_response(message_chat_id, authors[message_chat_id])

def show_author_info(message_chat_id, author_id):
	url = JSON_AUTHOR_URL + author_id
	data = get_json_request(url)
	botSendMessage(message_chat_id, data['name'] + '\n' + HTML_AUTHOR_URL + author_id)
