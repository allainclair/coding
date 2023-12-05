import json


class SearchByTag:
    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
        self.query = query_tag

    def search(self):
        if self._data:
            for item in self._data["items"]:
                tags = item.get("tags", [])
                if self.query in tags:
                    yield item

    def first(self):
        print(self._data)
        if self._data:
            for item in self._data["items"]:
                # print(item)
                # print(item["tags"])
                tags = item.get("tags", [])
                if self.query in tags:
                    return item
        raise StopIteration(f"No item matches the query: {self.query}")


def test_search_by_tag_1():
    # search = SearchByTag("3_1.json", "crime")
    # assert search.first() == {"name": "The Godfather", "tags": ["70s", "drama", "crime"]}
    # assert list(search.search()) == [{"name": "The Godfather", "tags": ["70s", "drama", "crime"]},
    #                            {"name": "The Dark Knight", "tags": ["action", "crime", "drama"]},
    #                            {"name": "The Godfather: Part II", "tags": ["70s", "crime", "drama"]}]

    search = SearchByTag("3_2.json", "90s")
    assert search.first()


def main():
    test_search_by_tag_1()


if __name__ == '__main__':
    main()
