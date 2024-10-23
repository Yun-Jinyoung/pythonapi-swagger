import json

def load_test_data():
    with open('data.json') as f:
        return json.load(f)

def generate_random_email():
    # 임의의 이메일 생성 로직
    pass

# ... (다른 유틸리티 함수)