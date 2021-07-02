import elasticsearch
from elasticsearch import helpers


def create_index(index_name):
    response = client.indices.create(index=index_name)
    return response


def get_dictionary_words(filepath):
    return [word.strip() for word in open(filepath).readlines()]


if __name__ == "__main__":
    client = elasticsearch.Elasticsearch()

    index_name = "dictionary"
    print(create_index(index_name))

    my_words = get_dictionary_words("dictionary.txt")

    actions = [
        {
            "_index": index_name,
            "_id": id,
            "_source": {
                "word": word
            }
        }
        for id, word in enumerate(my_words)
    ]

    print("starting bulk push")
    helpers.bulk(client, actions)
    print("ending bulk push")
