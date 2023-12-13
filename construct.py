import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--rawcode', default='rawcode.py', type=str)
parser.add_argument('--jsoncode', default='jsoncode.json', type=str)
parser.add_argument('--prompt_index', default='0-8', type=str) # prompt对应的行索引
parser.add_argument('--solution_index', default='8-20', type=str)  # solution对应的行索引
parser.add_argument('--test_index', default='23-25', type=str)  # test对应的行索引

args = parser.parse_args()


all_line=[line for line in open(args.rawcode, encoding='utf-8')]


def f(index):
    indexs=list(map(int,index.split("-")))
    return indexs

prompt_indexs=f(args.prompt_index)
solution_index=f(args.solution_index)
test_index=f(args.test_index)

prompt="".join(all_line[prompt_indexs[0]:prompt_indexs[1]])
solution="".join(all_line[solution_index[0]:solution_index[1]])
test="".join(all_line[test_index[0]:test_index[1]])

with open(args.jsoncode,'a',encoding='utf-8') as fa:
    ex={
        'language': 'python',
        'domain': 'algorithm',
        'source': 'https://github.com/jiaoxn/SortAlgorithm/blob/82ddddd9068ab779b8586f1a40272956fc4fd687/ExchangeSort/bubble_sort.py#L18',
        'prompt': prompt,
        'solution': solution,
        'test': test
    }
    print(json.dumps(ex),file=fa)