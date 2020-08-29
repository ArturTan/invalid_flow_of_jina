__copyright__ = "Copyright (c) 2020 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

import os

import click
from jina.flow import Flow

RANDOM_SEED = 10  # 5
os.environ['PARALLEL'] = str(2)
os.environ['SHARDS'] = str(2)


def data_fn():
    for i in os.listdir("data/fulltexts/"):
        with open(f"data/fulltexts/{i}", 'r', encoding='utf-8') as f:
            content = f.read()
        yield content


@click.command()
@click.option('--task', '-t')
@click.option('--top_k', '-k', default=5)
def main(task, top_k):
    workspace_path = './test'
    os.environ['TMP_WORKSPACE'] = workspace_path
    if task == 'index':
        f = Flow().load_config('flow-index.yml')
        with f:
            f.index(input_fn=data_fn, batch_size=16)
    elif task == 'query':
        f = Flow().load_config('flow-query.yml')
        with f:
            while True:
                text = input('word definition: ')
                if not text:
                    break
                ppr = lambda x: print_topk(x, text)
                f.search_lines(lines=[text, ], output_fn=ppr, top_k=top_k)


if __name__ == '__main__':
    main()
