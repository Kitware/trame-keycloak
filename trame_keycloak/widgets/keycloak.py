"""Keycloak Widget support both vue2 and vue3 backend.

(Currently Work-In-Progress)
"""
from trame_client.widgets.core import AbstractElement
from .. import module

__all__ = [
    "Auth",
]


class HtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            self.server.enable_module(module)


# Expose your vue component(s)
class Auth(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__(
            "key-cloak",
            **kwargs,
        )
        self._attr_names += [
            "config",
        ]
        self._event_names += [
            "authenticated",
            "profile",
        ]

    @property
    def html(self):
        if len(self.children) == 1:
            self.children[0].v_slot = "{ user }"

        return super().html

    def login(self, options):
        """
        Redirects to login form.

        :param scope: Specifies the scope parameter for the login url. The scope 'openid' will be added to the scope if it is missing or undefined.
        :param_type scope: string

        :param redirectUri: Specifies the uri to redirect to after login.
        :param_type redirectUri: string

        :param prompt: By default the login screen is displayed if the user is not logged into
                           Keycloak. To only authenticate to the application if the user is already
                           logged in and not display the login page if the user is not logged in, set
                           this option to `'none'`. To always require re-authentication and ignore
                           SSO, set this option to `'login'`.
        :param_type prompt: None | login;

        :param action: If value is `'register'` then user is redirected to registration page,
                       otherwise to login page.
        :param_type action: string

        :param maxAge: Used just if user is already authenticated. Specifies maximum time since
                       the authentication of user happened. If user is already authenticated for
                       longer time than `'maxAge'`, the SSO is ignored and he will need to
                       authenticate again.
        :param_type maxAge: number

        :param loginHint: Used to pre-fill the username/email field on the login form.
        :param_type loginHint: string

        :param acr: Sets the `acr` claim of the ID token sent inside the `claims` parameter.
                    See section 5.5.1 of the OIDC 1.0 specification.
        :param_type acr: Acr

        :param idpHint: Used to tell Keycloak which IDP the user wants to authenticate with.
        :param_type idpHint: string

        :param locale: Sets the 'ui_locales' query param in compliance with section 3.1.2.1
                                                of the OIDC 1.0 specification.
        :param_type locale: string
        """
        self.server.js_call(self.__ref, "login", options)

    def logout(self, options):
        """
        Redirects to logout.

        :param redirectUri: Specifies the uri to redirect to after logout.
        """
        self.server.js_call(self.__ref, "logout", options)

    def register(self, options):
        """
        Redirects to registration form.


        :param scope: Specifies the scope parameter for the login url. The scope 'openid' will be added to the scope if it is missing or undefined.
        :param_type scope: string

        :param redirectUri: Specifies the uri to redirect to after login.
        :param_type redirectUri: string

        :param prompt: By default the login screen is displayed if the user is not logged into
                           Keycloak. To only authenticate to the application if the user is already
                           logged in and not display the login page if the user is not logged in, set
                           this option to `'none'`. To always require re-authentication and ignore
                           SSO, set this option to `'login'`.
        :param_type prompt: None | login;

        :param maxAge: Used just if user is already authenticated. Specifies maximum time since
                       the authentication of user happened. If user is already authenticated for
                       longer time than `'maxAge'`, the SSO is ignored and he will need to
                       authenticate again.
        :param_type maxAge: number

        :param loginHint: Used to pre-fill the username/email field on the login form.
        :param_type loginHint: string

        :param acr: Sets the `acr` claim of the ID token sent inside the `claims` parameter.
                    See section 5.5.1 of the OIDC 1.0 specification.
        :param_type acr: Acr

        :param idpHint: Used to tell Keycloak which IDP the user wants to authenticate with.
        :param_type idpHint: string

        :param locale: Sets the 'ui_locales' query param in compliance with section 3.1.2.1
                                                of the OIDC 1.0 specification.
        :param_type locale: string
        """
        self.server.js_call(self.__ref, "register", options)
