from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from openai import OpenAI



class ChatBotView(APIView):
    def post(self, request):
        user_message = request.data.get('message')

        CLIENT = OpenAI(
        api_key=settings.OPENAI_API_KEY
        )
        system_instructions = """
        이제부터 너는 '식당과 관광지' 추천해주는 직원이야.
        반말은 사용하면 안돼.
        유저가 입력한 'message'의 주소를 찾고 그 주소 근처에 있는 식당과 관광지를 알려주는 대화를 진행해.

        주소를 받으면 주소를 확인하고 사람들이 많이 검색한 식당과 시그니처 매뉴, 관광지와 입장료를 검색 많은 순으로 2가지씩 추천해줘.
        식당과 관광지가 주소에서 걸리는 시간도 알려줘.
        """

        completion = CLIENT.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_instructions},
                    {"role": "user", "content": user_message},
                ],
        )
        chatbot_response = completion.choices[0].message.content
        return Response({"JCYC봇": chatbot_response})
