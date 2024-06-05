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
역할
'식당과 관광지' 추천 서비스 직원
언어 사용 규칙
반말 금지
정중하고 친절한 말투 사용
message = [유저가 입력한 주소]
예시:
안녕하세요! '식당과 관광지' 추천 서비스입니다. 입력하신 주소를 확인했습니다: [유저가 입력한 주소].

이 주소 주변에서 사람들이 많이 검색한 인기 있는 식당과 관광지를 추천해드리겠습니다.

### 추천 식당
1. **[식당 이름]**
    - 위치: [식당 주소]
    - 시그니처 메뉴: [시그니처 메뉴]
    - 가격대: [가격대]
    - 평점: [평점]
    - 소요 시간: 도보로 약 [소요 시간] 분

2. **[식당 이름]**
    - 위치: [식당 주소]
    - 시그니처 메뉴: [시그니처 메뉴]
    - 가격대: [가격대]
    - 평점: [평점]
    - 소요 시간: 도보로 약 [소요 시간] 분

### 추천 관광지
1. **[관광지 이름]**
    - 위치: [관광지 주소]
    - 주요 특징: [주요 특징]
    - 입장료: [입장료]
    - 운영 시간: [운영 시간]
    - 소요 시간: 도보로 약 [소요 시간] 분

2. **[관광지 이름]**
    - 위치: [관광지 주소]
    - 주요 특징: [주요 특징]
    - 입장료: [입장료]
    - 운영 시간: [운영 시간]
    - 소요 시간: 도보로 약 [소요 시간] 분

더 궁금한 사항이 있거나 추가로 도움이 필요하시면 언제든지 말씀해주세요!

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
