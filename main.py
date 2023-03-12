import requests
import time

def get_tagged_questions(tag, fromdate):
    response = requests.get(url='https://api.stackexchange.com/2.3/questions', params={'site': 'stackoverflow', 'tagged': tag, 'fromdate': fromdate}).json()
    questions = '\n'.join([question['title'] for question in response['items']])
    print(f'Найдены следующие вопросы:\n{questions}')

if __name__ == '__main__':
    date_two_days_back = int(time.time()) - 2 * 24 * 60 * 60
    get_tagged_questions('python', date_two_days_back)