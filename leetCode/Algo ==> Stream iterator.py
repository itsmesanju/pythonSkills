class NewsTopicIterator:
    def __init__(self, news_stream):
        self.news_stream = news_stream
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.news_stream):
            topic = self.news_stream[self.current_index]
            self.current_index += 1
            return topic
        else:
            raise StopIteration

    def has_next(self):
        return self.current_index < len(self.news_stream)


class NewsTopicStream:
    def __init__(self, topics):
        self.topics = topics

    def iterator(self):
        return NewsTopicIterator(self.topics)


# Example usage:
news_topics = ["Breaking News", "Politics", "Technology", "Sports", "Entertainment"]

news_stream = NewsTopicStream(news_topics)
iterator = news_stream.iterator()

while iterator.has_next():
    print(iterator.__next__())
