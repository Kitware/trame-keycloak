from trame_keycloak.widgets.keycloak import *


def initialize(server):
    from trame_keycloak import module

    server.enable_module(module)
