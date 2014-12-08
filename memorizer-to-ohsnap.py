# -*- coding: utf-8 -*-

import requests
import json
from sys import stdin

def make_ohsnap_file(remote_file_uri):
    if not remote_file_uri:
        print('No remote URI specified!')
        return

    source = requests.get(remote_file_uri)
    data = source.json()

    output = {}
    output['subject'] = data['name'].upper()
    output['questions'] = []

    for q in data['questions']:
        question = {}
        question['description'] = q['question']
        question['answers'] = []
        for x in range(0, len(q['answers'])):
            question['answers'].append({'description': q['answers'][x], 'correct': x == q['correct']})
        output['questions'].append(question)

    with open('%s.json' % output['subject'], 'w') as f:
        f.write(json.dumps(output))

make_ohsnap_file(stdin.readline().strip())
