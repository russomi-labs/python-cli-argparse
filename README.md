# python-cli-argparse
- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
- [Usage](#usage)
- [References](#references)

## Overview

The command line interface (also known as CLI) is a means to interact with a command line script. Python comes with several different libraries that allow you to write a command line interface for your scripts, but the standard way for creating a CLI in Python is currently the Python `argparse` library.

The Python `argparse` library:

- Allows the use of positional arguments
- Allows the customization of the prefix chars
- Supports variable numbers of parameters for a single option
- Supports subcommands (A main command line parser can use other command line parsers depending on some arguments.)

Using the Python `argparse` library has four steps:

1. Import the Python argparse library
2. Create the parser
3. Add optional and positional arguments to the parser
4. Execute .parse_args()

## Getting Started

You can [create](https://cli.github.com/manual/gh_repo_create) a new repo using this template via the `gh` cli:

```bash
# gh repo create [<name>] [flags]
gh repo create gitops-labs/my-repo \
    --template gitops-labs/template
```

### Prerequisites

What things you need to install the software and how to install them.

```bash
brew install gh
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## Usage

Add notes about how to use the system.

## References

- [How to Build Command Line Interfaces in Python With argparse](https://realpython.com/command-line-interfaces-python-argparse/#what-is-a-command-line-interface)
- [Do-nothing scripting: the key to gradual automation](https://blog.danslimmon.com/2019/07/15/do-nothing-scripting-the-key-to-gradual-automation/)
- [Comparing Python Command-Line Parsing Libraries – Argparse, Docopt, and Click](https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/)
- [AWS cloudendure migration factory solution](https://github.com/awslabs/aws-cloudendure-migration-factory-solution)
- [How to Write Python Command-Line Interfaces like a Pro](https://towardsdatascience.com/how-to-write-python-command-line-interfaces-like-a-pro-f782450caf0d)
- [argparse — Parser for command-line options, arguments and sub-commands](https://docs.python.org/3/library/argparse.html)
- [Argparse Tutorial](https://docs.python.org/3/howto/argparse.html)
- https://mike.depalatis.net/blog/simplifying-argparse.html
- https://github.com/alephnull/rfw/blob/master/rfw/rfwc.py
- https://gist.github.com/mivade/384c2c41c3a29c637cb6c603d4197f9f
- https://github.com/mivade/arghelp
