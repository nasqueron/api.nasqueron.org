#   -------------------------------------------------------------
#   Nasqueron - API
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Build API files
#   License:        Trivial work, not eligible to copyright
#   -------------------------------------------------------------

API_FILES=infra/servers.json
YAML_TO_JSON=_utils/yaml2json.py

RM=rm -f

#   -------------------------------------------------------------
#   Main targets
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

all: $(API_FILES)

clean:
	${RM} ${API_FILES}

#   -------------------------------------------------------------
#   API targets
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

infra/servers.json:
	${YAML_TO_JSON} infra/datasource.yml servers > infra/servers.json
