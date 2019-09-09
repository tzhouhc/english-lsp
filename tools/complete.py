import autocomplete

from pygls.types import CompletionItem, CompletionList

autocomplete.load()


def _complete(english_server, params):
    results = ["what", "no"]
    return CompletionList(False, [CompletionItem(i) for i in results])
