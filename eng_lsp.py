#!/usr/bin/env python3
"""The English Language Server."""

import argparse

from tools.diagnose import _diagnose
from pygls.features import (
    TEXT_DOCUMENT_DID_OPEN,
    TEXT_DOCUMENT_DID_CHANGE,
    TEXT_DOCUMENT_DID_SAVE,
)
from pygls.server import LanguageServer
from pygls.types import (
    DidOpenTextDocumentParams,
    DidChangeTextDocumentParams,
    DidSaveTextDocumentParams,
)


# create global server
class EnglishLanguageServer(LanguageServer):
    def __init__(self):
        super().__init__()


english_server = EnglishLanguageServer()


@english_server.feature(TEXT_DOCUMENT_DID_CHANGE)
def did_change(ls, params: DidChangeTextDocumentParams):
    """Text document did change notification."""
    _diagnose(ls, params)


@english_server.feature(TEXT_DOCUMENT_DID_SAVE)
def did_save(ls, params: DidSaveTextDocumentParams):
    """Text document did save notification."""
    english_server.show_message_log("Doing some diagnostics")
    _diagnose(ls, params)


@english_server.feature(TEXT_DOCUMENT_DID_OPEN)
async def did_open(ls, params: DidOpenTextDocumentParams):
    """Text document did open notification."""
    _diagnose(ls, params)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbosity", help="The level of logging verbosity.")
    return parser.parse_args()


def main():
    english_server.start_io()


if __name__ == "__main__":
    main()
