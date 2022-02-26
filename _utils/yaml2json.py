#!/usr/bin/env python3

#   -------------------------------------------------------------
#   Nasqueron - API
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Create a JSON document from a YAML datasource
#   License:        Trivial work, not eligible to copyright
#   -------------------------------------------------------------


import json
import sys
import yaml


#   -------------------------------------------------------------
#   Convert
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def to_json(source_path, key=None):
    with open(source_path) as fd:
        data = yaml.safe_load(fd)

        if key:
            data = data[key]

        return json.dumps(data, indent=4)


#   -------------------------------------------------------------
#   Application entry point
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def run(source_path, key=None):
    print(to_json(source_path, key))


if __name__ == "__main__":
    argc = len(sys.argv)

    if argc < 2:
        print(f"Usage: {sys.argv[0]} <YAML datasource> [key to take]", file=sys.stderr)
        sys.exit(1)

    run(*sys.argv[1:3])
