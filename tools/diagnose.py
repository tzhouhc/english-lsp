import proselint

from pygls.server import LanguageServer
from pygls.types import Diagnostic, DiagnosticSeverity, Range, Position


# shared functionality that detects bad syntax
def _diagnose(english_server: LanguageServer, params):
    # Get document from workspace
    text_doc = english_server.workspace.get_document(params.textDocument.uri)
    raw_results = proselint.tools.lint(text_doc.source)
    english_server.show_message_log(f"{raw_results}")
    diagnostics = []
    for _, message, line, col, _, _, length, _, _ in raw_results:
        diagnostics += [
            Diagnostic(
                range=Range(Position(line, col - 1), Position(line, col + length)),
                message=message,
                severity=DiagnosticSeverity.Warning,
                source="eng-lsp",
            )
        ]
    english_server.show_message_log(f"{diagnostics}")

    # Send diagnostics
    english_server.publish_diagnostics(params.textDocument.uri, diagnostics)
