# The English LSP

This is an implementation of the language server protocol, server bit, for
the... well the English language. At least, a proposal for one.

## Features

**NOT ACTUALLY IMPLEMENTED YET**

### Text Completion
It's not really code completion if it's just code, but still -- completion is
nice to have. For that, my current idea is that we will suggest to you the "word
that is most likely to follow" your previous texts, filtered by your typing, and
weight-adjusted by what you already have in your text.

Ideas:
* python - autocomplete package

### Hover
It gives you a definition by looking up a dictionary. If it's a capitalized word
it tries to look for where you first mentioned it, or up on wikipedia. Maybe
even urban-dict?

### Jump to Def
Only works for proper nouns within th text.

### Symbols
It breaks down your sentences and paragraphs as symbols.

### References
Finds where else a word has been used.

### Diagnostics
Runs spell check and a limited extent of grammar check for you. Since we
obviously can't hope to get the full-extent of the English grammar's finer
details right, we'll just give them to you as nice little suggestions.

### Refactoring
Eh..

## FAQ

### Why?
Idk. For funsies I suppose.

### How does it improve upon the existing autocompleters?
It works as an LSP. It really has nothing else over them.
