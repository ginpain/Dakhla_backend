""""
from django.shortcuts import render
from django.http import JsonResponse
import os
import csv
import google.generativeai as genai
from difflib import SequenceMatcher
from django.views.decorators.csrf import csrf_exempt

# Path to your CSV file
CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), 'data_chatbot.csv')

# Load keywords from CSV file
def load_keywords(csv_file_path):
    keywords = []
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            keywords.extend([keyword.strip().lower() for keyword in row])  # Assuming each row contains one keyword per cell
    return keywords

relevant_keywords = load_keywords(CSV_FILE_PATH)

@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        api_response = get_chatbot_response(user_message)
        return JsonResponse({'response': api_response})
    return render(request, 'chat.html')

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def get_chatbot_response(message):
    message = message.lower()
    for keyword in relevant_keywords:
        if (keyword[:3] in message or keyword[-3:] in message or
            any(similar(keyword, word) > 0.7 for word in message.split())):
            api_key = os.getenv("GEMINI_API_KEY")
            genai.configure(api_key=api_key)

            generation_config = {
                "temperature": 1.35,
                "top_p": 0.95,
                "top_k": 64,
                "max_output_tokens": 8192,
                "response_mime_type": "text/plain",
            }

            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                generation_config=generation_config,
            )

            chat_session = model.start_chat(history=[])
            response = chat_session.send_message(message)
            return response.text
    return "sorry, I can't give you a response to this"

"""
from django.shortcuts import render
from django.http import JsonResponse
import os
import csv
import google.generativeai as genai
from difflib import SequenceMatcher
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# Path to your CSV file
CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), 'data_chatbot.csv')

# Load keywords from CSV file
def load_keywords(csv_file_path):
    keywords = []
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            keywords.extend([keyword.strip().lower() for keyword in row])  # Assuming each row contains one keyword per cell
    return keywords

relevant_keywords = load_keywords(CSV_FILE_PATH)

class ChatbotView(View):
    chat_sessions = {}

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        response = render(request, 'chat.html')
        response['X-CSRFToken'] = request.META.get('CSRF_COOKIE')
        return response

    def post(self, request):
        user_id = request.POST.get('user_id')  # Assuming each user has a unique ID
        user_message = request.POST.get('message')

        if user_id not in self.chat_sessions:
            self.chat_sessions[user_id] = []

        self.chat_sessions[user_id].append({"role": "user", "content": user_message})
        api_response = self.get_chatbot_response(user_message, self.chat_sessions[user_id])
        self.chat_sessions[user_id].append({"role": "model", "content": api_response})

        return JsonResponse({'response': api_response})

    def similar(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    def get_chatbot_response(self, message, history):
        # Format the history correctly
        formatted_history = [
            {"role": entry["role"], "parts": [{"text": entry["content"]}]}
            for entry in history
        ]

        message = message.lower()
        for keyword in relevant_keywords:
            if (keyword[:3] in message or keyword[-3:] in message or
                any(self.similar(keyword, word) > 0.7 for word in message.split())):
                api_key = os.getenv("GEMINI_API_KEY")
                genai.configure(api_key=api_key)

                generation_config = {
                    "temperature": 1.35,
                    "top_p": 0.95,
                    "top_k": 64,
                    "max_output_tokens": 8192,
                    "response_mime_type": "text/plain",
                }

                model = genai.GenerativeModel(
                    model_name="gemini-1.5-flash",
                    generation_config=generation_config,
                )

                chat_session = model.start_chat(history=formatted_history)
                response = chat_session.send_message(message)
                return response.text
        return "Sorry, I can't give you a response to this."
